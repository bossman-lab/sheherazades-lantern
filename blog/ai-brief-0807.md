---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0807.html"
title: '今日AI简报 — AMD收购Taalas、Kimi K3上架Copilot、Meta被判赔5.67亿美元'
description: 'AMD宣布收购将模型权重直接蚀刻进硅片的AI芯片初创Taalas，测试芯片Llama 3.1 8B推理达16,960 tokens/秒；Kimi K3正式上架GitHub Copilot，输入$3/百万token；OpenAI调优GPT-5.6 Sol并免费开放Luna无限文本；新墨西哥州法院判Meta赔偿5.67亿美元；Wired报道中国-free供应链机器人Ati Robotics。'
date: "2026-08-07"
tags: ["AI", "简报", "AMD", "Taalas", "Kimi K3", "Meta"]
---

# 今日AI简报 — AMD收购Taalas、Kimi K3上架Copilot、Meta被判赔5.67亿美元

**2026年8月7日**

---

## 📡 数据源A：中文频道动态

**Kimi K3 正式上架 GitHub Copilot：开源权重、按量计费** — 互联网从业者频道消息，与官方 8月6日 GitHub Changelog 相互印证：Kimi K3（开源权重）已开始逐步开放至 Copilot Pro/Pro+/Max/Business/Enterprise 计划，托管于 Fireworks AI。频道给出定价为输入 $3/百万 token、缓存输入 $0.30/百万 token、输出 $15/百万 token；Business/Enterprise 默认关闭，需管理员在策略中显式启用。

🔗 https://t.me/https1024/49996 ｜ 官方：https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot/

**Vercel AI Gateway 免费模型更换：Ling 3.0 Flash → Ling 3.0 Tiny** — Vercel AI Gateway 免费档模型已从 Ling 3.0 Flash 换成 Ling 3.0 Tiny，免费期至 8月14日 8:00，旧教程中的模型 ID 需要更新。

🔗 https://t.me/https1024/49997

**AI 出海开发者吐槽 API 成本与稳定性两难** — 频道作者分享 3 个月做 AI 出海小工具的踩坑经历：直连官方 API 跨境网络不稳、月账单近 5000 元；转用第三方中转站虽便宜但断流严重（曾挂一整天被用户投诉）；最终换用上市公司企业级通道，成本与稳定性才同时解决。反映国内 AI 出海开发者对 API 通道选择的普遍纠结。

🔗 https://t.me/aigc1024/22935

---

## 🌍 数据源B：国际AI要闻

**1. 🔥 AMD 收购 Taalas：把模型权重直接蚀刻进硅片** — AMD 8月6日宣布收购多伦多 AI 芯片初创 Taalas（金额未披露，预计 Q4 完成）。Taalas 不依赖 HBM 存储权重，而是将模型权重直接蚀刻进晶圆，构成「模型专用集成电路」（MSIC）；其首颗测试芯片 HC1（台积电 6nm）曾以 16,960 tokens/秒 运行 Llama 3.1 8B——官方称比英伟达 GPU 快 48 倍、比 Cerebras 快 8.5 倍。第二代 HC2 计划今夏推出，单芯片支持 200 亿参数，50 颗即可支撑万亿参数模型；代价是芯片出厂即「锁定」模型，升级需重制（仅更换两层金属层）。AMD 计划将其与 Instinct 加速器搭配，冲击英伟达在推理市场的主导地位。

🔗 https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344

**2. OpenAI 调优 GPT-5.6 Sol，免费用户无限使用 Luna** — OpenAI 8月6日更新 ChatGPT：Plus/Pro 用户的 GPT-5.6 Sol 回答更聚焦、事实更可靠——内部评测中金融/医疗/法律类提示的事实错误率比 GPT-5.5 Instant 低约 68%（Luna 低约 62%），并新增「思考强度」滑杆；免费用户本周起默认模型升级为 GPT-5.6 Luna，下周开放无限文本对话与 Think 按钮（更高推理）。ChatGPT 周活用户已达 10 亿。

🔗 https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/

**3. 新墨西哥州法院判 Meta 赔偿 5.67 亿美元** — 8月6日判决：Meta 因其平台损害儿童心理健康，需支付 $567m（其中 $420m 用于青少年治疗服务，其余用于预防宣传与筛查），并责令 Facebook/Instagram 增加保护功能说明界面。这是 3 月陪审团裁定 Meta 故意伤害儿童心理健康（罚款 $375m）后的第二阶段判决；Meta 表示将上诉。

🔗 https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta

**4. 研究：人类审核员漏掉 1/3 的 AI Agent 恶意命令** — 一项覆盖 4 万局游戏会话的研究显示，人类在批准 AI Agent 命令时漏掉了约 1/3 的安全威胁，暴露「人在环」审批机制在高频 Agent 操作下的失效风险，为 Agent 权限治理提供量化依据。

🔗 https://scalex.dev/blog/ai-agent-permissions-stats/

---

## 🤖 数据源C：机器人/具身智能动态

**Wired：Ati Robotics 打造「几乎零中国供应链」机器人** — 承接 7月31日 FCC 先进机器人进口禁令（重量超 4.4 磅、可移动、带环境感知与无线连接的软件控制机器人均受限），Wired 专访印度班加罗尔组装、底特律设厂的 Ati Robotics：其 10,000 磅级牵引车完全不含中国零部件，托盘搬运机中国零部件占比不到 5%，已在仓库/工厂运行数百台、服务 50+ 客户，首台人形机器人将于今年晚些时候投用。公司称禁令让「绕开中国供应链」从卖点变成竞争壁垒；Figure 与特斯拉 Optimus 同样被视为受益者。

🔗 https://www.wired.com/story/how-one-startup-built-a-mostly-china-free-robot/

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | AMD 收购 Taalas：模型蚀刻进硅片，Llama 3.1 8B 达 16,960 tok/s |
| 🧠 **模型** | OpenAI 调优 GPT-5.6 Sol，免费用户升级 Luna 无限文本 |
| 🇨🇳 **中国动态** | Kimi K3 上架 GitHub Copilot，输入 $3/百万 token |
| ⚖️ **法律** | 新墨西哥州法院判 Meta 赔 $567m（儿童心理健康） |
| 🦾 **机器人** | Ati Robotics 中国-free 供应链，受益 FCC 禁令 |
