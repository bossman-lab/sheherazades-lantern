---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1003.html"
title: "今日AI简报 — ChatGPT 一键建站上线，AI 攻克 Stratego"
description: "OpenAI 推出 ChatGPT Sites：对话式建站、建应用、建游戏并一键托管；AI 15:1 击败 Stratego 世界冠军，训练成本仅数千美元；Redis 作者发布本地推理引擎 ds4；Amazon 拟将 80 亿美元 Nvidia 芯片资产化回租；波士顿动力发布 13 自由度新 Atlas 手。"
date: "2026-10-03"
tags: ["AI", "简报", "ChatGPT Sites", "Stratego", "Nvidia", "Boston Dynamics"]
---

# 今日AI简报 — ChatGPT 一键建站上线，AI 攻克 Stratego

**2026年10月3日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 OpenAI 推出 ChatGPT Sites：对话式建站、建应用、建游戏

OpenAI 上线 **ChatGPT Sites**（公开测试）：用户用自然语言描述需求，ChatGPT 即可生成网站、应用或小游戏，并在应用内浏览器中预览、迭代，随后一键发布。支持设定访问范围（仅自己／工作区／公开）、接入「ChatGPT 登录」以便访客保存进度、连接工作区已授权的工具，以及绑定自定义域名（重命名后旧地址自动跳转）。该功能面向符合条件的 ChatGPT Plus、Pro、Business、Enterprise、Edu 套餐开放，具体额度随套餐与地区而异。🔗 https://chatgpt.com/features/sites/

### 2. 🎯 AI 首次攻克 Stratego：15:1 击败世界冠军，训练成本仅数千美元

卡内基梅隆、MIT、纽约大学与斯坦福团队开发的 AI **Ataraxos**，在 20 局对弈中以 **15 胜 1 负 4 平**击败四届世界冠军、曾累计 600 余周世界第一的荷兰玩家 Pim Niemeijer（每胜一局付其 100 美元）。Stratego 是典型的不完全信息博弈——40 枚棋子身份隐藏、开局排列组合超过「十的六十次方」量级、单局常超 2000 步，此前连 DeepMind 的 DeepNash 也未能稳定取胜。Ataraxos 的关键是**额外训练了一个「信念模型」神经网络**，根据对手走法推断其暗子身份，从而把搜索从「遍历所有排列」缩为「采样合理排列」。它在 2025 年 Stratego 世锦赛上对现场挑战者 40 局胜 38 局。训练仅需 **16 张 GPU 一周**（外加训练信念模型 4 张 GPU 四天），成本数千美元；而 DeepNash 用 1024 张谷歌专用芯片训练 2–3 个月、估算耗资 **300 万–450 万美元**。同一架构还拿下了 Barrage Stratego、Hanabi 与中国斗地主。论文发表于《Nature》。🔗 https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/

### 3. 🧩 Redis 作者发布本地推理引擎 ds4：在家跑前沿开源权重

Redis 作者 **antirez（Salvatore Sanfilippo）**发布 **DwarfStar 4（ds4）**——一个用 C 写的窄口径本地推理引擎，面向高内存 Mac（Metal）、CUDA 与 ROCm 机器，支持 **DeepSeek V4／V4.1 Flash、GLM 5.x、Qwen3.8 Flash Next**，含文本与视觉模型、本地 API、CLI 与原生 agent。它用**非对称 2-bit 量化**压缩路由专家（MoE）、保留关键共享路径的精度，并支持把长前缀的 KV cache 落盘、按提示哈希续跑而无需重新预填充；`ds4-server` 兼容 OpenAI 与 Anthropic 风格接口，可接入 Claude Code、Codex CLI、OpenCode 等编码智能体。项目采用 MIT 许可，GitHub 已约 1.9 万星。🔗 https://dwarfstar.sh/

### 4. 💰 Amazon 拟将 80 亿美元 Nvidia 芯片「资产化」再回租

据路透社援引《金融时报》报道，**Amazon 正与投资者磋商**，计划把其在美国数据中心安装的数千枚 **Nvidia Grace Blackwell** 芯片（约 **80 亿美元**）转入一个特殊目的载体（SPV），再由该载体对外发债融资、Amazon 回租这些芯片自用。Amazon 拟向载体出让至多 **10%** 股权，借此以更「轻资产」的方式持有昂贵的 AI 半导体。这些芯片部署在五个州、逾十个数据中心（含内华达与弗吉尼亚）；Amazon 与 Nvidia 均未立即置评。🔗 https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/

### 5. 🕵️ 加州高管被控走私 3 亿美元 Nvidia AI 芯片至中国

美国司法部宣布，加州工业市（City of Industry）科技公司 **Earthmade Computer** 老板 **Greg Lui（38 岁）**于周四被捕，被控共谋违反《出口管制改革法》、走私及共谋洗钱。起诉书称其 2023–2024 年间采购含 Nvidia GPU 的受出口管制服务器，向美国厂商提交虚假的最终去向文件，先运往马来西亚、新加坡，再非法转运中国；其中一例为 **27 台含 H100 的服务器、约 760 万美元**。Earthmade 在 2024 年 1–10 月间从两家马来西亚货运公司收取逾 **1.76 亿美元**。此案是近期一系列打击先进 AI 芯片非法流向中国的联邦行动的延续。🔗 https://qz.com/greg-lui-earthmade-nvidia-ai-chips-smuggling-china-100226

---

## 🤖 数据源C：人形机器人动态

### 1. 🤖 波士顿动力发布新一代 Atlas 手：13 自由度，刻意去掉小指

**波士顿动力**发布新一代 **Atlas** 机器人手（GR3）：**13 个自由度**（上一代 GR2 为 7）、四指、更拟人的可对置拇指，采用**直接驱动**、无跨关节线缆，指尖与掌心覆盖**密集压力触觉传感器**。设计上刻意**舍弃小指**——CTO 曾让团队把无名指与小指绑一天后确认，多一根手指要多三个执行器及相应的成本、体积与故障率，「最好的零件就是没有零件」。手部尺寸接近成人大手、力量与前代相当（可搬运 100 磅以上、装满物品的小冰箱），并为高保真仿真与 sim-to-real 强化学习而设计，已取得动态任务的初步迁移结果。🔗 https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | OpenAI 推出 ChatGPT Sites，对话式一键建站／建应用／建游戏并托管 |
| 🧠 **研究** | Ataraxos 15:1 击败 Stratego 世界冠军，训练成本仅数千美元 |
| 💰 **基础设施** | Amazon 拟将 80 亿美元 Nvidia 芯片转入 SPV 回租；加州高管被控走私 3 亿美元芯片 |
| 🧩 **开源** | Redis 作者发布本地推理引擎 ds4，支持 DeepSeek V4.1／GLM 5.x／Qwen3.8 |
| 🤖 **机器人** | 波士顿动力发布新一代 Atlas 手：13 自由度、直接驱动 |
