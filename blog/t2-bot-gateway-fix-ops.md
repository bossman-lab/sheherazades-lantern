---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/t2-bot-gateway-fix-ops.html"
title: "Telegram Bot 突然不响应了？一个 socat 进程引发的故障排查"
description: "两个 Telegram bot 同时断联，网关进程还在、LM Studio 正常、ping 通——但端口不在了。从怀疑网络到定位到一根断掉的代理桥接线程，再到写成 systemd 服务的完整过程。"
date: "2026-05-17"
tags: ["运维", "Telegram", "Hermes Agent", "socat"]
---

# Telegram Bot 突然不响应了？

### — 一个 socat 进程引发的故障排查

*5 月 17 日凌晨，发现 @winkBBot 和 @kndAgentbot 都没有回应。查了一轮发现：网关进程在跑，LM Studio 正常，ping 通，SSH 能连——但 bot 就是没反应。*

---

## 症状

两个 Telegram bot 同时失去响应：

- **@winkBBot** — 发消息不回复，没有超时提示，直接沉默
- **@kndAgentbot (迪仔)** — 同上，完全无响应

T2 主机（极夜 T2，AMD HX370 / 96GB）本身是正常的：
- `ping` 延迟 3ms
- SSH 正常登录
- LM Studio 运行正常，两个模型都在 IDLE 状态
- 任务管理器显示 CPU 和内存使用正常

## 初步排查

先看 Hermes gateway 状态：

```
hermes gateway status
✓ Gateway is running (PID: 17276)
```

看起来正常。但继续查发现端口不在监听：

```
netstat -ano | findstr :18789
（空）
```

进程在，端口不在——说明 gateway 卡在某个状态没能正常启动 HTTP 服务。

查日志：

```
23:40:20  ERROR [Telegram] Telegram polling could not reconnect
          after 10 network error retries. Restarting gateway.
23:40:20  ERROR Fatal telegram adapter error: telegram_network_error

23:56:08  INFO  Proxy detected; passing explicitly to HTTPXRequest:
                http://192.168.3.135:7891
23:56:10  WARN  Connect attempt 1/8 failed:
                httpx.ConnectError: All connection attempts failed
...
00:07:38  WARN  Connect attempt 5/8 failed
00:18:42  WARN  telegram paused after 10 consecutive failures
```

**核心发现：** 网关连不上 Telegram API 服务器。它通过代理 `http://192.168.3.135:7891` 转发，但这个代理连接持续失败。

## 根因定位

T2 的代理架构：

```
T2 (Windows 11)
  └→ Hermes Gateway (port 18789)
       └→ HTTP Proxy: http://192.168.3.135:7891
                    ↓
               Linux server
                 socat :7891 → :7890
                    ↓
               Mihomo proxy (port 7890)
                    ↓
               Telegram API
```

T2 安装在 Windows 上，其 Hermes 网关为了访问 Telegram API 需要走 HTTP 代理。代理入口 `192.168.3.135:7891` 是一个 **socat 桥接**：它把来自 T2 的请求转发到本机的 Mihomo 代理（`:7890`）。

检查 socat 状态：

```
ss -tlnp | grep 7891
（空——socat 不在监听！）
```

**socat 进程不知道什么时候挂了。** 整个代理链断在最前端，T2 的请求到了 `192.168.3.135` 就被拒绝——没有端口在 7891 上监听。

## 修复过程

第一步是重建代理桥接：

```
socat TCP-LISTEN:7891,fork,reuseaddr TCP:127.0.0.1:7890 &
```

验证端口已监听：

```
ss -tlnp | grep 7891
LISTEN  0  5  0.0.0.0:7891  0.0.0.0:*  users:(("socat",pid=3415591,fd=5))
```

然后重启 T2 的两个网关：

```
# Default profile (winkBBot)
hermes gateway restart

# RP profile (kndAgentbot)
hermes gateway restart --profile rp
```

日志确认连接已恢复：

```
Connected to Telegram (polling mode)
telegram connected
Gateway running with 1 platform(s)
```

## 持久化：写成 systemd 服务

重启解决了眼前问题，但 socat 是手动启动的——系统重启、进程崩溃时不会自动恢复。写成一个 systemd 服务：

```
[Unit]
Description=Proxy bridge for T2 — socat :7891 → :7890
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/socat TCP-LISTEN:7891,fork,reuseaddr TCP:127.0.0.1:7890
Restart=always
RestartSec=10
User=nobody

[Install]
WantedBy=multi-user.target
```

```
systemctl enable socat-proxy-t2.service
systemctl start socat-proxy-t2.service
```

现在 socat 会随系统启动，崩溃后 10s 自动恢复。

## 几条教训

> **1. 「进程在跑」不等于「服务在工作」**
>
> `hermes gateway status` 显示 running，端口却不在监听。原因是网关启动后尝试连 Telegram，但因为代理不可用，在重试循环里一直卡着——进程跑着，但核心功能（HTTP 监听）还没初始化。
>
> **2. 中间件是单点脆弱环节**
>
> socat 这种小工具太不起眼了，以至于没人会想到去监控它。但它一旦挂了，整个代理链就断了。任何中间层（代理桥接、端口转发、DNS 解析）都应被当作关键基础设施来管理。
>
> **3. 问题定位的顺序：应用层 → 网络层 → 中间件**
>
> 这次排查的顺序是对的：先看应用层（gateway 状态、日志），再看网络层（ping、curl 测试），最后才发现中间件（socat 进程不在）。如果一开始就 `ss` 看端口监听状态，能更快定位。
>
> **4. 持久化没有例外**
>
> 手动启动的进程总有挂的一天。无论是 socat、sidecar、还是调试用的小工具——如果它必须一直在，就写成 systemd 服务或 Docker 容器。例外不存在。

---

**更新：** 现在 `socat-proxy-t2.service` 已在服务器上启用并自动启动。T2 的上游 bot (@winkBBot, @kndAgentbot) 均已恢复正常。
