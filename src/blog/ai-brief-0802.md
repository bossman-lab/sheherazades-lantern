---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0802.html"
title: '今日AI简报 — Seedance 2.5发布、Kimi K3 AMD逆袭、Nvidia担保2500亿'
description: '字节跳动发布视频生成模型 Seedance 2.5：单次生成30秒、一次参考30图+10视频+10音频；Wafer实测 Kimi K3 在 AMD MI355X 上每美元性能达 B300 的1.5倍；WSJ曝 Nvidia 洽谈为 OpenAI 数据中心担保2500亿美元融资；月之暗面 K3 训练用阿里2万卡集群；OpenAI 内部模型数学证明引争议。'
date: "2026-08-02"
tags: ["AI", "简报", "Seedance", "Kimi K3", "AMD", "Nvidia"]
---

# 今日AI简报 — Seedance 2.5发布、Kimi K3 AMD逆袭、Nvidia担保2500亿

**2026年8月2日**

---

## 📡 数据源A：中文频道动态

**高德地图语音唤醒误触发率高遭用户吐槽** — 有用户在比亚迪车内喊「小迪」时频繁误触发高德地图的语音唤醒，吐槽其误操作率如此之高「怎么好意思说自己有 AI」。车载环境下第三方地图 App 的语音唤醒缺乏车内上下文感知，是当前语音交互的一大痛点。

🔗 https://t.me/inside1024/82671

---

## 🌍 数据源B：国际AI要闻

**1. 字节跳动发布 Seedance 2.5：单次生成 30 秒视频，多模态参考大幅升级**

字节跳动 7 月 31 日发布新一代视频生成模型 Seedance 2.5：单次生成时长从 15 秒翻倍至 30 秒并支持多轮续写，一次可输入 30 张图片、10 段视频、10 段音频作为参考素材；新增时间戳级音视频定向编辑、绿幕与运镜控制。已在即梦 AI 与豆包 Pro 上线，API 即将通过 BytePlus ModelArk 提供。Hacker News 热帖（365 分）。

🔗 https://seed.bytedance.com/seedance2_5

**2. Kimi K3 在 AMD MI355X 上每美元性能反超 B300**

Wafer 实测：2.8T 参数的 Kimi K3 在 8×MI355X 节点上跑出 952 tok/s 聚合吞吐、118 tok/s 单流解码；按 $2.5/GPU·时计，每美元性能达 48 tok/s/$，是 B300（33 tok/s/$）的约 1.5 倍、B200（7 tok/s/$）的近 7 倍。AMD 为 K3 提供 day-0 支持，288GB 显存的 MI355X 也是少数能单节点容纳 K3 的芯片。HN 热帖 144 分，被视为「CUDA 护城河将死」的最新证据。

🔗 https://www.wafer.ai/blog/kimi-k3-mi355x

**3. Nvidia 洽谈为 OpenAI 数据中心担保 2500 亿美元融资**

据《华尔街日报》报道，Nvidia 正与 OpenAI 洽谈为其数据中心提供最高 2500 亿美元的融资担保。芯片巨头深度介入客户资本结构的「供应商融资」模式引发讨论：结合昨日报道的 Aschenbrenner 450 亿美元基金崩盘，市场对 AI 行业杠杆与资本循环风险的担忧进一步升温。

🔗 https://www.wsj.com/tech/ai/nvidia-in-talks-with-openai-to-guarantee-250-billion-financing-for-data-center-3dd6eae3

**4. 月之暗面 Kimi 训练算力来自阿里云 2 万块 Nvidia 芯片集群**

据彭博社报道，月之暗面（Moonshot）的 Kimi 模型训练使用了阿里巴巴云提供的约 2 万块 Nvidia 芯片集群——中国头部模型公司选择租用云算力而非自建集群来支撑前沿模型训练。

🔗 https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba

**5. OpenAI 内部模型据称解决 10 个重大数学难题，证明遭质疑**

OpenAI 内部模型（代号 Astra）据称解决了 10 个重大开放数学/计算机科学问题，其中包括对 Connes 刚性猜想的反证；该证明随即在学术社区引发激烈争议（philarchive 上有文章称其无效，支持者则称该质疑本身不成立）。同一周，自称「害怕 AI」的菲尔兹奖得主 Jacob Tsimerman 入职 OpenAI，《大西洋月刊》以「数学界正在发生奇怪的事」为题报道了这一连串动态。

🔗 https://www.theatlantic.com/technology/2026/07/jacob-tsimerman-math-fields-medal-openai/688120/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Seedance 2.5 发布：单次 30 秒、30 图 + 10 视频 + 10 音频参考 |
| ⛏️ **基础设施** | Kimi K3 在 AMD MI355X 每美元性能 48 tok/s/$，反超 B300 |
| 💰 **资本** | Nvidia 洽谈为 OpenAI 数据中心担保 2500 亿美元融资 |
| 🇨🇳 **中国动态** | 月之暗面用阿里 2 万卡集群训练 Kimi；Seedance 2.5 即梦上线 |
| 🧮 **研究** | OpenAI 内部模型 10 项数学突破引争议，菲尔兹奖得主入职 |
