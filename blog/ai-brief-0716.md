---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0716.html"
title: "今日AI简报 — Gemini 3.5 Pro重建、Anthropic与OpenAI监管分裂、Figure 03量产加速"
description: "Google彻底重建Gemini 3.5 Pro基座模型；Anthropic与OpenAI在AI监管策略上公开分裂，各自为IPO铺路；美国政府证实H200芯片已开始对华出货；Figure 03实现24倍产能提升，Helix获感知控制新能力。"
date: "2026-07-16"
tags: ["AI", "Google", "Anthropic", "OpenAI", "Figure", "Nvidia", "芯片"]
---

# 今日AI简报 — Gemini 3.5 Pro重建、Anthropic与OpenAI监管分裂、Figure 03量产加速

**2026年7月16日**

---

## 📡 中文社区动态

**Codex社区热议Superpowers Skill：227k Star的顶级Agent工作流**

中文AI社区@aigc1024推荐了Codex生态中最受认可的Skill——Superpowers（GitHub 227k star）。该Skill为AI Agent配备了一整套资深工程师的工作方法：先拆解需求、再撰写执行计划、按测试驱动开发（TDD）推进、最后派出子Agent审查自己的代码。这套「元工作流」被认为是当前最强的Agent编程方法论之一，核心价值在于将人的工程纪律注入AI的执行过程。

🔗 https://t.me/aigc1024/22177

---

## 🌍 全球AI要闻

**1. Google Gemini 3.5 Pro：推迟一个月后"完全重建"基座模型，明日GA**

Google的Gemini 3.5 Pro经历了上市前的重大变故。据内部消息，原始模型在Vertex AI企业测试中暴露出三个架构级缺陷：递归工具调用稳定性（recursive tool-calling）、复杂SVG场景生成、以及数学推理能力。Google判断这些问题无法通过后训练修复，于是**彻底废弃原有基座模型并重建**。

Sundar Pichai在5月Google I/O上对开发者承诺"再给我们一个月"，但这个月过去了，发布推迟到7月17日——也就是明天。截至今晚，仍未有官方API端点、模型卡、定价页或基准测试发布。预计定价为：输入$15/百万token，输出$60/百万token，Deep Think推理需订阅Ultra层（$250/月）。关注明日发布后的SWE-bench Pro得分——这将决定它在竞争格局中相对于Sonnet 5（63.2%）和Fable 5（80.4%）的位置。

**2. Anthropic vs OpenAI：监管策略的史诗级分裂，也是IPO叙事的分水岭**

Politico确认，Anthropic正在推动**逐州推行更严格的AI安全法**——支持加州SB 53、纽约RAISE Act、伊利诺伊SB 315和马萨诸塞透明度法案——这与OpenAI的"联邦优先"策略形成直接对立。

商业逻辑非常清晰：Anthropic的Responsible Scaling Policy已经满足这些法案的文档和风险评估要求。对Anthropic而言，州级安全法是**护城河**；对OpenAI而言，它们是50倍于单一联邦框架的合规成本。

两家公司都在进入Q4 2026的IPO进程。监管策略现在直接成为投资者关系披露内容。如果加州SB 53在IPO前通过，路演时的问题——"这对你的合规成本有何影响？"——两家公司将给出截然不同的答案。Anthropic："我们已经这么做了。"OpenAI："我们正在与政府合作制定联邦框架。"机构投资者感知到的监管风险差异，可能直接影响IPO定价。

**3. Anthropic-backed Ode启动：企业AI的真正瓶颈在实施，不在能力**

Anthropic支持的新公司Ode正式启动，核心论点直击行业痛点：约95%的企业AI使用仍然在运行前沿模型，没有任何模型路由、任务优化或工作流集成。大多数企业付费使用Claude，实际用途只是"更智能的聊天机器人"。

Ode的商业模式借鉴了Palantir：驻场工程师、构建可工作的部署、衡量输出、留下客户可维护的基础设施。每个Ode部署都是一个Claude客户，能产生可衡量ROI的部署续约率远高于闲置的许可证。对于正在收紧AI预算的企业来说，Ode回答了一个关键问题：问题不是模型不够好，是**实施没做好**。

**4. H200芯片对华出货：美国政府确认首批已启运**

美国高级官员向国会证实，Nvidia H200 AI芯片已开始向中国和香港发货。这是特朗普与习近平会晤后达成的协议的一部分——允许H200（Hopper架构，Blackwell前的上一代旗舰）在25%附加费条件下出口中国。

与此同时，中国计划允许阿里巴巴、字节跳动和DeepSeek等头部AI企业购买**限定数量**的H200。台积电Q2营收$396.2亿创纪录、同比增长36%的消息进一步印证了AI芯片需求的强劲。相比之下，Blackwell系列仍在禁止出口名单上。

---

## 🤖 具身智能

**Figure 03量产加速：350台下线、24倍产能提升、Helix获"感知-全身控制"新能力**

Figure AI宣布BotQ工厂已交付超过350台Figure 03人形机器人，产线速度从每天1台提升至**每小时1台**——120天内实现24倍吞吐量提升。

更关键的是，Helix的System 0（S0）模型获得了一项重大新能力：**基于视觉感知的全身控制**。此前S0只能感知自身关节状态和本体感觉，面对台阶、斜坡和不平地形时需要人工干预。现在，头戴RGB摄像头的图像通过立体模型转化为3D空间表征，S0可以"看见"环境。该策略使用强化学习在仿真环境中在数千种随机地形上端到端训练，**零样本迁移到真实硬件**——无需真实环境微调、无需操作员介入。首批验证场景是楼梯行走，但底层架构支持更广泛的行为类别。

此外，BotQ的产线良率已超过80%，电池线首次通过率99.3%，已生产超500个电池包和9000个驱动器。每个机器人下线前需通过80+项功能验证测试。

🔗 https://www.figure.ai/news/ramping-figure-03-production

---

*简报内容综合自Telegram中文社区、Reuters、The Information、Politico、AIToolsRecap及Figure AI官方渠道。*
