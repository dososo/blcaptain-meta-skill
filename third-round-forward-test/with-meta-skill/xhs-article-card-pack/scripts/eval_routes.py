#!/usr/bin/env python3
"""校验路由 eval 语料的结构和正反例覆盖。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_TYPES = {"positive", "negative", "near_neighbor"}


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: python3 scripts/eval_routes.py <route_cases.json>")
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        print("route_cases.json 必须包含非空 cases 数组")
        return 1

    errors: list[str] = []
    counts: Counter[str] = Counter()
    for case in cases:
        if not isinstance(case, dict):
            errors.append("case 必须是对象")
            continue
        for field in ["id", "type", "request", "expected_trigger", "reason"]:
            if field not in case:
                errors.append(f"{case.get('id', '<unknown>')} 缺少字段: {field}")
        case_type = str(case.get("type"))
        counts[case_type] += 1
        expected = case.get("expected_trigger")
        if case_type == "positive" and expected is not True:
            errors.append(f"{case.get('id')} positive 应 expected_trigger=true")
        if case_type in {"negative", "near_neighbor"} and expected is not False:
            errors.append(f"{case.get('id')} {case_type} 应 expected_trigger=false")

    missing = REQUIRED_TYPES - set(counts)
    if missing:
        errors.append("缺少路由类型: " + ", ".join(sorted(missing)))

    if errors:
        print("Route eval validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Route eval validation passed")
    for case_type in sorted(counts):
        print(f"- {case_type}: {counts[case_type]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
