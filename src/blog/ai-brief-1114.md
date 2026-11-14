---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1114.html"
title: "今日AI简报 — 英伟达的接班名单浮出，OpenAI 把机器人团队拆了"
description: "英伟达接触 Arm CEO Rene Haas，Kagan、Srouji、Waldman 同在候选名单；WSJ 披露 Kress 主张削减循环融资被黄仁勋当众斥责；OpenAI 撤掉独立机器人团队；ChatGPT Wallet 上线；华硕人形进自家主板厂；北京定 2028 年产 20 万台。"
date: "2026-11-14"
tags: ["AI", "简报", "Nvidia", "OpenAI", "Anthropic", "人形机器人", "支付"]
---

# 今日AI简报 — 英伟达的接班名单浮出，OpenAI 把机器人团队拆了

**2026年11月14日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 英伟达的接班名单浮出：Arm 老板被接触，CTO 与 Apple 硬件负责人同在列

接任黄仁勋的人选开始有名字了。**《金融时报》**11 月 13 日报道，英伟达已接触 **Arm CEO Rene Haas**——他在十几年前于英伟达工作过约七年，与黄仁勋及部分董事会成员仍保持密切关系。**Calcalist** 与 **Ynet** 给出的名单更具体：英伟达 CTO **Michael Kagan**、Apple 首席硬件官 **Johny Srouji**、以及 Mellanox 创始人兼前 CEO **Eyal Waldman**（Kagan 与 Waldman 都是 Mellanox 联合创始人，该公司 2020 年被英伟达以约 70 亿美元收购）；报道同时提到名单里还有 AMD、Apple 等公司的高管。眼下的临时 CEO 仍是 CFO **Colette Kress**，她同时保留 CFO 职位，11 月 17 日的 FY2027 Q3 财报按原计划发布。🔗 https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926 ｜名单 https://www.jpost.com/business-and-innovation/tech-and-start-ups/article-914815

### 2. 📉 WSJ：黄仁勋最后的日子，与那笔「循环融资」的账

《华尔街日报》11 月 13 日还原了黄仁勋离任前的那场会议：他把 CFO **Colette Kress** 和财务团队叫来诊断一笔越滚越大的账，**Kress 主张削减「循环融资」协议**，被他打断并当众形容为「a deer in the headlights（被车灯照住的鹿）」。争议的核心是英伟达用股权**投资 AI 初创公司、这些公司再拿钱回来买它的 GPU**——TechPowerUp 的转述指出，问题不在于这种做法本身（投资高增长公司是常规操作），而在于**没有公开数字说明有多少投资额最终以芯片采购的形式回流**：有的交易看起来是 1 美元换 1 美元营收，有的据称 1 美元能换 3 美元以上，而这些买家身上的非股权融资、债务与英伟达的兜底承诺都没有并表披露。🔗 https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus

### 3. 🤖 OpenAI 撤掉独立机器人团队：让通用模型直接开机器人

Fortune 11 月 13 日独家报道，**OpenAI 已解散独立的机器人团队**，研究人员被并入 Mark Chen 领导的**核心研究团队**，应用机器人与硬件团队则并入 Greg Brockman 领导的 **Applied** 组织；公司对外的说法是「加速而非放弃」——它想让通用模型自己去控制机器人，包括人形。证据链路上已经有点东西：在一项英伟达的研究里，由 **Astra** 驱动的智能体在**仿真操作基准**上拿到 **74.8% 成功率**，而该榜上最好的专用机器人模型是 **51.0%**。反面意见也在会上摆着——MIT 教授、Walden Robotics CEO Russ Tedrake 认为机器人公司仍有 AI 实验室没有的优势：真机已经在工厂地板上积累部署经验，而这些现场数据会让基座模型更有价值。细节上有个注脚：OpenAI 早在 CoRL 注册了展位，Fortune 到现场时 **208 号展位是空的**，几位原团队成员仍聚在那里被围观。🔗 https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/

### 4. 💳 ChatGPT Wallet 上线：代理能付钱了，但每笔都要你按一次指纹

11 月 13 日 OpenAI 发布 **ChatGPT Wallet**，与 **American Express、Mastercard、Visa** 合作，首批通过其购物代理 **dots** 面向**美国 ChatGPT Pro 订阅用户**开放。机制设计得很克制：卡只录一次，代理可以去找商品，但**每一笔都要用户核对商品、金额和卡，再用 Face ID 或指纹确认**；确认后由支付网络发放**单次交易令牌**（限定范围的卡号、安全码、有效期），商家和代理都看不到真实卡号，同时保留原卡的积分与争议处理权益。真正的阻力在商家侧——联合航空表示将禁止代理访问其订票系统，亚马逊也阻止代理在平台直接下单，理由都是自动化代理会绕过广告、会员与追加销售。🔗 https://openai.com/index/introducing-chatgpt-wallet/

### 5. 🏭 Anthropic 把 Claude 推进工厂：17 个技能 + 4 个连接器

Anthropic 发布 **Claude for Manufacturing** 插件：**17 个技能**覆盖报价、检验失败排查、故障诊断、供应商寻源、与 Autodesk Fusion 比对设计、生产报表，另配 **4 个连接器**（Autodesk Fusion、Infor、Microsoft 365、Oracle NetSuite），让 Claude 直接读写企业已有的系统。企业 GTM 负责人 Lauren Collett 的说法是，制造业的问题不是模型不够聪明，而是「人一天里有太多时间花在内部的搬运上」——在系统之间找数据、追数据、写成报告，下次再来一遍。没有连接器的系统也能用，新技能会陆续加。🔗 https://www.manufacturingdive.com/news/anthropic-launches-claude-for-manufacturing/874303/

---

## 🤖 数据源C：人形机器人动态

### 华硕推出首款人形 Gallop：第一份工作是在自家主板厂装配件

华硕 11 月 13 日发布首款人形机器人 **Gallop**，并把它直接放进集团旗下的一家 EMS 工厂学真活：给主板装配件。这个工位很硬——**15 种小零件**、很多还装在又薄又软的透明袋里，熟练工约 **20 秒**做完一块板，华硕给机器人定的目标是**同样 20 秒内做到 99.5% 成功率**，与人同标准。学习方式有三层：熟练工（经同意）头戴小相机示范真实操作，仿真再把每个样例生成大量变体，操作员用 VR 头显和手套在同样的零件与相机上遥操作带它做一遍。华硕明说不自研巨型模型——从领先的开源模型起步，靠模块化设计**等更好的模型出来就换上去**。时间表是 **2027 年客户试点、2028 年下半年上市**。🔗 https://humanoidbeat.com/news/asus-gallop-humanoid-motherboard-packing-pilots-2027.html

### 北京三年行动方案：2028 年整机产能 20 万台/年

北京市经信局 11 月 11 日印发**具身智能机器人产业三年行动方案（2026–2028）**：到 2028 年培育**至少 5 家国际领先、10 家国内领先**的人形机器人厂商，形成**年产 20 万台**整机的能力（代工与企业自产并用），京津冀合计占全国整机产能 **25%**、关键零部件本地配套率超 **60%**。为训练铺的底子是**超过 5 万 PFLOPS** 的具身智能算力集群、**100 个以上真实场景**采集的**逾 100 万小时**高质量机器人数据，外加真实任务测试场与中立的评测认证平台、公开模型排行榜。机器人本身也给了硬指标：额定负载**大于自重的 40%**、平均无故障时间**超 2000 小时**、设计寿命**超 5 年**、协同作业续航**至少 4 小时**。🔗 https://humanoidbeat.com/news/beijing-embodied-robot-plan-200000-units-a-year-2028.html

### 拓斯达推出全尺寸双足 Star：172cm、72kg，先做分拣搬运

中国工业机器人厂商**拓斯达**在 11 月 11 日东莞 TOPS DAY 2026 上发布首款全尺寸双足人形 **Star**：身高 **172cm**、体重 **72kg**，双臂各 **7 轴**、负载 **10kg**，腕部用交叉轴关节，动作更接近人手腕而不是传统工业臂。定位很务实——先做它已有客户的**物料搬运与分拣**，走「场景—机器人—数据—AI」闭环：让 Star 在真实作业中采数据反哺控制模型，而不是只靠仿真。同场还展出了子公司 Avmi 的五轴关节加工机床 S400，并宣布与凯航科技的采购协议；但量产时间、价格与首批客户都还没公布。🔗 https://humanoidbeat.com/news/topstar-star-industrial-humanoid-tops-day-2026.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 英伟达接班名单：Arm CEO Rene Haas 被接触，Kagan / Srouji / Waldman 在候选之列 |
| 📉 **治理** | WSJ 还原最后一场会议：Kress 主张削减循环融资，被黄仁勋当众斥为「被车灯照住的鹿」 |
| 🤖 **战略转向** | OpenAI 解散独立机器人团队，赌通用模型直接控制机器人（Astra 仿真基准 74.8%） |
| 💳 **支付** | ChatGPT Wallet 上线：Amex / Mastercard / Visa，单次令牌 + 每笔指纹确认 |
| 🏭 **企业** | Claude for Manufacturing：17 个技能、4 个连接器 |
| 🦾 **具身智能** | 华硕 Gallop 进自家主板厂（20 秒/99.5%）；北京定 2028 年产 20 万台；拓斯达 Star 172cm |
