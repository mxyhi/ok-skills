# OK Skills: Codex、Claude Code、Cursor、OpenClaw など向けの AI Coding Agent Skills 集合

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | 日本語 | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex、Claude Code、Cursor、OpenClaw、Trae、そのほか `SKILL.md` 互換ツール向けに厳選した AI coding agent skills と `CLAUDE.md` / `AGENTS.md` プレイブックをまとめたリポジトリです。

このリポジトリには現在 **29 個の再利用可能な skills** が含まれ、すべてトップレベルの skill ディレクトリとしてこのリポジトリで直接管理されています。`~/.agents/skills/ok-skills` に clone すれば、内部ディレクトリは `AGENTS.md` ベースの workflow が期待する layout にすでに合っており、[`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) は Claude Code 向けの agent playbook を提供します。

**Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、再利用できる **CLAUDE.md / AGENTS.md** プレイブック、実用的な **SKILL.md** 例を探しているなら、このリポジトリは見つけやすさと導入しやすさを意識して整理しています。

**よくある用途:** 最新ドキュメント参照、ブラウザ自動化、prompt engineering、複雑タスクの計画、フロントエンド設計、PDF / Word / PPTX / XLSX の作成と編集。

## このリポジトリが向いている人

- Codex、Claude Code、Cursor、OpenClaw、Trae などの AI coding agent を使っていて、その場しのぎの prompt ではなく再利用可能な skills を使いたい人
- `CLAUDE.md` / `AGENTS.md` / `SKILL.md` ベースの運用をしていて、プロジェクトをまたいで持ち運べるワークフローを整えたい人
- ドキュメント参照、ブラウザ自動化、計画、prompt engineering、フロントエンド設計、PDF、Office ドキュメント、スライド、スプレッドシート向けの実戦的な skills が必要な人

## まず入れるならこれ

最初に数個だけ入れるなら、まずは次の skills から始めるのがおすすめです。

- [planning-with-files](planning-with-files/SKILL.md): 複雑なタスク、調査、長時間にわたる作業をファイルベースで計画する skill
- [find-docs](find-docs/SKILL.md): 最新ライブラリ docs、API reference、Context7 ベースの例を取得する skill
- [agent-browser](agent-browser/SKILL.md): スクリーンショット、フォーム操作、スクレイピング、Web QA 向けのブラウザ自動化 skill

## 1 分で始める Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 後、リポジトリは `~/.agents/skills/ok-skills` に配置され、内部ディレクトリはすでに期待されるレイアウトになっています。

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

Claude Code または Codex のグローバル指示は [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) から始め、Claude Code の `CLAUDE.md` または Codex の `AGENTS.md` にコピー / マージできます。Chinese-first、KISS、最新ドキュメント / ソース確認、multi-agent 優先、`caveman` / `planning-with-files` / `karpathy-guidelines` のデフォルト有効化、厳格な TypeScript ルール、context-mode ルーティングをまとめた agent playbook です。再利用する前に `语言要求` セクションをプロジェクト向けに編集してください。`其他注意项` セクションはプロジェクトローカルな設定として必要に応じて編集できます。

次に `AGENTS.md` に最小限の trigger rules を追加するか、同じ skill trigger を `CLAUDE.md` / `AGENTS.md` に統合します。

```md
## Skills

- planning-with-files: 複雑なタスク、調査、または 5 回以上の tool call が見込まれる作業で使う。
- find-docs: 最新ライブラリ docs、API reference、Context7 ベースの例が必要なときに使う。
- agent-browser: ブラウザ自動化、スクリーンショット、スクレイピング、Web テスト、フォーム入力で使う。
```

あとは自然な指示で呼び出せます。

- `このモジュールをリファクタリングする前に planning-with-files を使って。`
- `この SDK の最新 docs を find-docs で取ってきて。`
- `この UI バグを agent-browser で再現して。`

## 用途別に Skills を探す

### Research & Docs

- [find-docs](find-docs/SKILL.md): 最新 docs lookup に特化した Context7 CLI ワークフロー
- [exa-search](exa-search/SKILL.md): Exa ツールを使った web、code、company research
- [get-api-docs](get-api-docs/SKILL.md): コーディング前に外部 API / SDK の最新ドキュメントを取得
- [find-skills](find-skills/SKILL.md): ユーザーが欲しい機能に対して既存 skill を探す

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`、`findings.md`、`progress.md` を使った永続的な markdown planning
- [autoresearch](autoresearch/SKILL.md): 明確な goal、metric、verify loop、keep/discard gate による自律的な goal-directed iteration
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): hard bug と performance regression のための規律ある診断ループ。
- [grill-with-docs](grill-with-docs/SKILL.md): domain language、`CONTEXT.md`、ADR に照らして plan を検証し、docs をその場で更新する。
- [grilling](grilling/SKILL.md): 直接の grill session と `grill-with-docs` で使う一問ずつの reusable interview loop。
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): locality、leverage、testability、AI navigation を高める architecture deepening の機会を見つける
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): 過度な複雑化、隠れた前提、検証不能な変更を減らす coding guidelines。
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): テスト内の `as` 型アサーションを `@total-typescript/shoehorn` へ移行する
- [tdd](tdd/SKILL.md): 機能、バグ修正、リファクタリング、振る舞い変更の前に test-first red-green-refactor を徹底する
- [systematic-debugging](systematic-debugging/SKILL.md): バグやテスト失敗、想定外の挙動で、修正案の前に根本原因を系統的に調べる

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): ナビゲーション、フォーム操作、スクリーンショット、スクレイピング向けのブラウザ自動化
- [kimi-webbridge](kimi-webbridge/SKILL.md): ローカルデーモン経由でユーザーの実ブラウザを操作し、ナビゲーション、フォーム入力、スクリーンショット、ページ読解、ログイン済みセッションに対応します。
- [browser-trace](browser-trace/SKILL.md): ブラウザ自動化実行の CDP trace、スクリーンショット、DOM dump を取得し、ページ単位に分割してデバッグする。
- [opencli](opencli/opencli-usage/SKILL.md): ブラウザのログイン状態を再利用し、公開 API や AI 生成アダプタで Web サイトを CLI 化する
- [xquik-twitter](xquik-twitter/SKILL.md): Xquik API で X/Twitter データを検索し、承認済みのアカウント操作を実行する。

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): `ai-elements` ライブラリ向けの AI チャット UI コンポーネントを構築する
- [huashu-design](huashu-design/SKILL.md): 高品質な HTML プロトタイプ、インタラクティブデモ、スライド、motion design、デザイン variants、動画書き出し、design critique を作る。
- [better-icons](better-icons/SKILL.md): CLI または MCP で 200 以上の Iconify ライブラリを検索し、SVG アイコンを取得する

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK (.NET) を使った DOCX の本格的な作成・編集・書式設定。
- [minimax-pdf](minimax-pdf/SKILL.md): トークンベースのデザインシステムで PDF を生成・入力・再レイアウト。
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS、XML ワークフロー、markitdown を使って PowerPoint を生成・編集・読取。
- [huashu-design](huashu-design/SKILL.md): HTML decks、編集可能 PPTX、MP4/GIF motion pieces、ナレーション付き design videos を作る。
- [minimax-xlsx](minimax-xlsx/SKILL.md): 低損失の XML ワークフローで Excel/スプレッドシートを開き、作成し、分析・編集・検証。

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) は [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) を upstream baseline として対応しています。この repository では、その upstream directory を local skill の canonical baseline として扱います。ローカル差分は `skills-ref` 互換の `SKILL.md` frontmatter と、インストール場所に依存しない相対 script path docs に限定します。

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
| [autoresearch](autoresearch/SKILL.md)                               | modify、verify、keep/discard、repeat workflows のための自律的な goal-directed iteration engine。                                                                                       | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | CLI または MCP ツールで 200 以上の Iconify ライブラリを検索し、SVG アイコンを取得する。                                                                                                       | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | ローカルデーモン経由でユーザーの実ブラウザを操作し、ナビゲーション、フォーム入力、スクリーンショット、ページ読解、ログイン済みセッションに対応します。                                      | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | ブラウザ自動化デバッグ用に CDP trace、スクリーンショット、DOM dump を取得する。                                                                                       | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | 技術的な正確性を保ったまま、洞穴人風の超短文で応答トークンを削減する。                                                                          | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | hard bug と performance regression のための規律ある診断ループ。                                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Context7 CLI を使って最新 docs、API reference、コード例を調べる。                                                                                                                            | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK (.NET) を使った DOCX の本格的な作成・編集・書式設定。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa を使って web、code、company research を行う。                                                                                                                                             | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | ユーザーが必要とする specialized capability に対して既存 skill を見つける。                                                                                                                   | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | 高品質な HTML プロトタイプ、インタラクティブデモ、スライド、motion design、デザイン variants、動画書き出し、design critique を作る。                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | コードを書く前に、外部 API や SDK の最新ドキュメントを取得する。                                                                                                                              | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | domain language、`CONTEXT.md`、ADR に照らして plan を stress-test し、docs を inline 更新する。                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | 直接の grill session と `grill-with-docs` で使う一問ずつの reusable interview loop。                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | locality、leverage、testability、AI navigation を高める architecture deepening の機会を見つける。                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | 過度な複雑化、隠れた前提、検証不能な変更を減らす coding guidelines。                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | test files の `as` type assertions を `@total-typescript/shoehorn` へ移行する。                                                                                                             | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | ブラウザのログイン状態を再利用し、公開 API や AI 生成アダプタで Web サイトを CLI 化する。                                                                                                     | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Xquik API で X/Twitter データを検索し、承認済みのアカウント操作を実行する。                                                                                                             | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | トークンベースのデザインシステムで PDF を生成・入力・再レイアウト。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`、`findings.md`、`progress.md` を使って複雑なタスクをファイルベースで計画する。                                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS、XML ワークフロー、markitdown を使って PowerPoint を生成・編集・読取。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | 機能、バグ修正、リファクタリング、振る舞い変更の前に使う。public interface 経由の integration-style test を優先する。                                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | バグ、テスト失敗、想定外の挙動に遭遇したとき、修正案を出す前に使う。                                                                                                                      | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 低損失の XML ワークフローで Excel/スプレッドシートを開き、作成し、分析・編集・検証。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## Contributing

新しい skills の追加や、既存 skills の改善に対する contribution を歓迎します。

1. trigger condition は明示的で検証可能にしてください。
2. 例は簡潔に保ち、実行しやすい形にしてください。
3. 外部 tool に依存する skill は、その依存関係を `SKILL.md` に明記してください。
4. skill を追加または名称変更した場合は、`README.md` と `README.zh-CN.md` を更新し、公開されている skill index が変わる場合はほかの翻訳版 README も更新してください。

## License

このリポジトリは [LICENSE](LICENSE) の下で提供されています。
