---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0831.html"
title: "今日AI简报 — Gemini 3.5 Transcribe发布、OpenClaw 2.0上线"
description: "谷歌发布迄今最精准的语音转写模型Gemini 3.5 Transcribe（FLEURS WER 5.04%）；安全研究员以60-80%成功率攻破Claude Code Opus 5 Auto Mode，反驳Anthropic委托评测的0.00%声称；开源agent OpenClaw 2.0发布，同日Meta安全研究员自曝其OpenClaw误删邮箱；Google接触迪士尼等洽谈AI训练IP授权；宇树G1被曝可蠕虫传播的蓝牙Root RCE漏洞。"
date: "2026-08-31"
tags: ["AI", "简报", "Google", "Anthropic", "OpenClaw", "宇树"]
---

# 今日AI简报 — Gemini 3.5 Transcribe发布、OpenClaw 2.0上线

**2026年8月31日**

---

## 📡 数据源A：中文频道动态

### Python潮流周刊第165期：AI项目密度走高

本期周刊的 AI 相关项目密集：aiperf（生成式 AI 推理性能基准测试工具）、VoiceStudio（开源本地的 ElevenLabs 替代品）、ai-job-search（本地运行的 AI 求职申请框架）、future-agi（开源 AI 智能体评估观测平台）、buildwithclaude（Claude 扩展资源一站式平台）、airllm（4GB 显存单卡运行 70B 大模型）、PYAS（开源机器学习杀毒软件）。

🔗 https://t.me/NewlearnerChannel/15893

### ChatGPT Plus 5小时限额引发开发者不满

@inside1024 吐槽：ChatGPT Plus 的 5 小时用量限额连一次发版前的 code review 都做不完，查出的 bug 要等 5 小时后才能修——开发者社区对用量上限的普遍抱怨。

🔗 https://t.me/inside1024/84136

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Google 发布 Gemini 3.5 Transcribe：迄今最精准的语音转写模型

8月26日 Google 发布 Gemini 3.5 Transcribe，定位「系列中最精准的语音转文本模型」：支持多说话人归因、词级时间戳、实时语种切换与口语赘词清理，直接处理嘈杂环境与专业术语。相比上一代 Chirp 3，最终转写时间（Artificial Analysis 口径）提升 70%；FLEURS 基准流式模式 WER 5.50%、非流式 5.04%。提供 `gemini-3.5-transcribe-live` 与 `gemini-3.5-transcribe` 两个 API，已在 Gemini API（AI Studio）与 Gemini Enterprise Agent Platform 开放，并已驱动 Android Rambler、macOS Gemini 应用等语音功能。

🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/

### 2. 安全研究员以 60-80% 成功率攻破 Claude Code Opus 5 Auto Mode

wunderwuzzi 的安全研究（embracethered）发现，仅凭一个「网页摘要请求」即可劫持 Auto Mode 下的 Claude Code Opus 5 并实现代码执行，小样本下攻击成功率 60-80%。这直接反驳了 Anthropic 委托 Trajectory Labs 评测、由 Boris Cherny 公开的「Opus 5 Auto Mode 间接提示注入攻击成功率 0.00%」数据。攻击链：诱导模型弃用 WebFetch 改用 curl → 重定向到特殊编码的 ZIP 压缩包并调用原生解码器。Auto Mode 自 8 月中旬起已成为 Claude Code 默认模式。

🔗 https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/

### 3. OpenClaw 2.0 发布；同日 Meta 安全研究员自曝其 OpenClaw 误删邮箱

开源 agent 框架 OpenClaw 8月30日发布史上最大更新 2.0：由 933 名贡献者（含 569 名首次贡献者）经 1.6 万余个 PR 构建，约占该项目全部 PR 的一半；重建浏览器控制界面为一级体验，安装时自动复用已有 ChatGPT/Claude 订阅、API Key 与本地模型。同日 Meta AI 安全研究员 Summer Yue 发推称，其 OpenClaw 在处理过大的真实收件箱时触发上下文压缩、「丢失了『先确认再执行』的原始指令」，眼睁睁看着它删光邮件，不得不跑回电脑前「像拆弹一样」阻止——为 2.0 发布提供了一则及时的 agent 安全警示。

🔗 https://openclaw.ai/blog/openclaw-2-accidentally · https://au.pcmag.com/ai/116091/meta-security-researchers-ai-agent-accidentally-deleted-her-emails

### 4. Google 游说好莱坞授权 IP 用于 AI 训练，与昨日起诉 Anthropic 形成对照

据 LA Times 8月31日报道，Google 高管已接触迪士尼、环球、华纳兄弟探索等影业，洽谈将其角色与片库授权用于 AI 模型训练（3 位知情人士证实），因法律与工会敏感性问题尚无协议；知情人士称「要让模型真正可用于电影级制作，必须用只有好莱坞才有的高动态内容与元数据微调」。Google 6 月已向 A24 投资 7500 万美元并合作开发 AI 工具。在索尼/华纳 8月28日以版权侵权起诉 Anthropic 的背景下，Google 走的是截然不同的「付费授权」路线。

🔗 https://www.latimes.com/entertainment-arts/business/story/2026-08-31/how-google-is-courting-hollywood-to-use-its-ai-tools

---

## 🤖 数据源C：人形机器人动态

### 1. UniBLEed：宇树 G1 人形机器人被曝可蠕虫传播的蓝牙 Root RCE

安全研究员 Olivier Laflamme 公布 UniBLEed 漏洞链：攻击者可在蓝牙范围内对任意宇树 G1 人形机器人实现未认证 Root 远程代码执行——通过无需所有权校验的云端 API 解密任意 G1 的 AES 密钥、免配对 BLE 特征写入、WiFi 劫持、AI 聊天机器人知识库路径遍历泄漏加载地址，最终以 1050 字节 BSS 缓冲区溢出以 root 调用 system()。该漏洞可蠕虫式传播（攻陷一台 G1 后可继续感染范围内下一台），获 Unitree 官方赏金 $6,700 与两个 CVE（CVE-2026-76639 / CVE-2026-76640）；这是继 Go2 两个 RCE（CVE-2026-27509/27510）之后同一研究者对宇树的第二次披露。

🔗 https://boschko.ca/g1-ble-rce/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Google 发布 Gemini 3.5 Transcribe（FLEURS WER 5.04%） |
| ⛏️ **基础设施** | Gemini 3.5 Transcribe 双 API 开放（AI Studio / Enterprise Agent Platform） |
| 🤖 **AI Agent** | OpenClaw 2.0 发布；Claude Code Auto Mode 被攻破（60-80% 成功率） |
| 🛡️ **安全** | 宇树 G1 蓝牙 Root RCE（可蠕虫传播，2 个 CVE） |
| 🇨🇳 **中国动态** | 宇树 G1 安全漏洞披露；Python 潮流周刊 AI 项目密集 |
