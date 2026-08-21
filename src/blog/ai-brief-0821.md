---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0821.html"
title: '今日AI简报 — DeepSeek发布视觉模型、OpenAI推零数据留存'
description: 'DeepSeek发布deepseek-v4-flash-vision-exp视觉实验模型（支持图文输入、三种传图方式）；OpenAI推出零数据留存ZDR并预览隐私保护安全系统，与Anthropic的30天留存政策形成对照；Codex用户突破2000万、开源harness升级为平台；据报Poolside与英伟达达成60亿美元授权协议；Gemini 3.7 Flash通过ARC-AGI官方验证（95.5%/84.6%）；宇树发布2米跳高「超人」机器人；SUPCON机器人交警上岗杭州。'
date: "2026-08-21"
tags: ["AI", "简报", "DeepSeek", "OpenAI", "Codex", "宇树"]
---

# 今日AI简报 — DeepSeek发布视觉模型、OpenAI推零数据留存

**2026年8月21日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 DeepSeek 发布 v4-flash-vision-exp：首个视觉实验模型上线

DeepSeek 官方 API 文档上线 `deepseek-v4-flash-vision-exp` 视觉模型（HN 130 分）：可同时接受图片与文本输入，用于描述图片、读取截图文字、分析图表等；支持 JPEG/PNG/GIF/WebP，兼容 OpenAI 的 Chat Completions 与 Responses API。传图有三种方式：base64 内联（请求体上限 48 MiB）、外链 URL（单图 ≤32 MiB、下载限时 60 秒）、Files API 文件引用（单图可至 64 MiB）。

🔗 https://api-docs.deepseek.com/guides/vision/

### 2. 🔐 OpenAI 推出零数据留存（ZDR）：前沿模型 API 处理完即弃，并预览「隐私保护安全系统」

OpenAI 8月19日宣布向符合条件的 API 客户开放 Zero Data Retention（零数据留存）：使用前沿模型时，提示与输出在处理后不再留存、也不进入滥用监控日志，员工无法审阅客户内容，企业 API 数据默认不用于训练；ZDR 下 `store` 被强制置为 false，数据可存放在客户自有基础设施，或由客户密钥加密的 OpenAI 基础设施上。公司同时预览「Private Safety Processing」安全机制——在不接触客户内容的前提下跨交互识别滥用模式。对照鲜明的是，竞争对手 Anthropic 对企业客户使用 Fable 5 与 Mythos 5 实施了 30 天留存政策。

🔗 https://openai.com/index/offering-zero-data-retention-for-frontier-models/ · https://www.axios.com/2026/08/19/openai-previews-zero-retention-safety-system-as-anthropic-requires-data-logs

### 3. 💻 Codex 用户突破 2000 万，开源 harness 升级为开发平台

OpenAI 官方开发者博客发布《Codex as a platform》：宣布将 Codex 的开源 agent harness 作为平台向开发者开放，提供 `codex exec`（非交互任务）、Codex SDK（编程式 agent 工作流）与 Codex app-server（持久会话/流式事件/审批处理）三种集成方式；同日 OpenAI 工程师 thsottiaux 发帖称 Codex 用户总数已达 2000 万，并向所有账户发放累积的重置额度。Codex 从「编程助手」向「可嵌入自有产品的 agent 运行时」演进。

🔗 https://developers.openai.com/blog/codex-as-a-platform

### 4. 💰 据报 Poolside 与英伟达达成 60 亿美元授权协议，另获 10 亿美元投资

Newcomer 独家报道（基于其获得的投资者信函）：AI 编程模型公司 Poolside AI 与英伟达签署 60 亿美元非独占授权协议，英伟达同时以 120 亿美元投前估值向 Poolside 投资 10 亿美元。交易尚未获两家公司官方确认。

🔗 https://www.newcomer.co/p/sources-poolside-strikes-6-billion

### 5. 🧠 Gemini 3.7 Flash 通过 ARC-AGI 官方验证：95.5% / 84.6%

ARC Prize 官网发布 Google Gemini 3.7 Flash 验证成绩（高努力档）：ARC-AGI-1 Semi-Private 得分 95.5%（每任务 $0.12），ARC-AGI-2 Semi-Private 84.6%（$0.25/任务）——后者较 0808 简报报道的 DeepSeek V4 Flash 0731（61.4%）高出 23 个百分点。0814 简报发布时该模型主打编码（DeepSWE 65.3%），此次抽象推理成绩为新增数据点。

🔗 https://arcprize.org/results/google-gemini-3-7-flash

---

## 🤖 数据源C：人形机器人动态

### 1. 🇨🇳 宇树发布「超人」机器人：2 米立定跳高、12.66 m/s 冲刺

宇树科技 8月17日公布新一代人形机器人（官方视频《Superman – Breaking the Limits of Humanity》）：腿部仅 0.85 米长，却完成 2 米立定跳高并以 12.66 m/s 极速冲刺——两项均超人类纪录（博尔特峰值速度约 12.42 m/s），落地稳定；公司称该全新机型仅用三个多月开发，仍有大幅提升空间。另据宇树 8月12日口径，公司迄今累计生产双足仿人人形机器人约 1.8 万台。上市首日暴涨后（0820 已报道），宇树以性能极限测试继续刷屏。

🔗 https://www.globaltimes.cn/page/202608/1368390.shtml · https://www.youtube.com/watch?v=O7OkiZfIlS4

### 2. 🇨🇳 SUPCON 机器人交警上岗杭州：5 个月发出 17 万次警告

路透社 8月20日报道：中控信息（SUPCON）开发的 T2 机器人交警在杭州路口执勤——1.88 米高、98 公斤，靠摄像头/雷达/车载计算识别未戴头盔骑手、越线停车与闯红灯行人，机械臂随信号灯同步打出交警手势，还能指路答疑、紧急呼叫当地警方；每日 7 时至 18 时在路口间自主移动，无需遥控。公司称自 5 月以来已在杭州部署 15 台、累计发出超 17 万次警告，相关违规月均下降逾 40%（路透未能独立核实）；全国约 8 城 3 省已部署近 50 台，年底预计接近 200 台。

🔗 https://www.reuters.com/technology/china-puts-robocops-traffic-duty-minus-arrest-powers-2026-08-20/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | DeepSeek 发布 v4-flash-vision-exp 视觉实验模型 |
| 🔐 **隐私/政策** | OpenAI 零数据留存 vs Anthropic 30 天留存 |
| 💻 **开发者平台** | Codex 用户破 2000 万，开源 harness 平台化 |
| 💰 **行业整合** | 据报 Poolside×英伟达 60 亿美元授权 |
| 🤖 **机器人** | 宇树 2 米跳高「超人」；SUPCON 机器人交警 |
