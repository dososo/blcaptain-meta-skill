# Gotchas

## 把文章摘要当成卡片脚本

失败现象：6 张卡都是摘要段落，没有视觉主体、滑动节奏和截图策略。

正确做法：先抽取主张、证据、行动，再分配到封面、场景、洞察、方法、证据、收束。

对应 eval：`evals/scenario_cases.json` 的 `exec-long-article-product-proof`。

## 标题压住头像或产品 UI

失败现象：封面标题覆盖五官，或第 5 卡标题盖住截图中的功能名、数据、按钮。

正确做法：头像和截图是受保护区域，标题与标注必须绕开关键区域。

对应 eval：`evals/failure_library.json` 的 `visual-occlusion`。

## 编造截图和产品结论

失败现象：为了让卡片更完整，补出素材里没有的功能、价格、数据或客户案例。

正确做法：来自截图的内容必须可追溯；不确定时写“待用户确认”。

对应 eval：`evals/failure_library.json` 的 `invented-product-proof`。

## 误触发到普通总结任务

失败现象：用户只是要摘要、改标题或写公众号摘要，却启用 6 卡流程。

正确做法：只有用户要求小红书图文、竖版卡片、轮播图、图文种草或明确素材转卡片时触发。

对应 eval：`evals/route_cases.json` 的 negative 和 near-neighbor 用例。
