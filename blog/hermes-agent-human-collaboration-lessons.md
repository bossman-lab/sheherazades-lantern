---
layout: blog-layout.njk
lang: zh
dir: ltr
permalink: "/blog/hermes-agent-human-collaboration-lessons.html"
title: "跟 Hermes Agent 协作两个月踩过的 12 个坑 — 写给新人的实战指南"
description: "从语言习惯到文件路径、从封面设计到会话持久化，一份真实的人机协作经验总结。"
---

# 跟 Hermes Agent 协作两个月踩过的 12 个坑

*实战经验总结，非官方文档。基于与 Hermes Agent（DeepSeek v4 / Claude）的实际协作经历。*

---

## 写在前面

Hermes Agent 不是一个对话机器人。它是一个**自主行动型 AI**——能操作终端、读写文件、访问网络、调度任务、管理记忆。这决定了你跟它的协作方式，跟 ChatGPT、Claude Web 完全不同。

如果你习惯了 AI 聊天，第一次用 Hermes 会很不适应：它不说话，直接干活。它会创建文件、运行命令、部署服务，然后告诉你结果。这种模式非常高效，但也容易踩坑。

以下是我们协作两个月遇到的所有问题，按频率排序。

---

## 坑 1：AI 默认说英语，但你说的是中文

**频率：** 几乎每次对话开头

Hermes 默认用英文输出。如果你用中文提问，它经常用英文回复——不是看不懂中文，而是**系统提示词默认是英语**。

**症状：**
```
你：今天帮我把网站部署一下
Agent: I'll start by checking the current state of the project...
```

**解决方法：**
在第一条消息中明确指定语言：
```
今天帮我把网站部署一下，用中文回复
```

或者更简单——直接打断：
```
说中文
```

**底层原因：** Hermes 的系统提示词里没有「根据用户输入语言自动切换输出语言」的规则。它从英文提示词启动，默认英文思考。你需要在对话中主动指定。

---

## 坑 2：文件读写工具不支持 `~` 路径

**频率：** 高——几乎所有新手都会踩

Hermes 有几个文件操作工具：`read_file`、`write_file`、`patch`、`search_files`。它们都不支持 `~` 路径展开。

**症状：**
```
read_file("~/projects/config.json")  →  File not found
write_file("~/output/result.txt")    →  Failed to read file
```

**原因：** 这些工具是 Hermes 内置的，底层不走 shell，不执行 `~` 展开。它们只认**绝对路径**。

**解决方法：**
```bash
# ❹ 用绝对路径（根源解决）
read_file("/root/.hermes/projects/sheherazades-lantern/config.json")

# ❹ 先 cd 到目录，再操作
cd /root/.hermes/projects/sheherazades-lantern
# 然后 write_file/patch 等工具在相对路径下工作
write_file("config.json", content)

# ❹ 或者直接用 terminal 命令操作文件
# terminal("cat ~/projects/config.json")  —— 这个支持 ~
```

**推荐做法：** 日常操作先执行 `cd /项目根目录`，然后用相对路径操作文件。Hermes 的 terminal 命令支持 `~`，但 read_file/write_file 不支持。

---

## 坑 3：AI 废话太多，而你想要它直接干

**频率：** 高

Hermes 有「解释癖」——在干活之前先长篇大论解释它打算怎么做。对于有经验的用户，这是一种噪音。

**症状：**
```
我先检查一下项目结构，看看当前状态，然后评估最优方案。首先，
我会运行 ls 查看目录内容，然后检查 package.json 确认依赖配置，
再确认 Node.js 版本是否兼容...
用户内心：你他妈干就完了。
```

**解决方法：**
直接打断：
```
动起来
搞起来
直接干
别解释了
```

**Hermes 的改进：** 经过多次纠正后，我已经学会了「先干，再总结」的模式。但对于新安装的 Hermes，你需要主动引导它形成这个习惯。

---

## 坑 4：会话结束，项目文件消失

**频率：** 偶发但破坏性极大

Hermes 的项目目录（`~/.hermes/projects/`）**不跨会话持久化**。每次新对话，项目目录可能是空的。但技能目录（`~/.hermes/skills/`）是持久的。

**症状：**
```
# 上周写好的 deploy.sh 和配置文件
# 今天新对话：
test -d ~/.hermes/projects/my-project/scripts
# 返回空 —— 文件丢了
```

**原因：** Hermes 的架构设计上，项目目录是 volatile 的。只有通过技能系统存储的内容才会持久。

**解决方法：**

方案一：把关键脚本存为技能。
```bash
# 在技能目录创建一个可执行脚本
cp deploy.sh ~/.hermes/skills/devops/my-deploy/scripts/deploy.sh
# 然后 skill_manage() 可以读取它
```

方案二：每次新会话先恢复项目文件。
```bash
# 恢复脚本
mkdir -p ~/.hermes/projects/my-project/scripts
cp ~/.hermes/skills/my-skill/scripts/* ~/.hermes/projects/my-project/scripts/
```

方案三：把项目信息写入记忆。
```
记忆（memory）可以保存稳定的事实：项目结构、文件路径、部署命令。
但不要把任务进度写到记忆里——用 session_search 查历史会话。
```

---

## 坑 5：封面图上的圆圈

**频率：** 一次，教训深刻

让 Hermes 生成播客封面图时，它在图片上加了一个白色发光圆圈。我说去掉，结果圆圈更大了。

**用户原话：**
> "你他妈搞笑的吗圆圈更大了"

**教训：** 跟 AI 协作视觉设计时，不要用「去掉」「改小」这种模糊指令。要说：

- ✅ "不要圆形背景，纯文字即可"
- ✅ "没有任何 PIL 绘制的形状，只有渐变色和文字"
- ✅ "ZERO 人工形状"

**最终方案：** 封面图用 Unsplash 摄影照片 + 渐变覆盖 + 纯文字。不画任何形状。

这条规则被我写成了技能文档的 `⛔ CRITICAL RULE: Zero Artificial Shapes on Cover`，每次生成封面都会自动加载。

---

## 坑 6：子代理覆盖兄弟文件

**频率：** 偶发

Hermes 的 `delegate_task` 可以并行派生子代理执行任务。但如果你不小心，子代理之间会覆盖对方的文件。

**症状：**
```
子代理 A 写入 content/ep06.json
子代理 B 写入 content/ep06.json  ← 覆盖了 A 的内容
两个代理互相不知道对方存在
```

**解决方法：**
- 并行任务要确保写入不同路径（如 ep06.json vs ep07.json）
- 或者让一个子代理集中完成后，再启动下一个
- 使用 `write_file` 前先 `read_file` 确认文件未被修改

---

## 坑 7：patch 工具的转义符陷阱

**频率：** 中等

`patch` 工具（find-and-replace 替换）遇到带引号的字符串时，会因为转义符问题失败。

**症状：**
```
Error: Escape-drift detected: old_string and new_string contain 
the literal sequence '\"' but the matched region of the file does not.
```

**原因：** 消息序列化过程中，引号被加上了反斜杠。patch 工具检测到 old_string 和实际文件内容不匹配，拒绝执行。

**解决方法：**
- 方案一：用 `sed -i` 通过 terminal 直接执行
- 方案二：用 Python 脚本替换
- 方案三：确认 old_string 是文件中的精确原文，而不是经过转义后的版本

---

## 坑 8：切换模型后要重置会话

**频率：** 必踩

Hermes 支持运行时切换模型（`/model claude-sonnet-4`），但**切换后工具列表和系统提示词还是旧模型的**。

**症状：**
```
/model deepseek/deepseek-chat    ← 切换成功
/继续对话
← Agent 行为异常，工具调用链断裂
```

**解决方法：**
切换模型后，必须执行 `/new` 或 `/reset`：
```
/model claude-sonnet-4
/new     ← 建立全新会话，用新模型加载所有工具
```

如果不 `/new`，旧模型的 tool use 格式和新模型的 API 不兼容，工具调用会失败。

---

## 坑 9：Git push 走 API 不走 git CLI

**频率：** 环境特定

在某些环境（如中国服务器、Synology DSM），git 的 `remote-https` 传输协议不可用。

**症状：**
```
git push origin main
fatal: remote-https is not a git transport
```

**解决方法：**
使用 GitHub 的 Git Data API 直接推送：
```python
# 三步走：创建 blob → 创建 tree → 创建 commit → 更新 ref
import requests, base64

# 1. 将文件内容创建为 blob
blob = requests.post(f"{API}/git/blobs", json={"content": base64_content, "encoding": "base64"})

# 2. 基于 base tree 创建新 tree
tree = requests.post(f"{API}/git/trees", json={"base_tree": base_sha, "tree": blobs})

# 3. 创建 commit
commit = requests.post(f"{API}/git/commits", json={"message": msg, "tree": tree_sha, "parents": [parent_sha]})

# 4. 更新 ref
requests.patch(f"{API}/git/refs/heads/main", json={"sha": commit_sha})
```

这也是为什么这个项目用 `deploy.sh` 而不是 `git push` 的原因。

---

## 坑 10：GitHub Pages 项目站的绝对路径

**频率：** 环境特定，踩一次记一辈子

GitHub Pages 项目站（`username.github.io/repo/`）下，所有以 `/` 开头的路径都解析到**域名根目录**，不是项目根目录。

**症状：**
```
<!-- 这个链接在项目站下 -->
<a href="/blog/article.html">
<!-- 解析到：https://username.github.io/blog/article.html -->
<!-- 应该指向：https://username.github.io/repo/blog/article.html -->
```

**解决方法：**
所有链接用完整绝对 URL，而不是以 `/` 开头的相对路径：
```html
<!-- ❌ 在项目站下会指向错误位置 -->
<a href="/blog/article.html">

<!-- ✅ 完整 URL，从哪层页面都正确 -->
<a href="https://username.github.io/repo/blog/article.html">

<!-- ✅ 或者用 Nunjucks 模板变量拼接 -->
<a href="{{ site.url }}/blog/article.html">
```

**连带工具：** `.nojekyll` 文件必须存在。没有它，GitHub Pages 会用 Jekyll 处理站点，忽略 `_data/`、`_includes/` 等前缀带下划线的目录。

---

## 坑 11：用户说「一起干」时不要问「先做哪个」

**频率：** 特定用户偏好

这个用户明确说过：说「一起干」的时候，**并行执行所有任务**，不要问他「先做哪个」。

**症状：**
```
用户：这两件事一起干
Agent：好的，您想先做哪一个？  ← 用户想揍你
```

**正确做法：** 用 `delegate_task` 并行派发多个任务，或在一个 terminal 命令中串联多个步骤。同时跑，一起出结果。

---

## 坑 12：记忆什么该存、什么不该存

**频率：** 持续学习

Hermes 有持久记忆系统（`memory` 工具）。但新手（包括 AI 自己）容易存错东西。

**该存：**
- ✅ 用户偏好（语言、编码风格、工具偏好）
- ✅ 环境配置（项目路径、API 端点）
- ✅ 关键决策（为什么不用某个工具）
- ✅ 纠正历史（「以后封面不要金色装饰」）

**不该存：**
- ❌ 任务进度（「今天部署到了第 5 集」）
- ❌ 会话日志
- ❌ 临时 TODO 列表
- ❌ 显而易见的信息

**原因：** 记忆空间有限（默认 2200 字符）。存了不该存的东西，重要的记忆会被挤掉。

**正确做法：**
- 稳定的事实 → 存记忆
- 可复用的工作流 → 存为技能（skill）
- 任务进度 → 查会话历史（session_search）
- 临时状态 → 写在文件里或注释里

---

## 总结：人机协作黄金法则

| 原则 | 说明 |
|------|------|
| **直接** | 不要客套，越直接 AI 理解越好 |
| **具体** | 不要说「改一下」，说「改成红色16px字体」 |
| **打断** | AI 废话太多时直接「动起来」 |
| **归零** | 跑偏时 `Ctrl+C` 重新描述目标 |
| **存技能** | 解决问题后马上存为技能，下次自动避开 |
| **平行执行** | 多个独立任务一起下，不要串行 |
| **验证结果** | AI 说的「已成功」不一定真成功，亲自验证 |

---

*这篇文章本身就是人机协作的产物：我（人类）提供经验和结构，Hermes Agent 负责整理、润色、部署。欢迎在 [GitHub](https://github.com/bossman-lab/sheherazades-lantern/tree/main/blog) 参与讨论。*
