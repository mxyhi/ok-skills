# OK Skills: Codex, Claude Code, Cursor, OpenClaw 등을 위한 AI 코딩 에이전트 스킬 모음

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | 한국어 | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex, Claude Code, Cursor, OpenClaw, Trae 및 기타 `SKILL.md` 호환 도구를 위한 큐레이션된 AI 코딩 에이전트 스킬과 `AGENTS.md` 플레이북 저장소입니다.

이 저장소에는 현재 **재사용 가능한 스킬 37개**가 포함되어 있습니다. 이 중 **29개는 루트 레벨 스킬**로 직접 관리되며, **8개의 벤더링된 GSAP 애니메이션 스킬**은 [`gsap-skills/`](gsap-skills/) 아래에 포함되어 있습니다. `~/.agents/skills/ok-skills`에 clone 하면 되고, 내부 디렉터리 구조는 이미 `AGENTS.md` 기반 워크플로가 기대하는 형태와 맞춰져 있습니다.

**Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, 재사용 가능한 **AGENTS.md** 플레이북, 바로 적용할 수 있는 **SKILL.md** 예제를 찾고 있다면 이 저장소는 검색성과 즉시 사용성을 모두 고려해 정리되어 있습니다.

**주요 사용 장면:** 최신 문서 조회, 브라우저 자동화, GitHub Actions 장애 분석, 프롬프트 엔지니어링, 복잡한 작업 계획, 프런트엔드 디자인, 그리고 PDF / Word / PPTX / XLSX 문서 작업.

## 이 저장소가 맞는 사람

- Codex, Claude Code, Cursor, OpenClaw, Trae 또는 다른 AI 코딩 에이전트를 사용하며, 일회성 프롬프트 대신 재사용 가능한 스킬을 원한다.
- `AGENTS.md` / `SKILL.md` 기반 워크플로를 운영하며, 프로젝트 간에 이식 가능한 지침을 원한다.
- 문서 조회, 브라우저 자동화, GitHub 워크플로, 계획 수립, 프롬프트 엔지니어링, 프런트엔드 디자인, PDF, Office 문서, 슬라이드, 스프레드시트용 검증된 스킬이 필요하다.

## 먼저 설치할 추천 스킬

처음 몇 개만 설치할 계획이라면 아래부터 시작하는 편이 좋습니다.

- [brainstorming](brainstorming/SKILL.md): 구현에 들어가기 전에 아이디어, 요구사항, 설계를 정리합니다.
- [planning-with-files](planning-with-files/SKILL.md): 복잡한 작업, 조사, 장기 실행 업무를 위한 파일 기반 계획 수립.
- [find-docs](find-docs/SKILL.md): 최신 라이브러리 문서, API 레퍼런스, Context7 예제 조회.
- [agent-browser](agent-browser/SKILL.md): 스크린샷, 폼 입력, 스크래핑, 웹 QA를 위한 브라우저 자동화.
- [gh-fix-ci](gh-fix-ci/SKILL.md): 실패한 GitHub Actions 체크를 읽고 수정 계획으로 정리.

## 1분 빠른 시작

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 이후 저장소 경로는 `~/.agents/skills/ok-skills`가 되며, 내부 디렉터리는 이미 기대 레이아웃을 따릅니다.

```text
~/.agents/skills/ok-skills/
  planning-with-files/
    SKILL.md
  find-docs/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

그리고 `AGENTS.md`에 아래처럼 간단한 트리거 규칙을 추가하면 됩니다.

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

- [brainstorming](brainstorming/SKILL.md): 구현에 들어가기 전에 아이디어, 요구사항, 설계를 정리합니다.
- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, `progress.md`를 사용하는 지속형 마크다운 계획 수립.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): locality, leverage, testability, AI navigation을 높이는 architecture deepening 기회를 찾음.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): 테스트의 `as` 타입 단언을 `@total-typescript/shoehorn`으로 마이그레이션.
- [tdd](tdd/SKILL.md): 기능, 버그 수정, 리팩터링, 동작 변경 전에 test-first red-green-refactor 적용.
- [systematic-debugging](systematic-debugging/SKILL.md): 버그, 테스트 실패, 예상치 못한 동작에서 수정안을 내기 전에 근본 원인을 체계적으로 조사.

### GitHub 워크플로

- [gh-address-comments](gh-address-comments/SKILL.md): 현재 PR의 리뷰/이슈 코멘트를 `gh`로 처리.
- [gh-fix-ci](gh-fix-ci/SKILL.md): 실패한 GitHub Actions 체크를 분석하고 로그를 요약하며 수정 계획을 세움.
- [yeet](yeet/SKILL.md): 사용자가 명시적으로 요청한 경우에만 `gh` 기반으로 stage, commit, push, PR 생성까지 한 번에 처리.

### 자동화 및 QA

- [agent-browser](agent-browser/SKILL.md): 탐색, 폼, 스크린샷, 스크래핑을 위한 브라우저 자동화.
- [browser-use](browser-use/SKILL.md): 탐색, 페이지 상태 확인, 폼 입력, 스크린샷, 정보 추출을 위한 지속형 브라우저 자동화 CLI.
- [browser-trace](browser-trace/SKILL.md): 브라우저 자동화 실행의 CDP trace, 스크린샷, DOM dump를 캡처하고 페이지별로 나눠 디버깅합니다.
- [opencli](opencli/opencli-usage/SKILL.md): 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다룹니다.

- [dogfood](dogfood/SKILL.md): 재현 가능한 증거를 남기는 구조화된 탐색 테스트.
- [electron](electron/SKILL.md): Chrome DevTools Protocol 기반으로 Electron 데스크톱 앱 자동화.

`dogfood/`와 `electron/`은 여전히 `vercel-labs/agent-browser`에서 vendored 되지만, upstream은 commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0`에서 이들을 `skills/`에서 `skill-data/`로 옮겨 installer discovery가 bootstrap skill `agent-browser`만 노출하도록 바꿨습니다. 이 저장소는 이 specialized skills가 여전히 upstream에서 유지되고 직접 유용하기 때문에 top-level 디렉터리로 계속 보존합니다.

### 프런트엔드 및 디자인

- [ai-elements](ai-elements/SKILL.md): `ai-elements` 라이브러리를 위한 AI 채팅 UI 컴포넌트 제작.
- [frontend-skill](frontend-skill/SKILL.md): 시각적으로 강한 랜딩 페이지, 웹사이트, 앱, 프로토타입, 데모, 게임 UI가 필요할 때 사용한다.
- [shader-dev](shader-dev/SKILL.md): ShaderToy 호환 실시간 비주얼을 위한 종합 GLSL 셰이더 기법.
- [better-icons](better-icons/SKILL.md): CLI 또는 MCP로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다.
- [`gsap-skills/`](gsap-skills/): core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks를 포함한 공식 GSAP 애니메이션 스킬 8개.

### 유틸리티 및 문서 작업

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK(.NET) 기반의 전문 DOCX 생성, 편집, 서식화.
- [minimax-pdf](minimax-pdf/SKILL.md): 토큰 기반 디자인 시스템으로 PDF를 생성, 입력, 재구성.
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS, XML 워크플로, markitdown으로 PowerPoint를 생성, 편집, 읽기.
- [minimax-xlsx](minimax-xlsx/SKILL.md): 손실을 최소화한 XML 워크플로로 Excel/스프레드시트를 열고, 생성하고, 분석·편집·검증.

## 벤더링된 스킬 팩

[`gsap-skills/`](gsap-skills/)에는 [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills)에서 가져온 GSAP 애니메이션 스킬 번들이 포함되어 있으며, 기준 커밋은 `aed9cfd3277740755f6bfc1155c7aa645403b760`입니다.

포함된 항목:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

출처 및 법적 고지는 [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md)와 [`gsap-skills/LICENSE`](gsap-skills/LICENSE)에 보존되어 있습니다.

[`planning-with-files/`](planning-with-files/)는 [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)를 upstream baseline으로 사용합니다. 이 저장소는 일반적인 `planning-with-files` 이름을 유지하고 Pi 전용 package metadata를 제거해 표준 `SKILL.md` workflow와 호환되도록 합니다.

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
| [better-icons](better-icons/SKILL.md)                               | CLI 또는 MCP 도구로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다.                                                   | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | 구현 전에 협업형 대화를 통해 아이디어를 검증된 설계와 명세로 구체화합니다.                                                                                         | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | 탐색, 페이지 상태 확인, 폼 입력, 스크린샷, 정보 추출을 위한 지속형 브라우저 자동화 CLI.                                                          | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [browser-trace](browser-trace/SKILL.md)                             | 브라우저 자동화 디버깅용 CDP trace, 스크린샷, DOM dump를 캡처합니다.                                                                               | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | 기술 정확성은 유지한 채 원시인 말투의 초압축 응답으로 토큰 사용량을 줄입니다.                                                                    | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | Context7 CLI를 사용해 최신 문서, API 레퍼런스, 코드 예제를 조회.                                                                                 | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK(.NET) 기반의 전문 DOCX 생성, 편집, 서식화. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa를 사용해 웹, 코드, 회사 정보를 조사.                                                                                                         | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | 사용자가 특정 기능을 필요로 할 때 기존 스킬을 탐색.                                                                                              | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | 시각적으로 강한 랜딩 페이지, 웹사이트, 앱, 프로토타입, 데모, 게임 UI를 만든다.                                                                   | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | ShaderToy 호환 실시간 비주얼을 위한 종합 GLSL 셰이더 기법. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | 코드를 작성하기 전에 최신 서드파티 API 또는 SDK 문서를 가져옴.                                                                                   | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 현재 브랜치의 PR 리뷰 및 이슈 코멘트를 `gh`로 처리.                                                                                              | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 실패한 GitHub Actions 체크를 확인하고 로그를 가져와 수정 계획을 세움.                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | locality, leverage, testability, AI navigation을 높이는 architecture deepening 기회를 찾음.                                                      | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | 테스트 파일의 `as` 타입 단언을 `@total-typescript/shoehorn`으로 마이그레이션.                                                                    | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | 의존성 소스 코드를 가져와 AI agents 에 더 깊은 구현 맥락을 제공합니다.                                                                            | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다루는 스킬입니다.                                               | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | 웹 앱을 체계적으로 테스트하고 스크린샷/영상과 함께 재현 가능한 이슈 리포트를 생성.                                                               | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | agent-browser와 Chrome DevTools Protocol을 통해 Electron 데스크톱 앱 자동화.                                                                     | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | 토큰 기반 디자인 시스템으로 PDF를 생성, 입력, 재구성. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`, `findings.md`, `progress.md`를 활용해 복잡한 작업을 파일 기반으로 계획.                                                          | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS, XML 워크플로, markitdown으로 PowerPoint를 생성, 편집, 읽기. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | 기능, 버그 수정, 리팩터링, 동작 변경 전에 사용. public interface 기반 integration-style test를 우선한다.                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | 버그, 테스트 실패, 예상치 못한 동작을 만났을 때 수정안을 내기 전에 사용.                                                                     | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 손실을 최소화한 XML 워크플로로 Excel/스프레드시트를 열고, 생성하고, 분석·편집·검증. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | 사용자가 명시적으로 요청한 경우에만 `gh`를 사용해 stage, commit, push, PR 생성을 한 번에 처리.                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

참고:
- `dogfood`와 `electron`의 upstream 경로는 `skills/`가 아니라 `skill-data/`입니다.
- upstream은 commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0`에서 이 specialized skills를 옮겨 installer discovery가 bootstrap skill `agent-browser`만 찾게 했습니다.
- 이 저장소는 이들이 upstream에서 계속 유지되고 직접 유용하기 때문에 top-level vendored skills로 의도적으로 유지합니다.

### 벤더링된 `gsap-skills/` 스킬

| Skill                                                         | 설명                                                                                            | Source URL                                                                                            |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | 코어 API: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | 타임라인: 시퀀싱, position 파라미터, labels, 중첩, 재생 제어.                                   | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: 스크롤 연동 애니메이션, pinning, scrub, triggers, refresh, cleanup.              | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | 플러그인: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase 등.                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.                      | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, refs, `gsap.context()`, cleanup, SSR.                                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | 성능: transforms 우선, will-change, batching, ScrollTrigger 팁.                                 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte 등: lifecycle, selector 스코프, 언마운트 시 cleanup.                                | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## 기여하기

새 스킬 추가나 기존 스킬 개선 기여를 환영합니다.

1. 트리거 조건은 명확하고 검증 가능해야 합니다.
2. 예시는 간결하고 실행 중심으로 유지하세요.
3. 외부 도구에 의존하는 스킬은 해당 의존성을 `SKILL.md`에 문서화하세요.
4. 스킬을 추가하거나 이름을 바꿀 때는 `README.md`와 `README.zh-CN.md`를 먼저 업데이트하고, 공개된 스킬 인덱스가 바뀌면 다른 번역 README도 함께 갱신하세요.

## 라이선스

이 저장소는 [LICENSE](LICENSE) 하에 배포됩니다.

일부 스킬은 디렉터리별 자산 및 출처 고지를 위한 추가 라이선스 파일이나 notice를 포함하며, 예시는 [`improve-codebase-architecture/`](improve-codebase-architecture/), [`migrate-to-shoehorn/`](migrate-to-shoehorn/), [`minimax-docx/`](minimax-docx/), [`gsap-skills/`](gsap-skills/)입니다.
