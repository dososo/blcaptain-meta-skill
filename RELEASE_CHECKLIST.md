# GitHub 发布检查表

发布前按顺序检查。不要因为某个检查“看起来没问题”就跳过命令。

## 1. 文件树卫生

```bash
find blcaptain-meta-skill third-round-forward-test \( -name '*.swp' -o -name '*.swo' -o -name '*~' -o -name '.DS_Store' -o -name '*.tmp' -o -name '*.bak' -o -name '__pycache__' -o -name '*.pyc' -o -type d -empty \) -print
```

预期：无输出。

## 2. 私有信息扫描

```bash
python3 - <<'PY'
from pathlib import Path
import importlib.util

validator_path = Path("blcaptain-meta-skill/scripts/validate_meta_skill.py")
spec = importlib.util.spec_from_file_location("validate_meta_skill", validator_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

roots = [Path("blcaptain-meta-skill"), Path("third-round-forward-test")]
failures = []
for root in roots:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in module.FORBIDDEN_PRIVATE_MARKERS:
            if marker in text:
                failures.append(f"{path}: private marker found")

if failures:
    print("\n".join(failures))
    raise SystemExit(1)
print("Private marker scan passed")
PY
```

预期：`Private marker scan passed`。

说明：`tasks/` 是本地内部工作日志，默认不随公开仓库发布。

## 3. Skill 包结构验证

```bash
python3 blcaptain-meta-skill/scripts/validate_meta_skill.py blcaptain-meta-skill
```

预期：`Validation passed: blcaptain-meta-skill`

## 4. 官方结构验证

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" blcaptain-meta-skill
```

预期：`Skill is valid!`

## 5. 路由评估

```bash
python3 blcaptain-meta-skill/scripts/eval_routes.py blcaptain-meta-skill/evals/route_cases.json
```

预期：13 条 route cases 通过。

## 6. 上下文预算

```bash
python3 blcaptain-meta-skill/scripts/context_budget.py blcaptain-meta-skill/SKILL.md
```

预期：低于 `max=1300`。

如需真实 tokenizer：

```bash
uv run --with tiktoken python blcaptain-meta-skill/scripts/context_budget.py blcaptain-meta-skill/SKILL.md --tokenizer openai --encoding o200k_base
```

## 7. 视觉资产渲染

```bash
mkdir -p /tmp/blcaptain-meta-skill-visual-check
for f in blcaptain-meta-skill/assets/visual-validation/*.svg; do magick "$f" "/tmp/blcaptain-meta-skill-visual-check/$(basename "${f%.svg}").png" || exit 1; done
magick identify -format '%f %wx%h\n' /tmp/blcaptain-meta-skill-visual-check/*.png
```

预期：

- `avatar.png 160x160`
- `card-01.png` 至 `card-06.png` 均为 `1080x1440`
- `product-screenshot.png 1080x720`

## 8. 子包证据验证

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" third-round-forward-test/baseline/no-skill-xhs-article-card-pack
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" third-round-forward-test/with-meta-skill/xhs-article-card-pack
```

with-meta 子包：

```bash
cd third-round-forward-test/with-meta-skill/xhs-article-card-pack
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_skill_pack.py .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/eval_routes.py evals/route_cases.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_card_plan.py assets/templates/sample-card-plan.json
```

## 9. 发布口径

发布页必须说清楚：

- 这是一个可安装的 Agent Skill 方法论包。
- 个人用途和开源项目免费。
- 闭源商业用途需购买商业授权。
- 不要把未完成的真实 E2E、平台遥测或人工批准说成已经完成。

## 10. GitHub 发布前人工确认

- [ ] README 已经能让第一次看到项目的人知道它是什么。
- [ ] LICENSE 与商业授权策略一致。
- [ ] `tasks/` 不进入公开仓库，或已经人工脱敏。
- [ ] 仓库描述已填写。
- [ ] 发布标签、版本号和 release notes 已确认。
- [ ] 如果面向商业客户，商业授权联系方式已补充。
