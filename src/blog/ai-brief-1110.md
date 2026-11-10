---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1110.html"
title: "今日AI简报 — Anthropic 的一天：Fable 公开、Mythos 持证、IPO 报区间"
description: "Anthropic 同日发布同底层的 Claude Fable 5.2 与 Mythos 5.2，并启动 IPO 路演、拟募约 693 亿美元；Google 承认把个人 Drive/Gmail 送进人工审核；Meta 推出每百万 token 0.1 美元的 Muse Ember；Fireworks 二次被黑波及 Notion；英伟达 GR00T 2 让 G1 现场跑全身体控。"
date: "2026-11-10"
tags: ["AI", "简报", "Anthropic", "Meta", "机器人", "隐私"]
---

# 今日AI简报 — Anthropic 的一天：Fable 公开、Mythos 持证、IPO 报区间

**2026年11月10日**

---

## 📡 数据源A：中文频道动态

### myco：给散落在各台机器上的 agent CLI 拉一张网

开源项目 **myco** 想解决一个很具体的痛点：Claude Code 在 Mac 上、Codex 在 VPS 上、claude.ai 云会话在做调研，三个 agent 互不相识，**你**成了它们之间的消息总线——复制提示词、等结果、再粘贴回去。myco 给每个 agent 一个名字和收件箱，任何 agent 都能找到同伴、派活、收回复；空闲 agent 被消息唤醒后恢复**自己原来的会话**，上下文不重置。实现上是一个静态 Go 单二进制（hub、CLI、runner 同一个程序，SQLite 存储，无 cgo），每台机器一行 `curl | bash` 装好并入网，hub 可以跑在 VPS 上，也可以借 Cloudflare Tunnel / Tailscale Funnel 跑在自己电脑上；另带 exec 节点、附件 SHA-256 校验、发送方 allow-list，以及一个 MCP 端点让 ChatGPT / Claude 以 connector 身份加入。内置支持 claude、codex、gemini、cursor、opencode、pi、kiro。🔗 https://github.com/chenhg5/myco ｜ 📎 https://t.me/https1024/54490

---

## 🌍 数据源B：国际AI要闻

### 1. 🧠 Claude Fable 5.2 / Mythos 5.2：同一个模型，两种准入

11 月 9 日，Anthropic 把 Claude Fable 与 Claude Mythos 一起升到 **5.2**——官方明确说二者是**同一个底层模型**，区别只在准入：Fable 带网络与生物安全护栏、向所有用户开放；Mythos 走今年扩容的 Cyber 与 Life Sciences 验证计划、按资质放行（10 月红队报告里那个「尚未发布的 Mythos」就此落地）。输出比 5.1 快 **30%**，价格降到每百万 token **$8 输入 / $40 输出**，另有把生成速度再提 **2.5 倍**的 fast mode（$16 / $80）。基准上：FrontierCode 2.0 在 Xhigh 档 **49.1%**（Fable 5.1 为 32.4%、Opus 5.5 45.5%、GPT-6 Astra 42.8%、Gemini 4 Carbon 41.1%）；FrontierSWE v2 **69.9%**；RoboDojo Sim **64.9%**（前代 27.6%）；HLE 带工具 **74.2%**；Mythos 在 CyScenarioBench **76.3%**、CVE 重发现 **89.6%**、24 小时从头设计蛋白结合体 **85.1%**。官方举的例子包括：一名工程师让它从空目录起步、协调 **1000 多个子智能体**连跑 8 天，写出一个能在笔记本上启动的完整操作系统；以及 30 小时内形式化费马大定理。Anthropic 同时称其核心代码库 **90% 以上**的已合并改动由 Claude 写成。🔗 https://www.anthropic.com/claude-fable-and-mythos-5-2

### 2. 📈 Anthropic 启动 IPO 路演：8.25 亿股、$70–78、代码 ANT

同一天，Anthropic 正式启动 IPO 路演：拟发行 **8.25 亿股** A 类普通股（其中 8.0135 亿股由公司发行，2,365 万股来自老股东，公司不从老股东减持中取得任何收益），定价区间 **每股 $70–78**，另授予承销商 30 天 **1.2375 亿股**超额配售权，申请以代码 **ANT** 在纳斯达克全球精选市场上市。按区间本身计算，募资约 **578–643 亿美元**；Reuters 按含超额配售的口径称最高约 **693 亿美元**。这是 1107 简报所载「中期选举后估值预期从 2 万亿美元下调、连 $1.5 万亿都算 stretch」之后的下一个里程碑——从匿名人士嘴里的估值区间，走到了招股书里白纸黑字的发行价区间。承销商是高盛与摩根士丹利，也就是 1109 简报里把 Claude Code 收回给 1.2 万工程师专用的那两家中的高盛。🔗 https://www.anthropic.com/news/roadshow-launch

### 3. 🔍 Gemini 把个人 Drive 文件与邮件送进人工审核，且是自动触发

HN 628 分的一份调查（附完整复现步骤的 GitHub 仓库）指出：Google 已悄悄推翻 2023 年「Gmail、Docs、Drive 的个人内容不会被人工审核看到」的承诺。现行 Gemini 帮助文档与 10 月 16 日改写的 2023 年博客都写明：已连接的 Drive/邮件会进入人工审核流程，审核员看到的「可能就是这个邮件或文件本身」，并警告不要把含机密信息的应用连到 Gemini。作者实测的关键点是**自动触发**：在普通对话里随口提到行程、账单、续费，即使不写 @Drive / @Gmail，Gemini 也会在后台发起 Workspace 检索；由于工具调用是概率性的，同一次提问会随机落在四种状态之一——完全不检索、只给元数据摘要、摘出 2–6 句含账号与确认号的原文、或把整份文件原文灌进上下文。作者的结论是：一次没测出泄露不能证伪这条管线，那只是随机抽了一次；而 Google 的正则与 NER 清洗对叙事型数据（账号、确认号、交易日期、可组合出身份的细节）本就无能为力。🔗 https://github.com/thisisme6598/gemini_files/

### 4. 🪶 Meta Muse Ember：每百万 token 0.1 美元，冲效率前沿

Meta 11 月 9 日发布 **Muse Ember**，定位「最小、最省」的模型，专打 agent 一天要重复几百次的小活：工具调用、编码子任务、路由、抽取、长文档解析。定价 **每百万 token $0.10 输入 / $0.004 缓存输入 / $0.50 输出**，1M 上下文、最多 512K 输出，原生多模态（文本/图像/音频/视频），以 `muse-ember-1.0` 上线 Meta Model API 与 Muse Code。Artificial Analysis 口径下智能指数 **36**、每任务成本约 **$0.14**——同指数的 Claude Haiku 5.5 每任务 $0.41，GPT-6 Luna 只有 28 分；端到端业务流 AutomationBench **37.8**（Haiku 13.9、Luna 20.2）、Terminal-Bench 4.0 **40.9**、OSWorld 2.1 **69.5**（部分分）。官方称它是第一个用 Muse Wonder Full 训练出来的专业化模型，路线是用前沿大模型带出「便宜到可以在每个产品里都部署」的小模型。🔗 https://research.meta.ai/blog/muse-ember

### 5. 🔐 Fireworks AI 数周内第二次被黑，Notion AI 聊天记录外泄

Bloomberg 11 月 9 日报道，英伟达投资的推理平台 **Fireworks AI** 向客户通报了数周内的**第二次**入侵。受影响的 Notion 随后给出时间线：本月早些时候从 Fireworks 得知风险，**11 月 3 日**切断全部连接、删除 Fireworks 侧数据、停掉所有训练；**11 月 6 日** Fireworks 通知可能有客户数据被访问，**11 月 8 日**确认了新的数据集。Notion 称**不到 1% 的工作区**可能受影响，泄露的是 Insights 功能所用的**无法归属**的 Notion AI 聊天记录——不带作者、不带工作区标识、不含工具调用结果（即不含 Notion 页面内容）；Insights 已停用，也不再通过 Fireworks 提供开源权重模型。Notion 的建议是把这批数据当作已泄露：若这期间往 Notion AI 里贴过密码或 API key，立即轮换。🔗 https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor ｜ https://www.bloomberg.com/news/articles/2026-11-09/nvidia-backed-fireworks-ai-notifies-customers-of-its-second-hack-in-weeks

---

## 🤖 数据源C：人形机器人动态

### 英伟达 GR00T 2：看人类视频学活，5 次演示把成功率从 40% 拉到 95%

英伟达 GEAR 团队发布 **GR00T 2**，把世界模型与动作模型合成一个 **world-action model**：一个扩散 Transformer 同时去噪未来视频与机器人动作，先预测场景该怎么变，再由每个机器人专属的小头把计划翻成电机指令。预训练混三类数据——**40.27 万小时**第一人称人类工作视频、**1.0184 万小时**手持 UMI 夹爪演示（2,897 个任务）、**2.35 万小时**机器人遥操作，覆盖平行夹爪、灵巧手与 Unitree G1。核心卖点是 **X-Adapt**：只在人类视频里见过的技能可以搬到没练过的机器人身上——人类戴手套演示化学实验台铺滤纸，Dexter 20 次试验全部成功；在 50 个目标机器人从未见过的任务上零样本成功率 **40%**，每任务加 5 次演示（不到 3 分钟机器人数据、单张 RTX 5090 上 30 分钟 LoRA）后升到 **95%**。**GR00T 2 Turbo** 更小，能跑在 G1 自带的 Jetson Thor 上，单次预测 **124 毫秒**，经 SONIC 全身控制器 48/48 次舀爆米花、清桌 93%；加仿真数据后分布外任务成功率从 **6.7% 升到 63.3%**。代码 12 月放出，Human-1M-100K 数据集已在 Hugging Face 开放。🔗 https://research.nvidia.com/labs/gear/gr00t-2/

### 新华社 × 优必选：全球首款仿生机器人主播「新语」「新颜」

11 月 5 日，新华社在北京「人工智能与中国式现代化」论坛上，与优必选联合发布两款仿生人形机器人主播——男主播「**新语**」、女主播「**新颜**」，称是全球首款，其中一台当场播报了开场新闻。机器人按真人比例定制，**张艺谋**担任总视觉设计，目标是把新闻播报的庄重严谨与仿生真实感放在一起，而不是单纯追求像人。技术上接的是新华社「新华智电」时事信息智能体与权威语料库，优必选提供仿生皮肤、本体硬件、操作系统、情感大模型与整机制造；官方强调「内容可溯源、避免生成式幻觉」——机器人只检索并播报经审核的稿子。新华社新媒体中心把它定位为编辑部里的新岗位（信息呈现、多语种输出、现场互动），记者与编辑仍是编辑主体；未来设想用于城市接待、海外文化交流与深空报道。🔗 https://www.unite.ai/xinhua-unveils-bionic-humanoid-robot-news-anchors-with-ubtech/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🧠 **最热** | Claude Fable 5.2 / Mythos 5.2：同底层、两套护栏，FrontierCode 2.0 49.1% 登顶，价格降至 $8/$40 |
| 📈 **资本市场** | Anthropic 启动路演：8.25 亿股、$70–78、代码 ANT，含超额配售最高约 693 亿美元 |
| 🔍 **隐私** | Gemini 承认把个人 Drive/邮件送人工审核，且普通对话会自动触发 Workspace 检索 |
| 🪶 **效率** | Meta Muse Ember：$0.10/百万输入 token，智能指数 36、每任务约 $0.14 |
| 🔐 **安全** | Fireworks AI 数周内二次被黑，Notion 不到 1% 工作区的 AI 聊天记录外泄 |
| 🤖 **具身智能** | GR00T 2 用人类视频做跨本体迁移，5 次演示达 95%；新华社与优必选发布仿生机器人主播 |
