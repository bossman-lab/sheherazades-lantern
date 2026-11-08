---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1108.html"
title: "今日AI简报 — 苹果在给你的家庭关系建档，Claude Code 把密码写进了仓库"
description: "每台 Mac 内置个人知识图谱：51 个数据库、181 类实体，连亲属关系都能推断；Claude Code 把密钥写进项目文件，1,122 个公开仓库中招；微软研究院 AI Frontiers 团队解散；OpenAI 发布 BioBasicsBench 湿实验室基准；智元 6 台机器人便利店值夜班；中国起草机器人终身身份证。"
date: "2026-11-08"
tags: ["AI", "简报", "Apple", "Anthropic", "OpenAI", "Nvidia", "机器人"]
---

# 今日AI简报 — 苹果在给你的家庭关系建档，Claude Code 把密码写进了仓库

**2026年11月8日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🧠 每台 Mac 都在悄悄画一张「你的人际关系图」

安全研究团队 Eighth Rank（Dario Pasquini 等）11 月 7 日发布对 Apple Intelligence「个人知识图谱」的解剖报告：**macOS 13（2022）起，每台 Mac 都自带一对守护进程**（`knowledgeconstructiond` 等），把通讯录、日历、照片人脸、信息、邮件、位置、屏幕使用时间等信号交叉比对，在本地建起一张关于「你是谁、你认识谁、他们彼此是什么关系、你何时在哪做什么」的图。

细节相当具体：数据存放在 `~/Library/IntelligencePlatform` 下的 **51 个 SQLite 数据库**（受 TCC 完全磁盘访问保护）；核心的 `graph.db` 是三元组存储，使用 **181 个实体类、278 个谓词**。系统不只记录你亲手填的，还自己推断——**包括「亲属关系（kinship）」**，并把推断值和你输入的值放在同一张表里，只用一个置信度分数区分。团队开源了本地查看工具 iKnow，还做了「武器化」推演：一旦这份图谱落到坏人手里，再配上一个被消融（abliterated）的模型，就成了隐私的单点故障。

🔗 https://8rank.ai/game/apple-intelligence-personal-knowledge-graph

### 2. 🔑 Claude Code 的「别再问了」把密码写进项目文件：1,122 个公开仓库中招

Apiiro 扫描 GitHub 发现，**1,122 个公开仓库的 `.claude/settings.local.json` / `settings.json` 里存着明文口令、API key 等凭据**——来源是用户在 Claude Code 里点「Don't ask again」批准了一条带密钥的命令。更麻烦的是传播方式：这个文件生成在项目目录内，而 Claude Code 只把它写进**全局 gitignore，不是仓库的 `.gitignore`**，于是新克隆或第二台机器会照常把它提交上去。团队追踪的 1,105 个仓库里，有 **539 个**出现过由 Claude 自己 co-author 的提交修改了这个文件。

🔗 https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again

### 3. 🏢 微软研究院 AI Frontiers 走到终点：Langford 称「只做 scaling 不算研究」

MSR 的 **AI Frontiers**（约 50 人，2023 年 ChatGPT 之后组建，产出过 AutoGen、Fara 等）今年 9 月初被并入 Microsoft AI，创始负责人 **John Langford 11 月 7 日发文宣布团队终结、自己离职**。理由很直接：MAI 由前 Inflection 团队主导，核心哲学是「aggressively scaling, not research」，与 AIF 的研究路线不兼容，而且「有充分证据表明他们并不真的需要我们」。

他也顺手反驳了「规模即一切」：字节的 Recycler 实验显示 Full Bandwidth Transformer 的变体可能等效于两倍大小的模型——在行业投入接近万亿美元的背景下，把训练与推理成本减半值多少钱，可以自己算。AIF 其他创始领导层「似乎也得出了类似结论」，明年的实习生计划已取消。

🔗 https://hunch.net/?p=13764006

### 4. 🧪 OpenAI 发布 BioBasicsBench：让智能体读凝胶图、看细胞照片

OpenAI 与酶设计公司 Ligo 合作推出 **BioBasicsBench**，用 **100 项常规湿实验室任务**测智能体能否读懂原始实验数据：凝胶与印迹图 31 项、实验记录与手写笔记 27 项、仪器导出表 20 项、台面与试剂照片 18 项、显微图像 14 项、仪器屏幕与曲线 13 项、测序文件 12 项、操作视频 7 项。任务不只要求给结论，还要求发现错误、判断「这批证据根本支撑不了结论」。

评测覆盖 7 个模型、37 种推理强度设置，每题 5 次共 **18,500 次结果**。xhigh 档平均得分：**GPT-6 Astra 66.7%**（95% 置信区间 60.3–73.1），GPT-6.1 Sol 62.0%，GPT-5.6 Sol 43.8%，GPT-6 Luna 38.3%，GPT-5.5 35.4%。OpenAI 的判断是：**原生多模态能力可能是读懂日常实验的关键**，而图像判读、对照检查与实验上下文仍是短板。

🔗 https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

### 5. 🚢 获准买英伟达 H200 的中国公司，办公室是空的

《纽约时报》调查、The Verge 转述：特朗普政府放松对华芯片限制（英伟达上缴 15% 销售额）后，商务部批准了一批中国公司采购 **H200**。其中 **New Matrix** 注册 17 个月，办公楼名录里查不到这家公司，物业也没有任何记录——办公室「只剩灰色的空壳和从天花板垂下的电线」。其股东与一家 2024 年起被美国列入黑名单的中国私募股权基金有关联。报道称这不是孤例，而是一种模式：与受出口管制实体有关联的公司被批准购买英伟达芯片，商务部与英伟达的尽职调查都受到质疑。

🔗 https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government

---

## 🤖 数据源C：机器人与具身智能

### 1. 🏪 智元 6 台机器人便利店值 24 小时班：1,730 项任务，两台没通过考核

11 月 2–3 日，智元（AgiBot）把 **6 台 G2 人形机器人**送进上海徐汇一家真实营业的便利店，做了一场名为「Robots Never Clock Out」的 24 小时直播挑战，覆盖午高峰、晚高峰、夜班与早餐四个班次。任务包括上架补货、做咖啡和热食、迎宾、清理垃圾；还加了刻意刁难：分辨含糖与无糖可乐、在通道上放障碍物、在机器人取餐时晃动容器。

最终完成 **1,730 项任务**，其中迎宾 683 次、取送商品 369 次、咖啡 147 杯；**6 台中 4 台通过考核**。巡架补货那台因「主动性不足、跟不上门店周转」未通过；清洁机器人则在夜班遇到满溢的垃圾桶后偏离路线、跑出店外。TechSpot 也提醒关键数字缺失：是否中途充电、维护、人工协助，以及速度与成本是否比得上人类店员，报告都没有说明。

🔗 https://www.techspot.com/news/114445-six-humanoid-robots-worked-24-hour-shift-convenience.html

### 2. 🪪 中国起草「一机一码」：每台机器人都要有终身身份证

工信部 11 月 6 日就机器人身份编码规则公开征求意见（截止 12 月 5 日）：**在中国制造的每一台整机机器人**（工业、服务、特种）出厂前，必须由厂商写入不可篡改的终身识别码，实行「一机一码」，数字存储并同时以人眼可读与机器可读的形式标注；厂商须在统一平台登记产品及其关键零部件、软件，并在 20 个工作日内备案所用编码。草案只覆盖中国制造的机器人，未提进口、收费或罚则，生效日期仍写作「202X」。

底数不小：2026 年 1–9 月，规模以上工业企业生产工业机器人 **794,781 台，同比 +29.1%**。人形机器人已有类似的 29 位编码标准，截至 5 月平台已编码超过 **28,000 台**。欧盟《机械法规》2027 年 1 月 14 日起要求标注型号、制造年份与批次/序列号——中国的做法是把「身份证」前置到出厂环节。

🔗 https://asia-tech-news.ghost.io/china-drafts-lifetime-id-codes-for-every-robot-it-makes-not-just-humanoids/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🧠 **端侧隐私** | 每台 Mac 自 macOS 13 起建个人知识图谱：51 个数据库、181 类实体、278 个谓词，连亲属关系都推断 |
| 🔑 **AI 安全** | Claude Code 把批准过的命令连同密钥写进项目文件，1,122 个公开仓库泄露凭据，539 个仓库由 Claude 自己提交 |
| 🏢 **研究机构** | 微软 AI Frontiers 解散，Langford 直指 MAI「只做 scaling」，创始领导层集体离开 |
| 🧪 **模型评测** | BioBasicsBench 100 项湿实验室任务：GPT-6 Astra 66.7%，GPT-5.6 Sol 43.8%，图像与对照仍是短板 |
| 🚢 **出口管制** | NYT：获准买 H200 的 New Matrix 办公室是空壳，股东关联黑名单私募 |
| 🏪 **机器人落地** | 智元 6 台 G2 在上海便利店值 24 小时班，完成 1,730 项任务，4 台通过考核 |
| 🪪 **机器人监管** | 工信部起草「一机一码」终身身份证，覆盖全部整机；前 9 月工业机器人产量 79.5 万台、+29.1% |
