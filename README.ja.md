**言語:** [简体中文](README.md) | [English](README.en.md) | **日本語** | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Bahasa Indonesia](README.id.md) | [हिन्दी](README.hi.md)

![version](https://img.shields.io/badge/version-v1.0-2563eb)
![skill](https://img.shields.io/badge/skill-blcaptain--meta--skill-7c3aed)
![workflow](https://img.shields.io/badge/workflow-8_steps-059669)
![languages](https://img.shields.io/badge/languages-11-f59e0b)
![status](https://img.shields.io/badge/status-public_release-111827)

# BLCaptain Meta Skill：再利用できる Skill を作るための Skill

バージョン：v1.0

AI を日常的に使い始めると、かなり現実的な問題にぶつかります。

同じ種類の仕事を何度も説明する。同じ基準を毎回伝える。同じワークフローを、次の会話ではまた最初から説明し直す。

BLCaptain Meta Skill は、その問題を解決するための Skill です。

Claude Skills、Codex Skills、汎用 Agent Skills に対応し、繰り返し使う経験、SOP、ツール手順、デザイン基準、制作プロセスを、インストール可能・呼び出し可能・検証可能・継続改善可能な Skill パッケージに整理します。

これは「長い prompt」をもう一つ作るものではありません。「自分ならこう進める」という暗黙知を、Agent が安定して再利用できる能力プロダクトに変えるための方法論です。

> 繰り返し発生し、残す価値のあるワークフローを渡すと、それを Skill 化すべきか判断し、実際に納品可能な能力パッケージへ導きます。

## どこから生まれたか

この Skill は、Codex と Claude Code が 7 ラウンド協調し、反復改善した結果です。

開発は次の 8 ステップに厳密に従いました。

```text
調査 → 分析 → 計画 → 開発 → 検証 → テスト → 監査受入 → 要約と反復
```

| 役割 | 主な作業 |
| --- | --- |
| Claude Code | コード読解、要求分解、アーキテクチャ計画、レビューと監査意見 |
| Codex | コード修正、コマンド実行、テスト修正、証拠追加、リリース前検証 |
| 人間レビュー | 方向付け、境界設定、修正継続と公開判断 |

各ラウンドでレビュー、修正、再検証、再監査を行いました。現在の公開版は、実際の場面、失敗例、検証コマンド、レビュー意見によって磨かれたものです。

## なぜ必要か

AI ワークフローは通常、3 つの段階を進みます。

| 段階 | よくある状態 | 問題 |
| --- | --- | --- |
| AI を使える | prompt を書き、単発タスクを終えられる | 毎回文脈を説明し直し、結果が不安定 |
| 方法を残せる | SOP、テンプレート、prompt、事例がある | 人は理解できても、Agent が安定して実行できるとは限らない |
| 能力をプロダクト化できる | Skill、リソース、スクリプト、eval、リリースチェックがある | 再利用、検証、保守、納品ができる |

BLCaptain Meta Skill は 3 段階目に集中します。個人の知見、チームの方法、業務プロセス、制作システムを Agent が呼び出せる再利用可能な能力に変えます。

## 解決する問題

| よくある問題 | 結果 | この Skill の支援 |
| --- | --- | --- |
| Skill を長い prompt として扱う | 文章は多いが、いつ使うかが曖昧 | 先にトリガー境界、正例、反例、ルーティング説明を設計 |
| すべてを `SKILL.md` に詰め込む | コンテキストが重くなり Agent が鈍る | 「薄い入口 + 厚いリソース」構造に分解 |
| 検証がない | 完成して見えるが実運用で崩れる | route eval、scenario eval、failure library、回帰記録を追加 |
| Skill 化すべきか分からない | 単発タスクまで保守対象になる | 実装前に Non-Skill gate で判断 |
| 失敗知がない | 正常系だけ動き、境界で壊れる | gotchas、反例、リスク、修正策を資産化 |
| 公開前に不安 | ファイルはあるが信頼できない | validator、context budget、quick validate、公開チェックリストで確認 |

つまり、「この prompt は良さそう」から「他人がインストールし、理解し、呼び出し、検証し、保守できる能力パッケージ」へ進むための支援です。

## 対象ユーザー

- AI ユーザー：日常タスク、好み、文章スタイル、作業手順を残す。
- プロダクトマネージャー：要求分析、PRD、ユーザーインタビュー、競合分析、レビュー手順を安定化する。
- 運用担当：SOP、配信、キャンペーン振り返り、コミュニティ運営、ユーザー接点をパッケージ化する。
- 開発者 / エンジニア：コーディング規律、テスト、リリース、レビュー、ツールチェーンを実行可能にする。
- テスター：正例、反例、境界例、回帰ケースを設計する。
- デザイナー：審美ルール、ブランド制約、レイアウト体系、避けるべき表現を実行基準に変える。
- クリエイター：記事、画像、動画、資料、講座、企画の制作フローを再利用可能にする。
- 業界専門家：専門判断、相談プロセス、サービス基準、業務経験をプロダクト化する。

## 適用範囲

Skill 化に向くタスクには、通常次の特徴があります。

| 特徴 | 意味 |
| --- | --- |
| 高頻度で繰り返す | 一度きりではなく、今後も行う |
| 明確な成果物 | 文書、コード、画像、表、監査報告、計画などで納品できる |
| 品質基準がある | 良い、悪い、出荷不可を説明できる |
| 境界がある | いつ発火し、いつ発火すべきでないか分かる |
| 失敗例がある | AI が間違えやすい点をルール化できる |
| 保守価値がある | 節約時間、低減リスク、品質向上が保守コストを上回る |

向かないタスク：

- 単発の事実確認。
- 一回だけの要約、翻訳、書き換え。
- 安定した手順のない初期探索。
- 検証する意思のないワークフロー。

## できること

| 用途 | 適した場面 |
| --- | --- |
| 0 から Skill を作る | ワークフローはあるが `SKILL.md`、リソース、スクリプト、eval の分け方が分からない |
| 古い prompt を強化する | 便利だが長すぎる、壊れやすい、検証できない prompt がある |
| 既存 Skill をレビューする | トリガー境界、テスト、リスク、公開準備を確認したい |
| チーム SOP を作る | チーム知を Agent が実行できるプロセスにしたい |
| 制作パイプラインを作る | 記事、画像、動画、資料、講座の制作手順を再利用したい |
| 公開準備をする | GitHub 公開前に構造、プライバシー、汚染物、token、証拠を確認したい |

## 生成されるもの

| 成果物 | 用途 |
| --- | --- |
| `SKILL.md` | 読み込み条件、最初の行動、参照先を示す薄い入口 |
| `references/` | 深い方法、境界、手順、役割連携、プラットフォーム差異 |
| `assets/templates/` | brief、仕様、eval case、gotcha、反復記録のテンプレート |
| `scripts/` | 決定的な検証スクリプト |
| `evals/` | ルーティング、シナリオ、失敗ライブラリ、forward-test、回帰証拠 |
| `examples/` | 実装例と適用例 |
| `manifest.json` | バージョン、状態、検証コマンド、証拠ファイル、公開管理 |

## ワークフロー

```mermaid
flowchart LR
    A["調査<br/>タスク・ユーザー・失敗を収集"] --> B["分析<br/>NABC・ROI・境界"]
    B --> C["計画<br/>ファイル構造・検証計画"]
    C --> D["開発<br/>SKILL.md・リソース・スクリプト・テンプレート"]
    D --> E["検証<br/>構造・リンク・コンテキスト・汚染物"]
    E --> F["テスト<br/>正例・反例・近接例・回帰"]
    F --> G["監査受入<br/>リスク・公開・証拠"]
    G --> H["要約と反復<br/>証拠と次回を記録"]
```

| ステップ | 答える問い |
| --- | --- |
| 調査 | ユーザーは誰か。実タスクは何か。成功例と失敗例は何か。 |
| 分析 | Skill 化する価値はあるか。境界、ROI、代替案は何か。 |
| 計画 | ファイル構造、リソース層、検証計画、公開基準をどうするか。 |
| 開発 | `SKILL.md`、references、templates、scripts、evals を作る。 |
| 検証 | 構造、リンク、コンテキスト予算、私的情報残り、公開汚染物を確認する。 |
| テスト | 正例、反例、近接例、失敗例で動作を証明する。 |
| 監査受入 | 公開できるか、足りない証拠は何かを判断する。 |
| 要約と反復 | 結論、残リスク、次の改善を記録する。 |

短く言えば、作る価値を判断し、境界を設計し、最小の有用な Skill を作り、証拠で動作を証明します。

## 主要メカニズム

### 1. Non-Skill Gate

すべてを Skill にする必要はありません。まず次のどれが適切かを判断します。

- 単発回答
- 通常ドキュメント
- プロジェクトルール
- スクリプト / CLI
- テンプレート
- メモリ
- 本当の Skill

### 2. NABC + ROI

| 次元 | 問い |
| --- | --- |
| Need | ユーザーの本当の痛みは何か。繰り返すか。 |
| Approach | どの手順、リソース、スクリプト、制約で解くか。 |
| Benefit | 通常チャットより何を節約し、改善し、リスク低減するか。 |
| Competition | なぜ文書、スクリプト、テンプレート、プロジェクトルール、単発 prompt ではないのか。 |

### 3. 薄い入口、厚いリソース

`SKILL.md` は短く高信号に保ちます。複雑な方法、例、失敗ライブラリ、テンプレート、スクリプトは必要時だけ読み込むリソースに置きます。

### 4. 失敗ライブラリ優先

安定した Skill は、発火すべきでない場面、正しそうに見えて誤りの出力、変わりやすいプラットフォーム規則、必ずユーザーに確認すべき動作、権限や安全リスクのあるコマンドを記録します。

### 5. 証拠駆動の公開

信頼できる公開は、route eval、scenario eval、failure library、regression history、validator、context budget、公開衛生チェックから生まれます。

## 使い方

```text
Use $blcaptain-meta-skill この繰り返しワークフローを公開可能な Agent Skill にしてください。
```

```text
Use $blcaptain-meta-skill 社媒カード制作フローを Skill にしたいです。
```

```text
Use $blcaptain-meta-skill 既存 Skill をレビューし、eval、gotchas、公開チェック、ガバナンスを補ってください。
```

## インストール

### Codex / ローカル Agent

`blcaptain-meta-skill/` を skills ディレクトリにコピーします。

```bash
mkdir -p ~/.codex/skills
cp -R blcaptain-meta-skill ~/.codex/skills/
```

新しいセッションで実行します。

```text
Use $blcaptain-meta-skill 繰り返しワークフローを Skill にしたいです。
```

### Claude Skills / その他の Agent

1. Agent が `blcaptain-meta-skill/SKILL.md` を読めるようにします。
2. `references/`、`assets/templates/`、`examples/`、`evals/`、`scripts/` にアクセスできることを確認します。
3. 対象プラットフォームのインストール先と metadata ルールを再確認します。
4. 公開前に検証コマンドを実行します。

## 検証

```bash
python3 blcaptain-meta-skill/scripts/validate_meta_skill.py blcaptain-meta-skill
python3 blcaptain-meta-skill/scripts/eval_routes.py blcaptain-meta-skill/evals/route_cases.json
python3 blcaptain-meta-skill/scripts/context_budget.py blcaptain-meta-skill/SKILL.md
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" blcaptain-meta-skill
```

より厳密な token、視覚、公開衛生チェックは `RELEASE_CHECKLIST.md` を実行してください。

## リポジトリ構造

```text
.
├── README.md
├── README.ja.md
├── RELEASE_CHECKLIST.md
├── docs/
├── blcaptain-meta-skill/
└── third-round-forward-test/
```

## よくある場面

| 場面 | こう依頼できます |
| --- | --- |
| 0 から新規 Skill | “繰り返しワークフローがあります。Skill 化すべきか判断し、構造を設計してください。” |
| 古い prompt 改造 | “この prompt をインストール可能な Skill にしてください。” |
| 既存 Skill レビュー | “routing、eval、gotchas、公開汚染物、ガバナンス不足を確認してください。” |
| チーム SOP | “この運用 SOP を Agent が実行・検証・改善できる Skill にしてください。” |
| 制作フロー | “私のコンテンツ制作プロセスをテンプレート、反例、プラットフォームチェック付きの Skill にしてください。” |
| 公開準備 | “公開チェックリストを走らせ、GitHub 公開可能か教えてください。” |

## FAQ

### これは prompt ですか？

いいえ。prompt も含みますが、中心は入口、リソース、テンプレート、スクリプト、検証、証拠、公開管理を含む能力パッケージです。

### 技術者でなくても使えますか？

使えます。ワークフローと目的を説明すれば、Agent がこの Skill の流れに沿って分解できます。GitHub 公開時は、検証スクリプトに慣れた人の確認を推奨します。

### 向いているタスクは？

繰り返し発生し、価値が高く、手順が安定し、間違いやすく、検証可能で、再利用できるタスクです。

### 向かないタスクは？

単発説明、簡単な要約、一時的なブレスト、一回だけの翻訳、安定していない探索です。

### 公開まで代行できますか？

構造、スクリプト、検証、公開準備は支援できます。最終的なプライバシー、実素材、リポジトリ文言、公開方針、保守責任は人間が判断します。

## 作者

爆裂队长NEXT

15yr PM. Fired myself. Hired 10 AIs. Turns out managing AIs is harder than managing humans.

AI Agents BLTeam の実戦記録。現場で使った生の知見と一次信号を継続共有します。

X/Twitter: [@thinkszyg](https://x.com/thinkszyg)

メール: blteam2026@outlook.com

## License

個人利用およびオープンソースプロジェクトでは無料で利用できます。クローズドソースの商用利用には商用許可が必要です。

詳細は [LICENSE](LICENSE) を参照してください。
