#!/usr/bin/env python3
"""Validate the blcaptain-meta-skill package structure."""

from __future__ import annotations

import fnmatch
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "manifest.json",
    "references/00-real-delivery-first.md",
    "references/01-non-skill-decision.md",
    "references/02-skill-design-and-packaging.md",
    "references/03-eval-protocol.md",
    "references/04-safety-and-supply-chain.md",
    "references/05-governance-and-operations.md",
    "references/06-platform-differences.md",
    "references/07-role-playbooks.md",
    "assets/templates/skill-brief.md",
    "assets/templates/skill-design-spec.md",
    "assets/templates/eval-case.md",
    "assets/templates/gotcha.md",
    "assets/templates/iteration-record.md",
    "assets/templates/governance-manifest.json",
    "evals/route_cases.json",
    "evals/scenario_cases.json",
    "evals/failure_library.json",
    "evals/forward_test_results.json",
    "evals/regression_history.json",
    "evals/platform_schema_tokenizer_check.json",
    "examples/three-scenario-worked-examples.md",
    "examples/visual-card-validation.md",
    "scripts/validate_meta_skill.py",
    "scripts/context_budget.py",
    "scripts/eval_routes.py",
]

PLACEHOLDERS = ["TO" + "DO", "T" + "BD", "待" + "补", "待" + "定", "[" + "TO" + "DO"]
FORBIDDEN_PRIVATE_MARKERS = [
    "gui" + "zang",
    "归" + "藏",
    "歸" + "藏",
    "BL" + "Team",
    "man" + "xiaochu",
    "/Users/" + "man" + "xiaochu",
    "Meta " + "Skill " + "Evidence Console",
    "Description must be a string, " + "got list",
    "未使用" + "独立子代理",
]
# Release-hygiene pollutants must never ship inside a publishable Skill package.
POLLUTANT_FILE_GLOBS = [
    "*.swp",
    "*.swo",
    "*~",
    ".DS_Store",
    "*.tmp",
    "*.bak",
    "*.pyc",
]
POLLUTANT_DIR_NAMES = ["__pycache__"]
ALLOWED_TIERS = {"scaffold", "production", "library", "governed"}
ALLOWED_STATUSES = {"experimental", "active", "deprecated"}
ALLOWED_FORWARD_STATUSES = {"pass", "partial", "fail"}
RESOURCE_DIRS = ["references", "examples", "evals", "assets/templates"]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def load_json(path: Path, failures: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"Invalid JSON: {path}: {exc}", failures)
        return {}


def resource_files(root: Path) -> set[str]:
    resources: set[str] = set()
    for rel_dir in RESOURCE_DIRS:
        directory = root / rel_dir
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if path.is_file():
                resources.add(str(path.relative_to(root)))
    return resources


def package_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def scan_pollutants(root: Path, failures: list[str]) -> None:
    """Reject editor temp files, OS cruft, and Python build artifacts in the package."""
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        name = path.name
        if path.is_dir():
            if name in POLLUTANT_DIR_NAMES:
                fail(f"Release pollutant directory found in package: {rel}", failures)
            continue
        for glob in POLLUTANT_FILE_GLOBS:
            if fnmatch.fnmatch(name, glob):
                fail(f"Release pollutant file found in package: {rel}", failures)
                break


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    if not root.exists():
        return [f"Skill root not found: {root}"]

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            fail(f"Missing required file: {rel}", failures)

    scan_pollutants(root, failures)

    for path in package_files(root):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in FORBIDDEN_PRIVATE_MARKERS:
            if marker in text:
                fail(f"Private or machine-specific marker found in {rel}: {marker}", failures)

    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return failures

    skill_text = skill_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != root.name:
        fail(f"Frontmatter name must equal directory name: {root.name}", failures)
    description = frontmatter.get("description", "")
    if not description.startswith("Use when"):
        fail("Frontmatter description must start with 'Use when'", failures)
    if len(description) > 1024:
        fail("Frontmatter description exceeds 1024 characters", failures)

    for marker in PLACEHOLDERS:
        if marker in skill_text:
            fail(f"Placeholder marker found in SKILL.md: {marker}", failures)

    for rel in sorted(resource_files(root)):
        if rel not in skill_text:
            fail(f"Resource exists but is not navigated from SKILL.md: {rel}", failures)

    manifest = load_json(root / "manifest.json", failures)
    for key in ["name", "version", "owner", "updated_at", "review_cadence", "status", "maturity_tier", "lifecycle_stage", "validation_commands"]:
        if key not in manifest:
            fail(f"manifest.json missing key: {key}", failures)
    if manifest.get("name") != root.name:
        fail("manifest.json name must equal skill directory name", failures)
    if manifest.get("status") not in ALLOWED_STATUSES:
        fail(f"manifest.json status must be one of {sorted(ALLOWED_STATUSES)}", failures)
    tier = manifest.get("maturity_tier")
    if tier not in ALLOWED_TIERS:
        fail(f"manifest.json maturity_tier must be one of {sorted(ALLOWED_TIERS)}", failures)
    lifecycle_stage = manifest.get("lifecycle_stage")
    if lifecycle_stage not in ALLOWED_TIERS:
        fail(f"manifest.json lifecycle_stage must be one of {sorted(ALLOWED_TIERS)}", failures)
    target_maturity = manifest.get("target_maturity")
    if target_maturity is not None and target_maturity not in ALLOWED_TIERS:
        fail(f"manifest.json target_maturity must be one of {sorted(ALLOWED_TIERS)}", failures)
    openai_yaml = (root / "agents/openai.yaml").read_text(encoding="utf-8") if (root / "agents/openai.yaml").is_file() else ""
    if "$blcaptain-meta-skill" not in openai_yaml:
        fail("agents/openai.yaml default_prompt must mention $blcaptain-meta-skill", failures)
    short_match = re.search(r"short_description:\s*\"(.+)\"", openai_yaml)
    if not short_match:
        fail("agents/openai.yaml missing quoted short_description", failures)
    elif not 25 <= len(short_match.group(1)) <= 64:
        fail("agents/openai.yaml short_description must be 25-64 characters", failures)

    route_cases = load_json(root / "evals/route_cases.json", failures)
    for keyword in route_cases.get("description_must_include", []):
        if keyword not in description:
            fail(f"Description missing required route keyword: {keyword}", failures)
    cases = route_cases.get("cases", [])
    counts = {case.get("type"): 0 for case in cases}
    for case in cases:
        counts[case.get("type")] = counts.get(case.get("type"), 0) + 1
        for key in ["id", "type", "query", "expected_route"]:
            if key not in case:
                fail(f"Route case missing {key}: {case}", failures)
        case_type = case.get("type")
        if case_type in {"negative", "near_neighbor"} and not case.get("forbidden_signals"):
            fail(f"{case.get('id')} must define forbidden_signals", failures)
        if case_type == "near_neighbor" and not case.get("target_artifact_signals"):
            fail(f"{case.get('id')} must define target_artifact_signals", failures)
    minimums = route_cases.get("minimum_counts", {})
    for case_type, minimum in minimums.items():
        if counts.get(case_type, 0) < minimum:
            fail(f"Not enough {case_type} route cases: {counts.get(case_type, 0)} < {minimum}", failures)

    scenarios = load_json(root / "evals/scenario_cases.json", failures).get("scenarios", [])
    if len(scenarios) < 3:
        fail("scenario_cases.json must include at least 3 scenarios", failures)

    failures_data = load_json(root / "evals/failure_library.json", failures).get("families", [])
    if len(failures_data) < 6:
        fail("failure_library.json must include at least 6 failure families", failures)

    forward_tests = load_json(root / "evals/forward_test_results.json", failures).get("results", [])
    if len(forward_tests) < 3:
        fail("forward_test_results.json must include at least 3 fresh-context results", failures)
    for result in forward_tests:
        if result.get("status") not in ALLOWED_FORWARD_STATUSES:
            fail(f"Forward test status must be one of {sorted(ALLOWED_FORWARD_STATUSES)}: {result.get('id', '<unknown>')}", failures)
        for key in ["id", "scenario", "agent", "test_level", "status", "evidence", "residual_risk"]:
            if key not in result:
                fail(f"Forward test missing {key}: {result}", failures)
        if result.get("status") in {"partial", "fail"} and not result.get("remediation"):
            fail(f"Forward test partial/fail requires remediation: {result.get('id', '<unknown>')}", failures)

    regression_records = load_json(root / "evals/regression_history.json", failures).get("records", [])
    if not regression_records:
        fail("regression_history.json must include at least one regression record", failures)
    for record in regression_records:
        for key in ["id", "change", "baseline", "rerun_commands", "result", "residual_risk"]:
            if key not in record:
                fail(f"Regression record missing {key}: {record}", failures)
        if not record.get("baseline"):
            fail(f"Regression record must include baseline evidence: {record.get('id', '<unknown>')}", failures)
        if not record.get("rerun_commands"):
            fail(f"Regression record must include rerun commands: {record.get('id', '<unknown>')}", failures)

    if tier == "governed":
        satisfied_evidence = manifest.get("satisfied_promotion_evidence")
        remaining_requirements = manifest.get("remaining_promotion_requirements")
        if not isinstance(satisfied_evidence, list) or not satisfied_evidence:
            fail("governed maturity requires non-empty satisfied_promotion_evidence", failures)
        if remaining_requirements is not None and not isinstance(remaining_requirements, list):
            fail("governed maturity requires remaining_promotion_requirements to be a list when present", failures)
        elif remaining_requirements:
            fail("governed maturity requires empty remaining_promotion_requirements", failures)
        if not regression_records:
            fail("governed maturity requires non-empty evals/regression_history.json records", failures)

    platform_check = load_json(root / "evals/platform_schema_tokenizer_check.json", failures)
    targets = platform_check.get("targets", [])
    if not targets:
        fail("platform_schema_tokenizer_check.json must include targets", failures)
    for target in targets:
        if not target.get("schema_sources"):
            fail(f"Platform check target missing schema_sources: {target.get('platform', '<unknown>')}", failures)
        schema_status = target.get("schema_result", {}).get("status")
        if schema_status not in {"pass", "reviewed", "partial"}:
            fail(f"Platform check schema_result has invalid status: {target.get('platform', '<unknown>')}", failures)
        tokenizer_status = target.get("tokenizer_result", {}).get("status")
        if tokenizer_status not in {"pass", "reviewed", "not_executed_no_credentials"}:
            fail(f"Platform check tokenizer_result has invalid status: {target.get('platform', '<unknown>')}", failures)

    if tier == "governed":
        has_execution_forward_test = any(
            result.get("test_level") == "execution_forward_test" and result.get("status") == "pass"
            for result in forward_tests
        )
        if not has_execution_forward_test:
            fail("governed maturity requires at least one passing execution_forward_test", failures)

    return failures


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    failures = validate(root)
    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
