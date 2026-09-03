---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0903.html"
title: '今日AI简报 — Google发布Gemini 3.8 Flash与Flash Cyber、Meta推出Muse Spark 1.3'
description: 'Google发布Gemini 3.8 Flash与3.8 Flash Cyber——六周内第三个Flash版本，长程编码逼近前沿大模型，Cyber变体漏洞发现与修补达前沿水平、仅限可信防御者；Meta推出Muse Spark 1.3（工具调用少约20%）；美国司法部在纽约时报诉OpenAI案中支持训练数据合理使用立场；盛大陈大年携27B本地模型StartLux回归。'
date: "2026-09-03"
tags: ["AI", "简报", "Gemini", "Meta", "OpenAI", "版权"]
---

# 今日AI简报 — Google发布Gemini 3.8 Flash与Flash Cyber、Meta推出Muse Spark 1.3

**2026年9月3日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Google 发布 Gemini 3.8 Flash 与 3.8 Flash Cyber

9月2日，Google 发布 Gemini 3.8——距 3.7 Flash 仅三周，是六周内第三个 Flash 版本，官方称其为「迄今最强的推理与编码模型」，速度与成本与 3.7 持平。两个变体共享同一基础智能：**3.8 Flash** 面向长程编码与自主智能体，DeepSWE v1.1 长程软件工程评测上超越多数更大的前沿模型，Vals 金融 Agent V2、Harvey 法律 Agent 基准领先，HLE-Verified 得分 54.9%；**3.8 Flash Cyber** 面向网络安全——CyberGym 自主漏洞发现达前沿水平，内部 20 种语言真实代码库漏洞发现成功率超 70%，CWE-Bench 漏洞修补 pass@1 47.2%（对照某前沿模型 47.8%，成本显著更低），设计上优先防御性修补而非攻击利用，仅通过 Fairwind 计划向可信防御者开放。2027 年 1 月起定价 $1.50/$7.50 每百万输入/输出 token（介绍期定价持续至 2026 年底）。

🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/

### 2. Meta 发布 Muse Spark 1.3

Meta 9月2日发布 Muse Spark 1.3（0806 简报曾覆盖 1.2 代，本次为版本升级新进展），即日在 Muse Code 与 Meta Model API 上线。相比 1.2，Meta 工程师实测工具调用减少约 20%、token 消耗减少约 25%；长程多任务场景下指令遵循更可靠，能主动澄清歧义、卡住时求助、执行重要操作前先确认，抗 prompt 注入的对抗鲁棒性增强。max reasoning 模式将在安全测试完成后推出；官方路线图提及更大的模型与 Muse Spark 开源权重（同门 30B 本地模型 Muse Glimmer 已于 8 月开源）。该消息在 HN 获 600+ 分，社区评测（Artificial Analysis）显示其超越 Google 前沿模型。

🔗 https://research.meta.ai/blog/introducing-muse-spark-1-3 · https://developer.meta.com/ai/models/muse-spark/

### 3. ⚖️ 美国司法部在版权诉讼中支持 OpenAI

9月2日，特朗普政府在《纽约时报》诉 OpenAI 案中提交 20 页利益声明，为 OpenAI 未经授权使用版权材料训练模型辩护：主张 LLM 训练属于「转换性」合理使用，「对合理使用原则的误解性限制将扼杀创造性进步、阻碍美国繁荣」，并称维持全球 AI 领导地位是美国的核心利益（援引 2025 年 AI 行政令）。这是美国政府在「AI 训练数据是否合法」这一核心争议上迄今最明确的官方表态。

🔗 https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/ · https://www.nytimes.com/2026/09/02/technology/justice-department-openai-copyright-suit.html

### 4. 🇨🇳 陈大年携 27B 本地模型公司 StartLux 回归

盛大网络联合创始人、连尚网络（WiFi 万能钥匙）掌门人陈大年，隐退多年后携新公司 StartLux（原「原点星汇」）重回大模型赛道。首款模型 StartLux-V1.0-27B-Preview 在中国信通院可信 AI 大模型评测 MCP 专项（地点导航、浏览器自动化、金融分析等六类真实 Agent 任务）综合得分 39.25% 位列第二——距榜首、1.6 万亿参数的 DeepSeek-V4-Pro 仅差 1.3 个百分点，并拿下地点导航、金融分析、浏览器自动化三项单项第一；27B 同规模下比 Qwen 3.6 高出 5.34 个百分点。公司主打「真·本地模型」：不依赖云端、可在消费级 PC 直接运行，年内计划推出企业/个人用户一键部署的本地智能解决方案。

🔗 https://chinaonchina.com/article/chen-dawei-returns-enters-the-large-model-sector（转引量子位）

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Google 发布 Gemini 3.8 Flash/Cyber，六周内第三个 Flash 版本 |
| 🤖 **模型** | Meta 推 Muse Spark 1.3：工具调用 −20%、token −25% |
| ⚖️ **政策** | 美司法部支持 OpenAI：版权材料训练属合理使用 |
| 🇨🇳 **中国动态** | 陈大年携 27B 本地模型 StartLux 回归，MCP 评测紧咬 DeepSeek-V4-Pro |
