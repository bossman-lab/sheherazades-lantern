---
layout: blog-layout.njk
lang: en
dir: ltr
permalink: "/blog/hermes-agent-install-guide-beginners.html"
title: "Hermes Agent 安装入门指南 — 从零到有（含中国大陆避坑）"
description: "Hermes Agent 是一个开源 AI 代理框架。这篇指南覆盖安装、配置代理、网关部署、Telegram 接入，以及在中国大陆环境下的所有坑点。"
---

# Hermes Agent 安装入门指南 — 从零到有

*字数：约 3,000 字 | 阅读时间：10 分钟 | 适用系统：Linux / macOS / WSL*

---

## 什么是 Hermes Agent？

[Hermes Agent](https://github.com/NousResearch/hermes-agent) 是 Nous Research 开发的开源 AI 代理框架。它跟 Claude Code、OpenAI Codex 属于同一类产品——能自主调用工具、操作终端、读写文件、访问网络、管理记忆的 AI 助手。

但 Hermes 有几个独特之处：

- **技能系统** — 代理自己会写技能文档，从经验中学习，越用越懂你
- **跨会话记忆** — 记得你是谁、你的偏好、你的项目
- **多平台网关** — 同一个代理跑在 Telegram、Discord、Slack 等 10+ 平台上
- **模型无关** — OpenRouter、Anthropic、OpenAI、DeepSeek、本地模型随便换
- **开源免费** — MIT 协议，随便用

---

## 第一步：安装

### 标准安装（海外用户）

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

这行命令会：
1. 克隆仓库到 `~/.hermes/hermes-agent/`
2. 创建 Python 虚拟环境并安装依赖
3. 安装 Node.js 依赖
4. 创建 CLI 命令 `hermes`

### 中国大陆安装

海外用户一条命令搞定，但如果你在**中国大陆**，上面的命令会卡在网络问题上：

**问题 1：raw.githubusercontent.com 被 DNS 污染**

```bash
# 方案 A：加 hosts
echo "185.199.108.133 raw.githubusercontent.com" >> /etc/hosts

# 方案 B：用镜像拉取
# 手动下载 install.sh
wget https://ghproxy.net/https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh
bash install.sh
```

**问题 2：GitHub 克隆慢**

```bash
# 方案：用镜像克隆
# 等 install.sh 卡住后 Ctrl+C，手动 clone
git clone https://ghproxy.net/https://github.com/NousResearch/hermes-agent.git ~/.hermes/hermes-agent
# 然后重新运行 install.sh（它会跳过已存在的目录）
bash install.sh
```

**问题 3：pip 安装依赖慢**

```bash
# install.sh 运行前先配置 pip 镜像
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
# 或 install.sh 里卡 pip install 的时候 Ctrl+C，配置好镜像再重跑
```

### 安装后验证

```bash
hermes --version        # 检查版本
hermes doctor           # 检查依赖完整性
hermes config path      # 看看配置文件在哪
```

---

## 第二步：配置模型和 API Key

### 环境变量配置文件

Hermes 的 API 密钥存在 `~/.hermes/.env` 文件：

```bash
hermes config env-path   # 查看 .env 路径
# 或直接编辑
nano ~/.hermes/.env
```

### 推荐模型配置

```bash
# OpenRouter（推荐入门，支持最多模型，一个 API Key 访问多个模型）
OPENROUTER_API_KEY=sk-or-v1-xxx...

# Anthropic（效果最好但贵）
ANTHROPIC_API_KEY=sk-ant-xxx...

# DeepSeek（性价比高，国内可直连）
DEEPSEEK_API_KEY=sk-xxx...

# 国内用户推荐方案
# 1. DeepSeek（国内直连，速度快）
# 2. OpenRouter（走代理的话）
# 3. 通义千问 DashScope
DASHSCOPE_API_KEY=sk-xxx...
```

### 选择模型

```bash
hermes model    # 交互式选择模型和供应商
```

这会打开一个列表，选择供应商后选择模型。常用组合：

| 用途 | 供应商/模型 | 特点 |
|------|------------|------|
| 日常使用 | `deepseek/deepseek-chat` | 便宜，国内直连 |
| 代码 | `anthropic/claude-sonnet-4` | 代码能力最强，贵 |
| 推理 | `openrouter/qwen/qwq-32b` | 强推理，中等价格 |
| 免费 | OpenRouter 上的免费模型 | 适合测试，不稳定 |

---

## 第三步：启动聊天

### 终端模式

```bash
hermes                     # 交互式聊天
hermes chat -q "你好"      # 单次查询
hermes --resume last       # 恢复上次会话
```

首次启动时 Hermes 会加载工具、创建会话，可能需要 5-15 秒。看到提示符后就可以输入了。

### 常用终端命令

| 命令 | 作用 |
|------|------|
| `/new` | 新会话（重要：切换模型后必须执行） |
| `/model` | 查看当前模型 |
| `/model <name>` | 切换模型（如 `/model claude-sonnet-4`） |
| `/quit` | 退出 |
| `/retry` | 重发上一条消息 |
| `/title 会话名` | 命名会话 |

---

## 第四步：接入 Telegram（最常用场景）

Telegram 网关让 Hermes 在手机上也能用。这是新手最容易踩坑的地方。

### 获取 Bot Token

1. 在 Telegram 中搜索 `@BotFather`
2. 发送 `/newbot`
3. 输入 bot 名称（如 `My Hermes Agent`）
4. 输入 username（必须以 `bot` 结尾，如 `MyHermesAgentBot`）
5. 复制返回的 token（格式：`123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`）

### 配置网关

```bash
hermes gateway setup
```

按提示输入 bot token。或者编辑 `.env`：

```bash
# 在 ~/.hermes/.env 中添加
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

### 启动网关

```bash
# 前台测试（先确保能跑通）
hermes gateway run

# 后台服务
hermes gateway install
hermes gateway start
hermes gateway status
```

### Telegram 网关天坑

**坑一：匿名管理员**

如果你是 Telegram 群的匿名管理员，代理会收到你的消息但拒绝回复。因为匿名管理员的 sender ID 是 `1087968824`，不是你的真实 ID。

```bash
# 修复：在 .env 中加入群组 chat ID
TELEGRAM_GROUP_ALLOWED_CHATS=-1001234567890
# chat ID 可以通过 @getidsbot 获取
```

**坑二：中国大陆无法直连 Telegram**

```bash
# 如果你有代理（如 Clash/Mihomo）
# 在启动网关前设置环境变量
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
hermes gateway run        # 在代理环境下启动
```

**坑三：网关自动重启后代理失效**

`hermes gateway install` 创建的 user-level systemd 服务在 root 用户下无效。需要用 system-level 服务。

```bash
# 创建 /etc/systemd/system/hermes-gateway.service
# 内容包含：
# - Environment="http_proxy=http://127.0.0.1:7890"
# - Restart=always
# - WantedBy=multi-user.target

systemctl daemon-reload
systemctl enable hermes-gateway.service
systemctl start hermes-gateway.service
```

---

## 常见问题排查

### `hermes doctor` 检查清单

```bash
hermes doctor    # 自动检查配置和依赖
```

常见输出及应对：

| 问题 | 解决 |
|------|------|
| `pip: externally-managed-environment` | 不用系统 pip，用 venv 里的 pip：`~/.hermes/hermes-agent/venv/bin/pip install ...` |
| `No API key configured` | 检查 `~/.hermes/.env` 是否有正确的 API key |
| `Tool X not available` | 运行 `hermes tools` 检查是否启用了该工具集 |
| `Gateway: disconnected` | 检查 bot token 是否正确，网络是否能连 Telegram |

### 网关日志

```bash
# 查看网关日志
journalctl -u hermes-gateway.service -n 50 -f    # systemd 服务
tail -f ~/.hermes/logs/gateway.log                # 原始日志
```

### 代理没有回复

1. 先 `/restart` 网关
2. 检查日志 `grep -i error ~/.hermes/logs/gateway.log`
3. 确认 bot 是群组管理员（如果在群组中使用）
4. 确认 BotFather 中关闭了 Privacy Mode：`/setprivacy` → 选择你的 bot → `Disable`
5. 在终端里直接 `hermes` 测试模型是否正常响应

---

## 新手常见误区

### 误区 1：装完就跑

装完 `hermes` 后第一件事应该是 `hermes setup` 配置模型和 tool。很多人直接 `hermes` 结果没配置 API Key，报错退出。

**正确顺序：**
```bash
curl -fsSL ... | bash    # 安装
hermes doctor            # 检查
# 编辑 ~/.hermes/.env 添加 API Key
hermes model             # 选择模型
hermes                   # 开始用
```

### 误区 2：切换模型后不重启

`/model claude-sonnet-4` 切换模型后，必须执行 `/new` 或 `/reset`，否则工具列表和系统提示词还是旧模型的——**不会自动刷新**。

### 误区 3：内存上限满了不知道

默认 `memory_char_limit` 是 2200 字符。代理写满后旧记忆会被自动删除。调大上限：

```bash
hermes config set memory.memory_char_limit 5000
hermes config set memory.user_char_limit 3000
```

### 误区 4：Windows 上直接用

Hermes 依赖大量 Linux 工具（git、systemd、bash）。Windows 用户必须用 WSL2。WSL2 上 systemd 需要额外配置：

```bash
# /etc/wsl.conf
[boot]
systemd=true
```

### 误区 5：没开代理就跑 Telegram 网关

在中国大陆，**Telegram Bot API 是被阻断的**。不配好代理就直接 `hermes gateway run`，网关能启动但收不到任何消息，看日志全是超时。

**正确做法：** 启动前设置 `http_proxy`，或在 systemd 服务文件中写入代理环境变量。

---

## 总结：5 分钟快速上手

```bash
# 1. 安装
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 2. 配置 API Key
echo 'OPENROUTER_API_KEY=sk-or-v1-xxxx' >> ~/.hermes/.env

# 3. 选择模型
hermes model        # 选 deepseek/deepseek-chat 或任意

# 4. 启动
hermes

# 5. 配置 Telegram（可选）
hermes gateway setup    # 输入 Bot Token
hermes gateway run      # 前台测试
```

**中国大陆用户额外步骤：**
```bash
# 先配 pip 镜像
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 安装时遇到 GitHub 慢用代理
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

# Telegram 网关需配代理
hermes gateway run    # 在代理环境下启动
```

---

*这篇文章是基于实际部署经验整理的。项目地址：[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)*
