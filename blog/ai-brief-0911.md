---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0911.html"
title: '今日AI简报 — Anthropic披露AI滥用全景、Cognition发布SWE-2'
description: 'Anthropic发布9月威胁情报报告，披露7类AI滥用（含中国实验室蒸馏、导弹制导代码）；Cognition发布编码模型SWE-2，逼近Fable 5.1且便宜64%；OpenAI表态愿放缓前沿AI；数学家质疑OpenAI使用未发表成果。'
date: "2026-09-11"
tags: ["AI", "简报", "Anthropic", "OpenAI", "Cognition", "机器人"]
---

# 今日AI简报 — Anthropic披露AI滥用全景、Cognition发布SWE-2

**2026年9月11日**

---

## 📡 数据源A：中文频道动态

### 频道爆料：黑市流通二手模型数据集，「中转站」数据泄露引担忧

@inside1024 频道称，黑市上出现二手「Fable 数据集」与 Anthropic 报告，矛头指向把用户请求转发给境外模型的「中转站」产业，并断言这将成为重大安全事件、多部委或将整顿该行业。该说法目前属频道单方爆料（未经官方证实），但其核心——代理/中转服务截留并转卖用户与 Claude 的对话记录——恰好与 Anthropic 9月10日官方报告的「非法蒸馏」章节相互印证（详见数据源B）。🔗 https://t.me/inside1024/84797

### 开源 AI 工具三连：公众号自动化、Agent 架构图、国标公文生成

@text1024 正式开源「wewrite」公众号自动化发文 Skill（兼容 Claude Code/OpenClaw）——一句话跑通热点抓取 → 选题打分 → 框架生成 → 写作 → SEO 优化 → AI 配图 → 排版 → 推草稿箱全流程；@aigc1024 推荐专为 AI Agent 画架构图的开源 Skill「svg-diagram」（框高按字号算、连线走曲线、箭头与目标框保持固定间距）；@https1024 转发「gongwen-gbt9704-skill」，按 GB/T 9704-2012 生成规范中文公文 DOCX（A4 版心、字体字号、层级、文号署名日期、页码）并附带格式校验。🔗 https://github.com/oaker-io/wewrite · https://github.com/bybit-exchange/svg-diagram · https://github.com/mizzlelover/gongwen-gbt9704-skill

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 Anthropic 发布 9 月威胁情报报告：从「助手」到「编排者」的 AI 滥用全景

Anthropic 9月10日发布今年首份威胁情报报告，覆盖 2025年12月至2026年8月其拦截的七类滥用（网络攻击、影响行动、监控、诈骗、生物武器、常规武器、非法蒸馏），涉及 Claude Haiku/Sonnet/Opus（未波及 Fable/Mythos 级）。报告要点：

- **网络攻击**：一条与俄罗斯 Midnight Blizzard 特征一致的攻击链（GTG-20006）用 AI 自动检测恶意软件是否被查杀，并自动重写以规避检测；另有据称来自中国湖南的两名本科生用「智能体蜂群」攻击约 50 家机构，包括一个东南亚政府机构（窃取公民记录）。AI 让单个操作员可在 2-3 小时内完成攻击、并行处理数十个目标。
- **监控**：马里一名顾问据称独自用 Claude 搭建监控平台 Lakana 360，覆盖全国约 2500 万张 SIM 卡、绕过法院命令要求；伊朗攻击者用恶意 Firefox 扩展抓取身份信息。
- **常规武器**：记录 6 起案例（中国 3、俄罗斯 2、也门 1）。也门一案涉及射程 2000 公里以上的多级弹道导弹与高超音速滑翔飞行器，用 Claude Code 替代软件工程师编写制导与控制代码。
- **生物领域**：5 起案例，当事人均为在职科学家（含某军事研究所的基孔肯雅病毒功能增益研究）；Anthropic 强调判断极其微妙，未断言其有恶意。
- **非法蒸馏**：点名 7 家中国实验室。其中 Moonshot 据称把用户请求静默转发给 Claude、再把回答显示为自家 Kimi 的输出——10 天内通过 5380 个欺诈账号转发近 30 万次请求，5-7 月累计超 2300 万次交换；DeepSeek、智谱、小米、商汤、MiniMax 亦被点名。

🔗 https://www.anthropic.com/threat-intelligence-report-september-2026

### 2. 💻 Cognition 发布 SWE-2 编码模型：能力逼近 Fable 5.1、便宜 64%

Cognition 9月10日发布 SWE-2，称首次把强化学习扩展到「数万亿参数」规模，并在单次训练中同时优化所有推理强度档位（Pareto 前沿内的线性成本惩罚）。关键数据：FrontierCode 1.1 Main 得分 50.0%（Fable 5.1 为 50.9%、GPT-5.6 Sol 47.5%、GPT-6 Astra 53.3%），DeepSWE 1.1 73.0%，Terminal-Bench 2.1 92.8%，且比 Fable 5.1 便宜 64%。SWE-2 由 Kimi K3（2.8T 参数）后训练而来，官方称同分情况下比 SWE-1.7 少用 58% 轮次、平均成本低 81%，今日起上线 Devin Desktop/CLI/Web 与 Fusion。🔗 https://cognition.com/blog/swe-2

### 3. ⏸️ OpenAI 向员工表态「愿放缓前沿 AI」，政策讨论升温

彭博社 9月11日报道，OpenAI CEO Sam Altman 向员工表示，公司对放缓前沿 AI 开发持开放态度。背景是 OpenAI 首席科学家 Jakub Pachocki 9月6日发文呼吁业界在安全措施到位前实施「自愿放缓」，称「担心没人为机器智能持续快速攀升的后果作好准备」；美国参议员 Bernie Sanders 已提出禁止 AI 超智能、暂停先进 AI 开发的立法草案。🔗 https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff

### 4. 🧮 「能否信任 OpenAI 处理未发表数学」争议发酵

数学家 Andreas Thom 9月9日公开质疑 OpenAI 的透明度：在与 Kun–Thom 方法相关的「非 sofic 群」结果公布后，他曾邮件询问自己数月来在 ChatGPT 上关于扩展匹配问题的讨论是否（1）进入训练数据、（2）可被推理过程访问；得到的「没有发生」回复被指只回应了第（2）项。而在 Buckmaster–Alpöge 流体力学结果一案中，OpenAI 称「无法排除」去标识化的用户使用数据曾帮助改进其模型。该帖在 Hacker News 以 825 分登顶，折射学界对 AI 公司使用未发表成果的信任裂痕。🔗 https://mathstodon.xyz/@andreasthom/117240535270608201

### 5. 🧱 OpenAI 上线 Agents API：会话、沙箱与多智能体一体化

OpenAI 开发者文档上线 Agents API，把智能体运行所需的会话状态、托管/自托管沙箱、MCP/函数/插件工具、Web 搜索与多智能体（默认最多 4 个并发子智能体）整合进统一接口，并提供追踪与可观测性。文档注明该 API 目前仅支持美国数据驻留、不支持零数据保留（ZDR）——即便选择自托管沙箱也不例外。🔗 https://developers.openai.com/api/docs/guides/agents-api/overview

---

## 🤖 数据源C：人形机器人动态

### Reuters：中国加速人形机器人军事化，规划城市巷战编队

路透社 9月7日梳理 100 余份中国军方采购公告、学术论文、专利与公司资料后报道：中国国防体系正加速人形机器人的军事研究并为战时部署作准备——解放军报在「世界人形机器人运动会」闭幕后两日呼吁加快把实验室前沿技术转移到军事训练场、打造「战斗员」机器人；国防科大 2025年8月一篇论文设想由 6 台「战斗机器人」（人形、机器狗或无人车）分入两支突击队、配合步兵逐层逐屋清楼；兵器工业集团 Norinco 的 Fuxi 全尺寸人形机器人宣称可执行哨戒、全天候侦察与危险任务，并可搭配遥操作系统由人远程操控。路透同时指出，目前没有武装人形机器人编入解放军作战单位的证据，机器人在受控演示外仍能耗高、可靠性差；BofA 数据显示 2025 年中国厂商约占全球人形机器人出货量的 95%。🔗 https://www.reuters.com/world/china/dance-floor-war-china-readies-humanoid-robots-combat-2026-09-07/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | Anthropic 发布9月威胁情报报告，披露七类 AI 滥用全景 |
| 🛡️ **AI 安全** | 数学家质疑 OpenAI 使用未发表成果；报告点名7家中国实验室蒸馏 Claude |
| 💻 **模型动态** | Cognition 发布 SWE-2，逼近 Fable 5.1 且便宜 64% |
| ⏸️ **政策** | OpenAI 表态愿放缓前沿 AI；Sanders 提禁止超智能法案 |
| 🤖 **机器人** | Reuters：中国加速人形机器人军事化，规划城市巷战编队 |
