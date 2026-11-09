---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1109.html"
title: "今日AI简报 — 风控收紧：英伟达被查、高盛收回 Claude Code"
description: "英伟达董事会就黄仁勋遭外国情报行动启动独立调查；高盛把 Claude Code 收回给工程师专用；OpenAI 发布 GPT-6 Cyber 网络安全模型并评为 Critical；Anthropic 34 亿美元自建燃气发电；中国否决软银收购 ABB 机器人中国业务。"
date: "2026-11-09"
tags: ["AI", "简报", "英伟达", "OpenAI", "Anthropic", "机器人"]
---

# 今日AI简报 — 风控收紧：英伟达被查、高盛收回 Claude Code

**2026年11月9日**

---

## 📡 数据源A：中文频道动态

### Python 潮流周刊第 174 期：AI 项目密度拉满

本期项目清单几乎被 AI 工具占满：**mcode-stack**（MiniMax 团队的 AI 编码工作流与技能集）、**BMAD-METHOD**（AI 驱动的敏捷开发方法论）、**artemis**（自然语言驱动 Android 自动化）、**ego-lite**（把已登录的浏览器交给智能体）、**agent-zero**（给智能体一台 Linux 电脑）、**Hy-Memory**（智能体多场景记忆库）、**jeff**（0.8B 小模型为本地大模型做快速决策）、**KittenTTS**（CPU 上跑的开源语音合成）、**taste-skill**（让编码智能体先定美术方向）、**deepopen-3d-webs**（单图生成可漫游三维场景）。文章侧同样偏 AI：306 行 Python 写一个编码智能体、全靠 AI 做出一款 3D 游戏的完整流程、CPython 将移除实验性 JIT。🔗 https://t.me/NewlearnerChannel/16113

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 黄仁勋承认婚外情，英伟达董事会启动独立调查

11 月 8 日，英伟达官网同时刊出黄仁勋致全体员工信与董事会声明。黄仁勋在信中承认「对妻子不忠」，向家人、同事、董事会、合作伙伴与股东道歉，并表示对报道中提出的**国家安全关切**，董事会已启动独立调查、他将全面配合。董事会声明称，调查由**独立董事组成的委员会**在**外部独立律师**协助下主导，审查「近期报道称创始人兼 CEO 成为外国情报行动目标」一事；董事会表示目前**没有理由认为国家安全或英伟达机密受损**，但会检视所有可得信息，并对黄仁勋及其管理团队表达信心。此前 11 月 7 日简报已报道美国众议院三个委员会要求黄仁勋出席 11 月 18 日闭门简报、以及情报界认为其被外国情报行动瞄准。🔗 https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors

### 2. 🏢 高盛收回 Claude Code 与 GitHub：只留给工程师

据彭博报道，高盛 10 月更新的内部指引把 **Anthropic 的 Claude Code 与微软 GitHub 限制给工程师使用**（约 1.2 万人，全行约 4.7 万人），交易员与投行人员失去权限，横跨交易、量化研究与软件工程的 strats 仍可用。原因是生产力与风险复核：编码智能体以使用者同等权限读文件、写程序并直接运行，交易员搭的脚本往往绕过代码评审、测试、部署管控与投行/交易台之间的信息隔离。今年 7 月高盛 CIO Marco Argenti 还在推广非技术员工的「vibe coding」；4 月该行已禁止香港投行人员使用 Claude。耐人寻味的是，高盛与摩根士丹利正是 Anthropic 的 IPO 主承销商——后者 10 月 26 日递交 S-1，预计 11 月底前以代码 **ANT** 在纳斯达克挂牌。🔗 https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers

### 3. 🔐 OpenAI 发布 GPT-6 Cyber，网络安全能力评为 Critical

11 月 5 日，OpenAI 推出网络安全专用模型 **GPT-6 Cyber**，主打「能力强 + 守边界」：ExploitGym 得分 **48.5%**，较 GPT-5.6 Cyber 的 32.1% 提升约 51%；新基准 RemoteExploitBench 上 GPT-6 Astra **100% 拒答**，GPT-6 Cyber 完成 **95%**；Web 渗透测试漏洞召回 40.3%（Astra 32.0%）。越界测试中，不加部署提示时 **99.93%** 的测试未攻击范围外服务，加提示后达 **100%**。实绩方面，研究人员用它在一个浏览器项目中找出 **81 个此前未知的高危漏洞**（Mozilla 已发布修复），并完成 Linux 内核 **948 个提权利用**的开发——后者即 11 月 7 日简报所载 Linux 审计的同一批成果。OpenAI 已将其在 Preparedness Framework 下的网络安全评级升至 **Critical**（GPT-5.6 Cyber 为 High），首批仅通过 API 与 Codex 向审核过的 Daybreak Red 客户开放，11 月 12 日还将举办「Cyber at the Frontier」主题演讲。🔗 https://openai.com/index/introducing-gpt-6-cyber

### 4. ⚡ Anthropic 34 亿美元自建燃气发电，锁定稀缺机组

据英国《金融时报》报道，Anthropic 达成一项约 **34 亿美元**的燃气发电交易，为其数据中心供电，方式是**绕过传统电力供应商、直接锁定稀缺的发电设备**；中文科技媒体转述的规模约为 **1.7 吉瓦（GW）**。在 AI 算力需求推高电力紧张、涡轮机等设备交付排期拉长的背景下，头部实验室正从「买电」转向「自己组织发电资产」。🔗 https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0

### 5. 📜 Asahi Linux 弃 MIT 转 GPL：AI 被用来「洗代码」

让 Linux 跑上 Apple Silicon 的 Asahi Linux 宣布，**所有仓库从 MIT 改为 GPL v2 或更高版本**，此后只使用强 copyleft 许可。项目称原因是有人把开发者个人 fork 中**尚未发布的在研代码**直接拿去发布，或用 **LLM 重写以掩盖来源**，用于「取代项目并在 Apple Silicon 上激进变现」；MIT 只要求保留版权声明、不要求公开改动，没有防恶意行为的条款。Asahi 本就禁止 AI 生成代码贡献，报告还提到 Aurora Silicon 的 Borealis（其 HoneyKrisp Vulkan 驱动的分支）等 AI 辅助开发项目，并类比 WINE 在 2002 年从 MIT 转 LGPL 的往事。🔗 https://itsfoss.com/news/asahi-linux-drops-mit-for-gpl/

---

## 🤖 数据源C：人形机器人动态

### 中国否决软银收购 ABB 机器人中国业务

软银 11 月 5 日收到中国监管方通知，**禁止其收购 ABB 机器人的中国业务**。这笔交易 2025 年 10 月宣布、总额约 **54 亿美元**，软银称是其「物理 AI」战略的一环（软银同时是 OpenAI 的大额投资方）；ABB 表示中国是其**第二大市场**，在华销售超过 **90%** 来自本地制造，ABB 机器人约有 **7,000 名**员工、2024 年营收 **23 亿美元**（约占集团 7%）。交易已于今年 2 月通过经营者集中审查，卡在国家安全审查——据 FT 报道，担忧点包括在华机器人数据与资产外流、被用于在海外训练 AI 模型。彭博 11 月 7 日称双方正研究**剥离中国业务**以挽救剩余交易；同类先例是今年 4 月中国否决 Meta 收购智能体公司 Manus。🔗 https://www.freemalaysiatoday.com/category/business/2026/11/06/china-blocks-us-5-4bil-abb-robotics-purchase-by-japan-s-softbank

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 黄仁勋承认婚外情，英伟达董事会就「外国情报行动」启动独立调查 |
| 🏢 **企业落地** | 高盛把 Claude Code/GitHub 收回给 1.2 万工程师，交易员失去权限 |
| 🔐 **AI 安全** | GPT-6 Cyber 发布，攻防能力大涨、越界率仅 0.07%，评级升至 Critical |
| ⚡ **基础设施** | Anthropic 34 亿美元锁定燃气发电，绕过传统电力供应商 |
| 💻 **开源生态** | Asahi Linux 弃 MIT 转 GPL，反击用 LLM 洗掉来源的「代码洗白」 |
| 🇨🇳 **中国动态** | 中国以国家安全为由否决软银收购 ABB 机器人中国业务，双方拟剥离中国业务 |
