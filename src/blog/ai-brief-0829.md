---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0829.html"
title: "今日AI简报 — OpenAI终止向Cursor供模型、Anthropic发布MHS硬件标准"
description: "OpenAI通知SpaceX将终止向Cursor供应模型（拟11月12日断供）；Anthropic发布模型硬件标准MHS研究预览；Google推出Gemini Omni 1.1 Flash视频模型；阿里发布Qwen3.8-Flash并开源；智谱开放GLM-5.3权重；Meta数据中心机器人实验曝光。"
date: "2026-08-29"
tags: ["AI", "简报", "OpenAI", "Anthropic", "谷歌", "阿里", "智谱"]
---

# 今日AI简报 — OpenAI终止向Cursor供模型、Anthropic发布MHS硬件标准

**2026年8月29日**

---

## 📡 数据源A：中文频道动态

### Seedance 2.5 视频成本讨论：30 秒视频 7.1 美元 vs 一百多元人民币

出海运营频道 @yunying23 讨论 Seedance 2.5 的生成成本：作者自述同样 30 秒视频成本为 7.1 美元（折合不到 50 元人民币），而不少人反映要花一百多元——猜测是生成内容复杂度不同导致成本差异，或有人被第三方平台加价。

🔗 https://t.me/yunying23/11303

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 OpenAI 通知 SpaceX：将终止向 Cursor 供应模型

8月28日 OpenAI 宣布已通知 SpaceX，拟于 2026 年 11 月 12 日停止向 Cursor 提供 OpenAI 模型——按合同给出了最长通知期，期间继续供应。理由是无法确信 SpaceX 会遵守服务条款：马斯克旗下公司曾有违约前科（收购 Twitter 后撕毁合同），且今年早些时候马斯克在宣誓下承认 xAI 蒸馏过 OpenAI 数据。OpenAI 称将尽力支持受影响的开发者，双方合作已近四年。

🔗 https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/

### 2. Anthropic 发布「模型硬件标准」MHS：面向硬件的 MCP

8月27日 Anthropic 以研究预览形式发布 Model Hardware Standard（MHS），为 AI 模型与科研、机器人、制造硬件之间建立统一接口层，被称作「硬件版 MCP」——开发者可让 Claude 直接操作显微镜、机械臂、量子计算机等设备。官方称该标准可将科学实验耗时从数周缩短到数天，让实验室设备「开箱即用」接入模型驱动的工作流。

🔗 https://finance.sina.com.cn/tech/roll/2026-08-28/doc-inipvmnh0287214.shtml · https://www.theregister.com/ai-and-ml/2026/08/28/anthropic-proposes-plumbing-spec-to-link-ai-agents-to-lab-kit-and-robots/5293135

### 3. Google 发布 Gemini Omni 1.1 Flash 视频生成模型

8月27日发布：可分析最长 10 秒的此前视频内容、以 10 秒为增量续写至 40 秒（前代仅参考最后 1 秒）；支持首尾帧控制以生成更平滑转场；新增 360p 预览模式，生成速度最高提升 60%、成本约为 720p 的三分之一；最终输出最高 4K。API 定价：360p $0.03/秒、720p $0.10/秒、1080p $0.15/秒、4K $0.30/秒；Adobe Firefly、Figma Weave、Runway 等平台已接入。

🔗 https://ai.google.dev/gemini-api/docs/omni

### 4. 阿里通义发布 Qwen3.8-Flash，并开源 Flash-Next 权重

8月26日晚发布：多模态 MoE 模型，主模型 125B 参数、每 token 激活 6B，配备 51B N-gram Embedding，支持百万级上下文；训练成本约为上一代 Qwen3.7-Plus 的九分之一，在 14 项基准测试中 8 项取得最佳（MMLU-Pro、SuperGPQA、BBH、SWEBench-Pretrain、MGSM、MMMU 等）。同步开源 Qwen3.8-Flash-Next 权重——采用 GDN 与 QSA 混合注意力等新架构，官方称提前公开了下一代 Qwen4 架构的部分设计供社区研究。

🔗 https://www.bjnews.com.cn/detail/1787921654019285.html

### 5. 智谱正式开放 GLM-5.3 权重：主打智能体编程与网络防御

8月28日智谱开放 GLM-5.3 模型权重（8月14日 API 首发时预告约两周后开源，因后训练中网络安全能力增长快于预期、需补做安全评估而推迟）。官方称这是 GLM 系列在智能体编程与网络防御方面能力最强的模型，AA 综合智能指数 60 分；支持自由下载、本地部署与微调，大型云厂商商用托管需经智谱审核。0814 简报曾预告权重开源，0827 报道了 GLM-5.3-Flash 开源，本次为旗舰模型本体权重落地。

🔗 https://huggingface.co/zai-org/GLM-5.3 · https://app.myzaker.com/news/article.php?pk=6a924f87b15ec041cd47236c

---

## 🤖 数据源C：人形机器人动态

### 1. Wired 曝光：Meta 正在数据中心测试机器人

Wired 8月28日独家报道（此前未披露）：Meta 正测试机器人执行插拔线缆、服务器断电重启等原由技术人员承担的工作，供应商包括 Watney Robotics、Kinova、ABB——其中 Kinova Gen3 机械臂用于服务器断电（power cycling）测试，另有形似「手指」的简易机器人可远程触发设备重启。一名数据中心员工估计，若成功可替代部分岗位高达 80% 的工作量；Meta 未予置评，发言人强调公司仍在大量招聘数据中心员工。

🔗 https://www.wired.com/story/inside-metas-experiments-with-data-center-robots/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | OpenAI 拟终止向 Cursor 供应模型（SpaceX 收购后断供） |
| ⛏️ **基础设施** | Anthropic 发布 MHS 硬件标准，Claude 可操控实验设备 |
| 🤖 **AI Agent** | Gemini Omni 1.1 Flash 视频生成；Meta 数据中心机器人实验 |
| 🇨🇳 **中国动态** | 阿里 Qwen3.8-Flash 发布并开源；智谱开放 GLM-5.3 权重 |
