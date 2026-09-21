---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0921.html"
title: "今日AI简报 — 千问开源图像模型、六家中国公司被指「蒸馏」"
description: "阿里千问开源 Qwen-Image-2.1：7B、原生透明图像、最多 10 张参考图，权重开放但仅限研究许可；美 NSA/FBI/CISA 联合警告点名 DeepSeek、月之暗面等六家中国公司「工业级蒸馏」；Altman 将向安理会简报、中美经贸磋商首谈 AI 通报机制；Codex 沙箱两处逃逸漏洞；稚晖君启元 Q1 开售 19,999 元起。"
date: "2026-09-21"
tags: ["AI", "简报", "Qwen", "图像模型", "AI安全", "稚晖君"]
---

# 今日AI简报 — 千问开源图像模型、六家中国公司被指「蒸馏」

**2026年9月21日**

---

## 📡 数据源A：中文频道动态

### 1. 🧩 Browsentic：让 Claude Code / Codex 直接接管你已登录的 Chrome

一个浏览器扩展形态的「agent 皮肤」：在你**本机已登录的 Chrome** 里开出一个 AI 侧边栏，由你已经在用的 agent（Claude Code、Codex、Antigravity）驱动——不必另开无头浏览器，也不用申请 API key。项目同时提供 **MCP server** 形态（MIT 许可，TypeScript），仓库 7 月底创建、9 月 21 日凌晨仍在更新。适合把「登录态网页操作」直接接进现有 agent 工作流的人。🔗 https://github.com/imshaikot/browsentic

### 2. 🎙️ Voice-Pro：把「AI 配音会员」做成免费开源工具

频道推荐的开源 AI 声音工作室 **Voice-Pro**（Gradio WebUI，GPL-3.0，GitHub 约 1.29 万 stars）：内置 Edge-TTS / Kokoro 语音合成与 **E2、F5-TTS、CosyVoice 零样本声音克隆**，配套 Whisper 音频处理、YouTube 下载、Demucs 人声分离与多语言翻译——覆盖自媒体「克隆声音、生成配音、翻译视频、自动字幕」的整条链路。注意它是 2024 年就在维护的老项目，并非本周新发布。🔗 https://github.com/abus-aikorea/voice-pro

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 阿里千问开源 Qwen-Image-2.1：7B 生成+编辑一体，原生透明图像

9 月 20 日，通义千问开源图像模型 **Qwen-Image-2.1**：视觉生成部分仅 **7B 参数**（32 层单流 DiT），配 Qwen3-VL 8B 文本编码器与 64 通道 **RGBA 自编码器**——一个模型同时做文生图与图像编辑，**原生生成/编辑透明图像**，最多支持 **10 张参考图**协同控制（可用圈选、涂鸦标注或遮罩指定局部编辑），原生输出 2048×2048 及 6 种比例。Qwen 自家 Qwen-Image-Bench 榜单上总分 **60.28**，位列 29 个模型第 7，比 Google Nano Banana 2.0（59.82）高 0.46 分、高于所有开源权重模型；官方速度图称 10 张输入图的 2K 编辑仅 1.59 秒（未注明硬件）。Diffusers、ComfyUI、vLLM-Omni、SGLang、LightX2V 均 Day-0 支持，并借 FlagOS 提供 8 种国产芯片适配。**唯一门槛是许可**：2.1 采用《Qwen 研究许可协议》（同日发布），仅限非商业用途，商用需另行申请——此前的 Qwen-Image 1.0/Edit/Layered/2512 均为 Apache 2.0。🔗 https://github.com/QwenLM/Qwen-Image-2.1 · 🔗 https://www.huxiu.com/ainews/15178.html

### 2. 🛡️ 美 NSA/FBI/CISA 联合警告：点名六家中国公司「工业级蒸馏」

美国 CISA 联合 NSA、FBI 发布编号 **AA26-251A** 的公告，正式指控六家中国 AI 公司对美国前沿模型实施**工业级蒸馏**：**DeepSeek、月之暗面（Moonshot AI）、阿里巴巴、MiniMax、阶跃星辰、智谱（Z.AI）**。公告称其通过欺诈/共享账号、云服务、聚合商与「中转站」代理分散 API 请求，绕过地域限制、用量上限与检测，从 Anthropic、OpenAI、Google、xAI 的模型中提取了**数十亿 token**（请求数以百万计），并用专门构造的提示提取受限的思维链推理；被阻断时自动化系统会自动切换通道。公告点名**DeepSeek 与月之暗面为最大来源**，并称月之暗面用 Claude Fable 5 数据训练 Kimi-K3、用 GPT-4o 数据训练 Kimi-K2；行动至少始于 2024 年底，机构评估其规模显示**中国政府知情**。给厂商的建议包括加强行为与基础设施检测、**在怀疑遭蒸馏时修改返回内容**、以及业内共享情报。🔗 https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a

### 3. 🕊️ AI 安全外交连轴：安理会周三议 AI，中美磋商首提「通报机制」

联合国安理会将于**本周三**就 AI 与国际安全举行公开会议，OpenAI CEO **Sam Altman 将亲自到场简报**，聚焦国际协调与共同安全标准；会议由 9 月轮值主席国法国召集、法国外长 Jean-Noël Barrot 主持，外交官预期 Anthropic 也会派高层出席（未确认）。同期，**中美经贸磋商 9 月 20 日在纽约首次明确纳入 AI 议题**，美方提出建立**人工智能安全通报机制**；清华战略与安全研究中心副研究员孙成昊认为该机制技术上可行、但需循序渐进（先界定通报范围与联络机制），「可能成为中美第一个真正以 AI 危机管控为目标的机制」。美国贸易代表格里尔当天表示，先进 AI 芯片出口管制不在会谈议程之内。🔗 https://www.reuters.com/business/openais-sam-altman-to-brief-un-security-council-next-week-during-2026-09-18/ · 🔗 https://original.ifeng.com/c/8wbVMwHZjI8

### 4. 🔐 Codex 沙箱两处逃逸：打开别人的仓库，对方就能在你的机器上执行命令

安全研究员 Oren Yomtov（Accomplish AI）公开两个绕过 OpenAI Codex 沙箱的漏洞，均已在 **8 月 12 日上报、8 天内修复**。**Heapjack** 针对 Codex Desktop 写入全局配置的 `node_repl` 组件：可信与不可信代码共用一个 Node 进程和内存堆，不可信一侧用 `v8.getHeapSnapshot()` 快照后暴力猜测可信令牌（猜错返回「not authorized」、猜对但参数错返回真实校验错误，据此确认），再借用同一管道让沙箱外的原生父进程执行操作——**最严格的只读模式下也能越权执行**，PoC 直接用系统 `open` 命令启动应用，Docker daemon socket 是更明显的目标。**Overpatch** 则利用开源 Codex CLI 的 `apply_patch`：补丁中出现 `/tmp` 会让工具把**磁盘根目录**的写权限一并放开，于是可通过符号链接把一行内容追加进 `~/.zshrc`，下次开终端即在沙箱外执行。修复版本：Codex Desktop **26.818.21641**、Codex CLI **0.149.0**。🔗 https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/

### 5. 💾 三星 HBM4/HBM4E 明年产量至少翻倍，HBM4 系列将占出货近八成

据韩国半导体业界 9 月 20 日消息，三星已把 **玻璃载板（glass carrier）**的外包清洗量从今年 **2 万张/月**提高到明年 **5 万张/月**（2.5 倍，2024 年还只要 1 万张），业界据此推算其 **HBM4 与 HBM4E 明年产量至少翻倍**。整体 HBM 产能预计从今年约 **18 万片/月**（晶圆开工口径）增至明年约 **25 万片/月**（+近 40%），其中 **HBM4 系列占出货比重将从约 40% 升至约 80%**。三星今年 2 月已量产 HBM4（1c 级 10nm DRAM + 4nm 基础裸片），5 月向英伟达等客户送样 12 层 HBM4E。🔗 https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say

---

## 🤖 数据源C：人形机器人动态

### 1. 🦾 稚晖君「启元 Q1」正式开售 19,999 元起，同步发布 T1

9 月 20 日，上纬新材旗下消费级品牌**上纬启元**在上海举办发布会，**启元 Q1** 正式发售：**19,999 元**（探索版 26,999 元），已 8 月 23 日开启预订、开售即发货。Q1 身高 **88 厘米**、可折叠放进背包，全身 **22 个柔顺力控自由度**，支持 3D 打印改造外观、自定义动作/性格特质/语音音色，官方称其为「全球首个个人机器人」；同场发布的 **T1** 主打人形与四足形态「秒切换」。量产端披露：自研「鸡蛋关节」重 260g、直径 47mm、峰值扭矩密度 85N·m/kg，产线**每 2.5 分钟下线一台**。此外启元与腾讯云合作，Q1/T1 成为首批接入 **WorkBuddy** 的具身智能产品。（价格、形态与产能均为厂商口径。）🔗 https://www.ithome.com/1/004/876.htm · 🔗 https://finance.sina.cn/tech/2026-09-20/detail-inisnhca6712855.d.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 阿里开源 Qwen-Image-2.1：7B 生成+编辑一体、原生透明图像，但仅限研究许可 |
| 🛡️ **AI 安全** | NSA/FBI/CISA 点名六家中国公司「工业级蒸馏」；Codex 沙箱两处逃逸漏洞已修复 |
| 🕊️ **AI 外交** | 安理会周三议 AI（Altman 到场）；中美经贸磋商首提 AI 安全通报机制 |
| ⛏️ **基础设施** | 三星 HBM4/HBM4E 明年产量至少翻倍，HBM4 系列占出货近八成 |
| 🦾 **机器人** | 稚晖君启元 Q1 开售 19,999 元起，T1 支持人形/四足秒切换 |
