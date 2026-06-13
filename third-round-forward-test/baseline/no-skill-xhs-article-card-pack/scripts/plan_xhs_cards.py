#!/usr/bin/env python3
"""从中文长文生成小红书 6 卡方案骨架。"""

import argparse
import json
import re
from pathlib import Path


KEYWORDS = (
    "问题",
    "痛点",
    "方法",
    "步骤",
    "案例",
    "产品",
    "截图",
    "数据",
    "经验",
    "建议",
    "结论",
    "为什么",
    "如何",
    "因为",
    "所以",
)


CARD_ROLES = [
    ("封面钩子", "用对象、冲突或结果让目标读者停下"),
    ("场景痛点", "指出读者正在遇到的具体卡点"),
    ("核心洞察", "提炼原文最值得被记住的新判断"),
    ("方法步骤", "把判断改写成可执行动作"),
    ("证据/产品", "用截图、案例或细节证明能落地"),
    ("总结行动", "给出收藏、评论或下一步行动理由"),
]


def clean_text(text: str) -> str:
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[。！？!?；;])\s*|\n+", text)
    return [p.strip(" \t-—·") for p in parts if len(p.strip()) >= 8]


def sentence_score(sentence: str, index: int) -> int:
    score = min(len(sentence), 80)
    score += sum(18 for word in KEYWORDS if word in sentence)
    if index < 4:
        score += 16
    return score


def pick_points(sentences: list[str], limit: int = 6) -> list[str]:
    ranked = sorted(
        enumerate(sentences),
        key=lambda item: sentence_score(item[1], item[0]),
        reverse=True,
    )
    chosen: list[tuple[int, str]] = []
    seen = set()
    for index, sentence in ranked:
        compact = re.sub(r"\W+", "", sentence)[:24]
        if compact in seen:
            continue
        seen.add(compact)
        chosen.append((index, sentence))
        if len(chosen) == limit:
            break
    return [sentence for _, sentence in sorted(chosen)]


def short(text: str, limit: int = 54) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "..."


def build_cards(args: argparse.Namespace, points: list[str]) -> list[dict[str, str]]:
    title = args.title or "这篇文章的核心观点"
    audience = args.audience or "目标读者"
    product = args.product or "产品/方法"
    screenshots = args.screenshot or []
    cards = []
    for index, (role, goal) in enumerate(CARD_ROLES, start=1):
        point = points[index - 1] if index - 1 < len(points) else "待从原文补充关键句"
        if index == 1:
            card_title = f"{audience}先看懂：{short(title, 16)}"
            visual = "强标题 + 头像/产品截图局部 + 1 个场景标签"
            asset = args.avatar or (screenshots[0] if screenshots else "头像或产品截图占位")
        elif index == 5:
            card_title = f"把它落到{short(product, 10)}里看"
            visual = "真实产品截图为主，配 1 至 3 个标注和局部放大"
            asset = screenshots[0] if screenshots else "产品截图占位"
        elif index == 6:
            card_title = "收藏前，记住这 3 句"
            visual = "三条总结 + 行动建议 + 作者头像小署名"
            asset = args.avatar or "作者头像占位"
        else:
            card_title = {
                2: "真正卡住你的不是工具",
                3: "核心其实只有这一句",
                4: "照这个顺序拆就够了",
            }[index]
            visual = "标题、短正文、结构化图示或对比栏"
            asset = "不强制使用素材"
        cards.append(
            {
                "card": str(index),
                "role": role,
                "goal": goal,
                "title": card_title,
                "body_seed": short(point, 90),
                "visual": visual,
                "asset": asset,
                "prompt_seed": f"竖版3:4小红书图文卡片，{role}，主题：{title}，读者：{audience}，画面：{visual}，预留清晰中文标题区域，不生成乱码文字。",
            }
        )
    return cards


def render_markdown(cards: list[dict[str, str]], args: argparse.Namespace) -> str:
    lines = [
        "# 小红书 6 卡方案骨架",
        "",
        f"- 主题：{args.title or '待命名'}",
        f"- 目标读者：{args.audience or '待确认'}",
        f"- 产品/方法：{args.product or '待确认'}",
        f"- 头像：{args.avatar or '未提供'}",
        f"- 截图：{', '.join(args.screenshot or []) or '未提供'}",
        "",
        "| 卡片 | 角色 | 标题草案 | 正文素材 | 视觉 | 使用素材 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for card in cards:
        lines.append(
            "| {card} | {role} | {title} | {body_seed} | {visual} | {asset} |".format(
                **card
            )
        )
    lines.extend(
        [
            "",
            "## 下一步精修",
            "- 把“正文素材”改写成每张卡 35 至 90 个汉字的短文案。",
            "- 检查截图、头像、产品名是否真实来自用户材料。",
            "- 为每张卡补充最终图片提示词、负面提示词和审校点。",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="从中文长文生成小红书 6 张竖版图文卡片方案骨架。"
    )
    parser.add_argument("article", help="中文文章文本文件路径")
    parser.add_argument("--title", help="文章或卡片主题")
    parser.add_argument("--audience", help="目标读者")
    parser.add_argument("--product", help="产品、方法或案例名称")
    parser.add_argument("--avatar", help="头像或作者图片路径")
    parser.add_argument("--screenshot", action="append", help="产品截图路径，可重复传入")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="输出格式，默认 markdown",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    article = clean_text(Path(args.article).read_text(encoding="utf-8"))
    sentences = split_sentences(article)
    points = pick_points(sentences)
    cards = build_cards(args, points)
    payload = {
        "topic": args.title,
        "audience": args.audience,
        "product": args.product,
        "cards": cards,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(cards, args))


if __name__ == "__main__":
    main()
