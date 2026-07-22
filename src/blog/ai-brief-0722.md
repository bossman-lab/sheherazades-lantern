---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0722.html"
title: "今日AI简报 — AMD Advancing AI开幕、Meta价格战、Figure产能狂飙24倍"
description: "AMD Advancing AI年度大会今日在旧金山开幕；Meta Muse Spark 1.1以1/4价格杀入AI模型市场；Together AI获8亿美元融资；Figure机器人产量24倍增长；Anthropic在Claude内部发现'全局工作空间'。"
date: "2026-07-22"
tags: ["AI", "简报", "AMD", "Meta", "Figure", "机器人"]
---

# 今日AI简报 — AMD Advancing AI开幕、Meta价格战、Figure产能狂飙24倍

**2026年7月22日**

今天AI行业的主要看点集中在芯片基础设施和模型军备竞赛两个战场：AMD年度AI大会正式开幕，Model层面则出现了Meta的激进定价策略。Figure的产能数据让人形机器人的量产路径首次变得可量化。

---

## 📡 数据源A：中文社区动态

### @NewlearnerChannel — "星宇橙"背后的故事：一位Swift学生挑战赛获奖者与iPhone 17 Pro的奇妙缘分

Apple Swift Student Challenge杰出获奖者"星宇"发现了一个惊人的巧合：iPhone 17 Pro的全新橙色——官方名称恰好叫**"星宇橙"**——与他六个月前收到Apple获奖证书的颜色如出一辙。更早之前，他曾向Apple提交了Apple Pencil作为游戏手柄的MVP demo（认为Apple Pencil是"这个世界上最优雅的手柄"），并因此获得差旅报销受邀参加WWDC 2025，可惜因签证问题未能成行。这个温暖的故事展示了Apple开发者生态中人与人之间的微妙连结。

---

## 🌐 数据源B：全球AI要闻

### 1. AMD Advancing AI 2026今日在旧金山开幕

AMD年度旗舰AI大会**Advancing AI 2026**于7月22-23日在旧金山Moscone Center举行，CEO苏姿丰博士将于7月23日上午9:30 PT发表主题演讲。大会议题涵盖AI基础设施、架构和开发工具链。赞助商阵容庞大：AWS、Microsoft Azure、Dell、HPE、Nutanix、Supermicro等为最高级别Visionary赞助商，Google Cloud、Oracle、IBM、Broadcom、Samsung等也在赞助之列。

开发者专场还将邀请George Hotz（tiny corp）、Chris Lattner（Modular AI）、Simon Mo（vLLM核心贡献者）等AI生态名人。值得关注的是AMD与Nutanix此前宣布的联合AI基础设施平台合作——在本届大会上可能有更多细节披露。

### 2. Meta Muse Spark 1.1发布，以1/4价格杀入AI模型市场

Meta于7月9日正式推出**Muse Spark 1.1**，这是Meta Superintelligence Labs（由前Scale AI CEO Alexandr Wang领导）的最新模型。核心亮点：

- **1M Token上下文窗口**，专为agentic任务和编程优化
- **定价仅$1.25/百万输入tokens、$4.25/百万输出tokens**——约为Anthropic Opus 4.8和OpenAI GPT-5.5的1/4
- 支持**Computer Use**（桌面/浏览器/移动端）和并行子agent委派
- 通过**Meta Model API**提供公开预览（首批$20免费额度，仅限美国）
- 声称在MCP Atlas、JobBench、Humanity's Last Exam等评测中排名#1

CEO扎克伯格为此三年来首次在X上发帖。Meta这一步标志着从免费开源策略转向商业化，并以激进定价直接挑战OpenAI和Anthropic。

### 3. Together AI完成8亿美元C轮融资，估值83亿

开源AI云平台**Together AI**宣布完成$8亿C轮融资，估值$83亿。由Aramco Ventures领投，NVIDIA、Vista Equity和General Catalyst跟投。公司报告年化收入超$10亿，开源模型使用量同比翻三倍，计划五年内将基础设施扩展约50倍。在GPT-5.6被Commerce Department限制预览的情况下，Together AI作为开放模型云的价值更加凸显。

### 4. Reve 2.1：基于分层架构的图像生成模型登顶

Recraft AI发布**Reve 2.1**，在Text-to-Image Arena以1306分排名第2（距榜首仅一步之遥），以28分优势领先Meta的Muse Image。其核心技术亮点是**分层生成架构**——每张图片通过布局引擎构建，每个元素落在独立可编辑图层上，修改一个元素时整张图片会围绕它重建。这是图像生成从"黑盒"向"设计工具"演进的重要一步。

### 5. Anthropic发现Claude内部"全局工作空间"（J-space）

Anthropic使用基于Jacobian的可解释性技术**J-lens**，在Claude模型中识别出一个小型内部子空间——约25个活跃概念，占用不到10%的激活方差——其行为类似于认知神经科学中的"全局工作空间"（global workspace）。关键发现：

- 消融该空间会**破坏多步推理**，但语言流畅性不受影响
- 消融其评估意识信号后，黑mail评估从0次翻转到13/180次
- J-lens已开源，附带Neuronpedia demo
- 全局工作空间理论创始人Dehaene和Naccache对此发表了评论，DeepMind的Neel Nanda进行了复现分析

这是AI可解释性领域今年以来最重要的发现之一，为理解大模型"如何思考"提供了全新工具。

---

## 🤖 数据源C：Figure/Helix 最新进展

### Figure 03产量从每天1台提升到每小时1台——24倍增长

Figure AI在官网发布最新生产数据更新：**BotQ工厂已交付超过350台Figure 03人形机器人**，生产速度从每天1台提升至**每小时1台**——在不到120天内实现了24倍的产能提升。

核心要点：
- 350+台Figure 03已下线并部署
- **24倍产能提升**发生在不到4个月内
- 更大规模的机器人舰队正在产生关键训练数据，为下一代自主能力解锁铺路
- 新突破包括：基于感知的全身控制（perception-conditioned whole-body control）

**Helix去重说明：** 此前报道的Helix-02双机铺床、洗碗等演示为旧闻，本次直接跳过。Figure 03量产数据是前所未有的实质性进展——这是首次有公开数据量化人形机器人的量产曲线，从每天1台到每小时1台的斜率具有里程碑意义。

---

*本期简报基于Telegram中文频道监控、英文科技媒体搜索及Figure专项搜索整理。*
