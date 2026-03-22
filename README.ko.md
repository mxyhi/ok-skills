# OK Skills: Codex, Claude Code, Cursor, OpenClaw 등을 위한 AI 코딩 에이전트 스킬 모음

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | 한국어 | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

Codex, Claude Code, Cursor, OpenClaw, Trae 및 기타 `SKILL.md` 호환 도구를 위한 큐레이션된 AI 코딩 에이전트 스킬과 `AGENTS.md` 플레이북 저장소입니다.

이 저장소에는 현재 **재사용 가능한 스킬 55개**가 포함되어 있습니다. 이 중 **29개는 루트 레벨 스킬**로 직접 관리되며, **18개의 벤더링된 디자인 스킬**은 [`impeccable/`](impeccable/README.md) 아래에, **8개의 벤더링된 GSAP 애니메이션 스킬**은 [`gsap-skills/`](gsap-skills/) 아래에 포함되어 있습니다. `~/.agents/skills/ok-skills`에 clone 하면 되고, 내부 디렉터리 구조는 이미 `AGENTS.md` 기반 워크플로가 기대하는 형태와 맞춰져 있습니다.

**Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, 재사용 가능한 **AGENTS.md** 플레이북, 바로 적용할 수 있는 **SKILL.md** 예제를 찾고 있다면 이 저장소는 검색성과 즉시 사용성을 모두 고려해 정리되어 있습니다.

**주요 사용 장면:** 최신 문서 조회, 브라우저 자동화, GitHub Actions 장애 분석, 프롬프트 엔지니어링, 복잡한 작업 계획, 프런트엔드 디자인, 그리고 PDF / Word / PPTX / XLSX 문서 작업.

## 이 저장소가 맞는 사람

- Codex, Claude Code, Cursor, OpenClaw, Trae 또는 다른 AI 코딩 에이전트를 사용하며, 일회성 프롬프트 대신 재사용 가능한 스킬을 원한다.
- `AGENTS.md` / `SKILL.md` 기반 워크플로를 운영하며, 프로젝트 간에 이식 가능한 지침을 원한다.
- 문서 조회, 브라우저 자동화, GitHub 워크플로, 계획 수립, 프롬프트 엔지니어링, 프런트엔드 디자인, PDF, Office 문서, 슬라이드, 스프레드시트용 검증된 스킬이 필요하다.

## 먼저 설치할 추천 스킬

처음 몇 개만 설치할 계획이라면 아래부터 시작하는 편이 좋습니다.

- [planning-with-files](planning-with-files/SKILL.md): 복잡한 작업, 조사, 장기 실행 업무를 위한 파일 기반 계획 수립.
- [context7-cli](context7-cli/SKILL.md): 최신 라이브러리 문서와 Context7 기반 참고 자료 조회.
- [agent-browser](agent-browser/SKILL.md): 스크린샷, 폼 입력, 스크래핑, 웹 QA를 위한 브라우저 자동화.
- [gh-fix-ci](gh-fix-ci/SKILL.md): 실패한 GitHub Actions 체크를 읽고 수정 계획으로 정리.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): 더 안정적인 LLM 워크플로를 위한 프로덕션 지향 프롬프트 패턴.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): 고품질 프런트엔드 디자인 스킬과 함께 제공되는 전체 디자인 명령 번들.

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
  context7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

그리고 `AGENTS.md`에 아래처럼 간단한 트리거 규칙을 추가하면 됩니다.

```md
## Skills
- planning-with-files: 복잡한 작업, 조사, 또는 5회 이상의 도구 호출이 예상되는 작업에 사용.
- context7-cli: 최신 라이브러리 문서, API 레퍼런스, Context7 예제가 필요할 때 사용.
- agent-browser: 브라우저 자동화, 스크린샷, 스크래핑, 웹 테스트, 폼 입력이 필요할 때 사용.
```

그다음 자연스럽게 요청하면 됩니다.

- `이 모듈을 리팩터링하기 전에 planning-with-files를 사용해줘.`
- `이 SDK의 최신 문서를 context7-cli로 찾아줘.`
- `이 UI 버그를 agent-browser로 재현해줘.`

## 사용 사례별 스킬 탐색

### 조사 및 문서

- [context7-cli](context7-cli/SKILL.md): 문서 조회, 스킬 관리, MCP 설정을 위한 공식 Context7 CLI 워크플로.
- [exa-search](exa-search/SKILL.md): Exa 도구를 활용한 웹, 코드, 회사 조사.
- [get-api-docs](get-api-docs/SKILL.md): 코드를 작성하기 전에 최신 서드파티 API 및 SDK 문서를 가져옴.
- [find-skills](find-skills/SKILL.md): 사용자가 특정 기능을 원할 때 기존 스킬을 찾아줌.

### 계획 및 프롬프트

- [brainstorming](brainstorming/SKILL.md): 구현 전에 의도, 요구사항, 설계를 명확히 함.
- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, `progress.md`를 사용하는 지속형 마크다운 계획 수립.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): 프로덕션 LLM 시스템을 위한 고급 프롬프트 설계 패턴.
- [subagent-driven-development](subagent-driven-development/SKILL.md): 현재 세션에서 서로 독립적인 구현 작업 계획을 새 subagent와 단계별 리뷰로 실행.
- [test-driven-development](test-driven-development/SKILL.md): 구현 전에 테스트부터 작성하도록 강제.

### GitHub 워크플로

- [gh-address-comments](gh-address-comments/SKILL.md): 현재 PR의 리뷰/이슈 코멘트를 `gh`로 처리.
- [gh-fix-ci](gh-fix-ci/SKILL.md): 실패한 GitHub Actions 체크를 분석하고 로그를 요약하며 수정 계획을 세움.
- [yeet](yeet/SKILL.md): 사용자가 명시적으로 요청한 경우에만 `gh` 기반으로 stage, commit, push, PR 생성까지 한 번에 처리.

### 자동화 및 QA

- [agent-browser](agent-browser/SKILL.md): 탐색, 폼, 스크린샷, 스크래핑을 위한 브라우저 자동화.
- [browser-use](browser-use/SKILL.md): 탐색, 페이지 상태 확인, 폼 입력, 스크린샷, 정보 추출을 위한 지속형 브라우저 자동화 CLI.
- [chrome-cdp](chrome-cdp/SKILL.md): CDP로 로컬의 기존 Chrome 세션에 연결해 가벼운 페이지 점검과 상호작용을 수행.
- [bb-browser](bb-browser/SKILL.md): 사용자의 실제 브라우저와 로그인 상태를 활용한 정보 수집 및 브라우저 자동화.
- [pinchtab](pinchtab/SKILL.md): 안정적인 접근성 참조를 사용해 Pinchtab의 로컬 HTTP API로 Chrome 제어.
- [electron](electron/SKILL.md): Chrome DevTools Protocol 기반으로 Electron 데스크톱 앱 자동화.
- [opencli](opencli/SKILL.md): 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다룹니다.
- [dogfood](dogfood/SKILL.md): 재현 가능한 증거를 남기는 구조화된 탐색 테스트.

### 프런트엔드 및 디자인

- [ai-elements](ai-elements/SKILL.md): `ai-elements` 라이브러리를 위한 AI 채팅 UI 컴포넌트 제작.
- [better-icons](better-icons/SKILL.md): CLI 또는 MCP로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): Vercel Engineering이 정리한 React / Next.js 성능 가이드.
- [remotion-best-practices](remotion-best-practices/SKILL.md): React 기반 영상 작업을 위한 Remotion 가이드.
- [`gsap-skills/`](gsap-skills/): core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks를 포함한 공식 GSAP 애니메이션 스킬 8개.
- [`impeccable/`](impeccable/README.md): `frontend-design`, `adapt`, `audit`, `polish` 등을 포함한 18개의 벤더링된 프런트엔드 디자인 스킬 번들.

### 유틸리티 및 문서 작업

- [docx](docx/SKILL.md): 서식, 댓글, 변경 내용 추적을 포함한 Word 문서 생성/읽기/편집/조작.
- [pdf](pdf/SKILL.md): 렌더링 기준 검토를 포함한 PDF 읽기/생성/검토.
- [pptx](pptx/SKILL.md): 슬라이드 덱, 템플릿, 프레젠테이션 콘텐츠 생성/읽기/편집/조작.
- [xlsx](xlsx/SKILL.md): 스프레드시트 생성, 편집, 수식, 분석.
- [skill-creator](skill-creator/SKILL.md): 더 구조적인 스킬과 도구 연동을 위한 스킬 생성/업데이트 가이드.

## 벤더링된 스킬 팩

[`impeccable/`](impeccable/README.md)에는 [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable)에서 가져온 디자인 중심 번들이 포함되어 있으며, 기준 커밋은 `d6b1a56bc5b79e9375be0f8508b4daa1678fb058`입니다.

포함된 항목:

- `frontend-design`: 대표 프런트엔드 디자인 스킬
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

출처 및 법적 고지는 [`impeccable/NOTICE.md`](impeccable/NOTICE.md)와 [`impeccable/LICENSE`](impeccable/LICENSE)에 보존되어 있습니다.

[`gsap-skills/`](gsap-skills/)에는 [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills)에서 가져온 GSAP 애니메이션 스킬 번들이 포함되어 있으며, 기준 커밋은 `4300e310513b0ddc0b121a5c0e0bd2e5c2325ff2`입니다.

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

## 공통 전제 조건

- 일부 스킬은 `gh`가 설치되어 있고 로그인되어 있다고 가정합니다.
- 브라우저 관련 스킬은 Chrome/CDP를 사용할 수 있는 환경이 필요할 수 있습니다.
- 서드파티 문서 조회 스킬은 외부 CLI 또는 MCP 도구에 의존할 수 있으므로, 자세한 내용은 각 `SKILL.md`를 확인하세요.

## 전체 스킬 인덱스

벤더링되거나 외부에서 가져온 스킬은 `Source URL`이 정식 업스트림을 가리키며, 그렇지 않은 경우 이 저장소의 스킬 디렉터리를 가리킵니다.

### 루트 레벨 스킬

| Skill | 설명 | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | AI 에이전트를 위한 브라우저 자동화 CLI: 탐색, 폼 입력, 스크린샷, 추출, 웹 테스트. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | 조합형 패턴과 shadcn/ui 관례를 따라 ai-elements 라이브러리용 AI 채팅 UI 컴포넌트를 생성. | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [bb-browser](bb-browser/SKILL.md) | 사용자의 실제 브라우저와 로그인 상태를 통해 공개 페이지, 내부 시스템, 로그인 후 워크플로까지 다루는 정보 수집 및 브라우저 자동화 스킬입니다. | [epiral/bb-browser](https://github.com/epiral/bb-browser/tree/main/skills/bb-browser) |
| [better-icons](better-icons/SKILL.md) | CLI 또는 MCP 도구로 200개 이상의 Iconify 아이콘 라이브러리를 검색하고 SVG 아이콘을 가져옵니다. | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills) |
| [brainstorming](brainstorming/SKILL.md) | 구현 전에 의도, 요구사항, 설계를 명확히 한다. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [browser-use](browser-use/SKILL.md) | 탐색, 페이지 상태 확인, 폼 입력, 스크린샷, 정보 추출을 위한 지속형 브라우저 자동화 CLI. | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use) |
| [chrome-cdp](chrome-cdp/SKILL.md) | CDP로 로컬의 기존 Chrome 세션에 연결해 가벼운 탭 점검, 스크린샷, DOM 접근, 입력, 탐색을 수행한다. | [pasky/chrome-cdp-skill](https://github.com/pasky/chrome-cdp-skill/tree/main/skills/chrome-cdp) |
| [context7-cli](context7-cli/SKILL.md) | Context7 CLI를 사용해 문서 조회, 스킬 관리, MCP 설정을 수행. | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | 서식, 댓글, 변경 내용 추적, 이미지 업데이트를 포함한 Word 문서 생성/읽기/편집/조작. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | 웹 앱을 체계적으로 테스트하고 스크린샷/영상과 함께 재현 가능한 이슈 리포트를 생성. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | agent-browser와 Chrome DevTools Protocol을 통해 Electron 데스크톱 앱 자동화. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | Exa를 사용해 웹, 코드, 회사 정보를 조사. | Custom |
| [find-skills](find-skills/SKILL.md) | 사용자가 특정 기능을 필요로 할 때 기존 스킬을 탐색. | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | 코드를 작성하기 전에 최신 서드파티 API 또는 SDK 문서를 가져옴. | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | 현재 브랜치의 PR 리뷰 및 이슈 코멘트를 `gh`로 처리. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | 실패한 GitHub Actions 체크를 확인하고 로그를 가져와 수정 계획을 세움. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [opencli](opencli/SKILL.md) | 브라우저 로그인 상태 재사용, 공개 API 접근, AI 생성 어댑터로 웹사이트를 CLI처럼 다루는 스킬입니다. | [jackwener/opencli](https://github.com/jackwener/opencli) |
| [pdf](pdf/SKILL.md) | 렌더링 검토와 Python 도구를 포함해 PDF를 읽고, 생성하고, 검토. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | 안정적인 접근성 참조를 사용해 Pinchtab의 HTTP API로 헤드리스/헤디드 Chrome을 제어하여 웹 자동화, 스크래핑, 폼 입력, 탐색, 스크린샷, 추출을 수행. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | `task_plan.md`, `findings.md`, `progress.md`를 활용해 복잡한 작업을 파일 기반으로 계획. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | PowerPoint 프레젠테이션, 템플릿, 레이아웃, 노트, 슬라이드 콘텐츠 생성/읽기/편집/조작. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | 안정적인 프로덕션 LLM 워크플로를 위한 고급 프롬프트 엔지니어링 패턴. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | React와 Remotion으로 영상을 만들기 위한 모범 사례. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | 전문 지식과 도구 연동을 갖춘 스킬을 만들거나 업데이트하는 가이드. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [subagent-driven-development](subagent-driven-development/SKILL.md) | 현재 세션에서 독립적인 작업으로 구성된 구현 계획을 새 subagent와 단계별 리뷰로 실행. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) |
| [test-driven-development](test-driven-development/SKILL.md) | 기능이나 버그 수정을 구현하기 전에 사용. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | Vercel Engineering이 정리한 React / Next.js 성능 최적화 가이드. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | 스프레드시트 생성, 편집, 수식, 서식, 분석. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | 사용자가 명시적으로 요청한 경우에만 `gh`를 사용해 stage, commit, push, PR 생성을 한 번에 처리. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### 벤더링된 `impeccable/` 스킬

| Skill | 설명 | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | 개성이 있고 프로덕션 수준의 고품질 프런트엔드 인터페이스를 제작. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | 다양한 화면 크기, 디바이스, 맥락에 맞게 디자인을 조정. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | 목적 있는 모션과 마이크로 인터랙션을 추가. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | 접근성, 성능, 테마, 반응형 품질을 감사. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | 안전하지만 밋밋한 디자인을 더 흥미롭게 만듦. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | 불명확한 UX 문구와 안내를 개선. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | 지나치게 단색인 인터페이스에 전략적인 색을 추가. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | UX 관점에서 디자인 효과를 평가. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | 인터페이스에 개성과 기억에 남는 디테일을 추가. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | 디자인을 본질만 남기도록 정제. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | 재사용 가능한 컴포넌트, 토큰, 패턴을 디자인 시스템으로 통합. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | 오류 처리, i18n, 오버플로, 엣지 케이스 대응력을 개선. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | 기능을 디자인 시스템에 맞춰 정규화. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | 온보딩, 빈 상태, 첫 사용 경험을 개선. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | 로딩, 렌더링, 모션, 번들 효율을 개선. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | 정렬, 간격, 일관성, 디테일을 마무리 점검. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | 디자인 품질은 유지하면서 시각적 공격성을 낮춤. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | 설계 컨텍스트를 수집하고 향후 작업을 위한 지속 가이드로 저장. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### 벤더링된 `gsap-skills/` 스킬

| Skill | 설명 | Source URL |
| --- | --- | --- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md) | 코어 API: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core) |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md) | 타임라인: 시퀀싱, position 파라미터, labels, 중첩, 재생 제어. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline) |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: 스크롤 연동 애니메이션, pinning, scrub, triggers, refresh, cleanup. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md) | 플러그인: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase 등. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins) |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md) | gsap.utils: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils) |
| [gsap-react](gsap-skills/gsap-react/SKILL.md) | React: useGSAP, refs, `gsap.context()`, cleanup, SSR. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react) |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md) | 성능: transforms 우선, will-change, batching, ScrollTrigger 팁. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance) |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md) | Vue, Svelte 등: lifecycle, selector 스코프, 언마운트 시 cleanup. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks) |

## 기여하기

새 스킬 추가나 기존 스킬 개선 기여를 환영합니다.

1. 트리거 조건은 명확하고 검증 가능해야 합니다.
2. 예시는 간결하고 실행 중심으로 유지하세요.
3. 외부 도구에 의존하는 스킬은 해당 의존성을 `SKILL.md`에 문서화하세요.
4. 스킬을 추가하거나 이름을 바꿀 때는 `README.md`와 `README.zh-CN.md`를 먼저 업데이트하고, 공개된 스킬 인덱스가 바뀌면 다른 번역 README도 함께 갱신하세요.

## 라이선스

이 저장소는 [LICENSE](LICENSE) 하에 배포됩니다.

일부 스킬은 디렉터리별 자산 및 출처 고지를 위한 추가 라이선스 파일이나 notice를 포함하며, 예시는 [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), [`skill-creator/`](skill-creator/), [`xlsx/`](xlsx/)입니다.
