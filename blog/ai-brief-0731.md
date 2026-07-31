---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0731.html"
title: '今日AI简报 — DeepSeek V4 Flash正式版发布、Gemini Robotics 2全身智能、Chrome用AI修复千余漏洞'
description: 'DeepSeek V4 Flash正式版发布，Terminal Bench从56.9跃升至82.7；Chrome 149/150两个版本用AI修复1072个安全漏洞；Google发布Gemini Robotics 2实现全身控制；FCC全面禁运外国机器人；Zoox获首个商用豁免。'
date: "2026-07-31"
tags: ["AI", "简报", "DeepSeek", "Gemini Robotics", "Chrome"]
---

# 今日AI简报 — DeepSeek V4 Flash正式版发布、Gemini Robotics 2全身智能、Chrome用AI修复千余漏洞

**2026年7月31日**

---

## 📡 数据源A：中文频道动态

**1. Codex 上线图像 Agent 专用 UI 模式**

来自 AI 探索指南频道（@aigc1024）：Codex 新增专为图像 Agent 设计的 UI 模式——生成图片后点击即可在侧边栏弹出预览窗口，支持直接评论、擦除和调整大小；左上角切换按钮可进入「纯图像流」模式，聊天流只显示图片；还支持多选图片一并加入输入框，让 GPT 批量修改。博主认为该交互专为 GPT Image 2.0 打造，比「无限画布」等复杂交互更易理解，或将蚕食设计 Agent 市场。
🔗 https://t.me/aigc1024/22707

**2. DeepSeek V4 Flash 上架 ColaOS Token Plan**

@aigc1024 消息：DeepSeek V4 Flash 现已上架 Cola 的 Token Plan 和积分模型，据称智能水平超过 GLM 5.2、接近 GPT 5.6 Luna（Max），官方表示可借此推出免费计划。这一消息与今日 DeepSeek 官方更新日志（见数据源B）互相印证。
🔗 https://t.me/aigc1024/22706

**3. Gemini Spark 接入 Chrome，可代填账号密码**

来自互联网从业者充电站（@https1024）：Gemini Spark 已接入 Chrome，获得用户授权后，可利用 Chrome 中已登录的账号和保存的密码完成网页任务。
🔗 https://t.me/https1024/49816

---

## 🌍 数据源B：国际AI要闻

**1. DeepSeek V4 Flash 正式版发布：Terminal Bench 56.9 → 82.7**

DeepSeek 官方更新日志（7月31日）将 V4 Flash 从 Preview 转正：Terminal Bench 从 56.9 跃升至 82.7（+25.8），Toolathlon 从 51.8 升至 70.3（+18.5）。与 GPT-5.6 Terra 互有胜负——Terminal Bench 82.7 vs 78.4 占优，DeepSWE 54.4 vs 69.6 落后。模型为 284B-A13B 的 MoE 开源权重，原生支持 Responses API 格式并针对 Codex 适配。Hacker News 热帖（369分）评价：以 Sonnet 级性能卖 GPT-3 级价格，缓存读取成本 $0.0028/MTok 仅为 GPT-5.6 Luna（$0.02）的约七分之一。
🔗 https://api-docs.deepseek.com/updates/

**2. Chrome 用 AI 修复安全漏洞：两个版本超此前 23 个版本总和**

Google 安全博客（7月30日）披露：Chrome 149 与 150 两个里程碑共修复 1,072 个安全漏洞，超过此前 23 个里程碑修复数量总和；基于 Gemini 的漏洞挖掘 agent 还发现了一个潜伏 13 年以上的沙箱逃逸漏洞。博客同时提出浏览器「持续动态修补、自动重启」的长期愿景——与中文社区今日热议的「Chrome 动态更新，安全补丁免重启」消息一致。
🔗 https://blog.google/security/chrome-stronger-with-every-update/

**3. LinkedIn 上线「Seems like AI slop」按钮**

LinkedIn 新增「看起来像 AI 垃圾内容」标记按钮，用户可对疑似 AI 生成的灌水内容进行标注。社区反应普遍正面，认为能帮助过滤平台上泛滥的 AI 生成帖。
🔗 https://thenextweb.com/news/linkedin-seems-like-ai-slop-button

**4. NYT 特稿：Larry Ellison 押注 AI 热潮**

《纽约时报》杂志发表长篇特稿，分析 Oracle 创始人 Larry Ellison 在 AI 浪潮中的巨额押注，探讨他是否会成为「AI 泡沫」的标志性面孔，以及 Oracle 云业务与 AI 基建深度绑定的风险与回报。
🔗 https://www.nytimes.com/2026/07/31/magazine/larry-ellison-ai-oracle.html

---

## 🤖 数据源C：机器人动态

**1. Gemini Robotics 2 发布：全身控制 + 灵巧操作 + 多机协作**

Google DeepMind（7月30日）发布 Gemini Robotics 2 系列三款模型：Gemini Robotics 2（VLA 模型，首次实现从脚到指尖控制完整人形机器人，可驱动 Apptronik Apollo 2 完成行走、下蹲、取放等全身动作）、Gemini Robotics ER 2（具身推理模型，支持多步任务规划与多机器人团队协作，已在 Google AI Studio 开放）、Gemini Robotics On-Device 2（可本地运行，仅需数小时数据即可适配全新机器人本体）。同一 checkpoint 可控制三种不同硬件。
🔗 https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

**2. FCC 全面禁令：不止人形机器人，扫地机器人也在列**

美国政府宣布禁止「先进机器人设备」进口，FCC 确认范围远超人形机器人：任何在地面移动、重量超过 4.4 磅、具备环境感知与无线连接的软件控制机器人——包括扫地机器人、割草机器人、 sidewalk 快递机器人和仓库搬运机器人——均被纳入禁令；已售产品不受影响，厂商被要求转向美国本土制造。
🔗 https://www.theverge.com/policy/972312/us-robot-ban-sweep-up-chinese-vacuums

**3. Zoox 获 NHTSA 首个商用豁免，8月起拉斯维加斯收费运营**

亚马逊旗下 Zoox 获得 NHTSA 为无方向盘 Robotaxi 颁发的首个商用豁免：两年内每年最多部署 2,500 辆，下月起在拉斯维加斯开始收费运营，之后扩展至更多城市。Zoox CEO 称这是「整个自动驾驶行业的重要里程碑」。
🔗 https://www.cnbc.com/2026/07/30/amazon-zoox-robotaxi-rides-las-vegas.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | DeepSeek V4 Flash 转正：Terminal Bench 82.7，开源权重对标 GPT-5.6 |
| ⛏️ **基础设施** | Chrome AI 修漏洞：两个版本 1,072 个，超此前 23 版总和 |
| 🤖 **AI Agent** | Codex 图像 Agent UI 模式；Gemini Spark 接入 Chrome 代填账号 |
| 🦾 **机器人** | Gemini Robotics 2 全身控制；FCC 禁运外国机器人；Zoox 获批商用 |

---

**本期简报涉及话题：** DeepSeek V4 Flash | Chrome 安全 | Codex | Gemini Robotics | FCC 机器人禁令 | Zoox
