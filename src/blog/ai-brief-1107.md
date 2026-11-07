---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1107.html"
title: "今日AI简报 — AI股大跌，Anthropic IPO 估值预期从2万亿缩到1.1万亿"
description: "中期选举后纳指单日跌超5%，Anthropic IPO 估值预期从2万亿美元降至1.1-1.3万亿；OpenAI 新融资110亿美元、估值1.25万亿；Google 发布 Gemini Omni 1.2 Flash 视频模型；OpenAI 用AI挖出948个Linux内核提权漏洞；黄仁勋被国会传唤；Agility 登陆纳斯达克。"
date: "2026-11-07"
tags: ["AI", "简报", "Anthropic", "OpenAI", "Google", "Nvidia", "机器人"]
---

# 今日AI简报 — AI股大跌，Anthropic IPO 估值预期从2万亿缩到1.1万亿

**2026年11月7日**

---

## 🌍 数据源B：国际AI要闻

### 1. 📉 AI 股遭遇中期选举后抛售，Anthropic IPO 估值预期大幅下调

美国中期选举后，AI 板块出现剧烈回调：**纳斯达克周四（11月5日）单日下跌超过 5%，为 19 个月来最大跌幅**。市场担忧民主党在华盛顿获得更大话语权、加上选民对数据中心的普遍反弹，会拖慢 AI 基建扩张——此前 10 月已是纳指自 2025 年 3 月以来表现最差的一个月，领跌的正是芯片股与新型云（neocloud）厂商。

这股寒意直接吹到了 **Anthropic 的 IPO** 上。公司此前一度瞄准 **2 万亿美元**估值，但多位利益相关方对 CNBC 表示，如今连 **1.5 万亿美元**都算「勉强（stretch）」，一名投资者认为 **1 万亿至 1.25 万亿美元**是更现实的目标。Anthropic 将以 **ANT** 为代码在纳斯达克上市，预计下周启动路演、数周内挂牌；其 5 月的私募估值还是 **9,650 亿美元**。分析师认为，承销商大概率会把发行价定在此前预期区间的低端，「市场非常需要这次 IPO 成功」。🔗 https://www.cnbc.com/2026/11/06/investors-brace-for-anthropic-valuation-1point5-trillion-a-stretch.html

### 2. 💰 OpenAI 新轮融资已募 110 亿美元，估值 1.25 万亿美元

据彭博报道，**OpenAI 在一轮尚未关闭的新融资中已募得 110 亿美元，估值 1.25 万亿美元**；该轮预计在未来数周内完成，总额可能达到约 **200 亿美元**——低于 9 月底传出的 **300 亿美元**目标。OpenAI 原称会在今年上市，随后推迟，市场普遍预期其 IPO 将落在明年。

值得注意的是，Anthropic 与 OpenAI 两家头部实验室的估值预期在同一天被下调，且都发生在 AI 交易整体走弱的背景下。🔗 https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/

### 3. 🎬 Google 发布 Gemini Omni 1.2 Flash：原生 15 秒视频，降价 30%

Google DeepMind 11 月 5 日推出 **Gemini Omni 1.2 Flash** 视频生成模型，并已在 Gemini API、Google Cloud 与 Gemini for business 全面可用（Google Vids 同步上线）。核心升级：**原生 15 秒视频**（上一代 Omni 1.1 为 10 秒），支持按 **1 秒步长**在 3–15 秒间指定时长；**多轮对话式剪辑**，改一个细节不必整段重生成；参考图/参考视频（最长 3 秒）/音频提示的**一致性明显增强**，人脸、服装、包装文字与品牌色在多机位间保持稳定。

价格**较 1.1 下调 30%，720p 视频为每秒 0.07 美元**。官方建议的工作流是：先用 360p/720p 快速出草稿、用追加编辑修细节，再把满意的版本升到 1080p 或 4K。🔗 https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/

### 4. 🛡️ OpenAI 用 AI 在 Linux 内核挖出 948 个本地提权漏洞

OpenAI 公布自主漏洞挖掘项目成果：其原型系统在 Linux 内核中标记 **2,308 个候选漏洞**、动态复现 **1,724 个**，最终确认 **948 个可用的本地提权（LPE）漏洞**——让无特权本地用户拿到 root，并已为维护者生成候选补丁。整套扫描消耗 **120 万美元 API 额度**。

一个反直觉的发现是：**GPT-5.5 Cyber 找出的新型 LPE 数量是 GPT-5.6 Sol 的 5 倍以上**，尽管两次扫描之间内核已打了三个月的加固补丁。OpenAI 研究者的判断是：未来几年内，前沿模型很可能能发现任意软件项目中的漏洞，届时「没有未知漏洞」的世界将迫使操作系统、浏览器、图像解析库、TCP/IP 栈等核心软件转向高保障开发与形式化验证。🔗 https://openai.com/index/a-thousand-fewer-paths-to-root/

### 5. 🏛️ 黄仁勋被国会传唤：就「中国间谍瞄准英伟达 CEO」作证

美国众议院中国委员会、外交事务委员会与情报委员会三位共和党主席联名致函英伟达 CEO **黄仁勋**，要求其出席 **11 月 18 日**三个委员会的联合闭门简报会。信中说：「近期报道就中华人民共和国获取美国敏感技术与信息提出了重大国家安全关切。」

此前《纽约时报》报道，美国情报官员认为黄仁勋是一场**中国间谍行动的目标**，焦点人物是新加坡云服务公司 **Megaspeed** 的高管 **Alice Huang**——该公司采购了数十亿美元的英伟达芯片。英伟达否认相关说法，并拒答黄仁勋是否会出席，仅表示「与客户会面是 CEO 工作的一部分，Jensen 每年与数千名客户高管交流」。🔗 https://arstechnica.com/tech-policy/2026/11/nvidia-ceo-jensen-huang-summoned-by-congress-over-chinese-espionag

---

## 🤖 数据源C：机器人与具身智能

### 1. 🦾 Agility Robotics 登陆纳斯达克：美国首只「纯人形机器人」股票

11 月 5 日，**Agility Robotics 完成与 Churchill Capital Corp XI 的合并，以代码 AGLT 在纳斯达克开始交易**（认股权证 AGLTW），成为**美国首家公开上市的、拥有实际商业部署的纯人形机器人公司**。合并与相关融资合计募得约 **4.65 亿美元**毛资金，其中包括富士康领投的约 **2.01 亿美元** PIPE 与交割前到账的 1 亿美元股权融资；英伟达、亚马逊、软银愿景基金二期均为其股东。

基本面数字：Digit 系列已在 GXO、舍弗勒、丰田加拿大等站点累计运行 **超过 65,000 小时**，在 GXO 佐治亚站点搬运**逾 10 万个周转箱**；9 月发布的 **Digit 5 已获得超过 3 亿美元多年期承诺订单**（以合同里程碑与规格达成为条件），另有 30 多家潜在客户在谈。Digit 5 计划 **2027 年上半年早期客户访问、2027 年底全面上市**。CEO Peggy Johnson 称，抢先上市意味着「别人会拿我们当参照，不只是看指标，也看安全」。🔗 https://www.agilityrobotics.com/content/agility-becomes-first-u-s-publicly-listed-pure-play-humanoid-robotics-company-begins-trading-today-on-nasdaq-as-aglt

### 2. 🚗 马斯克宣布停产 Cybertruck，为 Cybercab 让出产能

马斯克确认，特斯拉将在 **2027 年年中前后**在得州超级工厂**逐步停产 Cybertruck**，把产能让给 **Cybercab 无人驾驶出租车**。2026 年三季度，特斯拉含 Cybertruck 在内的「其他车型」仅交付 **8,300 辆**，而 Model 3/Y 合计交付 **47.8 万辆**——这款争议车型始终没能打开主流市场。此举是特斯拉把资源从卖车转向自动驾驶与机器人业务的最新信号。🔗 https://www.cnbc.com/2026/11/06/tesla-cybertruck-texas-musk.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 📉 **资本市场** | 中期选举后纳指单日跌超 5%，Anthropic IPO 估值预期从 2 万亿降至 1.1–1.3 万亿美元，下周启动路演 |
| 💰 **融资** | OpenAI 新轮已募 110 亿美元、估值 1.25 万亿美元，全轮或约 200 亿美元，低于 300 亿目标 |
| 🎬 **视频模型** | Gemini Omni 1.2 Flash：原生 15 秒、多轮对话剪辑、降价 30% 至每秒 0.07 美元（720p） |
| 🛡️ **AI 安全** | OpenAI 用 AI 在 Linux 内核确认 948 个本地提权漏洞，耗 120 万美元 API 额度 |
| 🏛️ **地缘政治** | 黄仁勋被要求 11 月 18 日赴国会闭门作证，涉「中国间谍瞄准英伟达 CEO」报道 |
| 🦾 **机器人** | Agility 以 AGLT 登陆纳斯达克，募资约 4.65 亿美元；Digit 5 获超 3 亿美元订单 |
