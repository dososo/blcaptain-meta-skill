# with-meta-skill 测试报告：xhs-article-card-pack

## 结论

是否使用 `blcaptain-meta-skill`：是。

本轮按 `blcaptain-meta-skill/SKILL.md` 执行了 Research → Analyze → Plan → Develop → Validate → Test → Audit → Summarize 流程，并结合系统 `skill-creator` 规范创建了一个可复用 Agent Skill 包：`xhs-article-card-pack`。

最终官方 quick validate 已通过。

## Non-Skill Gate

决策：做 Skill。

原因：
- 这不是一次性摘要或翻译，而是重复发生的创作流程。
- 输入同时包含中文长文、人像/头像、产品截图，容易出现信息压缩、视觉遮挡、事实编造和误触发问题。
- 输出可以通过 6 卡结构、文案预算、素材策略、路由 eval、failure library 和样例 JSON 校验。
- baseline 对照只有初始化占位 `SKILL.md`，缺少真实 description、references、templates、evals、failure/gotcha 和验证脚本。

替代方案：
- 只写一段提示词：最快，但失败点不可复用，容易漏掉截图保真和头像遮挡检查。
- 只写 SOP 文档：能指导人，但不能帮助 Agent 路由、加载资源和运行校验。
- 只写脚本：无法处理创作判断、视觉取舍和长文信息架构。

成熟度层级：Production 轻量版。理由是该流程值得复用且有 eval/脚本验证，但还没有真实用户长期回归数据，不标记为 Library 或 Governed。

机会评分：19/24。

| 维度 | 分数 | 说明 |
| --- | ---: | --- |
| 重复频次 | 2 | 内容创作者和产品运营会反复做长文转卡片 |
| 单次价值 | 3 | 能显著节省结构化、视觉提示词和 QA 时间 |
| 失败成本 | 2 | 错误会导致内容不可读、截图失真或事实编造 |
| 专家经验密度 | 3 | 需要内容、视觉、小红书读法和素材安全判断 |
| 工具/资产复用 | 3 | 可复用模板、eval、failure library、校验脚本 |
| 可验证性 | 2 | 结构和预算可验证，最终审美仍需人工判断 |
| 分发潜力 | 2 | 可供个人/团队内容生产复用 |
| 维护可控性 | 2 | 依赖少，但平台尺寸和内容风格需定期复核 |

## NABC / ROI

Need：用户需要把中文长文、头像、产品截图稳定转成小红书优先的 6 张竖版图文卡片，而不是每次重新提示 Agent 如何拆文、排卡、保护素材和检查风险。

Approach：做薄 `SKILL.md` 负责触发和导航；把长流程放进 `references/`，把输出模板放进 `assets/templates/`，把路由/执行/失败用例放进 `evals/`，把确定性校验放进 `scripts/`，用 `manifest.json` 记录治理元数据。

Benefit：减少重复提示词，降低“摘要冒充卡片”“头像/截图被遮挡”“编造产品证据”“误触发普通摘要任务”等失败概率。预计复用 2-3 次即可抵消创建成本。

Competition：一次性 prompt、Notion SOP、设计模板、纯图片生成提示词都更轻，但无法同时覆盖 Agent 路由、资源按需加载、失败库和机器校验。

## 创建的文件

- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/SKILL.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/agents/openai.yaml`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/assets/templates/card-plan-template.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/assets/templates/image-prompt-template.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/assets/templates/sample-card-plan.json`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/evals/failure_library.json`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/evals/route_cases.json`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/evals/scenario_cases.json`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/manifest.json`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/references/content-workflow.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/references/gotchas.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/references/visual-standards.md`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/scripts/check_card_plan.py`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/scripts/eval_routes.py`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack/scripts/validate_skill_pack.py`
- `${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/report.md`

## 命令与输出

读取并验证 meta skill 自身：

```bash
python3 blcaptain-meta-skill/scripts/validate_meta_skill.py blcaptain-meta-skill
```

输出：

```text
Validation passed: blcaptain-meta-skill
```

```bash
python3 blcaptain-meta-skill/scripts/eval_routes.py blcaptain-meta-skill/evals/route_cases.json
```

输出：

```text
Route eval fixture passed
Cases: 13
- boundary: 2
- near_neighbor: 3
- negative: 4
- positive: 4
```

baseline 对照校验：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py third-round-forward-test/baseline/no-skill-xhs-article-card-pack
```

输出：

```text
Skill is valid!
```

对照结论：baseline 包结构有效，但只包含 `SKILL.md`、`agents/openai.yaml`、两份 references 和一个规划脚本；未形成 Non-Skill gate、NABC/ROI、eval fixtures、failure library、manifest、regression history 或视觉产物验收。

初始化骨架时的失败：

```bash
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py xhs-article-card-pack --path ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill --resources scripts,references,assets --interface display_name='XHS Article Card Pack' --interface short_description='把中文长文与素材转成 6 张小红书卡片' --interface default_prompt='Use $xhs-article-card-pack to turn this Chinese article, avatar, and product screenshots into a 6-card Xiaohongshu vertical carousel plan.'
```

输出：

```text
Initializing skill: xhs-article-card-pack
   Location: ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill
   Resources: scripts, references, assets

[OK] Created skill directory: ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack
[OK] Created SKILL.md
[ERROR] short_description must be 25-64 characters (got 19).
```

最终校验：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_skill_pack.py .
```

输出：

```text
Skill pack validation passed
- required_files: 15
- route_cases: 7
- scenario_cases: 4
- failure_cases: 4
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/eval_routes.py evals/route_cases.json
```

输出：

```text
Route eval validation passed
- near_neighbor: 2
- negative: 2
- positive: 3
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_card_plan.py assets/templates/sample-card-plan.json
```

输出：

```text
Card plan validation passed: 6 cards, 3:4 canvas, copy budgets OK
```

```bash
PYTHONDONTWRITEBYTECODE=1 python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack
```

输出：

```text
Skill is valid!
```

上下文预算检查：

```bash
python3 ../../../blcaptain-meta-skill/scripts/context_budget.py SKILL.md
```

输出：

```text
OK SKILL.md: approx_tokens=623, mode=heuristic, lines=45, max=1300
```

写入边界检查：

```bash
find ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill -maxdepth 4 -type f -print | sort
```

输出为上方“创建的文件”中的 skill 包文件；当时尚未写入本报告。

```bash
find ${PROJECT_ROOT}/third-round-forward-test/with-meta-skill/xhs-article-card-pack -name '__pycache__' -o -name '*.pyc'
```

输出为空。

## 失败与修复

- 官方 `init_skill.py` 首次运行失败：`short_description` 长度为 19，不满足 25-64 字符约束。修复：手动创建 `agents/openai.yaml`，将 `short_description` 改为更完整的中文描述。
- baseline 对照包官方校验通过；它不是结构失败，而是治理/eval/manifest/failure/visual evidence 缺失，因此只作为能力产品化深度不足的对照。
- 写目录时误带了一个空的 `${PROJECT_ROOT}/third-round-test-dummy` 路径。修复：确认它是本轮误建的空目录后，用单一路径 `rmdir` 删除。
- 运行 Python 校验时产生了 `scripts/__pycache__/check_card_plan.cpython-313.pyc`。修复：按规则删除单个明确 pyc 文件，再用 `rmdir` 移除空 `__pycache__`，并用 `PYTHONDONTWRITEBYTECODE=1` 复跑全部验证。

## Route / Eval / Failure / Gotcha 覆盖

- route：`evals/route_cases.json` 包含 3 个正例、2 个反例、2 个近邻例。
- eval：`evals/scenario_cases.json` 包含执行、压力、回归场景。
- failure：`evals/failure_library.json` 覆盖摘要冒充卡片、视觉遮挡、事实编造、近邻误触发。
- gotcha：`references/gotchas.md` 将失败现象映射到正确做法和对应 eval。

## 残余风险

- 本轮完成的是结构、脚本和 fixture 校验；没有用真实用户文章、真实头像和真实产品截图做完整图片生成 forward-test。
- 小红书平台尺寸、裁切和推荐风格可能变化；Skill 已写明用户或平台给出最新尺寸时优先用户要求，但未联网核验当前官方规格。
- 视觉审美不能完全靠脚本保证；脚本只校验 6 卡结构、3:4 画布和基础文案预算。
- 本轮由独立子代理在 fresh context 下创建该子包；残余风险是报告本身仍主要证明结构、脚本和 fixture 级交付，尚未覆盖真实客户素材的端到端图片生成。
