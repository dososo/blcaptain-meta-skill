**언어:** [简体中文](README.md) | [English](README.en.md) | [日本語](README.ja.md) | **한국어** | [Português](README.pt.md) | [Русский](README.ru.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Bahasa Indonesia](README.id.md) | [हिन्दी](README.hi.md)

![version](https://img.shields.io/badge/version-v1.0-2563eb)
![skill](https://img.shields.io/badge/skill-blcaptain--meta--skill-7c3aed)
![workflow](https://img.shields.io/badge/workflow-8_steps-059669)
![languages](https://img.shields.io/badge/languages-11-f59e0b)
![status](https://img.shields.io/badge/status-public_release-111827)

# BLCaptain Meta Skill: 재사용 가능한 Skill을 만드는 Skill

버전: v1.0

AI를 자주 쓰기 시작하면 곧 이런 문제를 만나게 됩니다.

같은 일을 계속 설명하고, 같은 기준을 반복해서 알려주고, 같은 워크플로를 매번 다시 말해야 합니다.

BLCaptain Meta Skill은 바로 이 문제를 해결하기 위해 만들어졌습니다.

Claude Skills, Codex Skills, 범용 Agent Skills를 지원하며, 반복적으로 쓰는 경험, SOP, 도구 루틴, 디자인 기준, 창작 프로세스를 설치 가능하고 호출 가능하며 검증 가능하고 반복 개선 가능한 Skill 패키지로 정리합니다.

이것은 더 긴 prompt를 하나 더 쓰는 도구가 아닙니다. “나는 이 일을 이렇게 한다”를 “Agent가 안정적으로 재사용할 수 있는 능력 제품”으로 바꾸는 방법론입니다.

> 반복되고 보존할 가치가 있는 워크플로를 제공하면, Skill로 만들 가치가 있는지 판단하고 실제로 전달 가능한 능력 패키지로 만들도록 안내합니다.

## 어떻게 만들어졌나

이 Skill은 Codex와 Claude Code가 7차례 협업하고 반복 개선한 결과입니다.

개발 과정은 8단계 흐름을 따랐습니다.

```text
조사 → 분석 → 계획 → 개발 → 검증 → 테스트 → 감사 승인 → 요약과 반복
```

| 역할 | 주요 작업 |
| --- | --- |
| Claude Code | 코드 읽기, 요구사항 분해, 아키텍처 계획, 리뷰와 감사 의견 제공 |
| Codex | 코드 수정, 명령 실행, 테스트 수정, 증거 보강, 릴리스 전 검증 |
| 사람 리뷰어 | 방향 판단, 범위 제한, 수정 지속 여부와 공개 여부 결정 |

각 라운드는 리뷰, 수정, 재검증, 재감사를 거쳤습니다. 현재 공개 버전은 실제 시나리오, 실패 사례, 검증 명령, 리뷰 피드백으로 다듬어진 결과입니다.

## 왜 필요한가

AI 워크플로는 보통 세 단계로 발전합니다.

| 단계 | 일반적인 상태 | 문제 |
| --- | --- | --- |
| AI를 사용할 수 있음 | prompt를 쓰고 단발성 작업을 끝낼 수 있음 | 매번 맥락을 다시 설명하고 결과가 불안정함 |
| 방법을 정리할 수 있음 | SOP, 템플릿, prompt, 사례가 있음 | 사람은 이해하지만 Agent가 안정적으로 실행하지 못할 수 있음 |
| 능력을 제품화할 수 있음 | Skill, 리소스, 스크립트, eval, 릴리스 체크가 있음 | 재사용, 검증, 유지보수, 전달이 가능함 |

BLCaptain Meta Skill은 세 번째 단계에 집중합니다. 개인 노하우, 팀 방법, 비즈니스 프로세스, 창작 시스템을 Agent가 호출할 수 있는 재사용 능력으로 만듭니다.

## 해결하는 문제

| 흔한 문제 | 결과 | 이 Skill의 도움 |
| --- | --- | --- |
| Skill을 긴 prompt처럼 다룸 | 글은 많지만 언제 써야 할지 불명확함 | 트리거 경계, 긍정 사례, 부정 사례, 라우팅 설명을 먼저 설계 |
| 모든 것을 `SKILL.md`에 넣음 | 컨텍스트가 무거워져 Agent 성능이 떨어짐 | “얇은入口 + 깊은 리소스” 구조로 분리 |
| 검증이 없음 | 완성돼 보이지만 실제 사용에서 빗나감 | route eval, scenario eval, failure library, 회귀 기록 추가 |
| Skill로 만들지 판단하지 못함 | 단발 작업까지 유지보수 대상이 됨 | 구현 전 Non-Skill gate로 걸러냄 |
| 실패 경험이 없음 | 정상 사례는 되지만 경계에서 무너짐 | gotchas, 반례, 리스크, 수정 전략을 자산화 |
| 공개 전 확신이 없음 | 파일은 있지만 공개 가능성을 판단하기 어려움 | validator, context budget, quick validate, 릴리스 체크리스트 사용 |

즉 “이 prompt 괜찮은 것 같다”에서 “다른 사람이 설치하고 이해하고 호출하고 검증하고 유지할 수 있는 능력 패키지”로 이동하게 해줍니다.

## 누구에게 적합한가

- AI 사용자: 일상 작업, 개인 선호, 글쓰기 방식, 반복 워크플로를 보존합니다.
- 제품 매니저: 요구사항 분석, PRD, 사용자 인터뷰, 경쟁 분석, 리뷰 절차를 안정화합니다.
- 운영 담당자: SOP, 콘텐츠 배포, 캠페인 회고, 커뮤니티 운영, 사용자 접점을 패키지화합니다.
- 개발자 / 엔지니어: 코딩 규율, 테스트, 릴리스, 리뷰, 도구 체인을 실행 가능한 Skill로 만듭니다.
- 테스트 담당자: 긍정, 부정, 경계, 회귀 케이스를 설계합니다.
- 디자이너: 미감 규칙, 브랜드 제약, 레이아웃 체계, 디자인 금기를 실행 기준으로 바꿉니다.
- 크리에이터: 글, 이미지, 영상, 발표자료, 강의, 주제 발굴의 제작 흐름을 재사용합니다.
- 도메인 전문가: 전문 판단, 컨설팅 흐름, 서비스 기준, 비즈니스 경험을 제품화합니다.

## 지원 플랫폼

이 Skill은 Codex 전용도 아니고 Claude Code 전용도 아닙니다.

BLCaptain Meta Skill의 핵심은 표준 Skill 폴더입니다: `SKILL.md` + `references/` + `assets/` + `examples/` + `evals/` + `scripts/`. 로컬 Skill 폴더를 읽을 수 있거나 Agent Skills 방식의 기능을 지원하는 Agent라면 각 플랫폼 방식에 맞게 사용할 수 있습니다.

| 플랫폼 / 도구 | 지원 방식 | 설명 |
| --- | --- | --- |
| Codex / OpenAI Agent Skills | 직접 설치 | `blcaptain-meta-skill/`을 로컬 skills 디렉터리에 복사하고 `$blcaptain-meta-skill`로 호출합니다 |
| Claude Skills | 호환 사용 | 대상 플랫폼이 요구하는 위치에 `blcaptain-meta-skill/`을 가져오거나 배치합니다 |
| Claude Code | 호환 사용 | Claude Code가 이 저장소 또는 Skill 폴더를 읽게 하고 `SKILL.md`와 리소스 디렉터리를 사용합니다 |
| Skill 지원 Agent | 범용 방법론 패키지 | `SKILL.md`와 리소스 폴더를 읽을 수 있으면 실행할 수 있으며, metadata는 플랫폼별 조정이 필요할 수 있습니다 |
| 일반 챗봇 | 직접 설치 비권장 | 폴더, 스크립트, 리소스를 읽을 수 없다면 방법론 참고 자료로만 사용할 수 있습니다 |

공식 문서에서도 Agent Skills는 instructions, metadata, scripts, templates, resources로 Agent 능력을 확장하는 패키지로 설명됩니다. 이 프로젝트도 그 모델을 따르므로 특정 클라이언트에 묶인 prompt가 아닙니다.

## 적용 범위

Skill로 만들기 좋은 작업은 보통 이런 특징을 가집니다.

| 특징 | 의미 |
| --- | --- |
| 자주 반복됨 | 한 번이 아니라 앞으로도 계속 수행함 |
| 명확한 결과물 | 문서, 코드, 이미지, 표, 감사 보고서, 계획으로 전달 가능함 |
| 품질 기준 | 무엇이 좋은지, 나쁜지, 납품 불가인지 설명 가능함 |
| 경계 조건 | 언제 트리거되고 언제 트리거되면 안 되는지 알고 있음 |
| 실패 사례 | AI가 어디서 자주 틀리는지 알고 규칙으로 만들 수 있음 |
| 유지보수 가치 | 절약 시간, 리스크 감소, 품질 향상이 유지 비용보다 큼 |

적합하지 않은 작업:

- 단발성 사실 질문.
- 한 번만 하는 요약, 번역, 수정.
- 안정된 절차가 없는 초기 탐색.
- 검증할 의지가 없는 워크플로.

## 무엇에 쓸 수 있나

| 용도 | 적합한 상황 |
| --- | --- |
| 0부터 Skill 만들기 | 반복 워크플로는 있지만 `SKILL.md`, 리소스, 스크립트, eval로 나누는 법을 모름 |
| 오래된 prompt 업그레이드 | 유용하지만 너무 길고 취약하며 검증 불가능한 prompt가 있음 |
| 기존 Skill 리뷰 | 트리거 경계, 테스트, 리스크, 릴리스 준비를 점검해야 함 |
| 팀 SOP 구축 | 팀 지식을 Agent가 실행할 수 있는 절차로 만들고 싶음 |
| 창작 파이프라인 구축 | 글, 이미지, 영상, 자료, 강의 제작 흐름을 재사용하고 싶음 |
| 공개 준비 | GitHub 공개 전에 구조, 개인정보, 오염물, token, 증거를 확인해야 함 |

## 산출물

| 산출물 | 목적 |
| --- | --- |
| `SKILL.md` | 언제 로드할지, 먼저 무엇을 할지, 어디를 읽을지 알려주는 얇은入口 |
| `references/` | 깊은 방법론, 경계, 절차, 역할 협업, 플랫폼 차이 |
| `assets/templates/` | brief, 설계 사양, eval case, gotcha, 반복 기록 템플릿 |
| `scripts/` | 결정적 검증 스크립트 |
| `evals/` | 라우팅, 시나리오, 실패 라이브러리, forward-test, 회귀 증거 |
| `examples/` | 적용 방법을 보여주는 worked examples |
| `manifest.json` | 버전, 상태, 검증 명령, 증거 파일, 릴리스 거버넌스 |

## 워크플로

```mermaid
flowchart LR
    A["조사<br/>작업・사용자・실패 수집"] --> B["분석<br/>NABC・ROI・경계"]
    B --> C["계획<br/>파일 구조・검증 계획"]
    C --> D["개발<br/>SKILL.md・리소스・스크립트・템플릿"]
    D --> E["검증<br/>구조・링크・컨텍스트・오염물"]
    E --> F["테스트<br/>긍정・부정・근접・회귀"]
    F --> G["감사 승인<br/>리스크・공개・증거"]
    G --> H["요약과 반복<br/>증거와 다음 라운드 기록"]
```

| 단계 | 답하는 질문 |
| --- | --- |
| 조사 | 사용자는 누구인가? 실제 작업은 무엇인가? 성공과 실패 샘플은 무엇인가? |
| 분석 | Skill로 만들 가치가 있는가? 경계, ROI, 대안은 무엇인가? |
| 계획 | 파일 구조, 리소스 계층, 검증 계획, 공개 기준을 어떻게 정할 것인가? |
| 개발 | `SKILL.md`, references, templates, scripts, evals 작성 |
| 검증 | 구조, 링크, 컨텍스트 예산, 개인정보 잔여물, 릴리스 오염물 점검 |
| 테스트 | 긍정, 부정, 근접, 실패 사례로 작동을 증명 |
| 감사 승인 | 공개 가능한가? 어떤 증거가 부족한가? |
| 요약과 반복 | 결론, 잔여 리스크, 다음 개선점을 기록 |

짧게 말하면, 만들 가치가 있는지 판단하고, 경계를 설계하고, 가장 작은 유용한 Skill을 만든 뒤, 증거로 실제 작동을 입증합니다.

## 핵심 메커니즘

### 1. Non-Skill Gate

모든 것을 Skill로 만들 필요는 없습니다. 먼저 다음 중 무엇이 적합한지 판단합니다.

- 단발 답변
- 일반 문서
- 프로젝트 규칙
- 스크립트 / CLI
- 템플릿
- 메모리
- 진짜 Skill

### 2. NABC + ROI

| 차원 | 질문 |
| --- | --- |
| Need | 사용자의 실제 고통은 무엇인가? 반복되는가? |
| Approach | 어떤 절차, 리소스, 스크립트, 제약으로 해결할 것인가? |
| Benefit | 일반 채팅보다 무엇을 절약하고 개선하며 리스크를 줄이는가? |
| Competition | 왜 문서, 스크립트, 템플릿, 프로젝트 규칙, 단발 prompt가 아닌가? |

### 3. 얇은入口, 깊은 리소스

`SKILL.md`는 짧고 신호가 강해야 합니다. 복잡한 방법, 예시, 실패 라이브러리, 템플릿, 스크립트는 필요할 때만 읽는 리소스 폴더에 둡니다.

### 4. 실패 라이브러리 우선

안정적인 Skill은 트리거되면 안 되는 상황, 맞아 보이지만 틀린 출력, 변하기 쉬운 플랫폼 규칙, 반드시 사용자에게 물어야 하는 행동, 권한 또는 안전 리스크가 있는 명령을 기록합니다.

### 5. 증거 기반 공개

릴리스 신뢰도는 route eval, scenario eval, failure library, regression history, validator, context budget, 릴리스 위생 점검에서 나옵니다.

## 사용법

```text
Use $blcaptain-meta-skill 이 반복 워크플로를 공개 가능한 Agent Skill로 만들어 주세요.
```

```text
Use $blcaptain-meta-skill 소셜 미디어 카드 제작 워크플로를 Skill로 만들고 싶습니다.
```

```text
Use $blcaptain-meta-skill 이 기존 Skill을 리뷰하고 eval, gotchas, 릴리스 체크, 거버넌스를 보완해 주세요.
```

## 설치

### 1. 프로젝트 가져오기

Git으로 clone합니다.

```bash
git clone https://github.com/dososo/blcaptain-meta-skill.git
cd blcaptain-meta-skill
```

GitHub에서 `Code -> Download ZIP`을 눌러 내려받고 압축을 풀어도 됩니다.

### 2. Codex / 로컬 Agent

저장소 안의 Skill 패키지 폴더 `blcaptain-meta-skill/`을 skills 디렉터리에 복사합니다.

```bash
mkdir -p ~/.codex/skills
cp -R blcaptain-meta-skill ~/.codex/skills/
```

새 세션에서 사용합니다.

```text
Use $blcaptain-meta-skill 반복 워크플로를 Skill로 만들고 싶습니다.
```

### 3. Claude Skills / Claude Code / 기타 Agent

클라이언트마다 설치 화면은 다를 수 있지만 핵심 단계는 같습니다.

1. 이 저장소의 `blcaptain-meta-skill/` 폴더를 가져오거나 업로드하거나 Agent가 참조하게 합니다.
2. Agent가 `blcaptain-meta-skill/SKILL.md`를 읽을 수 있는지 확인합니다.
3. `references/`, `assets/templates/`, `examples/`, `evals/`, `scripts/` 접근을 확인합니다.
4. 대상 플랫폼의 metadata, 설치 경로, 권한을 다시 확인합니다.
5. 새 세션에서 호출합니다.

```text
Use $blcaptain-meta-skill 반복 워크플로를 Skill로 만들고 싶습니다.
```

플랫폼에 Skill 가져오기 기능이 없다면 이 저장소를 프로젝트 자료로 제공하고, 실행 전에 `blcaptain-meta-skill/SKILL.md`를 먼저 읽도록 요청하세요.

### 4. 설치 후 검증

기본 점검을 실행합니다.

```bash
python3 blcaptain-meta-skill/scripts/validate_meta_skill.py blcaptain-meta-skill
python3 blcaptain-meta-skill/scripts/eval_routes.py blcaptain-meta-skill/evals/route_cases.json
python3 blcaptain-meta-skill/scripts/context_budget.py blcaptain-meta-skill/SKILL.md
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" blcaptain-meta-skill
```

이 명령들이 통과하면 패키지 구조, 라우팅 fixture, 컨텍스트 예산을 사용할 수 있습니다.

## 검증

```bash
python3 blcaptain-meta-skill/scripts/validate_meta_skill.py blcaptain-meta-skill
python3 blcaptain-meta-skill/scripts/eval_routes.py blcaptain-meta-skill/evals/route_cases.json
python3 blcaptain-meta-skill/scripts/context_budget.py blcaptain-meta-skill/SKILL.md
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" blcaptain-meta-skill
```

더 엄격한 token, 시각, 릴리스 위생 검사는 `RELEASE_CHECKLIST.md`를 실행하세요.

## 저장소 구조

```text
.
├── README.md
├── README.ko.md
├── RELEASE_CHECKLIST.md
├── docs/
├── blcaptain-meta-skill/
└── third-round-forward-test/
```

## 대표 시나리오

| 시나리오 | 이렇게 말할 수 있습니다 |
| --- | --- |
| 0부터 새 Skill | “반복 워크플로가 있습니다. Skill로 만들 가치가 있는지 판단하고 구조를 설계해 주세요.” |
| 오래된 prompt 개선 | “이 prompt를 설치 가능한 Skill로 업그레이드해 주세요.” |
| 기존 Skill 리뷰 | “routing, eval, gotchas, 릴리스 오염물, 거버넌스 누락을 확인해 주세요.” |
| 팀 SOP | “이 운영 SOP를 Agent가 실행하고 검증하고 반복 개선할 수 있는 Skill로 만들어 주세요.” |
| 창작 흐름 | “콘텐츠 제작 프로세스를 템플릿, 반례, 플랫폼 체크가 있는 Skill로 만들어 주세요.” |
| 공개 준비 | “릴리스 체크리스트를 실행하고 GitHub 공개 가능 여부를 알려 주세요.” |

## FAQ

### 이것은 prompt인가요?

아닙니다. prompt도 포함하지만 핵심은入口, 리소스, 템플릿, 스크립트, 검증, 증거, 릴리스 거버넌스를 포함한 능력 패키지입니다.

### 비기술 사용자도 쓸 수 있나요?

가능합니다. 워크플로와 목표를 설명하면 Agent가 이 Skill의 흐름에 따라 분해를 도와줍니다. GitHub 공개 시에는 검증 스크립트에 익숙한 사람의 확인을 권장합니다.

### 어떤 작업이 가장 적합한가요?

반복되고, 가치가 높고, 절차가 안정적이며, 실수하기 쉽고, 검증 가능하고, 재사용 가능한 작업입니다.

### 어떤 작업은 적합하지 않나요?

단발 설명, 간단한 요약, 임시 브레인스토밍, 1회 번역, 안정되지 않은 탐색입니다.

### 공개까지 대신할 수 있나요?

구조, 스크립트, 검증, 공개 준비는 도울 수 있습니다. 개인정보, 실제 자료, 저장소 문구, 공개 포지셔닝, 유지보수 책임은 사람이 결정해야 합니다.

## 작성자

爆裂队长NEXT

15yr PM. Fired myself. Hired 10 AIs. Turns out managing AIs is harder than managing humans.

AI Agents BLTeam 실전 기록. 실제 운영에서 얻은 생산급 인사이트와 1차 신호를 공유합니다.

X/Twitter: [@thinkszyg](https://x.com/thinkszyg)

이메일: blteam2026@outlook.com

## License

개인 사용과 오픈소스 프로젝트에서는 무료로 사용할 수 있습니다. 폐쇄형 상업적 사용에는 상업적 허가가 필요합니다.

자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
