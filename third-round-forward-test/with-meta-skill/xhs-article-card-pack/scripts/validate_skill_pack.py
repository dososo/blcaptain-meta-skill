#!/usr/bin/env python3
"""校验 xhs-article-card-pack 的资源完整性。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from check_card_plan import validate_plan  # noqa: E402


REQUIRED_PATHS = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/content-workflow.md",
    "references/visual-standards.md",
    "references/gotchas.md",
    "assets/templates/card-plan-template.md",
    "assets/templates/image-prompt-template.md",
    "assets/templates/sample-card-plan.json",
    "evals/route_cases.json",
    "evals/scenario_cases.json",
    "evals/failure_library.json",
    "scripts/check_card_plan.py",
    "scripts/eval_routes.py",
    "scripts/validate_skill_pack.py",
    "manifest.json",
]


def _load_json(root: Path, relative: str) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            errors.append(f"缺少文件: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        skill_text = skill_path.read_text(encoding="utf-8")
        if "[TODO" in skill_text or "TODO:" in skill_text:
            errors.append("SKILL.md 仍包含 TODO 占位")
        for literal in [
            "references/content-workflow.md",
            "references/visual-standards.md",
            "references/gotchas.md",
            "evals/route_cases.json",
            "scripts/check_card_plan.py",
        ]:
            if literal not in skill_text:
                errors.append(f"SKILL.md 未直接引用 {literal}")
        if len(skill_text.splitlines()) > 140:
            errors.append("SKILL.md 超过 140 行，入口不够薄")

    try:
        route_cases = _load_json(root, "evals/route_cases.json").get("cases", [])
        route_types = {case.get("type") for case in route_cases if isinstance(case, dict)}
        for required_type in ["positive", "negative", "near_neighbor"]:
            if required_type not in route_types:
                errors.append(f"route_cases 缺少 {required_type}")
    except Exception as exc:
        errors.append(f"route_cases.json 无法解析: {exc}")

    try:
        scenario_cases = _load_json(root, "evals/scenario_cases.json").get("cases", [])
        if len(scenario_cases) < 3:
            errors.append("scenario_cases 至少需要 3 个执行或压力用例")
    except Exception as exc:
        errors.append(f"scenario_cases.json 无法解析: {exc}")

    try:
        failures = _load_json(root, "evals/failure_library.json").get("failures", [])
        if len(failures) < 3:
            errors.append("failure_library 至少需要 3 个失败案例")
        for failure in failures:
            if not failure.get("gotcha"):
                errors.append(f"{failure.get('id', '<unknown>')} 缺少 gotcha")
    except Exception as exc:
        errors.append(f"failure_library.json 无法解析: {exc}")

    try:
        manifest = _load_json(root, "manifest.json")
        for field in ["name", "version", "owner", "updated_at", "maturity_tier", "validation_commands"]:
            if field not in manifest:
                errors.append(f"manifest 缺少字段: {field}")
        commands = "\n".join(manifest.get("validation_commands", []))
        if "quick_validate.py" not in commands:
            errors.append("manifest.validation_commands 必须包含官方 quick_validate")
    except Exception as exc:
        errors.append(f"manifest.json 无法解析: {exc}")

    try:
        sample_plan = _load_json(root, "assets/templates/sample-card-plan.json")
        errors.extend(validate_plan(sample_plan))
    except Exception as exc:
        errors.append(f"sample-card-plan.json 无法解析或校验: {exc}")

    if errors:
        print("Skill pack validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill pack validation passed")
    print(f"- required_files: {len(REQUIRED_PATHS)}")
    print(f"- route_cases: {len(route_cases)}")
    print(f"- scenario_cases: {len(scenario_cases)}")
    print(f"- failure_cases: {len(failures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
