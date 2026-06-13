#!/usr/bin/env python3
"""校验 6 张小红书卡片计划的结构和基础文案预算。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_ROLES = ["cover", "context", "insight", "framework", "product-proof", "close"]
REQUIRED_CARD_FIELDS = [
    "id",
    "role",
    "headline",
    "body",
    "visual_focus",
    "asset_strategy",
    "layout_notes",
    "generation_prompt",
    "qa",
]


def _text_len(value: Any) -> int:
    return len(str(value).strip())


def validate_plan(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in ["title", "source_summary", "brand_voice", "canvas", "cards", "export"]:
        if field not in plan:
            errors.append(f"缺少顶层字段: {field}")

    canvas = plan.get("canvas", {})
    if isinstance(canvas, dict):
        width = canvas.get("width")
        height = canvas.get("height")
        if not isinstance(width, int) or not isinstance(height, int):
            errors.append("canvas.width 和 canvas.height 必须是整数")
        elif abs((width / height) - 0.75) > 0.02:
            errors.append("画布比例应接近 3:4")
        if canvas.get("safe_margin_px", 0) < 72:
            errors.append("safe_margin_px 不应低于 72")
    else:
        errors.append("canvas 必须是对象")

    cards = plan.get("cards")
    if not isinstance(cards, list):
        errors.append("cards 必须是数组")
        return errors

    if len(cards) != 6:
        errors.append("cards 必须正好包含 6 张卡")

    seen_roles: list[str] = []
    for index, card in enumerate(cards, start=1):
        if not isinstance(card, dict):
            errors.append(f"第 {index} 张卡必须是对象")
            continue

        for field in REQUIRED_CARD_FIELDS:
            if field not in card:
                errors.append(f"第 {index} 张卡缺少字段: {field}")

        if card.get("id") != index:
            errors.append(f"第 {index} 张卡 id 应为 {index}")

        role = card.get("role")
        if role in seen_roles:
            errors.append(f"角色重复: {role}")
        seen_roles.append(str(role))

        if _text_len(card.get("headline", "")) > 28:
            errors.append(f"第 {index} 张卡标题超过 28 个字符")
        if _text_len(card.get("body", "")) > 90:
            errors.append(f"第 {index} 张卡正文超过 90 个字符")
        if _text_len(card.get("generation_prompt", "")) < 40:
            errors.append(f"第 {index} 张卡 generation_prompt 过短")

        qa = card.get("qa")
        if not isinstance(qa, list) or len(qa) < 3:
            errors.append(f"第 {index} 张卡 qa 至少需要 3 项")

    missing_roles = [role for role in REQUIRED_ROLES if role not in seen_roles]
    if missing_roles:
        errors.append("缺少卡片角色: " + ", ".join(missing_roles))

    export = plan.get("export", {})
    if isinstance(export, dict) and export.get("card_count") != 6:
        errors.append("export.card_count 应为 6")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: python3 scripts/check_card_plan.py <card-plan.json>")
        return 2

    path = Path(sys.argv[1])
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"无法读取 JSON: {exc}")
        return 1

    errors = validate_plan(plan)
    if errors:
        print("Card plan validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Card plan validation passed: 6 cards, 3:4 canvas, copy budgets OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
