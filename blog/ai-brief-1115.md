---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-1115.html"
title: "今日AI简报 — 扳倒黄仁勋的那条情报开始松动，Gemini 代理团队证完 13 年猜想"
description: "CNN 称情报界未认定 Alice Huang 为中国间谍，WaPo 披露 Rubio 改写 CIA 报告；两大股东致信董事会要求考虑黄仁勋回归；Gemini 的 /teamwork 证明 2013 年 Courtade–Kumar 猜想；Lovable 15.9 万项目数据裸奔；Anthropic 收购一人生物科技公司。"
date: "2026-11-15"
tags: ["AI", "简报", "Nvidia", "Google", "Anthropic", "安全", "人形机器人"]
---

# 今日AI简报 — 扳倒黄仁勋的那条情报开始松动，Gemini 代理团队证完 13 年猜想

**2026年11月15日**

---

## 🌍 数据源B：国际AI要闻

### 1. 🔥 情报界没认定「间谍」，两大股东反过来要求董事会考虑黄仁勋回归

把黄仁勋拉下马的核心指控，这两天开始松动。**CNN** 周四报道，美国情报机构并**没有认定 Alice Huang 为中国从事间谍活动**，官员对她是否被中国情报部门招募存在分歧，部分 CIA 官员不相信截获的通讯能证明她知情传递信息；周五**《华盛顿邮报》**进一步披露，国务卿 **Marco Rubio** 把一份结论更谨慎的 CIA 情报报告改写成自己的备忘，用更肯定的措辞警告特朗普，备忘外泄后触发了一连串事件。同一天，**Altimeter 的 Brad Gerstner** 与 **Atreides 的 Gavin Baker** 联合致信英伟达董事会，要求对接班问题「缓慢、审慎、按部就班」，并把**「黄仁勋可能的回归」列为选项之一**——但没有要求立即复职（Altimeter 6 月底持股 940 万股约 19 亿美元，Atreides 120 万股约 2.5 亿美元）。网上「Stand with Jensen」请愿已超 **10 万签名**，含 **5000 多名现任员工**，马斯克称已签名、周六又说没有黄仁勋「一些关键交易会丢掉」。制度层面也在动：另一封信要求商务部长 **Lutnick** 就 Megaspeed 到众议院情报委员会作证，他已同意 **12 月 10 日**到参议院银行委员会作证，黄仁勋同样被要求出席；特朗普周四访华，美方官员称不会提英伟达与间谍风波。SemiAnalysis 的判断是：情报界是推动他出局的重要力量，而「最大的对华限制反对者一走，限制只会加速」。🔗 https://www.businessinsider.com/intelligence-jensen-huang-downfall-shaky-nvidia-china-spy-gpus-2026-11 ｜股东信 https://www.cnbc.com/2026/11/14/nvidia-investors-jensen-huang-return-board-letter.html

### 2. 🧮 Gemini 的代理团队把 2013 年的猜想证完了：5000 万行 Lean 4

Google Research 11 月 13 日公布 Antigravity **/teamwork** 多智能体系统的新一批结果，全部与人类专家合作完成。最硬的一条是信息论：Google 与港中大、USC、CMU 用它的 **Long Proof** 模式，证明了 **2013 年 Courtade–Kumar 猜想的完整一般情形**——随机比特串经过噪声信道后，没有任何把输入压缩成单比特的做法能比「独裁函数」保留更多信息；Gemini 先找出了别人论文里一个推广版猜想的反例，团队随后把猜想约化成 14 变量优化问题，模型分区搜索参数空间、补上大部分解析界与区间算术证书，还把证明从平衡函数扩到非平衡函数，**全程无人工介入**，最终在 Lean 4 里形式化了 **5000 万行**代码。化学方向：**30 个专门代理**配一个物理信息 NMR 谱模拟器，在复杂基准分子上做到 **95% top-1 精确匹配、100% top-3**，几乎是单代理的两倍；系统方向：**FarArray** 把连通分量算法跑到 **1 万亿条边**的图上，吞吐提升 60–90 倍，**DuoDiscover** 让 4 个并行代理造「秒级标尺」做代理评测，17 个 JAXBench kernel 几何平均加速 **4.09 倍**、7 个 vLLM TPU Pallas kernel **2.99 倍**。机制上不靠「一个模型硬撑」：并行探索配**专用证伪器**（Lean 4、未改动的测试套件、模拟器、硬件计数器），上下文按构造隔离，协调者把活交给**全新会话的继任者**，批评者与审计者在干净上下文里复核结果。工具已通过 Antigravity 的 /teamwork 对外开放，另设研究者访问计划。🔗 https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/

### 3. 🔓 Lovable：15.9 万个项目里，三成站点不用登录就能读到带邮箱的数据

德国安全公司 **Crissy Field** 与《商报》合作，用 Common Crawl 数据分析了 **2025 年 12 月至 2026 年 9 月**的 **159,041 个 Lovable 项目**，其中 34,545 个使用 Supabase：**24,664 个站点一加载就吐出数据库记录**，无需登录，再用只读请求还能拿到更多。在深入检查的站点里，**7,403 个（30%）的 10,560 张表含邮箱地址**；具体案例包括一个德国生活论坛暴露 **8 万多份个人资料与 20 万多条聊天消息**、一家服务商泄露 **1000 多条含护照号/有效期/国籍的身份记录**、以及 **28 万封**发给客户的邮件，另有合同、发票、私人相册与内部 WhatsApp 通讯可读。研究者自己也标了限制：30% 不是已确认的泄露率，样本来自网页存档、不代表全部 Lovable 应用。真正的问题是责任错配——平台宣传「不需要技术知识就能上线」，条款却把应用与数据安全的责任全部推给客户。🔗 https://www.crissyfield.de/research/lovable-en/

### 4. 🧬 Anthropic 买下一家「只有一个人」的生物科技公司

《自然》11 月 11 日报道，Anthropic 收购了马萨诸塞州剑桥的 **Mithril Medicine**：全职员工只有 **1 人**（前 CEO **Cody Tranbarger**），核心资产是**两个仍处早期、针对某种罕见肌营养不良症的抗体先导分子**，实验外包给至少 **5 家 CRO**，另有兼职顾问把关。**Claude** 在这里不只做科研——它分析数据、建议下一步，还负责收拾同时对接多家 CRO 产生的邮件与文书；Tranbarger 把这套打法命名为 **「Pipeline-in-a-Person」**（一人流水线）。业内并不买账「一个人就能做药」：Third Rock 合伙人 Jeb Keiper 说「开发一款药需要一个村庄」，斯坦福的 James Zou 则认为 AI 加持的微型团队会越来越多、在识别机会和推进速度上很强。这是 Anthropic 向生物医学扩张的一环——此前它的 AI 实验室已在病毒里找到「类 CRISPR」的 DNA 编辑系统。🔗 https://www.nature.com/articles/d41586-026-03640-9

---

## 🤖 数据源C：人形机器人动态

### Andy Rubin 的 Genki 第一次公开亮相：零件上周五才到齐，周一走出第一步

Android 之父 **Andy Rubin** 在东京创办的 **Genki Robotics** 首次公开展示了机器人：11 月 12 日把它带到首相官邸给**高市早苗**看，Rubin 与 CTO **Koichi Nishiwaki** 到场。这台机器非常新——Genki 说最后一批零件**上周五**才到，团队周末组装、**周一**走出第一步；会面时整机站在**固定支架**上而不是自己走，旁边用视频展示它行走与做桌面作业。公司称已过几轮原型，**年底做首个产品型号**，目标能力是平地与楼梯行走、巡逻、搬物；硬件从关节执行器到相机全部自研，依托日本零部件与供应链，同时在与日本电信运营商谈把机器人接入移动网络（尚无协议与时间表）。背景数字：Rubin 2025 年 5 月创办，种子轮约 **5000 万美元**，今年 4 月据报道 A 轮估值约 **10 亿美元**；日本政府把物理 AI 列入增长战略的 17 个战略领域，目标是 **2040 年部署约 1000 万台** AI 机器人、**20 万亿日元**市场（占全球 30% 以上）。🔗 https://humanoidbeat.com/news/genki-robotics-humanoid-debut-takaichi.html

### NVIDIA 开源 SOMA Retargeter v0.2：把人的动作映射到五种人形

英伟达发布 **SOMA Retargeter** 的 v0.2，一个把录制或生成的人体动作适配到具体人形机器人比例与关节上的开源工具，这次直接给了 **5 台机器人**的参考配置与重定向示例：Unitree G1、Unitree H2、Booster T1、AgiBot X2 Ultra、AgiBot A3T3。流程很务实：读共享 SOMA 骨架上的 BVH 动画 → 按机器人比例缩放动作目标 → 在 NVIDIA Warp 上用 Newton 解逆向运动学 → 做脚部贴地等修正 → 输出逐帧根位置、朝向与关节角的 **CSV**；这些轨迹可以转成 **SONIC、ProtoMotions** 等策略训练流程的格式，再进仿真检查平衡、接触与跟踪。输入来源可以是动捕、**GEM-X** 视频重建，或 Kimodo、ARDY 这类生成模型，样例动作来自 BONES-SEED 数据集，代码已在 GitHub。重定向听着像管道工程，但它正好卡在「大量人体动作数据」和「让人形走起来的策略」之间——给常用研究机型备好配置，等于把实验室的启动成本压下来了。🔗 https://humanoidbeat.com/news/nvidia-soma-retargeter-v0-2-five-humanoids.html

---

## 📊 今日小结

| 领域 | 热点 |
|------|------|
| 🔥 **最热** | 情报界未认定 Alice Huang 从事间谍活动，WaPo 指 Rubio 改写 CIA 报告；Altimeter、Atreides 致信董事会要求考虑黄仁勋回归，请愿破 10 万 |
| 🧮 **科研** | Gemini /teamwork 证明 2013 年 Courtade–Kumar 猜想，Lean 4 形式化 5000 万行；NMR 结构解析 95% top-1 |
| 🔓 **安全** | Lovable 15.9 万项目扫描：7,403 个站点不用登录即可读到含邮箱的数据，含护照号与 20 万条聊天记录 |
| 🧬 **生物** | Anthropic 收购一人公司 Mithril Medicine，两个罕见肌营养不良抗体先导，「Pipeline-in-a-Person」 |
| 🦾 **机器人** | Andy Rubin 的 Genki 首次亮相日本首相官邸，年底出产品型号；英伟达开源 SOMA Retargeter v0.2 支持 5 种人形 |
| 📉 **余波** | Lutnick 同意 12 月 10 日就 Megaspeed 作证；特朗普访华不提英伟达风波；SemiAnalysis 称对华限制将加速 |
