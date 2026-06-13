#!/usr/bin/env python3
"""Estimate context cost for skill entry files."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path


CJK_RE = re.compile(r"[\u4e00-\u9fff]")
WORD_RE = re.compile(r"[A-Za-z0-9_]+")


def estimate_tokens(text: str) -> int:
    cjk_chars = len(CJK_RE.findall(text))
    ascii_words = len(WORD_RE.findall(text))
    other_chars = max(len(text) - cjk_chars, 0)
    return math.ceil(cjk_chars / 1.8 + ascii_words * 1.3 + other_chars / 8)


def openai_tokens(text: str, encoding: str) -> int:
    try:
        import tiktoken  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError(
            "OpenAI tokenizer mode requires tiktoken. "
            "Run with: uv run --with tiktoken python scripts/context_budget.py ..."
        ) from exc
    try:
        return len(tiktoken.get_encoding(encoding).encode(text))
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"Unable to load OpenAI tokenizer encoding '{encoding}': {exc}") from exc


def count_tokens(text: str, tokenizer: str, encoding: str) -> tuple[int, str, str]:
    if tokenizer == "openai":
        return openai_tokens(text, encoding), "tokens", f"openai:{encoding}"
    if tokenizer == "auto":
        try:
            return openai_tokens(text, encoding), "tokens", f"openai:{encoding}"
        except RuntimeError:
            return estimate_tokens(text), "approx_tokens", "heuristic"
    return estimate_tokens(text), "approx_tokens", "heuristic"


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate context budget for skill files.")
    parser.add_argument("files", nargs="+", help="Files to inspect")
    parser.add_argument("--max-tokens", type=int, default=1300, help="Recommended max tokens for SKILL.md")
    parser.add_argument(
        "--tokenizer",
        choices=["auto", "heuristic", "openai"],
        default="auto",
        help="Token counter to use; openai requires tiktoken.",
    )
    parser.add_argument("--encoding", default="o200k_base", help="OpenAI tiktoken encoding name")
    args = parser.parse_args()

    failed = False
    for item in args.files:
        path = Path(item)
        text = path.read_text(encoding="utf-8")
        try:
            tokens, token_label, mode = count_tokens(text, args.tokenizer, args.encoding)
        except RuntimeError as exc:
            print(f"ERROR {path}: {exc}")
            failed = True
            continue
        lines = text.count("\n") + 1
        status = "OK" if tokens <= args.max_tokens else "WARN"
        print(f"{status} {path}: {token_label}={tokens}, mode={mode}, lines={lines}, max={args.max_tokens}")
        if path.name == "SKILL.md" and tokens > args.max_tokens:
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
