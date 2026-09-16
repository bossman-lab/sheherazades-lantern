---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0916.html"
title: '今日AI简报 — 「系统一」模型问世、三大实验室密谈AI安全'
description: '前OpenAI研究员发布「系统一」模型Jev——放弃字符串生成、只输出类型安全的概率化决策，延迟70-500毫秒、输出token免费；Google发布Gemini 3.8 Live语音模型；OpenAI确认与Anthropic、Google DeepMind就AI安全磋商已数周；Mistral联手Mozilla驱动Firefox智能窗口。'
date: "2026-09-16"
tags: ["AI", "简报", "TypeSafe", "Gemini", "AI安全", "Mistral"]
---

# 今日AI简报 — 「系统一」模型问世、三大实验室密谈AI安全

**2026年9月16日**

---

## 📡 数据源A：中文频道动态

### 1. 🐝 Block 开源 Buzz：人与 AI Agent 在同一工作区协作，GitHub 已 3.2 万 Star

中文开发者频道近日集中推荐 Block 开源的 **Buzz**——一个基于 Nostr 签名事件的「蜂群式」协作平台，把人类、AI Agent、工作流、Git 事件与项目记忆放进同一个中转站（relay）。Agent 可以像同事一样被拉进频道，拥有自己的密钥与操作记录，能建仓库、提补丁、审代码、跑自动化，权限按角色分配；配套工具链包括 buzz-cli（JSON 进 / JSON 出）、buzz-acp（适配 Goose / Codex / Claude Code 的 ACP 运行器）与 buzz-workflow（YAML 自动化），桌面端覆盖 macOS / Linux / Windows。官方在 README 中明确「**不是** AI 替代方案——Buzz 在人留在环内、Agent 留在房间里时效果最好」。仓库为 Apache-2.0 协议，GitHub 现有 32.2k Star、4.2k Fork、2,618 次提交，9月16日仍在持续更新。🔗 https://github.com/block/buzz · @openclaw1024

### 2. 📘 《动手学 Pi》：沿 15 个 checkpoint 从零构建编码 Agent

频道推荐的这本中文开源教程《动手学 Pi》从一个真实的离线 Agent 日志出发，带读者走完 15 个关卡、从零实现一个完整编码 Agent：消息与模型协议 → 工具与 Agent 循环 → 会话树存储 → 上下文压缩 → 组装运行时跑评测。每章配齐「正文 / 对应提交 / 聚焦测试 / 故障实验」四件套，练习目录一行命令生成且不给答案，把说明丢给 AI 当陪练即可。该仓库 7 月上线，现有约 1.3k Star。🔗 https://github.com/hahhforest/pi-textbook · @openclaw1024

### 3. 🧰 开源小工具二连：浏览器内去背景 bg0、AI Skill 管理器 SkillSwitch

其一 **bg0**（9月14日刚上线）：完全在浏览器本地运行的背景移除工具，检测到 WebGPU 时用 WebGPU 推理、否则回退 WASM，输出透明 PNG；原图不上传，没有账号、计费和用量限制，现有 162 Star。其二 **SkillSwitch**：跨平台桌面应用，为 Claude Code / Codex CLI / Gemini CLI / Cursor / Windsurf 提供统一的 Skill 文件管理界面，支持安装、卸载、发现新 Skill、创建自定义 Skill 与备份恢复，现有 63 Star。🔗 https://github.com/opencoredev/bg0 · https://github.com/DargonLee/skill-switch · @https1024 @aigc1024

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 前 OpenAI 研究员结束两年隐身，发布「系统一」模型 Jev：并行采样、类型安全、输出 token 免费

9月14日，TypeSafe AI 发布首款 **System One 模型 Jev**，创始人 Diogo Almeida 曾在 OpenAI 参与塑造 ChatGPT 背后的指令跟随与对话研究，此后「花了四年追问一个问题：模型在聊天上早已超人，自动化在哪里？」。技术路线有三处不同：新架构 + **并行采样器**（一次查询生成全部输出，而非逐 token 自回归）+ 训练方法 **RLCD**（Reinforcement Learning for Calibrated Decisions，为「校准的决策」而非人类偏好或可验证奖励做强化学习）。最关键的取舍是**放弃生成字符串**：Jev 只输出结构预先定义的类型安全取值，附带校准过的概率与置信度，因此官方称它在数学上「不可能产生类型错误」，也就无法幻觉。代价是它不能写文章、不能写代码，定位是「前沿智能的函数调用：非结构化状态进，带类型的概率化决策出」，典型场景是智能体工作流里的模糊 if-语句（分类、路由、打分、抽取）、大数据 map-reduce 与实时应用。性能上：端到端延迟 70–500 毫秒，对照前沿 LLM 的 3–329 秒；定价输入 **$0.042/百万 token**、输出免费（官方称「便宜到不必计量」）；在工作流评测中以 GPT-6 Astra 与 Fable 5.1 的平均输出作参考答案，官网称占据帕累托前沿、快 **193.6 倍**、便宜 **444.6 倍**。名字取自卡尼曼《思考，快与慢》的「系统一」与经济学家杰文斯（效率提升反而推高总需求）。该发布在 Hacker News 获 1,488 分，是目前当日最高分的 AI 条目。🔗 https://typesafe.ai/blog/introducing-system-one-models-and-jev

### 2. 🎙️ Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking

9月15日，Google 推出两款实时对话模型：**Gemini 3.8 Live**（面向规模与成本效率，兼顾对话智能、流畅度与视觉落地）与 **Gemini 3.8 Live Extended Thinking**（面向高复杂度任务，边推理边说话）。官方给出的数据：3.8 Live Extended Thinking 在 Artificial Analysis 的 Speech-to-Speech 质量指数取得 **82.6 分、总榜第一**，智能体任务完成度 τ-Voice 68.6%、Sierra 的 τ-Voice-banking 35.1%，Big Bench Audio 97.7%；3.8 Live 则在 Speech Agent Arena 位列第二。能力点包括：近实时处理视觉输入、对话中途自动在 **97 种受支持语言**之间切换、在后台执行工具与 API 调用而不断对话；Extended Thinking 会用「让我查一下…」这类早期口语提示确认请求，并实时播报多步任务的进展。全部音频输出带 SynthID 不可感知水印。即日起在 Gemini API、Google AI Studio、Search Live 上线，Gemini Enterprise 私有预览；Workspace 侧以 Docs Live、Gmail Live、Keep Live 形式向订阅用户开放。🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/

### 3. 🤝 OpenAI 确认与 Anthropic、Google DeepMind 就 AI 安全磋商「已数周」；Dreamforce 上黄仁勋与 Amodei 立场分歧

9月15日，OpenAI 全球政策负责人 Chris Lehane 在华盛顿对记者确认，公司**已与竞争对手 Anthropic 和 Google DeepMind 就 AI 安全协作数周**（彭博社率先报道）。这一披露紧随 Amodei 9月12日的《We Must Pace the Frontier》长文——Altman、Hassabis、Musk 均已公开支持，Altman 表示 OpenAI 将加入 Anthropic，把第三方评估员嵌入公司内部；The Information 另报道三家正合作筹建一个行业标准机构，Altman 对员工称此事可能需要在没有美国政府支持的情况下推进。风险点在于部分人（包括 Altman 本人）提醒，此类协调若被认定抑制竞争可能触及反垄断法；Amodei 建议以「窄口径政府豁免」处理，Lehane 则称无需豁免。同日 Lehane 表示 OpenAI 支持 FRONTIER Act 中要求前沿实验室接纳「独立验证组织」的条款。与此同时，政治层面出现反调：特朗普称 AI 安全担忧为骗局、反对收紧监管，其 AI 顾问 David Sacks 亦称生存风险被夸大。同一天在 Salesforce Dreamforce 大会（约 1.2 万人到场）上，Amodei 与英伟达 CEO 黄仁勋先后登台，立场明显分歧：Amodei 称「引领行业向前的方式是树立榜样、说明人人都能做得更好」；黄仁勋则称之为「**假选择**」——速度与安全可以兼得，市场力量已经足够，行业**不需要新法律或新监管**，「能跑多快跑多快，但如果觉得失控或产品不安全，就停下来把它做对」。黄仁勋前一天在洛杉矶 All-In 峰会演讲时还接到特朗普来电，后者表达了对阻碍 AI 数据中心建设者的不满，黄仁勋回应「我们不会让这种事发生」。同场 Salesforce 与英伟达发布了基于英伟达开源权重 Nemotron 模型构建的 Agentforce 推理模型。🔗 https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/ · https://www.cnbc.com/2026/09/15/nvidia-and-anthropic-ceos-diverge-on-ai-safety-at-dreamforce.html

### 4. 🦊 Mistral × Mozilla：Firefox 的 AI 浏览助手改用 Mistral 模型

9月16日，Mistral 与 Mozilla 宣布合作：Mozilla 的 AI 浏览助手 **Firefox Smart Window**（beta）由 Mistral 模型驱动，帮助用户理解复杂搜索、记住刚浏览过的重要内容、并基于打开的标签页溯源信息。覆盖范围先为**法国与北美**用户，英国和德国预计年内跟进。两家公司强调四点：开源技术需要开源分发渠道、「AI 应为本地区语言和文化优化而非被出口过去」、用户对 AI 交互的控制权（默认不在 Mozilla 服务器保存对话，合作方承诺**零数据保留**）、以及「主权 AI」——Mozilla CEO Anthony Enzor-DeMeo 称「浏览器不应是一条单向漏斗」。🔗 https://mistral.ai/news/mistral-x-mozilla/

### 5. 🔓 AI 黑客智能体 25 分钟拿到 Baseten 的 GitHub 管理员令牌

安全公司 Strix 披露：为评估是否把自家代码与模型交给估值 130 亿美元的推理平台 Baseten，它把自家**自主黑客智能体**指向 `*.baseten.co` 扫描，约 **25 分钟**后该智能体就拿到一枚仍然有效的 GitHub 个人访问令牌（账号 `basetenbot`）。路径是：枚举子域 → 发现一个公开可匿名拉取的 Harbor 镜像仓库 → 下载 `baseten/baseten-app` 镜像 → 用 TruffleHog 扫描层并在镜像 config 的 `history[].created_by` 字段中找到令牌——该字段记录了 2023年3月3日 的构建命令，把 `GITHUB_TOKEN` 直接展开写进了构建历史。令牌权限包括对 Baseten 主产品仓库、驱动集群的 GitOps 仓库 `flux-cd` 与 Homebrew tap 的 **admin + push 权限**，以及多个私有仓库的读写权限（其中 `fde` 仓库还有按客户命名的目录层级）。Baseten 安全团队次日确认该问题为严重级别、将仓库转为私有并轮换了令牌。教训是：清理镜像里的凭据文件没用——构建历史里往往还有另一份副本；应改用 BuildKit secret mount，并即时吊销旧令牌。🔗 https://www.strix.ai/blog/baseten-harbor-github-pat-takeover

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 前 OpenAI 研究员发布「系统一」模型 Jev：放弃生成字符串、只输出类型安全决策，延迟 70–500 毫秒 |
| 🎙️ **模型发布** | Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking，语音质量指数登顶（82.6） |
| 🛡️ **AI 安全** | OpenAI 确认与 Anthropic、Google DeepMind 磋商数周；黄仁勋称安全与速度是「假选择」、无需新监管 |
| 🦊 **产品/生态** | Mistral 联手 Mozilla，Firefox Smart Window 改用 Mistral 模型，承诺零数据保留 |
| 🧰 **工具** | Block 开源 Buzz（3.2 万 Star）把人与 Agent 放进同一工作区；bg0 浏览器本地去背景、SkillSwitch 管理 AI Skill |
