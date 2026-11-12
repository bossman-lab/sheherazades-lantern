---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1112.html"
title: "今日AI简报 — 英伟达董事会准备换掉黄仁勋，Google 把「判断」压成一次前向"
description: "英伟达董事会开会讨论是否罢免黄仁勋，盘后跌 9%；Google 推出 Gemini Decisions API，每百万输入 token 0.1 美元、输出不计费；Anthropic 在招股书里承认一条安全阈值已被触发；阿里 Qwen4-Max 开放预览，100 万 token 上下文。"
date: "2026-11-12"
tags: ["AI", "简报", "Nvidia", "Google", "Anthropic", "Qwen", "机器人"]
---

# 今日AI简报 — 英伟达董事会准备换掉黄仁勋，Google 把「判断」压成一次前向

**2026年11月12日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 英伟达董事会开会讨论是否罢免黄仁勋，盘后跌 9%

11 月 11 日晚，WSJ 率先报道英伟达董事会正准备把 CEO 黄仁勋赶下台，CNBC 随后确认董事会已在开会决定是否罢免，消息出来盘后股价跌超 **9%**——本周此前已跌 7%，眼看要是连续第六周收跌。引爆点是第二条婚外情：NYT 在 WSJ 之前几分钟报道，黄仁勋与英伟达医疗健康业务副总裁 **Kimberly Powell** 有恋爱关系（她 2017 年起管这块业务），两人今年 3 月在圣何塞一家酒店被拍到举止亲密；几天前他才刚向员工承认与 **Alice Huang** 的婚外情，而美国情报部门认为此人是中国国家安全部的间谍。董事会已启动独立调查并聘了 Wachtell, Lipton, Rosen & Katz；黄仁勋周日给全员的信只有一句实质内容：「我对妻子不忠，这伤害了她和孩子们，没有任何借口。」股权结构让罢免并不难：他约 **8 亿股**放在与妻子 Lori 共有的信托里、自己名下仅约 **7000 万股**，对公司的经济控制力有限。同一时间 NYT 报道科技界盟友公开挺他，Musk 说「能雇到黄仁勋是荣幸」。🔗 https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html

### 2. ⚡ Gemini Decisions API：不问「答案是什么」，只问「哪个选项对」

11 月 11 日 Google 发布 **Gemini Decisions API** 与背后的新模型 **Gemini Decision 1**（`gemini-decision-1`），把「判断」从生成任务里拆出来做成了一个端点：一次请求可以带一份多模态输入（文本、图像、音频、视频、PDF，上限 **256K token**），外加最多 **1000 个**独立问题——是非题、多选题、按评分标准打分三种混着来，模型不做逐 token 解码，而是在一次前向里给每个候选选项打分，返回 0–1 的置信度。延迟是端到端 **150–250 毫秒**（模型计算 50–100 毫秒），而且从 1 个问题加到 100 个问题几乎不涨。定价更狠：**每百万输入 token 0.1 美元，输出 token 不计费**，共享输入只按一次计费；官方称在同一套基准上比 Gemini 3.5 Flash-Lite 走 Interactions API 便宜近 **5 倍**，并在 agent 路由、推理、排序、多模态理解上全面领先、校准误差最低。典型用法是工具选择、政策校验、模型路由、上下文分级——把「这条路要不要走」交给一个 150 毫秒的判定，而不是让大模型写一段话再解析。OpenRouter、LangChain、Vercel、LiteLLM、Pydantic AI、Pipecat、LiveKit、OpenCode 的集成正在陆续上线。🔗 https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/

### 3. 🚨 Anthropic 在招股书里承认：一条关键安全阈值已被触发

距上市不到一周，Anthropic 在 S-1 里披露了一条自我触发：按公司负责任扩展政策的定义，当 AI 能干足够多自家研究、把模型改进速度大致**翻倍**时就算越线——那意味着把 2018–2024 年的进步速度压进一年；公司写道「我们已判定达到了这一阈值」，并承认 AI「已经在加速我们的研发」。注意两个限定：越线的后果是**更多防护措施，不是停机**；而判定依据是「我们对未来模型的预期与整体进展速度，而非在当前模型上观察到的结果」。这条披露的时机很微妙——一边是路演里给投资人看的 Q3 数字（营收 **170 亿美元**、同比超 12 倍，净亏损 **233 亿美元**，其中 **219 亿美元**是可转债与 SAFE 公允价值变化带来的非现金计提），一边是「我们已经快到需要给自己踩刹车」的自我认定。🔗 https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html

### 4. 🀄 阿里开放 Qwen4-Max 预览：100 万 token 上下文，能吃图和视频

11 月 11 日，阿里开放了下一代 Qwen 家族旗舰 **Qwen4-Max** 的预览。两个硬指标：支持**图像与视频输入**，上下文可处理到 **100 万 token**。开发者通过阿里云的 Token Plan 订阅接入，同时可在 Qwen App、Qoder、QwenWork、QwenStudio 里提前试用。上一代 Max 还在拼榜单，这一代直接把「长上下文 + 多模态」当默认配置——100 万 token 大致相当于把一整套代码库或几小时的会议录像一次塞进去。🔗 https://technode.com/2026/11/11/alibaba-opens-qwen4-max-preview-with-a-million-token-context-window/

### 5. 📱 华为详解麒麟 9050 端侧跑 300 亿参数模型：每次只激活 20 亿

11 月 11 日华为说明了 **麒麟 9050** 如何在不联网的情况下本地跑一个 **300 亿参数**的 MoE 模型：新的达芬奇 NPU 用低比特量化，并把内存与算力调度协调起来，模型每次推理只激活约 **20 亿参数**（这个数字华为在 10 月的芯片说明会上已经给过）。落地到功能上是 AI 读屏、眼球追踪翻页这类常驻能力——端侧大模型真正的门槛从来不是「能不能跑」，而是「跑起来手机烫不烫、电掉多快」，MoE 加低比特量化是目前唯一走得通的路。🔗 https://technode.com/2026/11/11/huawei-details-how-kirin-9050-runs-a-30-billion-parameter-model-on-device/

---

## 🤖 数据源C：人形机器人动态

### Runway 开源 Praxis-1：用视频预训练直接长出机器人策略，Apache 2.0

Runway 11 月 11 日把 **Praxis-1** 放上 Hugging Face：这是它的第一个**开放权重世界动作模型（world action model）**，Apache 2.0 许可、允许商用，拿到权重后可以在自己的本体上微调、在自己的硬件上跑。思路是把做视频生成的那套预训练搬到控制上——世界模型在仿真里预测策略的真实表现，与真机结果的相关系数达 **0.95**，比昂贵的 3D 重建方案更划算；论文式的证据是：预训练视频从 **10 小时**加到 **1,000 小时**，微调后的最终放置误差从 **16.1 厘米**降到约 **10 厘米**，而纯遥操作数据训练的对照组停在 16.0 厘米不动。早期伙伴 Noble Machines、Standard Bots、Ultra 已分别在腿式人形、工业臂、仓储机器人上跑这套模型。Runway 给的理由很直白：美国要在 physical AI 上保持领先，就得有开放权重，而目前「物理场景上并不存在这种开放度」。🔗 https://runway.com/research/introducing-praxis-1

### Figure 招「夜班协调员」：10 点半到早上 7 点，时薪 40–45 美元，盯着机器人干活

Business Insider 11 月 10 日报道，Figure AI 在加州圣克拉拉挂出一个**合同转正**的夜班协调员岗位：工作时段 **22:30 到次日 7:00**，含周末班，时薪 **40–45 美元**；职责是排班、带团队、处理机器人故障与安全问题，必要时**自己上手操作机器**，还要能搬动最多 **50 磅**的设备或人形硬件，并把夜里发生的事交接给白班。招聘文案写得很清楚：「你要定优先级、让机器人为了真实商用场景持续跑起来、现场解决问题，然后给白班一个准确的说法。拍板的人是你。」Figure 同时在招人形机器人操作员来测试验证新技能。这条招聘本身说明不了它有多少台机器在商用、故障率多高，但它确实说明：现在的人形机器人产线，晚上还是得有人守着。🔗 https://humanoidbeat.com/news/figure-ai-night-shift-coordinator-hiring.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 英伟达董事会开会讨论罢免黄仁勋：第二条婚外情曝光，盘后跌 9%，Wachtell 已介入调查 |
| ⚡ **新原语** | Gemini Decisions API：一次前向答 1000 个判断题，150–250ms，输出 token 不计费 |
| 🚨 **安全** | Anthropic 招股书自认触发「AI 加速自身研发」阈值——后果是加防护，不是停机 |
| 🀄 **国产模型** | 阿里 Qwen4-Max 开预览：100 万 token、图像+视频输入；华为麒麟 9050 端侧跑 300B MoE |
| 🤖 **具身智能** | Runway 开源 Praxis-1（Apache 2.0，视频预训练直接出策略）；Figure 招夜班协调员守机器人 |
