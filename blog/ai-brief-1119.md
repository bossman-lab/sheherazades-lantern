---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1119.html"
title: "今日AI简报 — Anthropic 813 亿美元定价，英伟达对中国一颗不卖"
description: "Anthropic 以每股 83 美元定价、9.8 亿股募资约 813 亿美元，估值 1.5 万亿，今日纳斯达克开盘，超过 6 月 SpaceX 成为史上最大 IPO；英伟达临时 CEO Kress 在电话会明确「不再向中国出货任何授权 Hopper 数据中心产品」，60 万颗 H200 困在香港；微软 Ignite 一次放出七个模型，MAI Cyber 2 Flash 用不到 2% 的成本追平 GPT-6 Astra；谷歌同日发 Gemini 4 Neon 与 Genie 4。"
date: "2026-11-19"
tags: ["AI", "简报", "Anthropic", "英伟达", "微软", "Gemini", "机器人"]
---

# 今日AI简报 — Anthropic 813 亿美元定价，英伟达对中国一颗不卖

**2026年11月19日**

---

## 🌍 数据源B：国际AI要闻

### 1. 💰 Anthropic 定价 83 美元、募资 813 亿：史上最大 IPO，今天开盘

11 月 18 日 Anthropic 完成 IPO 定价：**每股 83 美元**，发行 **9.8 亿股**（其中公司出售 9.5635 亿股、老股东出售 2364 万股），**基础募资约 813 亿美元**，公司实收约 794 亿美元；若承销商全额行使 30 天内 1.47 亿股的超额配售权，总额可达 **约 935 亿美元**。按 AP 口径估值 **1.5 万亿美元**，规模已超过 6 月 SpaceX 的约 750 亿美元，成为史上最大 IPO。股票今日在纳斯达克以 **ANT** 开始交易、11 月 20 日交割；开盘前灰市指示价约高出定价 **20%**。同一天还有两个注脚：TechCrunch 统计上市后亚马逊与谷歌合计持股仍接近 **30%**；而定价前夜，AI 安全中心（CAIS）联合 Steven Pinker、诺奖经济学家 Oliver Hart、图灵奖得主 Judea Pearl、Lawrence Lessig、Hugging Face 的 Thomas Wolf 等人发表《MisAnthropic 声明》，直指 Anthropic「一边警告递归自我改进的危险，一边抢着先造出来；用安全品牌换取投资人、员工与公众的信任」——署名人里既有安全派也有加速派，共同点是不认「行业好人」这个位置。🔗 https://www.anthropic.com/news/anthropic-prices-initial-public-offering ｜ https://apnews.com/article/anthropic-ipo-pricing-70b660ddf900d90bbf484ecdf1fb441c ｜ https://www.businesswire.com/news/home/20261118974464/en/

### 2. 🚫 英伟达不再向中国出货任何 AI 芯片，包括已获批准的 H200

临时 CEO **Colette Kress** 在周二财报电话会上说得很直接：「我们的指引里没有任何授权 Hopper 数据中心产品，我们**已经不再向中国出货授权 Hopper 数据中心产品**。」这句话把前一日「Q4 指引假设对华数据中心芯片销售为零」从会计假设变成了既成事实——白宫去年 12 月批准 H200 对华销售，黄仁勋曾为此大力游说，如今公司主动收手。背景有两个：路透此前报道约 **60 万颗 H200** 因北京未批大规模进口而滞留香港、中国在刻意降低对美技术的依赖；而据 The Verge，公司也未解释停售原因、未说明是否还有别的对华业务。🔗 https://www.theverge.com/tech/1036445/nvidia-h200-ai-chips-china-stop-selling

### 3. 🪟 微软 Ignite 一次放出七个模型：把「够用」做成了一条产品线

11 月 18 日 Microsoft AI 在 Ignite 上发布**七款新模型**，逻辑高度统一——不求最强，只求「前沿水平的百分之多少，花百分之几的钱」。**MAI Cyber 2 Flash** 在 CyberGymE2E 基准上用**不到 2% 的单任务成本**追平 GPT-6 Astra，输出 token 价比上一代 MAI Cyber 1.1 Flash 低 **86%**；**MAI Image 2.7** 登顶 Artificial Analysis 图像编辑榜、以 GPT Image 2.6 Sunburst（max）**五分之一的价钱**超过它，文生图排第 4，Flash 版约 **10 美元/千张**；**MAI Realtime 1** 是微软首个实时语音到语音模型，称优于 GPT-Realtime 2.1，起步价 **每分钟音频 0.01 美元**；**Decision 1.1** 做模型路由，比 GPT-6.1 Sol 快 **50 倍**、便宜 **79 倍**，已有 4000 家客户；此外还有 MAI Transcribe 2（每月支撑 1000 万次问诊转录）、MAI Code 2 / Code 2 Flash（昨日已报道）。两个配套动作更值得记：新版 **MAI Licensed Weights** 允许企业拿前沿 MAI 模型用自己的数据微调、在自家 Azure 里跑，打的是「你的智能、你的智能体、你的权重」；自研加速器 **Maia 200** 已进入量产、跑微软最大的模型，**每瓦 token 数提升 1.7 倍**。🔗 https://microsoft.ai/news/microsoft-ignite-2026/

### 4. ⚡ Gemini 4 Neon：Carbon 的三倍速度、六成价格

11 月 18 日谷歌发布 **Gemini 4 Neon**，定位夹在旗舰 **Carbon** 与高效款 **Hydrogen**（11 月 17 日刚随 Antigravity 机器人插件亮相）之间，主打高频编程与企业工作流。官方对比是**速度为 Carbon 的 3 倍、成本仅 60%**，配 **100 万 token** 上下文与 **4 档思考深度**；Artificial Analysis 智能指数 **61 分、全球第 3**，编程智能体指数第 1、Vals Index 第 2，新浪财经引述的实测为单任务成本 **6.44 美元**、耗时约 21 分钟（较前代缩短约四成）。另有一个专门的 **Neon for Cyber** 版本面向安全团队，官方称最高思考档下对 Gray Swan 间接提示注入基准的攻击成功率为 0.0%、正常任务拒绝率降到 2% 以下。🔗 https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/

### 5. 🌍 Genie 4：可以在世界里「中途改剧本」的世界模型

同日谷歌把 **Genie 4** 推给符合条件的 Google AI Ultra 订阅者。与上一代最大的区别是**生成过程中可实时改写**：你正在世界里走，直接打一句新提示就能换天气、丢进一个角色或改变剧情走向，这是 Genie 第一次把画面与**实时原生音频**（环境声到角色对白）配对起来。Genie 3 也同步升级：单次生成从 60 秒延长到 **3 分钟**、支持多个世界串接、可用 **360 度全景图**作为新世界的种子。配套的 Project Genie agent 负责把一句自然语言变成完整世界（含配乐），并新增可探索、可 remix 的社区画廊；所有输出仍带 SynthID 水印。官方也如实列出了未解的问题：镜头延迟、复杂物理交互、实时音频精度与长时场景一致性。🔗 https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

### 6. 🔬 OpenAI 让模型改芯片：Jalapeño 省下 13% 面积，AMD GPU 提升 14%

OpenAI 11 月 18 日披露了「模型设计芯片」的完整数据。从 2025 年初的 **GPT-4o** 开始参与自研推理芯片 **Jalapeño**：向量单元标准单元面积减少约 **13%**、矩阵单元约 **10%**，其中一个乘法器重设计后面积省 **15%** 且延迟从两个时钟周期压到一个，这些改动已在流片点亮时得到硅验证。更硬的证据在第三方硬件上——与 **AMD** 合作，在「已高度优化的基线」上取得最高 **14%** 的 PPA 改进，靠的是模型重写描述电路的 SystemVerilog RTL，OpenAI 称这相当于「用不到 5 个月走完约一年的进展」，AMD 已把部分改动送进制造版本。评测侧用两颗开源 32 位 RISC-V 核（PicoRV32、Ibex）跑 **9,881 次**计分实验，**GPT-6.2 Astra 在两项任务、两颗核上均分最高**；下一步是与 **Synopsys** 合作训练 **GPT-Synopsys**，让它像资深设计师那样操作 EDA 工具。🔗 https://openai.com/index/advancing-chip-design-with-our-models/

---

## 🤖 数据源C：机器人与具身智能

### 1. 🦾 现代全资拿下波士顿动力，Atlas 第一次走出汽车业

两件事都发生在 11 月 18 日。其一是**股权收口**：现代 Glovis 的三季度监管文件显示，波士顿动力普通股相关的全部买入/卖出选择权已行使完毕，**软银剩余 9.65% 股份被买断**，现代汽车集团会长郑义宣与集团关联方合计持有 **100%**（Glovis 出资 465 亿韩元、持股升至 12.47%）。韩国 Herald 给出的路线图是：**2028 年形成年产 3 万台 Atlas 的产能**，先进佐治亚州的 HMGMA 工厂做零部件分拣搬运，验证后再上更复杂的装配；财务上波士顿动力前九个月营收 **1360 亿韩元（+29%）**，但因研发与产线投入净亏损扩大到 **6266 亿韩元**，上市时点被传在 2029–2030 年、官方未确认。其二是**场景外扩**：**GlobalFoundries 成为第一家测试 Atlas 的芯片制造商**，也是 Atlas 早期采用计划中首个汽车业之外的客户，厂内测试 **2027 年初**启动，先做用例评估与人员培训、不给机器人数量与任务清单；同时把四足机器人 Spot 的部署扩到纽约 Malta、佛蒙特 Burlington、德国德累斯顿与新加坡四地厂区——新加坡两台 Spot 自 4 月以来已行走近 **900 公里**、完成 **9 万次以上**巡检、任务成功率 **99%**。🔗 https://humanoidbeat.com/news/hyundai-full-ownership-boston-dynamics-softbank-stake-atlas.html ｜ https://humanoidbeat.com/news/globalfoundries-atlas-early-adopter-first-chipmaker-spot-fabs.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 💰 **最热** | Anthropic 定价 83 美元、9.8 亿股，基础募资约 813 亿美元（含超额配售最高约 935 亿），估值 1.5 万亿超 SpaceX 成史上最大 IPO；今日纳斯达克以 ANT 开盘，灰市指示高约 20% |
| ⚖️ **争议** | 定价前夜 CAIS 联合 Pinker、Judea Pearl、Lessig、Thomas Wolf 等发《MisAnthropic 声明》：安全品牌与实际路线不符；上市后亚马逊+谷歌仍持股近 30% |
| 🚫 **英伟达** | Kress 明确「不再向中国出货任何授权 Hopper 数据中心产品」，H200 的批准形同作废；约 60 万颗 H200 滞留香港 |
| 🪟 **微软** | Ignite 一次七款模型：Cyber 2 Flash 以不到 2% 成本追平 GPT-6 Astra、Image 2.7 登顶图像编辑榜、Realtime 1 每分钟 0.01 美元；另推 MAI Licensed Weights 与量产 Maia 200（每瓦 token +1.7x） |
| ⚡ **谷歌** | Gemini 4 Neon：Carbon 的 3 倍速度、60% 价格、AA 智能指数 61 排第三；Genie 4 支持生成中实时改世界并首次配上原生音频 |
| 🔬 **芯片设计** | OpenAI 模型让 Jalapeño 向量/矩阵单元面积各降 13%/10%，AMD 旗舰 GPU 优化最高 +14% PPA，称「5 个月走完一年」 |
| 🦾 **机器人** | 现代买断软银 9.65% 全资持有波士顿动力，目标 2028 年年产 3 万台 Atlas；GlobalFoundries 成首个测试 Atlas 的芯片厂（2027 年初） |
