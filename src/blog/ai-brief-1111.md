---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1111.html"
title: "今日AI简报 — 模型开始给自己写证明：Gemini 4 Carbon 全面开放，AlphaProof 验完 Signal 协议"
description: "Gemini 4 Carbon 面向所有人开放，三项 Agent 基准登顶、每任务成本不到对手一半；DeepMind AlphaProof Code 用 600 万行 Lean 在四周内形式化验证 Signal 协议；Anthropic 把白板、表格、数据搬进 Claude；Gemini Robotics 2.5 在奔驰产线做到 96% 成功率。"
date: "2026-11-11"
tags: ["AI", "简报", "Gemini", "Anthropic", "DeepMind", "机器人"]
---

# 今日AI简报 — 模型开始给自己写证明：Gemini 4 Carbon 全面开放，AlphaProof 验完 Signal 协议

**2026年11月11日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🧠 Gemini 4 Carbon 全面开放：三项 Agent 基准第一，成本不到对手一半

11 月 10 日，Google 把 **Gemini 4 Carbon** 从「只给 Fairwind 计划的防御方试用」推到全面开放——开发者、企业、科学家和普通用户都能用，AI Studio、Gemini 企业版、Gemini 应用与搜索 AI Mode 同步上线，Google AI Ultra 订阅者可在 Antigravity 里直接用。定位上，Argon 仍是多数软件工程与知识工作的默认选择，Carbon 专门吃「要多花 token 才能啃下来」的活：复杂多步编码与调试、开放式科研，它会在推理与验证循环上跑得更久。官方数字是 **CursorBench 4.0、Perplexity 的 WANDR、Zapier 的 AutomationBench 三项第一，且每任务成本比次优外部模型低 2 倍以上**；与 Artificial Analysis 合建的多模态知识工作基准 MKA 上排第二，但平均每任务成本是榜首的六分之一。价格沿用 Argon 的引入价 **$2/百万输入、$10/百万输出**，11 月 30 日后回到 **$4/$20**。同时预览 Antigravity 的 `/swarm`：一句提示变一支可实时追踪的 agent 团队，把架构设计、协调、审计交给 Carbon，并行隔离工作区里跑更快的小模型配合对抗性验证器。🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/

### 2. ✅ AlphaProof Code：600 万行 Lean、四周，把 Signal 协议的实现本身证完了

同一天，Google DeepMind 发布 **AlphaProof Code**——一个把形式化验证拆成「人定目标、agent 做证明」的多模型 agent 框架，拿下的第一个目标是 Signal 协议的加密实现。这条新闻的分量在两个「首次」：**第一次有 AI 参与把广泛部署的加密协议验证到这个深度，也是第一次有人（无论用不用 AI）把这类协议的实现代码形式化验证完**——多数协议验证只做到设计层，而真实漏洞往往藏在设计与实现之间。流程是：研究者与模型共同把 Signal 的安全目标翻译成数学规格（每条人工复核），随后由 **Gemini 4 Carbon** 驱动的 agent 生成 **600 万行以上 Lean** 证明，Lean 自动检查全部内容，agent 再把需要人看的部分标出来——只有代码库的 **1%** 需要专家逐行审查。整件事 **四周**做完，同类工作历史上以年计；为验证它不是「什么都能证」，团队把两个已修复的真实漏洞重新植入隔离版本，系统两次都给出了「这个版本不安全」的机器可检证明。验证产物已开源。🔗 https://deepmind.google/blog/introducing-alphaproof-code/

### 3. 📋 Anthropic 把办公套件搬进 Claude：白板、表格、数据，都在同一个窗口

11 月 10 日 Anthropic 发布 **Claude Whiteboards** 与 **Claude Sheets**（beta），并把 10 月上线的 Dashboards 转正更名为 **Claude Data**，三者对所有付费套餐开放，覆盖 web、桌面与移动端。白板是团队与 Claude 一起脑暴的共享画布：口述一个乱糟糟的计划，Claude 把它变成带时间线、负责人和日期的板子，拖框圈住任意区域就能追问，结束后一键转文档/演示，或导出到 Lucid、Miro、Vani by Zoho 继续做。表格能直接按提示生成带多标签页、公式、格式与下拉菜单的表，改单元格时逐条列出改动，需要完整 Excel 能力时导出 .xlsx/CSV。Claude Data 则加上**认证查询**（数据团队把唯一正确的口径钉住，图表带「认证」徽章）、数据故事、实时共享、缓存与改动追踪，接 Redshift/BigQuery/ClickHouse 等连接器。配合同日上线的交互式连接器（Adobe、Atlassian、Box、Notion 可作为完整应用在对话旁打开），Anthropic 补的是「产出留在 Claude 里继续改」这一环——赶在 11 月 19 日 Enterprise 默认开启 Claude Data 之前。🔗 https://claude.com/resources/articles/sheets-whiteboards-data

### 4. 🧱 「用 AI 写代码，会得到一个脆的代码库」：一位前 Meta 工程师的四条病理

HN 578 分、543 条评论的这篇长文值得单列。作者 Evan X. Merz 今年 5 月被 Meta 裁掉，他自述原因是「对把 LLM 当编码工具没那么积极」——在 Meta 最后几个月，他至少 **90% 的代码由 AI 生成**，那是拿到合格评级的底线，但 AI 没让他写出 10 倍的代码，连 2 倍都没有。他现在在另一家大厂 **100% 用 AI 写码**，因为「这是今天的期望」，于是把这套做法的病理写清楚：AI 写浅测试（大量 get/set 与只覆盖已有路径的 e2e，行覆盖率很好看、空洞没人看见）、写过度复杂的代码（一个方法能解决的事拆成三个 helper，把 DRY 执行到妨碍调试）、让人越来越不懂自己的代码库、以及提交速度快到评审只能扫一眼。症状也给了四条：事故变多、恢复变慢（因为没人熟悉那片代码）、错误只有真实用户看得见、体验持续退化——「AI 代码库是 AI 给 AI 写的软件」。🔗 https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/

### 5. 💰 OpenAI 营收升至 100 亿美元，亏损仍在扩大

WSJ 11 月 10 日报道，OpenAI 营收已升至 **100 亿美元**量级，但同期亏损继续扩大，成本结构没有随收入改善。报道本身在付费墙内，未公开具体亏损数字与统计口径。放在本周的语境里看：Anthropic 正带着招股书跑 IPO 路演，OpenAI 的收入曲线开始有形状，但两家都还没走出「规模越大、烧得越多」的阶段。🔗 https://www.wsj.com/business/earnings/openai-continues-to-suffer-heavy-losses-as-revenue-rises-to-10-billion-d2a96bbb

---

## 🤖 数据源C：人形机器人动态

### Gemini Robotics 2.5：200 项任务、成功率涨 30–100%，在奔驰产线做到 96%

Google DeepMind 11 月 10 日发布 **Gemini Robotics 2.5**，称是其最强 VLA 模型，一次把灵巧度、可靠性、安全性三条线同时往前推。评估覆盖 **200 项以上**任务（用夹子分餐、给礼盒系蝴蝶结、移液枪加样），相比上一代基线成功率高出 **30% 到 100%**（视任务类型），完成速度快 **20% 到 30%**；本体侧同时支持 Apptronik **Apollo 2**（配 22 自由度五指 SharpaWave 手）与 Franka Duo 双臂平台。真实场景的硬证据在奔驰：匈牙利 Kecskemét 与德国 Sindelfingen 产线上，Apollo 2 自主做**汽车零件 kitting**（把散装零件按每辆车的顺序分装到托盘），由 Gemini Robotics ER 管流程、2.5 控手和臂，成功率 **96%**。安全上新增推理时引导，绕障完成率提升 **33%**、在人附近作业提升 **43%**；同时开源 **ASIMOV-Jailbreak** 越狱基准（数百条伪装成正常指令的危险请求），Gemini 4 Argon 在其上抗越狱 **99.5%**（前代 ER 2 为 82%）。有意思的一层：Gemini 4 Argon 被当作仿真引擎反哺了这一代模型——从一张真实相机画面生成上千次带数字孪生的练习。🔗 https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/

### 蚂蚁旗下 Robbyant 开源 LingBot-Touch：约 5000 小时触觉数据，让机器手「摸着干」

蚂蚁集团旗下机器人公司 **Robbyant** 于 11 月 10 日放出 **LingBot-Touch** 的模型权重与推理代码。这是个专攻「用手摸」的模型：训练数据来自 **三类触觉传感器、近 5000 小时**录制，目标是同一套模型能跨不同硬件工作，而不是绑死在某一款机械手上。官方在**两只机械手、26 项真实任务**上做了评测，场景包括处理易碎物体和双手协同——触觉正是人形机器人干活时最容易掉链子的一环（视觉能告诉你杯子在哪，摸不出它会不会碎）。🔗 https://technode.com/2026/11/10/ant-groups-robbyant-open-sources-tactile-ai-model-for-robot-hands/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🧠 **最热** | Gemini 4 Carbon 全面开放：CursorBench 4.0 / WANDR / AutomationBench 三项第一，成本仅对手一半 |
| ✅ **可验证性** | AlphaProof Code：600 万行 Lean、四周，首次形式化验证 Signal 协议实现，人只看 1% 代码 |
| 📊 **办公** | Claude 白板 / 表格 / 数据三件套上线，交互式连接器把第三方应用搬进对话 |
| 🧱 **反方声音** | 前 Meta 工程师：90% 代码交给 AI 后，得到的是浅测试、过度复杂与「没人懂」的代码库 |
| 💰 **财务** | OpenAI 营收升至 100 亿美元，亏损仍在扩大 |
| 🤖 **具身智能** | Gemini Robotics 2.5 把奔驰产线 kitting 做到 96%；蚂蚁 Robbyant 开源 5000 小时触觉模型 |
