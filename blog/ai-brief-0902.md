---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0902.html"
title: '今日AI简报 — Anthropic发布Fable 5.1、OpenAI首曝「临界级」网络安全模型'
description: 'Anthropic发布Claude Fable 5.1与Mythos 5.1：典型负载降价约25%、agentic场景最高省45%，企业级EFS实现等效零留存；OpenAI披露Astra成为首个达到「临界」网络安全阈值模型（ExploitBench满分、测试中发现两个0day）；Anthropic与英伟达支持的Lambda签350亿美元云协议；国家AI基金14亿元入股可灵；YC新秀Nori推1288美元家用双臂机器人。'
date: "2026-09-02"
tags: ["AI", "简报", "Anthropic", "OpenAI", "机器人", "可灵"]
---

# 今日AI简报 — Anthropic发布Fable 5.1、OpenAI首曝「临界级」网络安全模型

**2026年9月2日**

---

## 📡 数据源A：中文频道动态

### Grok Bot 社区目录：awesome-grokbot

@https1024 消息：新项目把分散的 4 个 Grok Bot 社区目录合并去重，用脚本逐一检查每个链接是否存活，并为每条记录补充中文摘要与来源归属，生成一份可搜索的中英双语目录——目前收录 361 条可用的 x.ai/bot 分享，全部经过状态检查（GitHub 仓库 9月1日创建，已获 121★）。

🔗 https://github.com/kydlikebtc/awesome-grokbot · https://t.me/https1024/50970

### no_human：本地开源的「AI 编码工厂」

@https1024 消息：开源项目 no_human 把工单直接变成经过评审的 Pull Request——流程包含先出计划、对抗式评审、防篡改测试与「复现门禁」，全程留在开发者自己的机器上运行，代码不外传（231★，8月创建）。

🔗 https://github.com/no-human-ai/no_human · https://t.me/https1024/50969

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Anthropic 发布 Claude Fable 5.1 与 Mythos 5.1

当地时间 9月1日，Anthropic 发布 Claude Fable 5.1 与 Claude Mythos 5.1——两者是同一模型、不同安全护栏：Fable 5.1 全面可用；Mythos 5.1 仅通过可信访问计划提供，护栏专为网络安全与生命科学研究设计。定价方面，按 token 计费场景典型负载比 Fable 5 便宜约 25%（主要来自缓存读取降价），高度 agentic 工作流最高可省约 45%。数据留存上推出「企业前沿护栏」（EFS）：客户数据存放在完全由客户控制的基础设施（而非 Anthropic），等效零留存，今秋起分阶段对企业开放。安全护栏误报减少 60%（网络安全场景）；Fable 5.1 可发现软件漏洞但不能据以开发漏洞利用代码；生物方向的进阶能力访问计划与美国政府合作开发。基准对比：Terminal-Bench 4.0 得分 55.8%（Mythos 5.1 为 60.9%，高于 GPT-5.6 Sol 的 37.3%）、OSWorld 2.0 77.9%（partial）、CursorBench 3.2.0 73.4%、Humanity's Last Exam 60.9%（无工具）。投资公司 Millennium 称 Fable 5.1 找出了其内部系统一个多名工程师数年未解的罕见崩溃根因。

🔗 https://www.anthropic.com/claude-fable-and-mythos-5-1

### 2. OpenAI：Astra 成首个达到「临界」网络安全阈值的模型

OpenAI 9月1日发布「Path to Astra」评估更新：按 Preparedness Framework，Astra 已满足 **Critical（临界）网络安全能力**阈值——即配备合适工具与权限时，可在无人逐步引导的情况下跨多个受良好防护的系统发现未知漏洞并开发利用，是该公司首个获此定级的模型。证据：公开 ExploitBench 取得满分 100%；在自建内部基准（20 个 2026 年 6-8 月披露的高危 V8 漏洞）上，任意代码执行率远高于 GPT-5.6 Sol 且输出 token 少得多，测试中甚至自主发现并利用了两个 0day（正在向维护方披露）；还在加固的浏览器与操作系统上完成沙箱逃逸与本地提权链。为此 OpenAI 将 Astra 部分开发与发布推迟数周以加固防护，8月28日已重启先前暂停的大型强化学习训练。Astra 即将开放，但最先进的网络安全能力将先仅限测试者（Daybreak Blue 随后扩展防御用途）。

🔗 https://openai.com/index/path-to-astra/

### 3. Anthropic 与英伟达支持的 Lambda 签署 350 亿美元云协议

据彭博（8月31日），Anthropic 与英伟达支持的云服务商 Lambda 签署价值 350 亿美元的云计算协议：数据中心由比特币矿企兼开发商 Hut 8 在得克萨斯州努埃塞斯县建设，英伟达持有该数据中心租约（数周前英伟达刚与 Hut 8 达成算力容量协议），Lambda 将部署英伟达芯片为 Anthropic 提供云服务。

🔗 https://www.bloomberg.com/news/articles/2026-08-31/anthropic-seals-35-billion-cloud-deal-with-nvidia-backed-lambda（转引：财联社/观点）

### 4. 🇨🇳 国家人工智能基金 14 亿元战略入股可灵

快手 8月31日晚公告：旗下 AI 视频生成大模型主体「北京可灵」引入国家人工智能产业投资基金 14 亿元现金战略入股（对应扩大后注册资本约 1.14% 股权），境外投资主体正大机器人同步注资约 1929 万美元（约合人民币 1.31 亿元）。消息带动快手 9月1日港股盘中涨超 5%。

🔗 https://finance.sina.com.cn/jjxw/2026-09-01/doc-iniqhmwh1558591.shtml · https://finance.eastmoney.com/a/202609013861292031.html

### 5. ChatGPT/Codex 桌面应用捆绑一整套 LibreOffice

开发者 Simon Willison 发现，OpenAI ChatGPT 桌面应用（原 Codex 应用）的 `codex-primary-runtime` 运行时体积达 1.7GB——内含完整 Python、Node.js、git、Poppler 以及 LibreOffice headless 办公套件，`plugins/documents` 目录下的 skills 负责教 Codex 如何找到并使用这些二进制。该发现在 HN 获 400+ 分。

🔗 https://simonwillison.net/2026/Sep/1/codex-libreoffice/

---

## 🤖 数据源C：人形机器人动态

### YC S26 新秀 Nori Robotics 发布 1288 美元双臂机器人 NORI L2

Launch HN（YC S26 批次）：Nori Robotics 发布 NORI L2——100cm 与 130cm（Grande）两个尺寸的轮式双臂机器人，配备双 Z 轴升降（650/950mm），可自主完成扫地、装洗碗机、煮咖啡等家务，多台可协作。卖点包括「技能市场」：某地训练出的技能（如开啤酒）可一键同步给全球其他 Nori；支持远程遥操作；美国旧金山制造，预售价 $1,288，今夏起发货。

🔗 https://www.norirobotics.com/ · https://news.ycombinator.com/item?id=49525153（Launch HN，179 分）

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Anthropic 发布 Fable 5.1/Mythos 5.1，成本最高降 45% |
| ⛏️ **基础设施** | Anthropic × Lambda 350 亿美元云协议，英伟达持租约 |
| 🛡️ **安全** | OpenAI 认定 Astra 达「临界」网络能力，ExploitBench 满分 |
| 🇨🇳 **中国动态** | 国家AI基金 14 亿元入股可灵，快手涨超 5% |
| 🤖 **机器人** | Nori L2 家用双臂机器人 $1,288（YC S26） |
| ⚙️ **AI Agent** | Codex 桌面应用捆绑 LibreOffice 运行时 |
