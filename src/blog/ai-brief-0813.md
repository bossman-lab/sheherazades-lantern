---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0813.html"
title: '今日AI简报 — Qwen3.8-Max权重开源、DeepSeek V4 Pro转正、Grok 4.6发布'
description: '阿里兑现承诺开源Qwen3.8-Max权重（2.4T参数/95B激活，PaperBench 93.0超越GPT-5.6 Sol）；DeepSeek V4 Pro正式版0813上线（1M上下文/384K输出，价格未调）；xAI发布Grok 4.6追平GPT-5.6 Sol；OpenAI上线ChatGPT/Codex Linux桌面客户端；宇树IPO获8000倍超额认购。'
date: "2026-08-13"
tags: ["AI", "简报", "Qwen", "DeepSeek", "xAI", "OpenAI", "宇树"]
---

# 今日AI简报 — Qwen3.8-Max权重开源、DeepSeek V4 Pro转正、Grok 4.6发布

**2026年8月13日**

---

## 📡 数据源A：中文频道动态

### 1. @aigc1024 整理第一期「审美在线」照片类 Skill 合集

频道发布第一期 Skill 推荐，聚焦视觉/照片类共 6 个：photo-abstract-editorial（保留照片真实内容，提炼空间关系、构图节奏与色彩关系）、heytea-style（喜茶风格海报生成）、gc-minimal-zine-poster（把主题/句子/构想转化为 zine 纸张质感极简编辑海报）、ip_illustration_for_yourself（个人 IP 萌粒风插画）、photo-revival（把随手拍/废片重绘成诗性手绘插画）、tait-crt-interface-skill（早期计算机界面质感复古插画）。

🔗 https://t.me/aigc1024/23144

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 阿里兑现承诺：Qwen3.8-Max 权重正式开源，2.4T 参数上线 Hugging Face

Qwen3.8-2.4T-A95B 权重仓库正式上线 HF——8月3日简报曾报道 Qwen3.8-Max 发布并预告「下周开源 Max 级权重」，今日兑现：2.4T 总参数 / 95B 激活 MoE，纯文本模型、强制思考模式，支持 reasoning_effort（xhigh/medium/low）与 preserve_thinking；官方基准中 PaperBench 得分 93.0，超过 GPT-5.6 Sol 的 90.5，Terminal Bench 2.1 达 86.6，多项目 agent 编程/办公基准对齐或超越 Claude Opus 4.8。

🔗 https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B

### 2. 🔥 DeepSeek V4 Pro 转正：0813 正式版上线，1M 上下文 / 384K 输出

DeepSeek 官方 API 8月13日凌晨将 deepseek-v4-pro 对应版本更新为 DeepSeek-V4-Pro-0813，旗舰模型从预览进入正式发布（HN 963 分）：支持 1M Token 上下文、最大 384K Token 输出及 Tool Calls 等能力；价格未随转正上调（缓存命中输入 ¥0.025/百万 Token，未命中输入 ¥3/百万，输出 ¥6/百万），尽管官方此前公告计划整体调价。七牛云等 MaaS 平台已同步上线。

🔗 https://openrouter.ai/deepseek/deepseek-v4-pro-0813

### 3. 🤖 xAI 发布 Grok 4.6：强化长时运行 Agent 与视觉交互

Grok 4.6（8月12日）在 Grok 4.5 基础上重点强化长时 Agent 任务与视觉/交互工作：官方称 Artificial Analysis 智能指数追平 GPT-5.6 Sol，擅长把宽泛产品想法一步搭成可运行初版；即日起上线 Cursor、Grok Build 与 API（OpenRouter、Vercel、Cloudflare 同步），定价 $2/百万输入、$6/百万输出 Token，快档翻倍，首周 Grok Build 与 Cursor 内用量 2 倍。

🔗 https://x.ai/news/grok-4-6

### 4. 💻 OpenAI 上线 ChatGPT Desktop（Codex）Linux 客户端

OpenAI 发布 ChatGPT/Codex 桌面客户端 Linux 版（HN 230 分）：与编辑器、终端、网页端共享同一 ChatGPT 账户与工作流；社区讨论两极——有用户已在 Debian/KVM 下正常使用，也有人提醒将其视为高风险程序隔离运行（近期 Agent 安全事件频发背景下，对桌面端 Agent 的信任存疑）。

🔗 https://openai.com/codex/

### 5. 🛡️ 昨日已报道 Claude 内置水印，今日用户反弹

昨日简报报道 Anthropic 为 Claude 输出内置隐形水印；今日 TechCrunch 报道用户不满情绪发酵：水印让「用 Claude 写作业/写周报」更难掩饰，被部分用户视为抓作弊工具，而非防 AI 垃圾文本的手段。

🔗 https://techcrunch.com/2026/08/12/some-claude-users-are-mad-that-anthropics-new-watermarks-will-catch-them-cheating-at-their-jobs-classes/

---

## 🤖 数据源C：人形机器人动态

### 1. 宇树科技科创板 IPO 获 8000 倍超额认购

Reuters 8月10日：宇树（688836.SS）9 亿美元上海 IPO 获散户超 8000 倍超额认购，中签率约 0.018%（机构份额回拨后）；发行价 150.80 元（约 $22.36），估值超 600 亿元人民币，将成为中国首家境内上市的人形机器人公司；券商认为高估值发行或带动机器人板块整体重估。

🔗 https://www.reuters.com/world/asia-pacific/unitrees-shanghai-ipo-more-than-8000-times-oversubscribed-by-retail-investors-2026-08-10/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Qwen3.8-Max 权重正式开源（2.4T-A95B，PaperBench 93.0 超 GPT-5.6 Sol） |
| 🇨🇳 **中国动态** | DeepSeek V4 Pro 转正（1M 上下文/384K 输出）；宇树 IPO 超购 8000 倍 |
| 🤖 **AI Agent** | Grok 4.6 发布，AA 智能指数追平 GPT-5.6 Sol |
| 💻 **开发者工具** | OpenAI 发布 ChatGPT/Codex Linux 桌面客户端 |
| 🛡️ **安全/合规** | Claude 水印上线次日遭用户反弹 |
