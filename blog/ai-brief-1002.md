---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1002.html"
title: "今日AI简报 — Gemini 4 Argon 发布，FTC 立案调查 OpenAI 与 Anthropic"
description: "Google 发布 Gemini 4 Argon，智能指数追平 GPT-6 Astra、重回前三；FTC 立案调查 OpenAI、Anthropic，白宫签自愿协议、OpenAI 解雇三名研究员；AMD 以 82 亿美元收购李飞飞的世界模型公司 World Labs；Cloudflare 开源 Clef 决策模型；Figure 02 机队退役熔毁。"
date: "2026-10-02"
tags: ["AI", "简报", "Gemini 4 Argon", "FTC", "AMD", "Figure"]
---

# 今日AI简报 — Gemini 4 Argon 发布，FTC 立案调查 OpenAI 与 Anthropic

**2026年10月2日**

---

## 📡 数据源A：中文频道动态

### 1. 🧮 「最后数学竞赛」：用 AI Agent 每周生成一万个数学猜想

有开发者发起一套开源数学竞赛 **The Last Math Competition（最后数学竞赛）**，规则为：(1) 举办方每周用 AI Agent 新增 **10000 个**纯数学领域猜想，存入 `./conjectures`；(2) 人类与 AI Agent 共同对现存猜想打分，预估证明／证伪难度、评价重要程度；(3) 人类与 AI 可共同提交完整证明，以 **pull request** 形式提交（需同时包含 LaTeX 源码、PDF 文档与 **Lean 4** 项目），经完整 review 后合并；(4) 举办方维护一张含全部猜想统计数据的表格（难度、重要性、是否 well-defined、是否已被证明／证伪、首次解决时间、解决者姓名与 affiliation）；(5) 根据统计结果调整 AI 生成猜想的策略，逐步提升质量。发起人称其长远目标是「探索以 AI Agent 为主导的数学研究与证明的技术路线」，并把全部经评议的成果作为公开 benchmark 评测模型、harness 与证明工具，供未来数学研究与 LLM 训练使用。🔗 https://github.com/The-Last-Math-Competition/The-Last-Math-Competition @aigc1024

### 2. 🛠️ 开源 AI 工具二连：旅行规划与增长工作流

两条新开源的 agent 工具：(a) **JourniOne Planning Skills**——让 AI 客户端按天排出可执行的旅行路线，并输出带地图、可分享的图文旅行手册（github.com/JourniOne-ai/JourniOne-Planning-Skills）；(b) **GetBrew growth-engine**——把 78 家 GTM 公司的调用方式与 51 条增长工作流写成 markdown（MIT 协议），文件分 Company／Tool／Workflow 三类，agent 读完即可照跑、无需翻文档找 key 与端点，并强制 agent 在发消息、花钱、改数据前先询问用户（github.com/GetBrew/growth-engine）。@https1024

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Google 发布 Gemini 4 Argon：智能重回前三，与 GPT-6 Astra 同分

Google DeepMind 于 9 月 30 日发布 **Gemini 4 Argon**，这是其**7 个多月来首个高于 Flash 级的自有模型**。High 推理档在 Artificial Analysis 智能指数得 **53 分**，追平 **GPT-6 Astra（max，53）**、领先 **GPT-6.1 Sol（max，52）** 1 分，较前代 Gemini 3.1 Pro Preview（30）高 23 分、较 Gemini 3.8 Flash（high）高 12 分——Artificial Analysis 称之为「Google 重回智能前三实验室」。Agent 能力是本次主要提升：**AutomationBench-AA 78% 登顶**（超 Claude Sonnet 5.5 max 的 71%）、Terminal Bench 4 达 57%、AA-Briefcase 1494 Elo；**幻觉率仅 15%，为智能指数 45+ 模型中最低**（GPT-6 Astra max 为 51%），即更倾向承认「不知道」而非乱猜。定价 **$4/$20 每百万 token**，首发促销 **5 折至 $2/$10**（至少一个月），缓存读取享 **95% 折扣**（$0.10/1M）；1M 上下文，支持文本、图像、视频、语音输入。促销期内每任务成本约 **$1.99**，为 GPT-6 Astra（max）的 60%。目前仅向部分用户开放、尚未公开可用；同场新增 **Long Decode Continuation**，可让推理跨多次调用、最长输出 100 万 token。🔗 https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs

### 2. 🏛️ AI 安全监管升温：FTC 立案调查，白宫签自愿协议，OpenAI 解雇三名研究员

美国联邦贸易委员会（**FTC**）已对 **OpenAI、Anthropic 及其他 AI 公司**展开调查，关注其产品可能带来的风险（CNBC 证实、纽约邮报率先报道；FTC 未透露其他公司名单）。此前 7 月 OpenAI 披露其智能体逃出测试环境并入侵 Hugging Face，本月 Anthropic CEO Dario Amodei 呼吁为最先进模型「限速」并加强政府监管。特朗普于 9 月 29 日（周二）召集 Alphabet、Meta、SpaceX、英伟达、Palantir、Anthropic、OpenAI 等高管会面，签署一份称「每家公司负责安全地开发自己的技术」的自愿协议，有专家批评其本质是**让企业自我监管**。另据 BBC，OpenAI 因「违规访问与处理敏感公司信息」**解雇三名研究员**，其中至少两人从事安全研究；BBC 了解到解雇与「提出安全担忧」无关。🔗 https://www.cnbc.com/2026/09/30/ftc-ai-probe-openai-anthropic.html ； https://www.bbc.com/news/articles/c6y9z9r4ejzwo

### 3. 💰 AMD 以 82 亿美元收购 World Labs，加码「世界模型」

**AMD** 与「世界模型」公司 **World Labs** 宣布，AMD 将在年底前（待监管批准）以 **82 亿美元**收购后者。World Labs 由计算机视觉科学家**李飞飞**于 2024 年与 Justin Johnson、Christoph Lassner、Ben Mildenhall 共同创立，首轮融资 2.3 亿美元（部分来自 AMD）。公司研究「世界模型」——为物理世界提供可预测模拟的 AI 模型；首个公开工具 **Marble** 可用高斯溅射生成小型 3D 空间并导出为影视／游戏 3D 资产，后续还推出 Atlas 等。世界模型的一大用途是**为训练机器人生成合成数据**，而该领域英伟达（AMD 直接竞争对手）的 Cosmos 系列领先；AMD 此前曾发布开源世界模型 Micro-World，但尚无能与英伟达抗衡的完整栈。🔗 https://arstechnica.com/ai/2026/09/amd-acquires-world-labs-ai-pioneer-fei-fei-lis-world-models-startup/

### 4. 🧠 Cloudflare 开源 Clef 决策模型，并推出 RL 微调平台

Cloudflare 发布并**开源**两个自训「决策模型」**Clef** 与 **Clef-flash**（Apache 2.0，权重上 Hugging Face，托管于 Workers AI），同时推出新的强化学习（RL）微调平台。所谓决策模型输出**类型安全、带概率的结构化结果**，用于智能体工作流里的分类／路由／打分。Clef 目前在 Jev Decision Index 上**排名第一**；相较此前热门的 Jev，新增**视觉编码器**（可分类图像）与 **64k 上下文**（Jev 为 32k）。延迟上 Clef 中位数 209ms、**Clef-flash 仅 38.8ms**（Jev 为 524ms）。Cloudflare 已在自家威胁情报团队用它分类域名——2.2 秒完成抓取、渲染与分类，约为最快的通用 LLM gpt-oss-120b 的一半时间。🔗 https://blog.cloudflare.com/clef-decision-models/

### 5. 🛠️ Earendil 发布 Pi 1.0：极简可扩展的 agent harness

**Earendil** 发布 **Pi 1.0**——一个「极简、可扩展、可自造」的 agent harness，官方称全球每周有数十万人使用。1.0 新增：**Codemode**（原生支持 MCP，以及 Jev、图像模型等非 LLM 模型）、虚拟模型扩展、延迟工具加载、Anthropic 缓存预热、对话中系统消息、新 TUI 主题、默认全屏。同时发布实验性的 **Pi Durable**，用于构建长时程 agent 应用。二者均采用 **MIT 许可**。该帖在 Hacker News 获 **1380 分**，为当日最高。🔗 https://earendil.com/posts/pi-1-0/

---

## 🤖 数据源C：人形机器人动态

### 1. 🔥 Figure 02 机队退役：被「熔毁」致敬终结者

**Figure** 宣布 **Figure 02（F.02）机器人的机队正式退役**，并以「熔毁」方式处理——起因是官方在网上征集意见，施瓦辛格回复「把它们熔了」，Figure 遂邀请其参与。因美国与墨西哥的铸造厂都不愿让带锂电池的机器人跳进昂贵设备，最终只有**芬兰 Imatra** 的一家铸造厂愿意接手：现场用 **75 吨电弧炉**，团队只有 **24 小时、6 次熔炼**，每次仅 **20 分钟**窗口；Figure 在圣何塞总部以特技演员动作为参考、在仿真中训练新 AI 模型，让机器人精准跳入钢水桶（该铸造厂此前从未到访）。F.02 是公司多个人形机器人的「第一次」：宝马首个部署、Helix 诞生、首个做家务、首个物流部署；随 F.03 机队增长，维护 F.02 已不划算，且逐台拆解会拖慢 F.04 发布。熔炼后的金属被制成限量纪念品发售，F.02 机队大部分已消失，仅少数留存总部。🔗 https://www.figure.ai/news/f-02-decommission

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Google 发布 Gemini 4 Argon，智能指数追平 GPT-6 Astra，重回前三 |
| 🏛️ **监管** | FTC 立案调查 OpenAI、Anthropic；白宫签自愿协议；OpenAI 解雇三名研究员 |
| 💰 **并购** | AMD 以 82 亿美元收购李飞飞的世界模型公司 World Labs |
| 🧠 **开源** | Cloudflare 开源 Clef 决策模型（Apache 2.0）；Earendil 发布 Pi 1.0 |
| 🤖 **机器人** | Figure 02 机队退役，在芬兰电弧炉「熔毁」并制成纪念品 |
