---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0812.html"
title: '今日AI简报 — Gemini月活破10亿、xAI发布常驻云端Agent Grok Bot'
description: 'Gemini月活突破10亿成Google史上增长最快产品；xAI发布24/7常驻云端Agent Grok Bot（$120～200/月/人）；英伟达开源Nemotron 3.5 Lightning与NeMo Switchyard路由库；Anthropic为Claude输出内置隐形水印；OpenAI COO Brad Lightcap宣布离职。'
date: "2026-08-12"
tags: ["AI", "简报", "Gemini", "xAI", "Nvidia", "Anthropic", "OpenAI"]
---

# 今日AI简报 — Gemini月活破10亿、xAI发布常驻云端Agent Grok Bot

**2026年8月12日**

---

## 📡 数据源A：中文频道动态

### 1. 牛津团队论文走红：进化策略替代反向传播，RWKV-7 后训练提速约百倍

@aigc1024 频道消息：牛津大学团队的论文近日走红——用进化策略（Evolution Strategies）替代反向传播，将 RWKV-7 作为大规模并行后训练的主干。论文《Evolution Strategies at the Hyperscale》（arXiv:2511.16652，v2 于今日更新）：提出的 EGGROLL 方法把随机扰动结构化到低秩矩阵，将算术强度提升约百倍，billion 参数模型在大种群规模下训练速度提升约 100 倍，可达纯批推理吞吐的 91%；实验显示可实现纯整数数据类型循环语言模型的稳定预训练，后训练效果与 GRPO 相当。

🔗 https://t.me/aigc1024/23109 | 📄 https://arxiv.org/abs/2511.16652

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Gemini 月活突破 10 亿，成 Google 史上增长最快产品

Pichai 8月11日宣布 Gemini 月活跃用户达 10 亿，成为 Google 有史以来最快达到该里程碑的产品；其中 63% 的活跃用户使用语音输入，Gemini Live 用户中 20% 会共享摄像头与屏幕，每天生成约 1.5 亿张图片；iOS 端月活超 1 亿（需手动下载 App，非预装）。

🔗 https://arstechnica.com/ai/2026/08/google-says-gemini-has-reached-1b-users-faster-than-any-other-google-product/

### 2. 🤖 xAI 发布 Grok Bot：24/7 常驻云端 Agent

xAI 8月11日上线 Grok Bot：每个 Bot 拥有自己的「电脑」，可进驻用户的各类应用与工具中并行工作，7×24 小时运行、笔记本合盖也不中断；定价 $120/200 美元每月每员工（两档）。HN 讨论（300+ 分）焦点是数据信任——让第三方 Agent 常驻访问全部文件与账户的隐私风险。

🔗 https://x.ai/bot

### 3. ⛏️ 英伟达开源 Nemotron 3.5 Lightning 与 NeMo Switchyard 路由库

英伟达 8月11日发布 Nemotron 3.5 Lightning：30B 参数的 MoE 开源模型，面向长时运行 Agent 的高频专项任务（代码审查、工具调用、安全告警监控等），输出速度最高 4 倍、Agent 任务完成快 30%；同期发布 NeMo Switchyard——开源模型路由库，可在自有、开源与闭源模型之间智能分配请求，无需重写应用。

🔗 https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/

### 4. 🛡️ Anthropic 为 Claude 文本与图片内置隐形水印

Anthropic 宣布自 8月2日及之后发布的模型起，在 Claude 生成的文本中嵌入不可见、机器可读的水印信号：肉眼不可见、不影响可读性，随复制粘贴传播且能承受部分编辑（大幅改写或翻译可能失效）；水印位于模型层，聊天、API 与 Claude Code 全渠道生效，图片同样带水印。此举与 8月2日生效的欧盟 AI 法案透明度条款对齐。

🔗 https://fortune.com/2026/08/11/anthropic-claude-watermark-ai-text-police-ai-slop/

### 5. 🏢 OpenAI 高管震动：COO Brad Lightcap 离职，伦理负责人同周出走

8月11日 Brad Lightcap 在内部信（并公开于 X）中宣布离开 OpenAI「去开创一些新东西」：他 2018 年加入，任 CFO 四年、2022 年起任 COO，今年早些时候转任特殊项目负责人；此前与 Sam Altman 同在 Y Combinator。同周 FT 报道 OpenAI 伦理负责人也在入职不到一年后离职。

🔗 https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Gemini 月活破 10 亿，成 Google 史上增长最快产品 |
| 🤖 **AI Agent** | xAI 发布 Grok Bot：24/7 常驻云端 Agent，$120～200/月/人 |
| ⛏️ **基础设施** | 英伟达 Nemotron 3.5 Lightning（30B MoE）+ NeMo Switchyard 路由库 |
| 🛡️ **安全/合规** | Anthropic 为 Claude 输出内置隐形水印，对齐 EU AI Act |
| 🏢 **公司动态** | OpenAI COO Brad Lightcap 离职，伦理负责人同周出走 |
