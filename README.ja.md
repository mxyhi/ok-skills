# OK Skills: Codex、Claude Code、Cursor、OpenClaw など向けの AI Coding Agent Skills 集合

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | 日本語 | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex、Claude Code、Cursor、OpenClaw、Trae、そのほか `SKILL.md` 互換ツール向けに厳選した AI coding agent skills と `AGENTS.md` プレイブックをまとめたリポジトリです。

このリポジトリには現在 **51 個の再利用可能な skills** が含まれています。内訳は、このリポジトリで直接管理している **25 個のトップレベル skills** と、[`impeccable/`](impeccable/README.md) 配下に vendored bundle として収録されている **18 個のデザイン skills**、そして [`gsap-skills/`](gsap-skills/) 配下に vendored bundle として収録されている **8 個の GSAP アニメーション skills** です。`~/.agents/skills/ok-skills` に clone すれば、そのまま `AGENTS.md` ベースのワークフローで使えるディレクトリ構成になっています。

**Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、再利用できる **AGENTS.md** プレイブック、実用的な **SKILL.md** 例を探しているなら、このリポジトリは見つけやすさと導入しやすさを意識して整理しています。

**よくある用途:** 最新ドキュメント参照、ブラウザ自動化、GitHub Actions のデバッグ、prompt engineering、複雑タスクの計画、フロントエンド設計、PDF / Word / PPTX / XLSX の作成と編集。

## このリポジトリが向いている人

- Codex、Claude Code、Cursor、OpenClaw、Trae などの AI coding agent を使っていて、その場しのぎの prompt ではなく再利用可能な skills を使いたい人
- `AGENTS.md` / `SKILL.md` ベースの運用をしていて、プロジェクトをまたいで持ち運べるワークフローを整えたい人
- ドキュメント参照、ブラウザ自動化、GitHub ワークフロー、計画、prompt engineering、フロントエンド設計、PDF、Office ドキュメント、スライド、スプレッドシート向けの実戦的な skills が必要な人

## まず入れるならこれ

最初に数個だけ入れるなら、まずは次の skills から始めるのがおすすめです。

- [brainstorming](brainstorming/SKILL.md): 実装に入る前にアイデア、要件、設計を整理する
- [planning-with-files](planning-with-files/SKILL.md): 複雑なタスク、調査、長時間にわたる作業をファイルベースで計画する skill
- [context7-cli](context7-cli/SKILL.md): 最新ライブラリのドキュメントや Context7 ベースの参照情報を取得する skill
- [agent-browser](agent-browser/SKILL.md): スクリーンショット、フォーム操作、スクレイピング、Web QA 向けのブラウザ自動化 skill
- [gh-fix-ci](gh-fix-ci/SKILL.md): 失敗した GitHub Actions を調べ、ログを修正計画につなげる skill
- [impeccable](impeccable/impeccable/SKILL.md): 中核となる impeccable design skill と、それを支える一式のデザイン系コマンド群

## 1 分で始める Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 後、リポジトリは `~/.agents/skills/ok-skills` に配置され、内部ディレクトリはすでに期待されるレイアウトになっています。

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

次に `AGENTS.md` に最小限の trigger rules を追加します。

```md
## Skills

- planning-with-files: 複雑なタスク、調査、または 5 回以上の tool call が見込まれる作業で使う。
- context7-cli: 最新ライブラリ docs、API reference、Context7 ベースの例が必要なときに使う。
- agent-browser: ブラウザ自動化、スクリーンショット、スクレイピング、Web テスト、フォーム入力で使う。
```

あとは自然な指示で呼び出せます。

- `このモジュールをリファクタリングする前に planning-with-files を使って。`
- `この SDK の最新 docs を context7-cli で取ってきて。`
- `この UI バグを agent-browser で再現して。`

## 用途別に Skills を探す

### Research & Docs

- [context7-cli](context7-cli/SKILL.md): docs lookup、skill 管理、MCP セットアップ向けの公式 Context7 CLI ワークフロー
- [exa-search](exa-search/SKILL.md): Exa ツールを使った web、code、company research
- [get-api-docs](get-api-docs/SKILL.md): コーディング前に外部 API / SDK の最新ドキュメントを取得
- [find-skills](find-skills/SKILL.md): ユーザーが欲しい機能に対して既存 skill を探す

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): 実装に入る前にアイデア、要件、設計を整理する
- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`、`findings.md`、`progress.md` を使った永続的な markdown planning
- [test-driven-development](test-driven-development/SKILL.md): 実装前に先にテストを書くことを徹底する

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): 現在の PR 上の review comment や issue comment を `gh` で処理する
- [gh-fix-ci](gh-fix-ci/SKILL.md): 失敗した GitHub Actions を調べ、ログを要約して修正計画を立てる
- [yeet](yeet/SKILL.md): ユーザーが明示的に求めたときだけ、stage・commit・push・PR 作成を `gh` で一気通貫で行う

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): ナビゲーション、フォーム操作、スクリーンショット、スクレイピング向けのブラウザ自動化
- [browser-use](browser-use/SKILL.md): ナビゲーション、ページ状態の確認、フォーム入力、スクリーンショット、情報抽出のための永続的なブラウザ自動化 CLI。
- [opencli](opencli/opencli-usage/SKILL.md): ブラウザのログイン状態を再利用し、公開 API や AI 生成アダプタで Web サイトを CLI 化する

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): `ai-elements` ライブラリ向けの AI チャット UI コンポーネントを構築する
- [frontend-skill](frontend-skill/SKILL.md): 視覚的に強いランディングページ、Web サイト、アプリ、プロトタイプ、デモ、ゲーム UI が必要なときに使う
- [shader-dev](shader-dev/SKILL.md): ShaderToy 互換のリアルタイム表現を作るための包括的な GLSL シェーダ技法。
- [better-icons](better-icons/SKILL.md): CLI または MCP で 200 以上の Iconify ライブラリを検索し、SVG アイコンを取得する
- [remotion-best-practices](remotion-best-practices/SKILL.md): React ベースの動画制作向け Remotion ガイド
- [`gsap-skills/`](gsap-skills/): 公式 GSAP アニメーション skills 8 個（core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks）
- [`impeccable/`](impeccable/README.md): `impeccable`、`adapt`、`audit`、`polish` などを含む 18 個の vendored frontend design skills

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK (.NET) を使った DOCX の本格的な作成・編集・書式設定。
- [minimax-pdf](minimax-pdf/SKILL.md): トークンベースのデザインシステムで PDF を生成・入力・再レイアウト。
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS、XML ワークフロー、markitdown を使って PowerPoint を生成・編集・読取。
- [minimax-xlsx](minimax-xlsx/SKILL.md): 低損失の XML ワークフローで Excel/スプレッドシートを開き、作成し、分析・編集・検証。
- [skill-creator](skill-creator/SKILL.md): より構造化された skill や tool integration を備えた skills を作成・更新する

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) には、[`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) 由来の design-focused bundle が commit `00d485659af82982aef0328d0419c49a2716d123` の状態で vendored されています。

含まれているもの:

- `impeccable`: フラッグシップとなる frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

帰属表示および法的文書は [`impeccable/NOTICE.md`](impeccable/NOTICE.md) と [`impeccable/LICENSE`](impeccable/LICENSE) に保持されています。

[`gsap-skills/`](gsap-skills/) には、[`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) 由来の GSAP アニメーション skills bundle が commit `03d9f0c3dbf91e0b60582b64ed040c8911ca0174` の状態で vendored されています。

含まれているもの:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

帰属表示および法的文書は [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) と [`gsap-skills/LICENSE`](gsap-skills/LICENSE) に保持されています。

## よくある前提条件

- 一部の skills は `gh` がインストール済みかつ認証済みであることを前提にしています。
- ブラウザ系 skills では、Chrome / CDP を使える実行環境が必要になる場合があります。
- 外部 docs lookup 系の skills は追加の CLI や MCP tools に依存することがあります。詳細は各 `SKILL.md` を確認してください。

## Full Skill Index

`Source URL` は、skill が vendored / imported の場合は canonical upstream を指し、そうでない場合はこのリポジトリ内の skill ディレクトリを指します。

### Top-Level Skills

| Skill                                                               | 説明                                                                                                                                                                                          | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | AI agents 向けのブラウザ自動化 CLI。ナビゲーション、フォーム入力、スクリーンショット、データ抽出、Web テストに対応。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | composable patterns と shadcn/ui の慣習に沿って、ai-elements ライブラリ向けの AI チャット UI コンポーネントを作成する。                                                                       | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | CLI または MCP ツールで 200 以上の Iconify ライブラリを検索し、SVG アイコンを取得する。                                                                                                       | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | 実装前に、協働的な対話を通じてアイデアを確認済みの設計と仕様へ落とし込む。                                                                                       | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | ナビゲーション、ページ状態の確認、フォーム入力、スクリーンショット、情報抽出のための永続的なブラウザ自動化 CLI。                                                                              | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | 技術的な正確性を保ったまま、洞穴人風の超短文で応答トークンを削減する。                                                                          | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | Context7 CLI を使って docs lookup、skill 管理、MCP セットアップを行う。                                                                                                                       | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK (.NET) を使った DOCX の本格的な作成・編集・書式設定。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa を使って web、code、company research を行う。                                                                                                                                             | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | ユーザーが必要とする specialized capability に対して既存 skill を見つける。                                                                                                                   | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | 視覚的に強いランディングページ、Web サイト、アプリ、プロトタイプ、デモ、ゲーム UI を作成する。                                                                                                | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | ShaderToy 互換のリアルタイム表現を作るための包括的な GLSL シェーダ技法。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | コードを書く前に、外部 API や SDK の最新ドキュメントを取得する。                                                                                                                              | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 現在のブランチに対する PR review comment や issue comment を `gh` で処理する。                                                                                                                | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 失敗した GitHub Actions を調べ、ログを取得し、修正計画を立てる。                                                                                                                              | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | 依存パッケージのソースコードを取得し、AI agents により深い実装コンテキストを与える。                                                                                                        | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | ブラウザのログイン状態を再利用し、公開 API や AI 生成アダプタで Web サイトを CLI 化する。                                                                                                     | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [minimax-pdf](minimax-pdf/SKILL.md) | トークンベースのデザインシステムで PDF を生成・入力・再レイアウト。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`、`findings.md`、`progress.md` を使って複雑なタスクをファイルベースで計画する。                                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS、XML ワークフロー、markitdown を使って PowerPoint を生成・編集・読取。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | React と Remotion で動画を作るための best practices。                                                                                                                                         | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | specialized knowledge と tool integrations を備えた skills を作成または更新するためのガイド。                                                                                                 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | 機能追加やバグ修正の前に使う。                                                                                                                                                                | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 低損失の XML ワークフローで Excel/スプレッドシートを開き、作成し、分析・編集・検証。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | ユーザーが明示的に `gh` で stage・commit・push・GitHub PR 作成を一括で求めた場合にのみ使う。                                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

### Vendored `impeccable/` Skills

| Skill                                                    | 説明                                                                              | Source URL                                                  |
| -------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | 識別性が高く、本番品質のフロントエンド UI を作成する。                            | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | 画面サイズ、デバイス、コンテキストにまたがってデザインを適応させる。              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | 意図のあるモーションとマイクロインタラクションを追加する。                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | アクセシビリティ、パフォーマンス、テーマ、一貫性、レスポンシブ性を監査する。      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | 無難で地味なデザインを、より視覚的に強く魅力的にする。                            | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | わかりにくい UX copy や説明文を改善する。                                         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | 単調すぎる UI に戦略的な色を加える。                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | UX 観点でデザインの有効性を評価する。                                             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | UI に個性や印象に残る楽しさを加える。                                             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | デザインを本質まで削ぎ落とし、不要な複雑さを除く。                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | エラー処理、i18n、テキスト overflow、edge cases への耐性を高める。                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | レイアウト、余白、視覚的リズムを改善する。                                                                      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | フロントエンドのパフォーマンス、レンダリング、モーション、bundle 効率を改善する。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | 技術的に野心的な実装でインターフェースを従来の限界の先へ押し出す。                                                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | 最終品質調整として、整列、余白、一貫性、細部を磨く。                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | 強すぎる視覚的主張を抑えつつ、デザイン品質を維持する。                            | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | コードを書く前に機能の UX / UI を設計する。                                                                 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | フォント選定、階層、サイズ、ウェイト、可読性を改善する。                                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### Vendored `gsap-skills/` Skills

| Skill                                                         | 説明                                                                                             | Source URL                                                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | コア API: `gsap.to()` / `from()` / `fromTo()`、easing、duration、stagger、defaults、matchMedia。 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timeline: シーケンス、position parameter、labels、ネスト、再生制御。                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: スクロール連動アニメーション、pin、scrub、triggers、refresh、cleanup。            | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip、Draggable、MotionPath、ScrollToPlugin、CustomEase など。                          | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils: clamp、mapRange、normalize、random、snap、toArray、wrap、pipe。                      | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP、refs、`gsap.context()`、cleanup、SSR。                                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Performance: transforms、will-change、batching、ScrollTrigger tips。                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue、Svelte など: lifecycle、selector のスコープ、unmount 時の cleanup。                         | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Contributing

新しい skills の追加や、既存 skills の改善に対する contribution を歓迎します。

1. trigger condition は明示的で検証可能にしてください。
2. 例は簡潔に保ち、実行しやすい形にしてください。
3. 外部 tool に依存する skill は、その依存関係を `SKILL.md` に明記してください。
4. skill を追加または名称変更した場合は、`README.md` と `README.zh-CN.md` を更新し、公開されている skill index が変わる場合はほかの翻訳版 README も更新してください。

## License

このリポジトリは [LICENSE](LICENSE) の下で提供されています。

一部の skills には、skill 固有のアセットや帰属表示のために追加の license file / notice file が含まれます。対象には [`minimax-docx/`](minimax-docx/)、[`impeccable/`](impeccable/README.md)、[`gsap-skills/`](gsap-skills/)、[`skill-creator/`](skill-creator/) などがあります。
