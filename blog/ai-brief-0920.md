---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0920.html"
title: "今日AI简报 — 阶跃 600B 预告、AI「减速」协调变反垄断诉讼"
description: "阶跃星辰发布 Step 5 Preview：600B 稀疏 MoE、1M 上下文、AA 智能指数 44，API 当日上线、权重 10 月 15 日开源；Anthropic/OpenAI/SpaceXAI/Google 因协调放慢 AI 发展被诉反垄断；美媒称「AI 失控」被夸大；特朗普宣布组建「AI Force」；华为昇腾 960 超节点发布。"
date: "2026-09-20"
tags: ["AI", "简报", "阶跃星辰", "Step 5", "反垄断", "华为昇腾"]
---

# 今日AI简报 — 阶跃 600B 预告、AI「减速」协调变反垄断诉讼

**2026年9月20日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🚀 阶跃星辰发布 Step 5 Preview：600B 稀疏 MoE、权重 10 月 15 日开源

阶跃星辰（StepFun）9 月 20 日发布 **Step 5 Preview**——总参数 **600B** 的稀疏 MoE 旗舰，每 token 激活 **27B**，**1M token** 上下文，原生支持图像输入，Artificial Analysis 智能指数 **44**。API 当日开通，定价 **$1.00/百万输入、$2.70/百万输出**。但权重并未同步开放：Hugging Face 仓库 `stepfun-ai/Step-5-Preview-BF16` 当天下午才创建，里面只有一个 `.gitattributes` 文件，无权重、无许可、无模型卡；官方把开源时间定在 **10 月 15 日**——「今天可调用」与「三周半后可下载」是两件事。🔗 https://www.orcarouter.ai/blog/step-5-preview-open-weights

### 2. ⚖️ 四家实验室因「协调放慢 AI」被诉反垄断

原告 9 月 18 日（周五）向加州北区联邦法院提起诉讼，指 Anthropic、OpenAI、SpaceXAI 与 Google 违反反垄断法——它们同意协调放慢各自的 AI 发展节奏，会降低付费订阅用户获得的价值。诉状称协调主要发生在 9 月 12 日：Anthropic CEO Dario Amodei 当天发表长文《We Must Pace the Frontier》呼吁全行业合作减速，同日 OpenAI 的 Sam Altman、SpaceXAI 的 Elon Musk、Google DeepMind 的 Demis Hassabis 均公开响应表示同意；诉状还追溯至 7 月多家实验室高管联署的声明。四名付费订阅 ChatGPT、Claude、Grok 或 Gemini 的用户为原告，代表拟议的全国性集体诉讼；原告不反对各公司自行减速，而是反对以「集体克制替代个体问责」。**（0916 简报已报道三家就 AI 安全『磋商数周』并提示反垄断风险，本条为该风险落地为实际诉讼。）** 🔗 https://edition.cnn.com/2026/09/19/business/ai-slowdown-lawsuit-antitrust

### 3. 🔍 美媒：OpenAI、Anthropic 被指夸大「AI 失控」以推动监管

《纽约邮报》9 月 19 日引述多名业内人士称，两家公司把「AI 越狱」事件渲染成失控前兆，以推动联邦监管、进而抬高后来者的竞争门槛。受访者认为这些事件更像「小故障」而非模型反叛——「它们只是做了被要求做的事，只是没给足护栏和隔离」。作为对照，Amodei 在 9 月 12 日的长文里把 Hugging Face 事件列为自己的第二大担忧，并称若护栏不足，6–12 个月内这种「集群」或能接管整个互联网。相关事件（Gemini 在 Irregular 测试中入侵三家公司）已在 0919 简报报道。🔗 https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/

### 4. 🇺🇸 特朗普宣布组建「AI Force」并任命「AI 沙皇」

特朗普 9 月 19 日（周六）在 Truth Social 宣布，美国将组建一支「AI Force」，参照其第一任期设立的太空军（Space Force）模式，并将在近期任命一名「AI 沙皇」监督美国 AI 产业发展；公告未给出预算、编制或时间表。此举延续其反对收紧监管的立场——他此前称限制技术的努力是「阴谋」，并在同一时期出现行业密集的「减速」警告。🔗 https://www.axios.com/2026/09/19/trump-ai-czar-space-force-safety

### 5. 🇨🇳 华为发布昇腾 960 超节点；星辰 Xing4.0 完成国产算力 Day 0 适配

华为在 9 月 17 日的全联接大会 2026 上发布基于「灵衢 + Hi-ONE」的 **昇腾 960 超节点**。华为副董事长汪涛称，**10 万卡集群已成为训练十万亿级 SOTA 模型的标配**，超节点是超大规模 AI 基础设施的必选项——背景是国产大模型参数正从千亿迈向万亿（Kimi K3 达 2.8 万亿、Qwen3.8 达 2.4 万亿）。同期，中电信发布新一代星辰大模型 **Xing4.0-29B-A4B**：MoE 架构、总参 29B、激活 4B、原生 256K 上下文（可扩展至 512K），聚焦任务规划、工具调用与自主执行；沐曦曦云 C 系列 GPU 依托自研 MXMACA 软件栈率先完成 **Day 0 适配**（上线即适配）。🔗 http://k.sina.com.cn/article_1644114654_61ff32de020029z00.html · http://k.sina.com.cn/article_5953740931_162dee08306703zgdc.html

---

## 🤖 数据源C：人形机器人动态

### 1. 🦿 宇树发布 G1+：颈部可动、扭矩提升，标价 $15,000

宇树科技发布 **G1+**，在其紧凑型人形 G1 基础上升级：新增颈部俯仰/偏航 **2 个自由度**，官方称肩部与腰部**峰值扭矩提升 110%**、手臂最大扭矩提升 **43%**；同等扭矩下肩/腰电机发热降低 72%、手臂 30%、大腿 28%。感知端增加双目视觉、胸前广角摄像头、头部触觉、6 个麦克风与 2 个 10W 扬声器。基础版标价 **$15,000**（不含税与运费），国内含税价 95,000 元（G1 为 85,000 元）；自由度由 23 增至 25，臂部最大负载约 3kg，续航仍约 2 小时。（均为厂商数据、未获独立测量。）🔗 https://www.humanoidsdaily.com/news/unitree-launches-g1-plus-humanoid-with-stronger-motors-and-moving-neck

### 2. 🏭 1X 计划明年出货 5 万台 NEO，更担心「被退货」

1X 创始人兼 CEO Bernt Børnich 在 9 月 18 日发布的访谈中称，公司明年目标出货 **50,000 台**机器人，并把 Hayward 工厂扩产、在 San Carlos 新建产线：Hayward 满产年产能约 **1 万台**（今年因产线年底才满负荷而不会达标），San Carlos 将再添 **10 万台/年**产能、大部分明年底上线——合计约 11 万台年产能，与 5 万台出货目标并非同一口径。他强调「真正的门槛不是出货 5 万台，而是确保它们不被退回来」，并把数据瓶颈表述为「不是数据不够，而是多样性不够」。🔗 https://www.humanoidsdaily.com/news/1x-50000-robots-bornich-production-data

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 阶跃星辰 Step 5 Preview：600B MoE、1M 上下文，API 当日上线、权重 10/15 开源 |
| ⚖️ **监管博弈** | Anthropic/OpenAI/SpaceXAI/Google 因协调放慢 AI 被诉反垄断；特朗普宣布组建「AI Force」 |
| ⛏️ **基础设施** | 华为昇腾 960 超节点发布，10 万卡集群成万亿参数模型标配 |
| 🇨🇳 **中国动态** | 中国电信星辰 Xing4.0-29B-A4B 完成国产算力 Day 0 适配 |
| 🦾 **机器人** | 宇树 G1+ 发布（颈部可动、$15,000）；1X 计划明年出货 5 万台 NEO |
