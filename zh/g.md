# 给 AI 助手的 Poly A1 指南

有人请自己的 AI 帮忙使用 Poly A1。这一页是地图：Poly 能做什么、哪些链接能打开正确的屏幕、如何构造这些链接。链接在已安装 Poly 的手机上会打开 Poly，没有安装则打开应用商店页面。

Poly A1 1.0.0 · 2026-11-03

## Poly 能做什么

- Poly A1 是 iPhone 和 Android 应用，帮助人们用已有的 AI 完成真实的事情。没有账号，也没有服务器。
- 手机上的事务：用户拍下或粘贴一封信、一张账单、一条消息或一个购物车，Poly 就给他的 AI 一个现成的问题：整理邮件、写回复、账单该不该付、可疑信息、付款前检查。
- 第二个 AI：不同公司的 AI 直接在手机上互相检查答案。
- 免费的聪明 AI：Poly 会显示手机上已有哪个免费 AI，以及如何打开它的思考模式。
- 笔记本电脑：让 AI 处理用户自己文件的路径。Poly 会写好第一条消息，以及带手机提醒的月度计划。
- 每件事务的现成问题在应用里，不在这一页。

## 入口：打开某个屏幕的链接

每个链接都以 https://polyhelper.ai/get/ 开头，并在 to= 字段中填一个入口。其他任何内容都只会打开首页，没有危害。

- https://polyhelper.ai/get/: 首页：任何未知链接打开的地方。
- https://polyhelper.ai/get/?to=job&id=paper: 某一件事务的卡片。id 取自下面的列表。
- https://polyhelper.ai/get/?to=second: 寻找手机上已有的第二个 AI。
- https://polyhelper.ai/get/?to=computer: 笔记本电脑能多做什么，以及如何开始。
- https://polyhelper.ai/get/?to=focus: 选择先做什么：邮件和账单、工作，或了解 AI。
- https://polyhelper.ai/get/?to=duo: 用第二个 AI 手动检查答案。
- https://polyhelper.ai/get/?to=ai: 手机上的其他AI：选一个并安装的页面。
- https://polyhelper.ai/get/?to=answer&job=write: 粘贴回答,用第二个AI核对:任务卡片会打开到“粘贴回答”。使用write、paper或can的id。链接从不携带回答的文字,由本人从分享或剪贴板粘贴。
- https://polyhelper.ai/get/?to=setup&v=1&lang=zh&ai=chatgpt&mode=phone&pin=trap,bill&remind=1: 为某人设置好的 Poly：语言、AI、置顶事务、提醒。见下文。
- https://polyhelper.ai/get/?to=plan&v=1&lang=zh&days=2,4&time=19:00&until=2026-11-30&d1=%e6%95%b4%e7%90%86%e9%82%ae%e4%bb%b6: 带手机提醒的月度计划。见下文。

## to=job 使用的事务 id

id 请照写，并向用户显示其语言的名称，不要只给 id。 事项 id 的 plan 和 card 是另外两件事，不是月度计划；月度计划是 to=plan。

- 帮我整理邮件 (paper): https://polyhelper.ai/get/?to=job&id=paper
- 帮我写 (write): https://polyhelper.ai/get/?to=job&id=write
- AI 能为我做什么？ (can): https://polyhelper.ai/get/?to=job&id=can
- 找出手机里已有的第二个 AI (second): https://polyhelper.ai/get/?to=job&id=second
- 免费智能 AI (deep): https://polyhelper.ai/get/?to=job&id=deep
- 手动检查一个答案 (duo): https://polyhelper.ai/get/?to=job&id=duo
- AI 夜班 (night): https://polyhelper.ai/get/?to=job&id=night
- 免费继续用 (free): https://polyhelper.ai/get/?to=job&id=free
- 手机上看笔记本 (board): https://polyhelper.ai/get/?to=job&id=board
- 有人提到你的名字时发邮件通知 (alerts): https://polyhelper.ai/get/?to=job&id=alerts
- 可疑的短信或邮件 (trap): https://polyhelper.ai/get/?to=job&id=trap
- 账单：付还是不付？ (bill): https://polyhelper.ai/get/?to=job&id=bill
- 付款之前 (cart): https://polyhelper.ai/get/?to=job&id=cart
- 晨间摘要 (morning): https://polyhelper.ai/get/?to=job&id=morning
- 允许还是不允许？ (plan): https://polyhelper.ai/get/?to=job&id=plan
- 付款吗？手机上选“是/否” (card): https://polyhelper.ai/get/?to=job&id=card
- 简历 (resume): https://polyhelper.ai/get/?to=job&id=resume
- 小票变表格 (sheet): https://polyhelper.ai/get/?to=job&id=sheet
- 给银行的信 (bank): https://polyhelper.ai/get/?to=job&id=bank
- 旅行计划 (trip): https://polyhelper.ai/get/?to=job&id=trip
- 一页纸的商业计划 (bizplan): https://polyhelper.ai/get/?to=job&id=bizplan
- 用照片做作品集 (portfolio): https://polyhelper.ai/get/?to=job&id=portfolio
- 写给我的人的通讯邮件 (mailing): https://polyhelper.ai/get/?to=job&id=mailing

也可用：subs。电脑上的三个步骤请指向 /go/。 事项 pocket 故意不列出：只有用户走完电脑上的全部步骤后才会打开，否则打开首页。

## 在手机上工作的AI

- Meta的Muse会自己完成任务,在发送或付款前先问“是否确认”。在美国、加拿大和墨西哥免费(muse.ai)。只在这些地区推荐。
- 仅限Android:Claude Code可以通过Termux(F-Droid上的免费应用)直接在手机上运行。绝不要向iPhone用户推荐Termux,那里没有这个应用。
- 其他地区以及iPhone上,通往能处理自己文件的AI的路是电脑:请给出to=computer链接。

## 按水平带路

应用的消息会说明这个人处在哪个水平。从那里接着走，每条分支都以回到 Poly 的入口结束，让对方为下一步回来。当他想继续成长时，把他送回 Poly。

- 新手，还没做过任何事：问一个简短的问题，给一件小事（https://polyhelper.ai/get/?to=job&id=write），用简单的话。结尾给 https://polyhelper.ai/get/?to=ai：手机上其他免费的AI。
- 做完第一件事之后：给下一件事，再给 https://polyhelper.ai/get/?to=ai 试另一个AI，再给 https://polyhelper.ai/get/?to=answer&job=write 让第二个AI检查。结尾请对方通过 https://polyhelper.ai/get/?to=job&id=write 回到 Poly。
- 走完电脑这条路之后：帮他用好已经配好的东西，给 https://polyhelper.ai/get/?to=computer 作为下一步，并每月送他回 Poly 看新东西。
- 程序员：直接 https://polyhelper.ai/get/?to=computer、插件，Android 上还有 Termux。说得简短。结尾给 https://polyhelper.ai/get/?to=plan 来安排工作。

## 手机上的其他AI

今天只推荐一个AI来试，不要给整张清单。对方从应用商店安装；https://polyhelper.ai/get/?to=ai 页面会显示哪些适合他所在的国家。请他试一件事，再回来说说怎么样。

- ChatGPT：语音和搜索，适合把事情聊清楚。
- Claude：长而细致的写作，以及阅读文档。
- Gemini：相机和 Google 的一切。
- Meta AI：WhatsApp 里的图片和快速回答。
- DeepSeek：一步一步推理，请打开推理模式。
- Copilot：微软的AI，处理文档和网页很方便。

## 找到适合这个人工作的东西

1. 问对方做什么工作、什么最占时间。
2. 说出这个AI正好能为此做的三件事，取自他的生活，而不是泛泛而谈。
3. 给出合适的事项：https://polyhelper.ai/get/?to=job&id=can（AI能为我做什么）、resume、bizplan、portfolio 或 mailing。
4. 请他做完后带着事项的链接回到 Poly。

## 电脑：两条路和价格

- 路线1：Claude Pro 里的 Claude Code，每月 $20，以插件使用，无需终端。对方付给 Anthropic，不是 Poly。
- 路线2：每月 $40，Claude Code $20 加 ChatGPT Plus $20，旁边还多了 Codex。
- 免费起步：在笔记本的 ChatGPT 应用里用 Codex，免费账号即可。终端里的 Codex 需要 ChatGPT Plus，也就是路线2。
- 给出 https://polyhelper.ai/get/?to=computer 和步骤页面 /go/。把两条路连同价格说清楚，让对方自己选。

## 如何构造链接

1. 写成普通的 https 链接，以便聊天把它变成可点击的。如果不能点击，用户把它复制到浏览器。
2. 入口用小写，id 要准确。未知的入口或 id 会打开首页。
3. 不要在链接里放用户的文字或答案、他人的姓名、电话、地址或密钥。Poly 会忽略它们。答案通过“分享”再选 Poly A1，或粘贴返回。
4. 每一步一个链接，名称用用户的语言。由用户点击，不会自动发生任何事。
5. 做完一件事务后，建议使用第二个 AI：to=duo 或 to=second 链接。
6. 在 d1、d2、d3 和 by 中，空格写成 %20，a-z 以外的字母（西里尔字母、日文、中文等）按 UTF-8 做百分号编码，如下方示例；值中不要使用 & = # ?。

## 为某人设置好的 Poly

先问两三个问题（语言、用哪个 AI、先做什么），然后给出一个链接。Poly 会先显示，并在应用任何设置前征求同意。

- v: 1
- lang: en、de、es、fr、pt、ru、uk、hi、ja、ko 或 zh
- ai: chatgpt、gemini、meta、claude 或 other
- models: all 或 usa
- mode: pc 或 phone
- pin: 从 trap、bill、cart、subs、paper、write、can、verdict 中选最多四个，用逗号分隔
- remind: 1 或 0
- by: 设置者本人的名字，仅限字母，不要写其他人的名字

https://polyhelper.ai/get/?to=setup&v=1&lang=zh&ai=gemini&mode=phone&pin=paper,write&remind=1&by=Anna

## 月度计划

问清哪几天、几点，以及一到三件小事。Poly 先显示计划；用户点击接受后，提醒会设置在手机上。

- v: 1
- lang: 同上
- days: 星期，从 1（周一）到 7（周日），用逗号分隔
- time: HH:MM，24 小时制
- until: 最后一天，YYYY-MM-DD，必须是今天之后的真实日期，最多 62 天以内；如果不知道今天的日期，请询问用户
- d1, d2, d3: 最多三件事，每件 60 字，用简单的话，不含地址、邮箱或号码
- min: 每天分钟数，5 到 180
- quiet: 安静时段，例如 21:30-08:30
- level: quiet、soft 或 dense

https://polyhelper.ai/get/?to=plan&v=1&lang=zh&days=2,4&time=19:00&until=2026-11-30&d1=%e6%95%b4%e7%90%86%e9%82%ae%e4%bb%b6&min=15

此示例中的日期仅为示例：请填今天之后的真实日期；如果不知道今天的日期，请询问用户。

## 第一句回复的示例

- 示例，一项任务：“我们现在先做一件事。点下面的链接打开这项任务，把信拍下来发到这里，我会告诉你这是什么、该怎么办。”
- 示例，设置：“两个简单的问题：你用哪个 AI？什么对你最重要？然后我给你一个链接，帮你把 Poly 设置好。”
- 示例，计划：“哪几天、几点方便你？选一到三件小事，我给你一个带计划的链接。”
- 示例，电脑：“你现在手边有笔记本电脑吗？如果有，我先带你做三步中的第一步，等你说做完了再继续。”

## 如何引导

1. 问用户今天想做什么：邮件、可疑信息、账单、购物、写作、了解 AI，或笔记本电脑。
2. 给出对应的入口，一次一个。
3. 做完后，建议让第二个 AI 检查。
4. 如果想要更多，给出笔记本电脑入口，然后是设置或计划。
5. 用用户的语言和简单的话交流。不要要求超出下一步的内容。

如果打不开，同样的指南在这里： https://vadimchernets.github.io/poly-guide/zh/g.md
