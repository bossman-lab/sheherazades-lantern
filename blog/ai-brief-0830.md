---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0830.html"
title: "今日AI简报 — 腾讯开源Hy4预览版、索尼华纳起诉Anthropic"
description: "索尼华纳起诉Anthropic音乐版权侵权（每首索赔数十万美元）；美国法院裁定五角大楼将Anthropic列为供应链风险违宪；腾讯发布并开源Hy4 preview（770B参数）；OpenAI测试Codex持久模式；Figure推出Index众包数据平台；软银拟60亿美元控股1X。"
date: "2026-08-30"
tags: ["AI", "简报", "腾讯", "Anthropic", "OpenAI", "Figure"]
---

# 今日AI简报 — 腾讯开源Hy4预览版、索尼华纳起诉Anthropic

**2026年8月30日**

---

## 📡 数据源A：中文频道动态

### 办公agent与编程agent之辩：为什么说 Manus 被技术人员低估了

@aigc1024 转载长文《办公agent与编程agent》探讨两类产品的本质区别——是否要求使用者具备开发背景：编程agent是专业开发工具（靠 git 协作、代码直接暴露给用户），而办公agent面向非开发者，无需懂代码和 git、云端优先、沙盒隔离，作者认为后者才是真正的通用 agent，Manus 是云端优先的代表。文中观点：今年国内走红的是 OpenClaw、WorkBuddy 这类单机优先产品；技术人员容易把 Manus 当作「壳」而低估它（类比 2012 年 Meta 科学家低估 Instagram）；现阶段市场采纳 agent 产品更看重知名度与焦虑情绪而非质量，但收益终将跟随产品质量——愿意选高质量 agent 工具的公司会获得更多收益，这也是创业公司的机会（如肖弘做出 Manus，模仿者却很少）。

🔗 https://www.orangeclk.com/2026/08/30/office-vs-coding-agents/ · https://t.me/aigc1024/23876

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 索尼、华纳起诉 Anthropic：指控「历史上最大最明目张胆的知识产权盗窃」

8月28日晚，索尼音乐与华纳音乐子公司向加州北区联邦法院起诉 Anthropic 及其 CEO Dario Amodei、联合创始人 Benjamin Mann，48 页诉状指控其「大规模非法 torrenting、抓取、下载版权作品」用于训练 Claude 系列模型，涉及数千首版权音乐作品，每首索赔数十万美元，称这是「历史上最大最明目张胆的持续性知识产权盗窃之一」。这是继 2025 年 9 月 Anthropic 以 15 亿美元（美国史上最大版权和解）与作者/出版商达成和解后，音乐产业对其训练数据的又一次法律围剿；Anthropic 尚未回应。

🔗 https://www.axios.com/2026/08/29/anthropic-sony-warner-music-copyright

### 2. 美国法院裁定：五角大楼将 Anthropic 列为供应链风险属违宪

联邦法官 Rita Lin 8月28日裁定五角大楼将 Anthropic 列为国家安全/供应链风险的决定违宪，59 页裁决书写道：「空洞地援引国家安全，不是惩罚和报复政府批评者的空白支票」——法官指出五角大楼在列名后仍继续与 Anthropic 合作，与「真正担心其是破坏者」的说法不符。事件起因是 Anthropic 拒绝让军用 Claude 用于大规模监控美国人和全自主武器，2 月遭五角大楼列名、3 月起诉。政府预计上诉，Anthropic 还在华盛顿特区巡回法院单独挑战另一项指定。

🔗 https://www.axios.com/2026/08/28/judge-blocks-pentagon-anthropic-blacklist

### 3. 腾讯发布并开源 Hy4 preview：770B 参数、1M 上下文

8月28日腾讯发布并开源新一代大模型 Hy4 preview：总参数 770B、激活 49B，上下文超 1M token，定位生产力场景（编程、办公、科研、游戏开发）。API 定价 $0.834/百万输入 token、$2.501/百万输出 token、缓存命中 $0.042；WorkBuddy/CodeBuddy 上线两周免费（Hy3 免费期延至 9 月 30 日）。腾讯内部盲评（163 位专家、203 项工程任务）平均 2.99/4.00，略超 GLM-5.3（2.92）与 Kimi K3（2.94）。官方称 Hy4 preview 首次参与自身开发——自动优化训练方法、数据策略与底层算子，形成早期递归自改进闭环，并自主分析推理系统瓶颈、多轮优化算子融合与通信，使端到端吞吐提升 31.8%。

🔗 https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/

### 4. WIRED 曝 OpenAI 测试 Codex「持久模式」：最长连续运行 25 小时

WIRED 8月28日通过检查 Codex CLI 开源代码发现，OpenAI 正在测试「持久模式」：启用后智能体持续自主工作，直到用户手动将其「休眠」，测试环境中最长连续运行 25 小时（现有模式任务未完成也会在数分钟至数小时后自动终止）；配套「主动性」能力让智能体在答完请求后自行规划后续子任务、跨会话推进，还可主动发消息（要求克制使用），但不扩大操作权限。OpenAI 确认处于内部测试阶段、近期无上线计划；「主动性」代码位于 Codex 共享核心而非终端专用部分，意味着该能力可能扩展至桌面应用与 ChatGPT Work。

🔗 https://baijiahao.baidu.com/s?id=1874736979775656710&wfr=spider&for=pc

---

## 🤖 数据源C：人形机器人动态

### 1. Figure 推出 Index 众包数据平台：1600 万条人类动作视频训练 Helix

Figure AI 结束 4 个月隐身运营，正式推出众包数据平台 Index：邀请全球用户用手机录制家务/工作任务视频来训练 Helix。目前已达 26.4 万下载、覆盖 108 国的 4.4 万周活创作者、1600 万条视频上传（每秒处理 30 分钟视频，相当于每天 4.9 年的人类工作量），累计向创作者支付 1500 万美元，并承诺未来 12 个月在数据与算力上投入超 10 亿美元；每 1000 小时数据含 373 种任务、1146 种物体、116 种环境。Figure 明确表示「从供应商买数据无法满足吞吐/多样性/质量，只能自建管道」。

🔗 https://www.jiemian.com/article/15010498.html

### 2. 据报软银拟以 60 亿美元估值收购人形机器人公司 1X 多数股权

据 The Information 知情人士 8月27日透露，软银正与挪威人形机器人公司 1X Technologies 洽谈收购多数股权，交易估值约 60 亿美元，谈判仍在进行、条款可能变化。1X 主打家庭场景人形机器人 NEO，曾获 OpenAI 创业基金等投资，2025 年秋以 100 亿美元估值融资受挫。若交易达成，将是软银在人形机器人领域迄今最大的一笔直接控股投资。

🔗 https://finance.eastmoney.com/a/202608273856459797.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 索尼华纳起诉 Anthropic 音乐版权；法院裁定 Anthropic 黑名单违宪 |
| ⛏️ **基础设施** | 腾讯开源 Hy4 preview（770B/49B 激活、1M 上下文） |
| 🤖 **AI Agent** | OpenAI 测试 Codex 持久模式（最长连续运行 25 小时） |
| 🇨🇳 **中国动态** | 腾讯 Hy4 preview 开源；Figure Index 众包数据平台 |
