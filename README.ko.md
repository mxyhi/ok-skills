# OK Skills: Codex, Claude Code, Cursor, OpenClaw 등을 위한 AI 코딩 에이전트 스킬 모음

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | 한국어 | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex, Claude Code, Cursor, OpenClaw, Trae 및 기타 `SKILL.md` 호환 도구를 위한 큐레이션된 AI 코딩 에이전트 스킬과 `CLAUDE.md` / `AGENTS.md` 플레이북 저장소입니다.

이 저장소에는 현재 **재사용 가능한 스킬 32개**가 포함되어 있으며, 모두 루트 레벨 스킬 디렉터리로 이 저장소에서 직접 관리됩니다. `~/.agents/skills/ok-skills`에 clone 하면 되고, 내부 디렉터리 구조는 이미 `AGENTS.md` 기반 워크플로가 기대하는 형태와 맞춰져 있으며, [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md)는 Claude Code용 agent playbook을 제공합니다.

**Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, 재사용 가능한 **CLAUDE.md / AGENTS.md** 플레이북, 바로 적용할 수 있는 **SKILL.md** 예제를 찾고 있다면 이 저장소는 검색성과 즉시 사용성을 모두 고려해 정리되어 있습니다.

**주요 사용 장면:** 최신 문서 조회, 브라우저 자동화, 프롬프트 엔지니어링, 복잡한 작업 계획, 프런트엔드 디자인, 그리고 PDF / Word / PPTX / XLSX 문서 작업.

## 이 저장소가 맞는 사람

- Codex, Claude Code, Cursor, OpenClaw, Trae 또는 다른 AI 코딩 에이전트를 사용하며, 일회성 프롬프트 대신 재사용 가능한 스킬을 원한다.
- `CLAUDE.md` / `AGENTS.md` / `SKILL.md` 기반 워크플로를 운영하며, 프로젝트 간에 이식 가능한 지침을 원한다.
- 문서 조회, 브라우저 자동화, 계획 수립, 프롬프트 엔지니어링, 프런트엔드 디자인, PDF, Office 문서, 슬라이드, 스프레드시트용 검증된 스킬이 필요하다.

## 먼저 설치할 추천 스킬

처음 몇 개만 설치할 계획이라면 아래부터 시작하는 편이 좋습니다.

- [planning-with-files](planning-with-files/SKILL.md): 복잡한 작업, 조사, 장기 실행 업무를 위한 파일 기반 계획 수립.
- [find-docs](find-docs/SKILL.md): 최신 라이브러리 문서, API 레퍼런스, Context7 예제 조회.
- [agent-browser](agent-browser/SKILL.md): 스크린샷, 폼 입력, 스크래핑, 웹 QA를 위한 브라우저 자동화.

## 1분 빠른 시작

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 이후 저장소 경로는 `~/.agents/skills/ok-skills`가 되며, 내부 디렉터리는 이미 기대 레이아웃을 따릅니다.

```text
~/.agents/skills/ok-skills/
  CLAUDE_AGENTS.md
  planning-with-files/
    SKILL.md
  find-docs/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Claude Code 또는 Codex의 전역 지침은 [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md)에서 시작해 Claude Code의 `CLAUDE.md` 또는 Codex의 `AGENTS.md`로 복사하거나 병합할 수 있습니다. Chinese-first, KISS, 최신 문서/소스 확인, multi-agent 우선, `caveman` / `planning-with-files` / `karpathy-guidelines` 기본 활성화, 엄격한 TypeScript 규칙, context-mode 라우팅을 담은 agent playbook입니다. 재사용하기 전에 `语言要求` 섹션을 프로젝트에 맞게 수정하세요. `其他注意项` 섹션은 프로젝트 로컬 설정이므로 필요에 따라 수정할 수 있습니다.

그리고 `AGENTS.md`에 아래처럼 간단한 트리거 규칙을 추가하거나, 같은 skill 트리거를 `CLAUDE.md` / `AGENTS.md`에 병합하면 됩니다.

```md
## Skills

- planning-with-files: 복잡한 작업, 조사, 또는 5회 이상의 도구 호출이 예상되는 작업에 사용.
- find-docs: 최신 라이브러리 문서, API 레퍼런스, Context7 예제가 필요할 때 사용.
- agent-browser: 브라우저 자동화, 스크린샷, 스크래핑, 웹 테스트, 폼 입력이 필요할 때 사용.
```

그다음 자연스럽게 요청하면 됩니다.

- `이 모듈을 리팩터링하기 전에 planning-with-files를 사용해줘.`
- `이 SDK의 최신 문서를 find-docs로 찾아줘.`
- `이 UI 버그를 agent-browser로 재현해줘.`

## 사용 사례별 스킬 탐색

### 조사 및 문서

- [find-docs](find-docs/SKILL.md): 최신 문서 조회에 집중한 Context7 CLI 워크플로.
- [exa-search](exa-search/SKILL.md): Exa 도구를 활용한 웹, 코드, 회사 조사.
- [get-api-docs](get-api-docs/SKILL.md): 코드를 작성하기 전에 최신 서드파티 API 및 SDK 문서를 가져옴.
- [find-skills](find-skills/SKILL.md): 사용자가 특정 기능을 원할 때 기존 스킬을 찾아줌.

### 계획 및 프롬프트

- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, `progress.md`를 사용하는 지속형 마크다운 계획 수립.
- [autoresearch](autoresearch/SKILL.md): 명확한 목표, 지표, 검증 루프, keep/discard 게이트 기반의 자율 목표 지향 반복.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): 어려운 bug와 performance regression을 위한 엄격한 진단 루프.
- [grill-with-docs](grill-with-docs/SKILL.md): domain language, `CONTEXT.md`, ADR 기준으로 plan을 검증하고 docs를 inline 업데이트.
- [grilling](grilling/SKILL.md): 직접 grill session과 `grill-with-docs`에서 쓰는 reusable one-question-at-a-time interview loop.
- [handoff](handoff/SKILL.md): 현재 작업을 새 agent가 이어받을 수 있는 redacted handoff document로 압축.
- [teach](teach/SKILL.md): mission, resources, lessons, learning records를 쓰는 stateful teaching workspace 운영.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): locality, leverage, testability, AI navigation을 높이는 architecture deepening 기회를 찾음.
- [prototype](prototype/SKILL.md): throwaway logic 또는 UI prototype으로 design question에 빠르게 답함.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): 과도한 복잡성, 숨은 가정, 검증 불가능한 변경을 줄이는 코딩 행동 지침.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): 테스트의 `as` 타입 단언을 `@total-typescript/shoehorn`으로 마이그레이션.
- [tdd](tdd/SKILL.md): 기능, 버그 수정, 리팩터링, 동작 변경 전에 test-first red-green-refactor 적용.
- [systematic-debugging](systematic-debugging/SKILL.md): 버그, 테스트 실패, 예상치 못한 동작에서 수정안을 내기 전에 근본 원인을 체계적으로 조사.

### 자동화 및 QA

- [agent-browser](agent-browser/SKILL.md): 탐색, 폼, 스크린샷, 스크래핑을 위한 브라우저 자동화.
- [kimi-webbridge](kimi-webbridge/SKILL.md): 로컬 데몬으로 사용자의 실제 브라우저를 제어해 탐색, 폼 입력, 스크린샷, 페이지 읽기, 로그인 세션을 처리합니다.
- [browser-trace](browser-trace/SKILL.md): 브라우저 자동화 실행의 CDP trace, 스크린샷, DOM dump를 캡처하고 페이지별로 나눠 디버깅합니다.
- [opencli](opencli/opencli-usage/SKILL.md): 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다룹니다.
- [xquik-twitter](xquik-twitter/SKILL.md): Xquik API로 X/Twitter 데이터를 검색하고 승인된 계정 작업을 실행.

### 프런트엔드 및 디자인

- [ai-elements](ai-elements/SKILL.md): `ai-elements` 라이브러리를 위한 AI 채팅 UI 컴포넌트 제작.
- [huashu-design](huashu-design/SKILL.md): 고충실도 HTML 프로토타입, 인터랙티브 데모, 슬라이드 덱, motion design, 디자인 variants, 영상 export, 디자인 critique를 만든다.
- [better-icons](better-icons/SKILL.md): CLI 또는 MCP로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다.

### 유틸리티 및 문서 작업

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK(.NET) 기반의 전문 DOCX 생성, 편집, 서식화.
- [minimax-pdf](minimax-pdf/SKILL.md): 토큰 기반 디자인 시스템으로 PDF를 생성, 입력, 재구성.
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS, XML 워크플로, markitdown으로 PowerPoint를 생성, 편집, 읽기.
- [huashu-design](huashu-design/SKILL.md): HTML deck, editable PPTX, MP4/GIF motion pieces, narrated design videos를 만든다.
- [minimax-xlsx](minimax-xlsx/SKILL.md): 손실을 최소화한 XML 워크플로로 Excel/스프레드시트를 열고, 생성하고, 분석·편집·검증.

## 벤더링된 스킬 팩

[`planning-with-files/`](planning-with-files/)는 [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)를 upstream baseline으로 사용합니다. 이 저장소는 해당 upstream directory를 local skill의 canonical baseline으로 사용합니다. 로컬 차이는 `skills-ref` 호환 `SKILL.md` frontmatter와 설치 위치에 독립적인 상대 script path 문서로 제한됩니다.

## 공통 전제 조건

- 일부 스킬은 `gh`가 설치되어 있고 로그인되어 있다고 가정합니다.
- 브라우저 관련 스킬은 Chrome/CDP를 사용할 수 있는 환경이 필요할 수 있습니다.
- 서드파티 문서 조회 스킬은 외부 CLI 또는 MCP 도구에 의존할 수 있으므로, 자세한 내용은 각 `SKILL.md`를 확인하세요.

## 전체 스킬 인덱스

벤더링되거나 외부에서 가져온 스킬은 `Source URL`이 정식 업스트림을 가리키며, 그렇지 않은 경우 이 저장소의 스킬 디렉터리를 가리킵니다.

### 루트 레벨 스킬

| Skill                                                               | 설명                                                                                                                                             | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | AI 에이전트를 위한 브라우저 자동화 CLI: 탐색, 폼 입력, 스크린샷, 추출, 웹 테스트.                                                                | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | 조합형 패턴과 shadcn/ui 관례를 따라 ai-elements 라이브러리용 AI 채팅 UI 컴포넌트를 생성.                                                         | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | 수정, 검증, keep/discard, 반복 워크플로를 위한 자율 목표 지향 반복 엔진.                                                                                 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | CLI 또는 MCP 도구로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다.                                                   | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | 로컬 데몬으로 사용자의 실제 브라우저를 제어해 탐색, 폼 입력, 스크린샷, 페이지 읽기, 로그인 세션을 처리합니다.                                    | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | 브라우저 자동화 디버깅용 CDP trace, 스크린샷, DOM dump를 캡처합니다.                                                                               | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | 기술 정확성은 유지한 채 원시인 말투의 초압축 응답으로 토큰 사용량을 줄입니다.                                                                    | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | 어려운 bug와 performance regression을 위한 엄격한 진단 루프.                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Context7 CLI를 사용해 최신 문서, API 레퍼런스, 코드 예제를 조회.                                                                                 | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK(.NET) 기반의 전문 DOCX 생성, 편집, 서식화. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa를 사용해 웹, 코드, 회사 정보를 조사.                                                                                                         | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | 사용자가 특정 기능을 필요로 할 때 기존 스킬을 탐색.                                                                                              | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | 고충실도 HTML 프로토타입, 인터랙티브 데모, 슬라이드 덱, motion design, 디자인 variants, 영상 export, 디자인 critique를 만든다.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | 코드를 작성하기 전에 최신 서드파티 API 또는 SDK 문서를 가져옴.                                                                                   | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | domain language, `CONTEXT.md`, ADR 기준으로 plan을 stress-test하고 docs를 inline 업데이트.                                                          | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | 직접 grill session과 `grill-with-docs`에서 쓰는 reusable one-question-at-a-time interview loop.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [handoff](handoff/SKILL.md) | 현재 대화를 다른 agent가 이어받을 수 있는 redacted handoff document로 압축합니다. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) |
| [teach](teach/SKILL.md) | mission, resources, lessons, learning records를 통해 workspace 안에서 skill이나 concept을 가르칩니다. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | locality, leverage, testability, AI navigation을 높이는 architecture deepening 기회를 찾음.                                                      | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [prototype](prototype/SKILL.md) | throwaway logic 또는 UI prototype을 만들어 design question에 빠르게 답합니다. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | 과도한 복잡성, 숨은 가정, 검증 불가능한 변경을 줄이는 코딩 행동 지침.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | 테스트 파일의 `as` 타입 단언을 `@total-typescript/shoehorn`으로 마이그레이션.                                                                    | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다루는 스킬입니다.                                               | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Xquik API로 X/Twitter 데이터를 검색하고 승인된 계정 작업을 실행.                                                                                                      | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | 토큰 기반 디자인 시스템으로 PDF를 생성, 입력, 재구성. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`, `findings.md`, `progress.md`를 활용해 복잡한 작업을 파일 기반으로 계획.                                                          | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS, XML 워크플로, markitdown으로 PowerPoint를 생성, 편집, 읽기. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | 기능, 버그 수정, 리팩터링, 동작 변경 전에 사용. public interface 기반 integration-style test를 우선한다.                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | 버그, 테스트 실패, 예상치 못한 동작을 만났을 때 수정안을 내기 전에 사용.                                                                     | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 손실을 최소화한 XML 워크플로로 Excel/스프레드시트를 열고, 생성하고, 분석·편집·검증. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## 기여하기

새 스킬 추가나 기존 스킬 개선 기여를 환영합니다.

1. 트리거 조건은 명확하고 검증 가능해야 합니다.
2. 예시는 간결하고 실행 중심으로 유지하세요.
3. 외부 도구에 의존하는 스킬은 해당 의존성을 `SKILL.md`에 문서화하세요.
4. 스킬을 추가하거나 이름을 바꿀 때는 `README.md`와 `README.zh-CN.md`를 먼저 업데이트하고, 공개된 스킬 인덱스가 바뀌면 다른 번역 README도 함께 갱신하세요.

## 라이선스

이 저장소는 [LICENSE](LICENSE) 하에 배포됩니다.
