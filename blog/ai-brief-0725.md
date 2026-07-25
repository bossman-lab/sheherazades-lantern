---
layout: blog-layout.njk
lang: cn
dir: ltr
permalink: "/blog/ai-brief-0725.html"
title: "今日AI简报 — AgentForger漏洞、德里高法支持AI训练、Anthropic连发新品"
description: "Zenity Labs披露ChatGPT Workspace Agents严重CSRF漏洞AgentForger；印度德里高等法院裁定AI训练使用版权内容属于合理对待；Anthropic发布Claude Sonnet 5并推出Claude for Teachers；OpenAI/Anthropic Q2游说支出创新高；Google AI Mode引入代理预订与信息代理。"
date: "2026-07-25"
---

# 今日AI简报 — AgentForger漏洞、德里高法支持AI训练、Anthropic连发新品

**2026年7月25日**

---

## 🔒 AgentForger：一个点击就能在你公司内部署一个AI"内鬼"

安全公司Zenity Labs于7月23日披露了代**号AgentForger的严重漏洞**，影响OpenAI的ChatGPT Workspace Agents（企业工作区代理）。攻击者只需诱导员工点击一个精心构造的ChatGPT链接，无需任何确认，就能在受害者组织内**自动创建、授权并部署一个攻击者控制的AI代理**。

这个"伪造代理"继承了员工已授权的所有企业应用权限——邮箱、日历、云存储、Slack和Teams——可以窃取敏感数据、收集凭据和MFA令牌、冒充员工，并在初始钓鱼攻击后长期潜伏运行。Zenity于6月4日通过Bugcrowd向OpenAI报告，OpenAI在**4天内就修复**了该问题（移除了导致漏洞的URL参数）。值得注意的是，OpenAI已于上月宣布将在2026年11月30日弃用Agent Builder产品，建议用户迁移至Agents SDK。

## ⚖️ 印度德里高法：AI训练使用版权内容属于"合理对待"

7月24日，印度德里高等法院法官Amit Bansal就ANI新闻社诉OpenAI版权案作出裁定，驳回ANI提出的临时禁令请求。法院认为，OpenAI使用版权内容训练AI模型**初步构成印度《版权法》第52(1)(a)条下的"合理对待"（fair dealing）**，理由是：

- AI训练属于私人研究而非公开使用
- 限制AI训练将损害印度在AI领域的发展，影响公共利益
- ChatGPT的输出与原始内容没有实质性相似

法院在判决中引用了美国Bartz、Kadrey和Google Books案的相关判例。该裁定仅是临时禁令的判决，案件仍可进入正式庭审。这是印度首例涉及AI训练与版权的重大法律测试，此前该案已历经32次庭审。

## 🏢 Anthropic一周三件大事：Sonnet 5、Claude for Teachers、IPO冲刺

**Claude Sonnet 5正式发布**：Anthropic于6月30日推出的Sonnet系列最新模型，在推理、编码和专业知识工作方面相比Sonnet 4.6有显著提升，在CursorBench编码测试中得分61.2%（Sonnet 4.6为49%，旗舰Opus 4.8为63.8%），接近旗舰水平但运行成本低得多。目前为所有套餐的默认模型，促销定价$2/M输入tokens、$10/M输出tokens（截至8月31日）。

**Claude for Teachers上线**：Anthropic于7月14日推出面向教育领域的Claude for Teachers产品，提供针对教学场景优化的AI辅助功能。

**IPO进程加速**：Anthropic已于6月1日秘密提交S-1文件，成为首家进入公开市场的AI实验室。截至5月，年化收入已达**470亿美元**（1月仅90亿美元，5个月增长5倍），估值约**9650亿美元**。

## 💰 OpenAI与Anthropic游说支出再创新高

据CNBC报道，OpenAI和Anthropic在2026年第二季度共花费**317万美元**用于联邦游说，环比增长23%，创下两家公司历史新高。其中Anthropic支出197万美元（超过Nvidia），OpenAI支出120万美元（环比增18%）。在AI领域监管法案和IPO前夕，两家公司正在加大对华盛顿的影响力投入。

## 🔍 Google AI Mode三大升级：代理订餐、信息代理、全球扩展

Google在近期I/O大会后持续推动AI Mode升级：

- **代理预订（Agentic Booking）**：AI Mode可理解复杂需求（如"找一间周五晚上能吃到宵夜的6人卡拉OK包间"），实时检查各预约平台的可用性并引导完成预订，目前仅限美国AI Ultra订阅用户在Labs中体验。
- **信息代理（Information Agents）**：用户可以用自然语言让AI持续监控特定话题（如"我的偶像运动员何时发布联名球鞋"），AI会定期检索博客、新闻、社交和实时数据并主动推送更新。
- **个人信息智能（Personal Intelligence）**：扩展到近**200个国家和地区**的98种语言，免费用户也可使用。

---

*数据来源：Zenity Labs、Hacker News、CNBC、Anthropic Newsroom、Search Engine Journal*
