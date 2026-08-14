---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0814.html"
title: '今日AI简报 — Gemini 3.7 Flash、GLM-5.3发布、DeepSeek调价落地'
description: 'Google发布Gemini 3.7 Flash（DeepSWE 65.3%、首发价减半）；智谱发布GLM-5.3（纯后训练迭代、涌现网络攻防能力、两周后开源）；DeepSeek开源Agent框架Harness并公布峰谷调价方案（8月17日生效，闲时最高涨500%）；OpenAI×Cerebras推出GPT-5.6 Sol Ultrafast（最高750 tokens/秒）。'
date: "2026-08-14"
tags: ["AI", "简报", "Gemini", "GLM", "DeepSeek", "Cerebras"]
---

# 今日AI简报 — Gemini 3.7 Flash、GLM-5.3发布、DeepSeek调价落地

**2026年8月14日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Google 发布 Gemini 3.7 Flash：Flash 系列最强「工作马」模型

8月13日上线，距 3.6 Flash 仅三周，专注编程与 Agent 工作流：FrontierCode 1.1 Main 达 43.6%（3.6 为 34.4%）、DeepSWE v1.1 65.3%（49.0%）、WebDev Arena Elo 1588（1538）、GDP.pdf 34.0%（22.0%）、AutomationBench 30.4%（17.0%）。首发价 $0.75/百万输入、$3.75/百万输出 Token——为 3.6 Flash 原价一半，优惠至年底，2027 年 1 月起恢复 $1.50/$7.50。

🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/

### 2. 🔥 智谱发布 GLM-5.3：纯后训练迭代，涌现网络攻防能力

与 5.2 同基座、全部提升来自后训练扩展：Z.ai Code Bench 相对 5.2 提升 50%，Terminal Bench 2.1 得 88.2（超 Claude Opus 4.8 的 85.0，逼近 GPT-5.6 Sol 的 88.8），Terminal Bench 3.0 与 Agents' Last Exam 均达开源模型 SOTA；官方称攻防能力「涌现」速度超预期——CyberGym 84.5 开源最佳，ExploitBench 54.4，为 5.2（24.4）的两倍多。权重将在安全评估完成后约两周开源。

🔗 https://z.ai/blog/glm-5.3

### 3. 🧰 DeepSeek 开源 Agent 框架 Harness（开发者预览）

「Everything is a plugin」：基于 Cordis 内核，模型、工具、技能、会话、沙箱、存储、调度、UI 全部插件化，可配置替换而无需改源码；每次运行写入 append-only 会话日志（提示词、推理、工具调用、子 Agent 调度全记录），支持 Trajectory 视图回放/续跑/分叉；提供 Standard/Code/Minimal/Creator 四种运行模式，源码已放 GitHub。V4 Pro 正式版即依托 Harness 完成专项优化。

🔗 https://deepseek.com/harness/en/

### 4. 💰 DeepSeek 公布调价方案：峰谷定价 8 月 17 日生效

昨日已报道 V4 Pro 转正未调价，今日官方公布新 API 定价（北京时间 8 月 17 日 0 时生效）：高峰时段（9:00-12:00、14:00-18:00）价格为闲时两倍；闲时 V4 Pro 缓存命中输入 0.025→0.15 元/百万 Token（+500%）、未命中输入 3→4.5 元、输出 6→13.5 元——闲时最小涨幅 50%，峰值缓存命中档相对旧价约 12 倍（社区称「最高涨价 1000%」）。

🔗 https://api-docs.deepseek.com/news/news260813/

### 5. 🚀 OpenAI × Cerebras 推出 GPT-5.6 Sol Ultrafast：最高 750 tokens/秒

8月13日公布：OpenAI API 新增 Ultrafast 服务档位，由 Cerebras 晶圆级芯片（44GB 片上 SRAM）驱动，首批受邀客户预览，最高 750 输出 tokens/秒且「无质量损失」；官方测试中 HLE 全部 2500 题用时 11 小时 11 分，Claude Fable 5 需 78 小时 27 分（约快 7 倍、精度相当）；据 Artificial Analysis，输出速度比 Fable 5 快 11 倍、比 Opus 4.8（Fast 模式）快 5 倍。

🔗 https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Gemini 3.7 Flash 发布（DeepSWE 65.3%、首发价减半） |
| 🇨🇳 **中国动态** | 智谱 GLM-5.3 发布（涌现攻防能力）；DeepSeek Harness 开源 + 调价落地 |
| 💰 **价格动态** | DeepSeek 峰谷定价 8/17 生效，闲时最高涨 500% |
| ⚡ **基础设施** | OpenAI×Cerebras GPT-5.6 Sol Ultrafast（750 tok/s） |
