#!/usr/bin/env python3
"""Validate route eval fixture coverage for blcaptain-meta-skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def contains_any(text: str, signals: list[str]) -> bool:
    lowered = text.lower()
    return any(signal.lower() in lowered for signal in signals)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: eval_routes.py <route_cases.json>")
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    failures: list[str] = []

    counts: dict[str, int] = {}
    for case in cases:
        case_type = case.get("type")
        counts[case_type] = counts.get(case_type, 0) + 1
        for key in ["id", "type", "query", "expected_route"]:
            if key not in case:
                failures.append(f"{case.get('id', '<unknown>')} missing {key}")
        query = case.get("query", "")
        case_type = case.get("type")
        required = case.get("required_signals", [])
        if required and not contains_any(query, required):
            failures.append(f"{case.get('id')} query lacks required signals: {required}")
        forbidden = case.get("forbidden_signals", [])
        if case_type in {"negative", "near_neighbor"} and not forbidden:
            failures.append(f"{case.get('id')} must define forbidden_signals")
        if forbidden and contains_any(query, forbidden):
            failures.append(f"{case.get('id')} query contains forbidden signals: {forbidden}")
        target = case.get("target_artifact_signals", [])
        if case_type == "near_neighbor":
            if not target:
                failures.append(f"{case.get('id')} must define target_artifact_signals")
            elif not contains_any(query, target):
                failures.append(f"{case.get('id')} query lacks target artifact signals: {target}")

    for case_type, minimum in data.get("minimum_counts", {}).items():
        actual = counts.get(case_type, 0)
        if actual < minimum:
            failures.append(f"Need {minimum} {case_type} cases, found {actual}")

    expected_routes = {case.get("expected_route") for case in cases}
    required_routes = {"trigger", "no_trigger", "other_artifact", "trigger_for_decision_only"}
    missing_routes = required_routes - expected_routes
    if missing_routes:
        failures.append(f"Missing expected_route coverage: {sorted(missing_routes)}")

    if failures:
        print("Route eval fixture failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Route eval fixture passed")
    print(f"Cases: {len(cases)}")
    for key in sorted(counts):
        print(f"- {key}: {counts[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
