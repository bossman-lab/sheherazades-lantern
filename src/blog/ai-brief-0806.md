---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0806.html"
title: '今日AI简报 — DeepMind高层换帅、Jeff Dean离职创业、Meta发布编码代理'
description: 'Google DeepMind人事巨震：Hassabis转任GDM主席与Alphabet首席科学家，Koray接掌DeepMind，Jeff Dean 27年后离职创办公益公司；Meta发布终端编码代理Muse Code与Muse Spark 1.2；Cloudflare开源Cloudflare OS；Wired曝Meta广告库现AI生成CSAM广告；伦敦批准Wayve Robotaxi商业牌照。'
date: "2026-08-06"
tags: ["AI", "简报", "Google", "DeepMind", "Meta", "Cloudflare"]
---

# 今日AI简报 — DeepMind高层换帅、Jeff Dean离职创业、Meta发布编码代理

**2026年8月6日**

---

## 📡 数据源A：中文频道动态

**AI Agent 采用率之问：为什么科技圈之外几乎没人用 Agent？** — AI 方向频道提出一个「令人费解的问题」：模型已经很厉害、工具也很成熟，为什么我们的朋友和家人还是不用 Agent？作者认为，解答这个采用鸿沟问题「将会在未来一年获得回报」。

🔗 https://t.me/aigc1024/22899

**Gemini 网页版被吐槽拉胯：背后是 DeepMind 高层重组** — 互联网从业者频道吐槽 Gemini 网页版体验不佳，将原因指向 Google DeepMind 高层重组、多名 Gemini 核心成员离职创业——与本日 DeepMind 官方人事变动报道相互印证（见数据源B第1条）。

🔗 https://t.me/https1024/49973

---

## 🌍 数据源B：国际AI要闻

**1. 🔥 Google DeepMind 人事巨震：Hassabis 转任主席、Jeff Dean 离职创业**

Google 8月5日宣布 DeepMind 高层调整：Demis Hassabis 卸任日常运营职务，转任 Google DeepMind 董事会主席兼 Alphabet 首席科学家，继续领导 Isomorphic Labs；CTO Koray Kavukcuoglu 升任 GDM SVP 并接管 Gemini 模型开发与研究。效力 Google 27 年的 Jeff Dean 与 Sanjay Ghemawat 一同离职，创办一家独立公益公司，专注加速 ML、科学与工程研究，Google 将作为创始投资方与云合作伙伴。官方同时披露 Gemini App 月活已超 9.5 亿、Gemma 系列下载量超 9 亿。

🔗 https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/

**2. Meta 发布 Muse Code 终端编码代理与 Muse Spark 1.2**

Meta 8月5日推出 Muse Code（beta）：终端编码代理，通过常驻的异步后台代理并行处理任务，并以本地事件日志实现崩溃后可精确恢复的运行时；内置 /plan、/grill、/goal 等技能。底层模型 Muse Spark 1.2 为编码向更新，显著扩大编码训练算力与环境多样性，并用 Muse Spark 1.1 生成数据做自改进训练；已在 Muse Code 与 Meta Model API 开放，官方称更强大的模型在路途中。

🔗 https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2

**3. Cloudflare 开源 Cloudflare OS：面向 Agent 的开放工作平台**

Cloudflare 8月5日开源新版 Cloudflare OS：任何组织可自行部署并接入内部系统。核心设计是「代理默认零权限」——Agent 与生成的代码默认无法访问任何资源，通过 Gatekeeper 按策略授予单仓库级权限并记录其观察到的数据，「政策跟随代理所见」防止敏感信息经输出外泄；对话可演变为文档、应用或确定性工作流，每个「文件」都可是带持久状态的全栈应用。

🔗 https://blog.cloudflare.com/cloudflare-os/

**4. Wired 调查：Meta 广告库现 50+ 条含 AI 生成 CSAM 的付费广告**

Wired 报道，Tech Transparency Project 在 Meta 广告库发现 50 多条含 AI 生成儿童性虐待素材（CSAM）的图片/视频广告，去年 11 月至今年 8 月初运行，部分本周仍在投放，目标覆盖美、英及十余个欧洲国家，单条最多触达 2,563 个账户。研究者指出这些是「经 Meta 审核、批准并允许投放」的广告；Meta 事后已删除，这是数周内其平台第二次被发现此类广告。

🔗 https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/

**5. Neon + Castform：4B 开源模型检索能力追平 GPT-5.6 Sol，成本低 100 倍**

Neon 与 Castform 联合发布案例：4B 开源模型经 Castform 强化学习后训练，在检索任务上准确率与 GPT-5.6 Sol 相当，而成本低约 100 倍——典型的多轮 Agent 检索调用 gpt-5.6-sol 需 10 秒以上、端到端约 $0.03，后训练的开源小模型可在特定任务上以数量级更低的成本逼近前沿模型。

🔗 https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency

---

## 🤖 数据源C：机器人/具身智能动态

**伦敦批准 Wayve Robotaxi 商业牌照：Uber 车队年内可上路**

伦敦交通局（TfL）向 Uber 车队发放私人租赁牌照：采用英国公司 Wayve 自动驾驶技术的改装福特 Mustang Mach-E（摄像头+雷达），条件是车内必须有持证司机负责安全。已有 10 万人登记意向，「夏末」起将提供体验行程，之后正式开放；伦敦成为 Wayve 技术全球首个商业化运营城市。Figure/Helix 方面今日无实质性新进展，按去重规则不再重复报道。

🔗 https://www.bbc.co.uk/news/articles/c3w07qg43j6o

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | DeepMind 换帅：Hassabis 转任主席、Jeff Dean 27 年后离职创业 |
| 🤖 **AI Agent** | Meta 发布 Muse Code 终端编码代理 + Muse Spark 1.2 |
| ⛏️ **基础设施** | Cloudflare 开源 Cloudflare OS（代理零权限 + Gatekeeper 治理） |
| 🛡️ **安全/治理** | Wired 曝 Meta 广告库现 50+ 条 AI 生成 CSAM 广告 |
| 🚗 **自动驾驶** | 伦敦批准 Wayve Robotaxi 商业牌照，Uber 车队年内上路 |
