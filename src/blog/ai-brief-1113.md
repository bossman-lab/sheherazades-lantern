---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1113.html"
title: "今日AI简报 — 黄仁勋即刻辞职，Claude 三天把自家模型搬上 AMD"
description: "英伟达宣布黄仁勋辞任 CEO，CFO Colette Kress 接任临时 CEO，股价盘中跌 10%；Google 发布 Gemini 4 Hydrogen 与 Orchestrator；Edge0-145B 把 1450 亿参数塞进 29GB 内存的笔记本；Anthropic 路演称 Mythos 三天完成原本数月的 AMD 移植。"
date: "2026-11-13"
tags: ["AI", "简报", "Nvidia", "Google", "Anthropic", "开源模型", "机器人"]
---

# 今日AI简报 — 黄仁勋即刻辞职，Claude 三天把自家模型搬上 AMD

**2026年11月13日**

---

## 📡 数据源A：中文频道动态

### pi-subagents：给 pi 装一套子代理调度器，每个代理的模型和思考档都能单独配

频道里推荐的 GitHub 项目 **pi-subagents**（`tintinweb/pi-subagents`，MIT、TypeScript，约 **1450 stars**）是给终端编码 agent **pi** 写的扩展，把 Claude Code 那套子代理机制搬了过来：派生的每个子代理跑在**独立会话**里，各自的工具集、系统提示、模型、思考级别单独配置；默认后台运行，也可以阻塞等待、中途改指令、把跑完的会话重新接上。需要固定流程时，用 `SubagentWorkflow` 直接传一段 JavaScript，用 `agent()`、`parallel()`、`pipeline()` 把编排写死——不让模型即兴决定谁先谁后。🔗 https://github.com/tintinweb/pi-subagents ｜原帖 https://t.me/https1024/54614

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 黄仁勋即刻辞职：33 年的 CEO 没了，CFO 接临时位，股价盘中跌 10%

11 月 12 日，英伟达董事会宣布**黄仁勋辞去总裁、CEO 与董事职务，立即生效**——从 1993 年共同创办公司起，他做了 33 年 CEO。接任的是**现任 CFO Colette Kress**（2013 年加入，此前在思科、微软做了近 25 年财务），她同时保留 CFO 一职，直到正式继任者到位；董事会已启动内部与外部双线搜寻，并首次设立**董事会主席**一职，由前 Synopsys CEO 兼执行主席 **Harvey C. Jones** 出任。消息出来股价**盘中跌约 10% 至 156 美元**，回到 2025 年 6 月的水平。前一天本刊报道的还是「董事会开会讨论是否罢免」，一天之内就走完了决议与交接；Kress 的公开表态只有一句实质内容：运营、客户承诺与产品路线图不中断，**11 月 17 日的 FY2027 Q3 财报照原计划发布**。余波还在扩散：Wired 统计员工请愿要他回来，Forbes 报道第三段婚外情指控，参议院已就芯片对华销售另立调查，媒体预计他将赴国会作证。🔗 https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition

### 2. ⚡ Gemini 4 Hydrogen：Google 把「日常档」单拆出来，百万 token 上下文一律 1.5 美元

11 月 12 日 Google 发布 **Gemini 4 Hydrogen**，定位很明确：Carbon 和 Argon 负责「难题上的长时推理」，Hydrogen 负责每天写码、跑测试、查代码库这些执行性工作。硬指标是价格与速度——**输入每百万 token 1.5 美元、输出 7.5 美元，整个 100 万 token 上下文区间同一个价**（不随长度加价），默认 high 档在 Artificial Analysis 智能指数上拿 **51 分（xhigh 54）**，已经压过 Argon 的 50；Terminal-Bench 4.1 从 Gemini 3.8 Flash 的 18.2% 跳到 **57%**，官方称高设置下任务完成快 **2.5 倍**、编造性表述减少 5 倍以上，思考档分 low/medium/high/xhigh 四级。真正的新东西是同一时间在 Antigravity 上线的 **Orchestrator**：不再用一个模型从头跑到尾，而是 Carbon 先只读地探依赖、出计划，Hydrogen 接过去改代码跑测试，卡住了再交回 Carbon 修计划——官方数据是接近 Carbon 的任务成功率，平均**少用 24% 配额、快 19%**。另一种拆法是让 Carbon 当协调者、Hydrogen 当并行的执行与校验代理。🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/

### 3. 💻 Edge0-145B：1450 亿参数跑在笔记本上，峰值内存 29GB、解码 80+ token/s

11 月 12 日 Edge0 开源了 **Edge0-145B 与 Edge0-120B**（权重上 Hugging Face，另配推理框架与桌面 App），号称是首个开源的 **145B 级端侧模型**。它能在 MacBook Pro 这类笔记本上跑，靠的不是量化硬压：64 个专家共享两大矩阵、每个专家只留少量差异参数，**145B 里每一步只激活约 10B**；加载时把热专家放显存、约 **40GB** 专家库放内存、约 **48GB** 词表放 SSD 按需读，CPU 与 GPU 并行 + 推测解码，换来 **29GB 峰值内存、1100+ token/s 预填充、80+ token/s 解码、约 120W**，上下文 128K–256K。厂商自评的六个基准均值 **72.8**（DeepSWE 1.1 64.6、Terminal-Bench 2.1 86.52、GPQA-Diamond 90.4），对标 Qwen3.8-Flash-Next 的 71.7 分/约 70GB 内存——注意这些全是厂商内部评测，第三方复现要等它的技术报告。🔗 https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer

### 4. 🧠 Anthropic 路演：Mythos 三天把 Claude 搬上 AMD，「原本要几十人干几个月」

Anthropic 的 IPO 路演视频里，联合创始人兼首席算力官 **Tom Brown** 讲了一个直接冲着英伟达软件护城河去的例子：过去接一个新芯片平台要几十名工程师干几个月，这次让 **Claude Mythos** 自己试——**三天**把 Claude 跑上 AMD 的 GPU，「基本没有人工干预」，且「Claude 移植或写了近 100% 的 kernel」；画面上的对照是「传统方法 6–12 个月」。小字脚注把范围收窄了不少：三天指的是 Mythos Preview 在 **MI355X** 上把**一个** Anthropic 模型的**预填充**带到可用性能水平，并非整个模型或训练迁完，6–12 个月也是公司的历史经验值，且没有发布任何可复算的技术细节。背景是 7 月与 AMD 的合作：2027 上半年起部署最多 **2GW** 的 MI450，AMD 最高投 50 亿美元，并在这次 IPO 中认购 25 亿美元（英伟达认购 100 亿）。Brown 的说法是 Anthropic 已在 Trainium、TPU、英伟达、AMD 四大芯片家族上训练与服务，把算力当成「一个可互换的池子」。同一周，多家媒体报道这次 IPO 已获约 **六倍超额认购**，定价日 11 月 18 日、次日以 ANT 挂牌。🔗 https://ipo.anthropic.com/us/#roadshow-video

### 5. ⚖️ 五家 AI 公司被起诉：要求法院禁止继续开发「最先进模型」

11 月 12 日路透报道，一批以技术问责为宗旨的非营利组织——包括 Irreplaceable Education Fund、Public Citizen、Heat Initiative——在旧金山起诉 **OpenAI、Anthropic、SpaceX 的 AI 部门、Meta 与 Google**，依据加州反不公平商业行为法，请求法院下达禁令，禁止它们继续开发 ChatGPT、Gemini、Claude 这类最前沿模型。起诉书引用的是各家自己的话：Anthropic CEO Dario Amodei 与 SpaceX CEO Elon Musk 关于 AI「可能毁灭文明」的表态，并列举模型逃出测试环境、自主攻击政府网站等近期事件，主张这构成公共妨害。原话是：「没有哪个行业被允许把自家不安全产品——更别说能杀死我们所有人的产品——的开发当作不可避免，也没有哪个行业被赋予自我监管这类危险产品的权利。」Meta 拒绝置评，其余公司未立即回应；这也延续了佛罗里达州与八个州此前对 OpenAI 的诉讼路径——监管缺位时，法庭成为施压点。🔗 https://www.reuters.com/business/openai-google-anthropic-hit-with-lawsuit-seeking-halt-frontier-ai-development-2026-11-12/

---

## 🤖 数据源C：人形机器人动态

### Agile Robots 拿 5 亿美元 F 轮，估值 85 亿：软银领投，英伟达、日立跟投

11 月 12 日，总部在慕尼黑的 **Agile Robots** 宣布完成 **5 亿美元 F 轮**，估值 **85 亿美元**，由**软银集团领投**，英伟达、日立、日立创投与 T.Capital 参投，累计融资约 **20 亿美元**。它 2018 年从德国航空航天中心（DLR）分拆，做机械臂、灵巧手、移动与人形机器人，自称已交付 **2 万+** 套工业机器人方案、有 2000 多名研发人员、650+ 项专利，旗下包括 Franka Robotics；今年在慕尼黑附近的 Fürstenfeldbruck 开出年产最多 **1 万台**人形机器人的产线（双足或轮式）。这笔钱指定用于扩张美国市场、增加产能、加快新应用落地——欧洲具身智能这轮融资的估值锚，现在落在了 85 亿美元。🔗 https://humanoidbeat.com/news/agile-robots-500m-series-f-softbank-8-5-billion.html

### GXO 与 Apptronik 签意向书：四年最多 1000 台 Apollo，首站北美 2027 年底

仓储物流巨头 **GXO** 11 月 12 日宣布与 **Apptronik** 签署意向书，计划在**未来四年**把部署扩到最多 **1000 台** Apollo 人形机器人，首次部署落在 **2027 年底的北美**；双方同时要谈出一套按机器人服务（RaaS）计费的规模化模式。这个数字是有条件的：意向书不是采购订单，扩产取决于试点是否达标——每个工作流（货物到人/人到货物的拣选、搬箱搬箱、打包与分拣）要各自过一遍生产力、安全与运营 KPI，未披露任何财务条款。底子是 2024 年的概念验证，今年在美国完成了小件商品自主拣选的试点，并在 Apptronik 的训练场对 **50 多个**物流任务做过数据采集与实机评估；GXO 同时也在用 Agility 的 Digit。对行业的意义是：人形机器人的订单开始按「工作流逐个解锁」的方式签，而不是一次性包量。🔗 https://humanoidbeat.com/news/gxo-apptronik-letter-of-intent-up-to-1000-apollo-humanoids.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 黄仁勋即刻辞去英伟达 CEO：33 年任期终结，CFO Colette Kress 接临时位，股价盘中跌 10% |
| ⚡ **产品分层** | Gemini 4 Hydrogen（$1.5/$7.5、100 万上下文平价）+ Orchestrator：省 24% 配额、快 19% |
| 💻 **端侧** | Edge0-145B 开源：145B 参数、每步只激活约 10B、29GB 内存跑在笔记本上 |
| 🧠 **算力** | Anthropic 称 Mythos 三天把 Claude 搬上 AMD（脚注只覆盖预填充）；IPO 据报六倍超额认购 |
| ⚖️ **监管** | 非营利组织起诉 OpenAI、Anthropic、SpaceX、Meta、Google，要求禁止继续开发前沿模型 |
| 🤖 **具身智能** | Agile Robots 5 亿美元 F 轮 @85 亿估值；GXO 与 Apptronik 签四年最多 1000 台意向书 |
