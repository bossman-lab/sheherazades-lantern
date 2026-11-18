---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1118.html"
title: "今日AI简报 — GPT-6.2 单价再降 20%，英伟达交出没有黄仁勋的第一份财报"
description: "OpenAI 发布 GPT-6.2 Astra 与 Sol：Astra 输入输出各降 20%（$8/$40），Agents' Last Exam 超 GPT-6 Astra 5.2 分而成本不到三分之一；英伟达 Q3 营收 1158 亿美元、同比翻倍，董事会主席在电话会开场明说不让黄仁勋回归并已聘猎头，Q4 指引假设对华数据中心芯片销售为零；Anthropic 据 CNBC 将定价高于 70–78 美元区间，代码 ANT；微软发 MAI Code 2，98% 的 GPT-6.1 Sol 性能打四折。"
date: "2026-11-18"
tags: ["AI", "简报", "OpenAI", "Nvidia", "Anthropic", "微软", "人形机器人"]
---

# 今日AI简报 — GPT-6.2 单价再降 20%，英伟达交出没有黄仁勋的第一份财报

**2026年11月18日**

---

## 📡 数据源A：中文频道速览

### 1. 💰 一条「AI 信息差」的报价单：从 500 元到 3000 元，五段时间窗口

@aigc1024 转述了一个粉丝分享的案例，价值不在于这个人赚了多少，而在于它把过去两年 AI 的每个热点都标了价：TikTok 刚起来时教人下载、配环境，**500 元/人、收了 200 多人**（约 10 万元）；「小龙虾」火的时候上门安装调试，**2000 元/人、一百多个**（20 多万）；AI 数字人给门店做宣传视频，**500 元/条**（十几万）；企业 RAG 知识库搭建，**6000 元/客户、十几个**；现在换成「帮忙搞一个不封号的 Claude 账号」，**报价 3000 元、据说已预定 20 多单**。讲故事的人说这哥们自称做 TikTok 跨境，实际没开店、没注册账号、甚至没下载过 TikTok。**要注意最后一段已经踩进灰色地带**——账号代注册本质是绕过平台风控，不是技术服务；前面四段则是典型的信息差套利：需求真实存在，供给方只是「先学会一步」。🔗 https://t.me/aigc1024/27158

### 2. 🛠️ 两个开源小工具：让 Claude Code 剪视频，让 coding agent 改 Blender 模板

@https1024 转发了两个 11 月 13 日建仓的仓库。**scarlet**（360★）是一个 AI 视频剪辑器：把素材交给 Claude Code 或 Codex，用一句自然语言删掉访谈里的停顿、口误和重复 take，而且**只渲染改动的片段**供试听——省的是重编码时间，不是省点鼠标。**shred-kit**（45★）更偏玩具：一个 Blender + Python 的 8 秒竖版循环视频模板（印刷海报撕成纸条→碎纸机→逐行拼回），改文案、字体、配色靠跟 coding agent 对话，不用打开 Blender 界面。两个项目的共同点是：**AI 不再是界面里的一颗按钮，而是替你操作另一个软件的那个「人」**。🔗 https://github.com/Forward-Future/scarlet ｜ https://github.com/amirmushichge/shred-kit

---

## 🌍 数据源B：国际AI要闻

### 1. 🧠 GPT-6.2 Astra / Sol：更少 token、更便宜，但先被自家用户骂了一轮

11 月 17 日 OpenAI 发布 **GPT-6.2 Astra**（前沿档）与 **GPT-6.2 Sol**（日常档）。核心卖点是「同样的钱干更多活」：Astra 的 API 价格比 GPT-6 Astra **输入输出各降 20%**，缓存输入再打四折——**$8 输入 / $0.40 缓存输入 / $40 输出**（每百万 token）；Sol 则**沿用 GPT-6.1 Sol 的 $2 / $0.10 / $10**。基准上，Astra 在测多步专业工作的 **Agents' Last Exam** 上比 GPT-6 Astra 高 **5.2 分、成本不到三分之一**，比 Claude Fable 5.2 高 **5.5 分、成本仅 5%**；**Terminal-Bench-Science 0.1** 高 9 个百分点、成本不到三分之一；内部 GDPval v2 提升 6.2 分且**输出 token 少 22%**；法律基准 Harvey LAB-AA 上「通过率是 Fable 5.2 的两倍以上、成本约六分之一」，另有一个 **Astra for Law** 专项配置。两个要打的折扣：OpenAI 自己脚注说明 **Fable 5.2 的榜单成绩排除了 9 个用了 fallback 模型的任务**；而 HN 上首批用户反馈偏负面，有帖子直指「在已知的行为回归没修的情况下就发了 6.2」。可用性方面，Plus/Pro/Enterprise/Edu 的 ChatGPT Work 与 Codex 即日可用，**Pro 200 首次拿到 Ultrafast（先用 Sol）**，API 同日上线。🔗 https://openai.com/index/introducing-gpt-6-2-astra-sol/

### 2. 📉 英伟达交出没有黄仁勋的第一份财报：数字很漂亮，主席把门关死

11 月 17 日盘后，英伟达 Q3 FY2027：**营收 1158 亿美元（同比 +103%、环比 +20%）**，数据中心 **1076 亿（+110%）**，毛利率 74.8%，EPS **2.70 美元**——都高于分析师预期的 1091 亿 / 2.47 美元。但电话会的开场白比财报更硬：新任董事会主席 **Harvey Jones** 第一句话就是「董事会**一致接受**了他的辞呈，**不打算让 Jensen 重新担任 CEO**」，并声明不就辞职情形与正在进行的调查回答问题；董事会已聘 **Heidrick & Struggles** 寻找新 CEO。临时 CEO **Colette Kress** 的说法是「我们的领导层这一周站得很稳，我们搞得定」，并称台积电高层就在办公室协助，Vera Rubin「开局很猛、已开始出货」。真正被低估的是指引：**Q4 营收 1300 亿 ±3%**（高于预期 1252.5 亿），且**假设对华数据中心芯片销售为零**——这与商务部周一封堵「第三国租算力」的规则是同一条线。市场先给了正面反应：盘后涨 4.5%，但年内仍跌约 17%、市值约 3.8 万亿美元。当天黄仁勋在 X 上发声明称自己「没达到公司对每个人的标准」、后悔、会配合调查，并说若董事会认为有利愿回来；**12 月 1 日他将到国会作证**。贝索斯在 Semafor 会议上给了董事会一个反向建议：「如果不请回 Jensen，我也不会找外部人——英伟达太复杂了。」🔗 https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027 ｜ https://www.cbc.ca/news/business/nvidia-earnings-jensen-huang-9.7425620

### 3. 🔔 Anthropic 据称将定价高于区间：代码 ANT，明天开始交易

CNBC 的 David Faber 周二引多位消息人士称，Anthropic 的 IPO **很可能定在 70–78 美元现区间之上**；公司将在**纳斯达克**上市，代码 **ANT**，**11 月 19 日**开始交易。这条之所以值得单列，是因为它把 11 月 17 日简报里的数字改写了：按 8.25 亿股基础发行、区间上限 78 美元计算，基础募资约 **643.5 亿美元**；若定价高于区间，这个数字还要上移（含超额配售的口径另算）。另有一条同日细节：英伟达除此前承诺的 100 亿美元外，**又同意通过私募认购 100 亿美元 Anthropic 股票**——芯片供应商同时是股东和客户，这个闭环在 IPO 定价前夜显得格外扎眼。🔗 https://www.cnbc.com/2026/11/17/anthropic-ipo-price.html

### 4. 🪟 微软不装了：MAI Code 2 用 5% 的成本做到 Opus 5.5 的 96%

11 月 17 日 Microsoft AI 发布 **MAI Code 2** 与 **MAI Code 2 Flash**，定位非常明确——不追前沿，只打「企业日常写码」的性价比。四项常用编码基准的平均值（DeepSWE 1.1、Terminal Bench 2.1、SWE-Atlas、FrontierCode v1.1）：MAI Code 2 给出 **GPT-6.1 Sol 98% 的性能、40% 的成本**，以及 **Claude Opus 5.5 96% 的性能、5% 的成本**；Flash 则对标 GPT-6 Luna 与 Claude Haiku 5.5，成本分别是它们的 **65% 与 20%**。在盲测前端应用里，评审**67% 的情况下更喜欢它的结果**，胜过 GPT-6 Sol。官方的自我限定也写得很直白：**没有针对基础科学研究和超长程 agent 任务调优**。配合路透与 Axios 同日的解读，这就是微软「不再只做 OpenAI 的分销商」的又一步。🔗 https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/

---

## 🤖 数据源C：机器人与具身智能

### 1. 🇫🇷 法国 Genesis AI 融 5 亿美元、估值 35 亿：欧洲机器人最大轮次之一

11 月 17 日，法国初创 **Genesis AI** 宣布完成 **5 亿美元**融资、估值 **35 亿美元**，投资方包括前谷歌 CEO **Eric Schmidt**、**Khosla Ventures**、法国电信大亨 **Xavier Niel**、**英伟达**与法国国家投资银行 **Bpifrance**，A 轮由 Khosla、Premji Invest、Eclipse 联合领投。它的旗舰 **Eno** 刻意不做人形：三段像超大扑克牌的身体装在旋转轮式底座上，可折叠收进紧凑空间，工作时像弹簧盒一样「弹起」到接近人的身高；CEO **周贤**的解释是「我不理解机器人为什么需要头，那里又没有大脑」。公司把重点押在最难的一环——**灵巧手**，并自己设计执行器、电机、减速器与手，同时自研 AI 与训练系统以缩短迭代。落地路径是先美国（美国供应链、代工厂、客户），与 **LG CNS** 在制造和物流场景测试，**2027 年**才更大规模铺开。欧洲人形/工业机器人估值已排出一列：英国的 Humanoid、德国的 Neura Robotics、Agile Robots、RobCo。🔗 https://www.channelnewsasia.com/business/french-robot-maker-genesis-raises-500-million-35-billion-valuation-6559521

### 2. 🦾 Google 把机器人开发搬进 Antigravity：插上机械臂 10 分钟能动能标定

Google 11 月 17 日为 **Antigravity** 上线 **Robotics 插件**，把上周发布的 **Gemini 4 Hydrogen** 真正接到硬件上。两个数字最说明问题：在 **Artificial Analysis Robotics 0.1** 基准上，Hydrogen 用真实六轴机械臂做 8 项桌面任务（倒饮料、装箱等）拿到 **58 分**，与更贵的 Argon 相近；在 **ERQA** 的空间推理（多视角对应、3D 轨迹）上超过专门的 Gemini Robotics ER 2，官方直接建议 ER 2 用户迁到 Hydrogen。流程上，把 I2RT YAM 机械臂和深度相机插上笔记本、用自然语言让 Hydrogen 接管，**约 10 分钟完成装软件、找相机、标定与试动**；MuJoCo 直接跑在 Antigravity 里，可以「vibe sim」——用对话调形状、位置、物理参数，先在仿真里验证抓取再上真机。演示里从一张白板草图（传送带分拣零食）到一小时内在真机上稳定跑通。这条的意义不在分数，而在**机器人应用的门槛从「会搭整套栈」降到了「会描述任务」**。🔗 https://developers.googleblog.com/gemini-hydrogen-for-robotics/

### 3. 📈 人形机器人被做成 ETF：阿布扎比 12 月 8 日上市，代码 ROBOTS

阿布扎比投资机构 **Lunate** 计划 **12 月 8 日**在阿布扎比证券交易所上市 **Boreas VettaFi Humanoid Robots UCITS ETF**，代码 **ROBOTS**，跟踪 VettaFi Humanoid Robot Select Markets Net Total Return 指数，初始持有 **41 家公司**，覆盖半导体、机器人零部件、人形开发商与软件四段价值链。这是 Lunate 在该交易所的**第五只主题 ETF**（此前已有 AI 数据、电力与基础设施、量子计算、奢侈品），持仓名单与费率均未公布。对产业的意义比对投资者更直接：当一个主题能被做成指数和 ETF，说明**卖方已经能把它拆成可估值的β**——这通常比任何一台机器人的发布会更早反映资本市场的判断。🔗 https://humanoidbeat.com/news/lunate-boreas-humanoid-robots-etf-abu-dhabi-securities-exchange.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🧠 **最热** | OpenAI 发布 GPT-6.2 Astra / Sol：Astra $8/$40（输入输出各降 20%、缓存再打四折），Agents' Last Exam 超 GPT-6 Astra 5.2 分而成本不到 1/3；Sol 维持 $2/$10 |
| ⚠️ **口碑反差** | 基准很强但首批用户不买账：HN 有帖称「已知行为回归未修就发布」；OpenAI 脚注承认 Fable 5.2 对比分排除了 9 个 fallback 任务 |
| 📉 **英伟达** | Q3 营收 1158 亿（+103%）、数据中心 1076 亿；主席 Harvey Jones 开场明说「不打算让 Jensen 回归」并聘 Heidrick & Struggles；Q4 指引 1300 亿且假设对华芯片销售为零 |
| 🔔 **IPO** | Anthropic 据 CNBC 将定价高于 70–78 美元区间，纳斯达克代码 ANT，11 月 19 日交易；英伟达另以私募认购 100 亿美元 |
| 🪟 **微软** | MAI Code 2：GPT-6.1 Sol 的 98% 性能打四折、Opus 5.5 的 96% 性能只花 5%；Flash 对标 Luna / Haiku，明说不管硬科学与超长程 agent |
| 🇫🇷 **机器人融资** | Genesis AI 5 亿美元 @ 35 亿估值，Schmidt、Khosla、Nvidia、Bpifrance 入局；Eno 三段折叠机身 + 灵巧手，2027 年铺开 |
| 🦾 **开发门槛** | Google Antigravity Robotics 插件：机械臂 10 分钟标定、MuJoCo 内「vibe sim」、一小时跑通分拣产线；Hydrogen 在 AA Robotics 0.1 得 58 |
| 📈 **资本化** | Lunate 的 Humanoid Robots ETF 12 月 8 日在 ADX 上市（ROBOTS），41 家公司覆盖四段价值链 |
