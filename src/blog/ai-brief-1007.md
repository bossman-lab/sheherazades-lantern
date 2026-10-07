---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1007.html"
title: "今日AI简报 — Mistral 发布万亿参数模型「Le Chonk」，OpenAI 公开数学新成果"
description: "Mistral 发布万亿参数预览模型 Le Chonk（1T 总参/49B 激活），月底开放权重；OpenAI 公开内部模型新一批数学成果与 Lean 形式化证明；Google 发布多模态嵌入模型 EmbeddingGemma 2；OpenAI 推出 Decisions API 公测；五角大楼证实已停用 Anthropic 工具。"
date: "2026-10-07"
tags: ["AI", "简报", "Mistral", "OpenAI", "Google", "Anthropic"]
---

# 今日AI简报 — Mistral 发布万亿参数模型「Le Chonk」，OpenAI 公开数学新成果

**2026年10月7日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Mistral 发布万亿参数模型「Le Chonk」：月底开放权重

法国 **Mistral AI** 于 10 月 6 日推出 **Mistral Large 4（ML4）公开预览版，代号「le Chonk」**——原生多模态模型，**1 万亿总参数、490 亿激活参数**，在 Mistral 位于欧洲的自建数据中心用 **3,800 块英伟达 Grace Blackwell GPU 从零训练**，语料覆盖 **160 多种自然语言**（含全部欧盟官方语言）。Mistral 称其在网络安全、金融、法律等企业级负载上「在所有开源模型中达到 SOTA」，视觉定位等部分领域甚至超越前沿闭源模型，**宣称是「欧美最强开源模型」**。

目前权重仍闭源，**将于本月底正式开放下载**；官方正联合网络安全机构、合作伙伴与政府监管方，在真实业务环境中对「适当放宽内容审查、强化攻防能力」的测试版做红队测试。定价为**每百万输入 token 1.36 美元、输出 4.18 美元**；Artificial Analysis 综合智能指数 **38**（同类中位数 26）、输出约 116 tok/s、上下文窗口 520K。🔗 https://www.ithome.com/1/010/108.htm

### 2. 🧮 OpenAI 公开新一批数学成果：附 Lean 形式化证明与算力账单

OpenAI 于 10 月 6 日发布《Sharing AI progress in mathematics》，**公开一批由其内部前沿模型产出的新数学结果**。此次以 **GitHub 仓库**形式发布，附论文修订与引用协议，并**公开多份证明的 Lean 形式化版本**（可被计算机逐行校验）。为提升透明度，OpenAI 还公布了 **10 份模型推理摘要、按 ChatGPT Pro 用量折算的算力估计、以及尝试题目数量的统计**——称平均每个结果约消耗相当于「3 小时 ChatGPT Pro 思考」的算力。

OpenAI 表示，此次发布参考了普林斯顿高等研究院（IAS）「数学与人工智能咨询组」的公开建议，并承诺未来改进论文的引用与数学表述，同时将资助一系列研讨会与特别项目，帮助学界理解 AI 产出的重大数学成果。🔗 https://openai.com/index/sharing-ai-progress-in-mathematics/

### 3. 🔎 Google 发布 EmbeddingGemma 2：原生多模态端侧嵌入模型

Google DeepMind 推出 **EmbeddingGemma 2**——基于 Gemma 4 架构的**开源（Apache 2.0）多模态嵌入模型，7.4 亿参数**，可将**文本、图像、音频、视频**映射到统一嵌入空间，面向端侧、隐私优先场景。模块化设计下，纯文本工作负载仅需 **2.7 亿参数**，另可选配视觉（1.7 亿）与音频（3 亿）编码器；借助 Matryoshka 表示学习，输出向量可从 768 维动态截断至 128 维，**本地向量库存储最多降 6 倍**。

上下文窗口扩展到 **8K token**（较一代大 4 倍），单次可处理约 5.5 分钟音频、29 张图像或 58 帧视频；在 MTEB 代码基准上**提升 9.92 分（68.76→78.68）**。量化后在 Google Pixel 11 Pro 上，纯文本权重仅占约 **191MB** 内存，完整多模态模型约 567MB。🔗 https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/

### 4. 🧰 OpenAI 上线 Decisions API 公测：每百万输入 token 仅 0.10 美元

OpenAI 推出 **Decisions API（公开测试）**，面向分类、路由、审核等「决策」场景：模型用 **gpt-6-luna** 返回三类答案——`predicates`（条件为真的概率）、`choice`（从选项中择一）与 `score`（按等级打分），并附 `confidence` 置信度字段，可在一个请求里并行评估多个独立问题。

定价为**每百万输入 token 0.10 美元，且只收输入费、没有输出与缓存读写费用**；支持零数据保留（ZDR）与 HIPAA 合规场景，数据可驻留美国与欧洲（EEA + 瑞士）。OpenAI 给出的示例用法包括用一条请求同时判断商品图片是否有损坏并归类。🔗 https://developers.openai.com/api/docs/guides/decisions

### 5. 🏛️ 五角大楼证实已停用 Anthropic 工具

据 BBC 报道，美国国防部一名官员称五角大楼**已「停止使用 Anthropic 产品」**。报道指出，尽管国防部长赫格塞斯今年 2 月已将 Anthropic 列为国家安全「供应链风险」并设定六个月停用期限，**直至上周 Claude 仍被用于研究、分析与情报收集**——它嵌在 Palantir 运营的军方 Maven 智能系统中，也被用于对伊朗的军事行动。

Anthropic 发言人拒绝就五角大楼的声明置评。有专家认为，正因 Claude 深度集成进 Maven，快速移除并不容易。报道同时提及，特朗普上周在白宫两度会见 Anthropic CEO 达里奥·阿莫代伊并称赞他，双方紧张关系似有缓和；五角大楼近期已先后与 Google、xAI、OpenAI 签约，OpenAI 工具在部分军事部门的采用率上升。🔗 https://www.bbc.co.uk/news/articles/c5j9x9pr0240o

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Mistral 发布万亿参数模型 Le Chonk（1T 总参/49B 激活），月底开放权重 |
| 🧮 **AI for Math** | OpenAI 公开内部模型新一批数学成果，附 Lean 形式化证明与算力账单 |
| 🔎 **端侧 AI** | Google 发布多模态嵌入模型 EmbeddingGemma 2（7.4 亿参数，Apache 2.0） |
| 🧰 **开发者** | OpenAI 上线 Decisions API 公测，每百万输入 token 仅 0.10 美元 |
| 🏛️ **政策** | 五角大楼证实已停用 Anthropic 工具（此前仍嵌入 Maven 使用至上周） |
