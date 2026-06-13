---
name: xhs-article-card-pack
description: "Use when converting Chinese long-form articles, author/avatar images, and product screenshots into a Xiaohongshu-first six-card vertical carousel plan, storyboard, visual brief, image prompts, or QA checklist; especially for 小红书图文卡片、6张竖版卡片、长文视觉化、头像合成、产品截图种草、中文内容卡片."
---

# 小红书 6 卡图文卡片包

把中文长文章、头像和产品截图转成小红书优先的 6 张竖版图文卡片方案。默认交付可执行的卡片脚本、版式说明、素材处理建议、生成提示词和 QA 清单。

## 工作流

1. 先确认输入：文章正文、头像/人物图、产品截图、品牌语气、禁用信息、尺寸要求。缺少关键素材时，先用占位策略标注，不要虚构。
2. 抽取文章主张、证据、方法和可视化钩子；需要细化时读取 `references/content-workflow.md`。
3. 生成 6 卡结构：封面、问题/场景、核心洞察、方法/框架、产品截图证据、收束/行动。
4. 为每张卡写标题、正文、视觉主体、素材使用方式、版式约束、图片生成或设计提示词。
5. 按 `references/visual-standards.md` 做小红书竖版适配和可读性检查。
6. 用 `assets/templates/card-plan-template.md` 或 `assets/templates/sample-card-plan.json` 组织交付；需要机器校验时运行 `scripts/check_card_plan.py`。

## 资源导航

- 处理长文拆解、6 卡叙事和交付格式：读取 `references/content-workflow.md`。
- 处理头像、产品截图、视觉规范和审核清单：读取 `references/visual-standards.md`。
- 规避常见失败：读取 `references/gotchas.md`。
- 输出模板：使用 `assets/templates/card-plan-template.md`、`assets/templates/image-prompt-template.md`。
- 路由、执行和失败回归：查看 `evals/route_cases.json`、`evals/scenario_cases.json`、`evals/failure_library.json`。

## 强约束

- 保持 6 张卡，不自动扩成更多页；除非用户明确要求。
- 默认 3:4 竖版画布；如用户或平台要求不同尺寸，优先用户要求并说明变化。
- 标题不得遮挡头像五官、产品关键 UI、价格、数据或按钮。
- 产品截图中的功能、数据、价格和结论必须来自用户素材或明确标注为占位。
- 不把长文全文塞进卡片；每张卡只保留一个明确阅读动作。
- 不使用无意义渐变、发光、堆 emoji、过度圆角或同构图连续复制。
- 涉及医疗、金融、法律、投资等高风险内容时，标注人工复核，不给确定性承诺。

## 验证

```bash
python3 scripts/validate_skill_pack.py .
python3 scripts/eval_routes.py evals/route_cases.json
python3 scripts/check_card_plan.py assets/templates/sample-card-plan.json
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```
