# OK Skills: bộ AI coding agent skills cho Codex, Claude Code, Cursor, OpenClaw và hơn thế nữa

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | Tiếng Việt | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

Bộ sưu tập AI coding agent skills và playbook `AGENTS.md` được tuyển chọn cho Codex, Claude Code, Cursor, OpenClaw, Trae và các công cụ khác tương thích với `SKILL.md`.

Kho này hiện gồm **55 skill có thể tái sử dụng**: **29 skill cấp cao nhất** được duy trì trực tiếp trong repo này, cùng với **18 skill thiết kế được vendored** dưới [`impeccable/`](impeccable/README.md) và **8 skill animation GSAP được vendored** dưới [`gsap-skills/`](gsap-skills/). Chỉ cần clone vào `~/.agents/skills/ok-skills`; các thư mục bên trong đã khớp với bố cục mà workflow dựa trên `AGENTS.md` mong đợi.

Nếu bạn đang tìm **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, các playbook **AGENTS.md** có thể tái dùng, hoặc các ví dụ **SKILL.md** thực dụng, repo này được tổ chức để vừa dễ tìm kiếm vừa có thể dùng ngay.

**Các tình huống dùng phổ biến:** tra cứu tài liệu, tự động hóa trình duyệt, debug GitHub Actions, prompt engineering, workflow lập kế hoạch, thiết kế frontend, và xử lý PDF/Word/PPTX/XLSX.

## Repo này phù hợp với ai

- Bạn dùng Codex, Claude Code, Cursor, OpenClaw, Trae hoặc một AI coding agent khác và muốn dùng lại skill thay vì viết prompt ad-hoc.
- Bạn duy trì workflow với `AGENTS.md` / `SKILL.md` và muốn có hướng dẫn có thể dùng xuyên nhiều dự án.
- Bạn cần các skill đã được kiểm chứng cho tra cứu tài liệu, tự động hóa trình duyệt, workflow GitHub, lập kế hoạch, prompt engineering, thiết kế frontend, PDF, tài liệu Office, slide deck và bảng tính.

## Bắt đầu từ đây

Nếu lúc đầu bạn chỉ cài vài skill, hãy bắt đầu với những skill sau:

- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch dựa trên file cho tác vụ phức tạp, nghiên cứu và công việc kéo dài.
- [context7-cli](context7-cli/SKILL.md): lấy tài liệu thư viện mới nhất và các tham chiếu được Context7 hỗ trợ.
- [agent-browser](agent-browser/SKILL.md): tự động hóa trình duyệt cho ảnh chụp màn hình, biểu mẫu, scraping và web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): kiểm tra các check GitHub Actions thất bại và biến log thành kế hoạch sửa lỗi.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): các mẫu prompt hướng production cho workflow LLM đáng tin cậy hơn.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): skill thiết kế frontend chất lượng cao cùng cả bộ lệnh thiết kế đi kèm.

## Quick Start trong 1 phút

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Sau khi clone, repo sẽ nằm tại `~/.agents/skills/ok-skills`, và các thư mục bên trong đã theo đúng bố cục mong đợi:

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

Thêm các quy tắc kích hoạt đơn giản vào `AGENTS.md` của bạn:

```md
## Skills
- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- context7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Sau đó bạn có thể yêu cầu một cách tự nhiên:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Duyệt skills theo trường hợp sử dụng

### Nghiên cứu và tài liệu

- [context7-cli](context7-cli/SKILL.md): workflow Context7 CLI chính thức cho tra cứu tài liệu, quản lý skill và thiết lập MCP.
- [exa-search](exa-search/SKILL.md): nghiên cứu web, code và công ty bằng các công cụ tìm kiếm Exa.
- [get-api-docs](get-api-docs/SKILL.md): lấy tài liệu API và SDK bên thứ ba mới nhất trước khi viết code.
- [find-skills](find-skills/SKILL.md): khám phá các skill sẵn có khi người dùng cần một năng lực cụ thể.

### Lập kế hoạch và prompting

- [brainstorming](brainstorming/SKILL.md): làm rõ ý định, yêu cầu và thiết kế trước khi triển khai.
- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch Markdown bền vững với `task_plan.md`, `findings.md` và `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): các mẫu thiết kế prompt nâng cao cho hệ thống LLM production.
- [subagent-driven-development](subagent-driven-development/SKILL.md): thực thi kế hoạch triển khai với các tác vụ độc lập trong phiên hiện tại bằng subagent mới và các vòng review theo giai đoạn.
- [test-driven-development](test-driven-development/SKILL.md): buộc viết test trước khi triển khai.

### Workflow GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): xử lý comment review và issue trên PR hiện tại bằng `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): kiểm tra các check GitHub Actions thất bại, tóm tắt log và lập kế hoạch sửa.
- [yeet](yeet/SKILL.md): chỉ dùng khi người dùng yêu cầu rõ ràng việc stage, commit, push và mở GitHub pull request trong một luồng dùng `gh`.

### Tự động hóa và QA

- [agent-browser](agent-browser/SKILL.md): tự động hóa trình duyệt cho điều hướng, biểu mẫu, ảnh chụp màn hình và scraping.
- [browser-use](browser-use/SKILL.md): CLI tự động hóa trình duyệt dạng phiên bền vững để điều hướng, kiểm tra trạng thái trang, điền biểu mẫu, chụp màn hình và trích xuất dữ liệu.
- [chrome-cdp](chrome-cdp/SKILL.md): kết nối tới phiên Chrome cục bộ đang mở qua CDP để kiểm tra và tương tác trang nhẹ.
- [bb-browser](bb-browser/SKILL.md): thu thập thông tin và tự động hóa trình duyệt bằng trình duyệt thật cùng trạng thái đăng nhập của người dùng.
- [pinchtab](pinchtab/SKILL.md): điều khiển Chrome qua HTTP API cục bộ của Pinchtab bằng các accessibility ref ổn định.
- [electron](electron/SKILL.md): tự động hóa ứng dụng Electron desktop qua Chrome DevTools Protocol.
- [opencli](opencli/SKILL.md): biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI.
- [dogfood](dogfood/SKILL.md): exploratory testing có cấu trúc cùng bằng chứng có thể tái hiện.

### Frontend và thiết kế

- [ai-elements](ai-elements/SKILL.md): xây dựng các thành phần UI chat AI cho thư viện `ai-elements`.
- [better-icons](better-icons/SKILL.md): tìm kiếm, duyệt và lấy icon SVG từ hơn 200 bộ Iconify qua CLI hoặc MCP.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): hướng dẫn hiệu năng React và Next.js từ Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): hướng dẫn Remotion cho công việc video dựa trên React.
- [`gsap-skills/`](gsap-skills/): 8 skill animation GSAP chính thức (core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks).
- [`impeccable/`](impeccable/README.md): 18 skill thiết kế frontend được vendored, bao gồm `frontend-design`, `adapt`, `audit`, `polish` và nhiều skill khác.

### Tiện ích và biên soạn nội dung

- [docx](docx/SKILL.md): tạo, đọc, chỉnh sửa và xử lý tài liệu Word với định dạng, bình luận và tracked changes.
- [pdf](pdf/SKILL.md): đọc, tạo và rà soát PDF với kiểm tra dựa trên render thực tế.
- [pptx](pptx/SKILL.md): tạo, đọc, chỉnh sửa và xử lý slide deck, template và nội dung thuyết trình.
- [xlsx](xlsx/SKILL.md): tạo và chỉnh sửa bảng tính, công thức và phân tích.
- [skill-creator](skill-creator/SKILL.md): tạo mới hoặc cập nhật skill với cấu trúc và tích hợp công cụ tốt hơn.

## Gói skill vendored

[`impeccable/`](impeccable/README.md) chứa một bundle thiên về thiết kế được vendored từ [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) tại commit `d6b1a56bc5b79e9375be0f8508b4daa1678fb058`.

Gói này bao gồm:

- `frontend-design`: skill thiết kế frontend chủ lực
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Thông tin ghi nhận nguồn gốc và hồ sơ pháp lý được giữ trong [`impeccable/NOTICE.md`](impeccable/NOTICE.md) và [`impeccable/LICENSE`](impeccable/LICENSE).

[`gsap-skills/`](gsap-skills/) chứa một bundle animation được vendored từ [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) tại commit `4300e310513b0ddc0b121a5c0e0bd2e5c2325ff2`.

Gói này bao gồm:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

Thông tin ghi nhận nguồn gốc và hồ sơ pháp lý được giữ trong [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) và [`gsap-skills/LICENSE`](gsap-skills/LICENSE).

## Các điều kiện tiên quyết phổ biến

- Một số skill giả định rằng `gh` đã được cài đặt và đăng nhập.
- Các skill thiên về trình duyệt có thể cần môi trường hỗ trợ Chrome/CDP.
- Các skill tra cứu tài liệu bên thứ ba có thể phụ thuộc vào CLI hoặc công cụ MCP bên ngoài; hãy kiểm tra từng `SKILL.md` để biết chi tiết.

## Chỉ mục đầy đủ của skill

Cột `Source URL` trỏ tới upstream chính thức khi một skill được vendored/imported; nếu không, nó sẽ trỏ tới thư mục skill trong repo này.

### Top-Level Skills

| Skill | Mô tả | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | CLI tự động hóa trình duyệt cho AI agents: điều hướng, điền biểu mẫu, chụp màn hình, trích xuất và kiểm thử web. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | Tạo các thành phần giao diện chat AI mới cho thư viện ai-elements với mô hình composable và quy ước shadcn/ui. | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [bb-browser](bb-browser/SKILL.md) | Skill thu thập thông tin và tự động hóa trình duyệt bằng trình duyệt thật cùng trạng thái đăng nhập của người dùng, áp dụng cho trang công khai, hệ thống nội bộ và luồng sau đăng nhập. | [epiral/bb-browser](https://github.com/epiral/bb-browser/tree/main/skills/bb-browser) |
| [better-icons](better-icons/SKILL.md) | Tìm trong hơn 200 bộ Iconify và lấy icon SVG qua CLI hoặc công cụ MCP. | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills) |
| [brainstorming](brainstorming/SKILL.md) | Làm rõ ý định, yêu cầu và thiết kế trước khi triển khai. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [browser-use](browser-use/SKILL.md) | CLI tự động hóa trình duyệt dạng phiên bền vững để điều hướng, kiểm tra trạng thái trang, điền biểu mẫu, chụp màn hình và trích xuất dữ liệu. | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use) |
| [chrome-cdp](chrome-cdp/SKILL.md) | Kết nối tới phiên Chrome cục bộ đang mở qua CDP để kiểm tra tab nhẹ, chụp màn hình, truy cập DOM, nhập liệu và điều hướng. | [pasky/chrome-cdp-skill](https://github.com/pasky/chrome-cdp-skill/tree/main/skills/chrome-cdp) |
| [context7-cli](context7-cli/SKILL.md) | Dùng Context7 CLI để tra cứu tài liệu, quản lý skill và thiết lập MCP. | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | Tạo, đọc, chỉnh sửa và xử lý tài liệu Word với định dạng, bình luận, tracked changes và cập nhật hình ảnh. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | Kiểm thử web app một cách có hệ thống và tạo báo cáo lỗi có thể tái hiện với ảnh chụp và video. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | Tự động hóa ứng dụng Electron desktop thông qua agent-browser và Chrome DevTools Protocol. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | Dùng Exa cho nghiên cứu web, code và công ty. | Custom |
| [find-skills](find-skills/SKILL.md) | Khám phá các skill hiện có khi người dùng cần những năng lực chuyên biệt. | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | Lấy tài liệu API hoặc SDK bên thứ ba hiện tại trước khi viết code. | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | Xử lý comment review PR và issue trên nhánh hiện tại bằng `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | Kiểm tra các check GitHub Actions thất bại, kéo log và lập kế hoạch sửa. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [opencli](opencli/SKILL.md) | Biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI. | [jackwener/opencli](https://github.com/jackwener/opencli) |
| [pdf](pdf/SKILL.md) | Đọc, tạo và rà soát PDF với kiểm tra render và công cụ Python. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | Điều khiển Chrome headless hoặc headed qua HTTP API của Pinchtab cho tự động hóa web, scraping, điền biểu mẫu, điều hướng, ảnh chụp màn hình và trích xuất bằng accessibility ref ổn định. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | Lập kế hoạch dựa trên file cho các tác vụ phức tạp bằng `task_plan.md`, `findings.md` và `progress.md`. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | Tạo, đọc, chỉnh sửa và xử lý bản trình bày PowerPoint, template, layout, note và nội dung slide. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Các mẫu prompt engineering nâng cao cho workflow LLM đáng tin cậy trong production. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | Best practices để xây dựng video trong React với Remotion. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | Hướng dẫn tạo mới hoặc cập nhật skill với tri thức chuyên biệt và tích hợp công cụ. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [subagent-driven-development](subagent-driven-development/SKILL.md) | Thực thi kế hoạch triển khai với các tác vụ độc lập trong phiên hiện tại bằng subagent mới và các vòng review theo giai đoạn. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) |
| [test-driven-development](test-driven-development/SKILL.md) | Dùng trước khi triển khai bất kỳ tính năng hay bugfix nào. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | Hướng dẫn tối ưu hiệu năng React và Next.js từ Vercel Engineering. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | Tạo và chỉnh sửa bảng tính, công thức, định dạng và phân tích. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | Chỉ dùng khi người dùng yêu cầu rõ ràng việc stage, commit, push và mở GitHub pull request trong một luồng dùng `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendored `impeccable/` Skills

| Skill | Mô tả | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | Tạo giao diện frontend có bản sắc và chất lượng production cao. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | Điều chỉnh thiết kế cho nhiều kích thước màn hình, thiết bị và bối cảnh khác nhau. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | Thêm motion có chủ đích và micro-interaction. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | Audit chất lượng giao diện về accessibility, performance, theming và responsive design. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | Làm các thiết kế an toàn hoặc nhàm chán trở nên thú vị hơn về mặt thị giác. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | Cải thiện UX copy và hướng dẫn chưa rõ ràng. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | Thêm màu sắc có chiến lược cho các giao diện quá đơn sắc. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | Đánh giá hiệu quả thiết kế từ góc nhìn UX. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | Thêm cá tính và những điểm nhấn đáng nhớ cho giao diện. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | Chắt lọc thiết kế về dạng cốt lõi nhất. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | Gom và hợp nhất các component, token và pattern có thể tái sử dụng vào design system. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | Tăng độ bền vững quanh lỗi, i18n, tràn nội dung và các edge case. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | Chuẩn hóa một tính năng để khớp với design system. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | Thiết kế hoặc cải thiện onboarding và trải nghiệm lần đầu sử dụng. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | Cải thiện hiệu năng frontend, rendering, motion và hiệu quả bundle. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | Bước hoàn thiện cuối để chỉnh căn lề, khoảng cách, tính nhất quán và chi tiết. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | Giảm độ gắt về thị giác nhưng vẫn giữ chất lượng thiết kế. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Thu thập bối cảnh thiết kế và lưu lại làm hướng dẫn lâu dài cho công việc sau này. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### Vendored `gsap-skills/` Skills

| Skill | Mô tả | Source URL |
| --- | --- | --- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md) | Core API: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core) |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md) | Timeline: sắp xếp chuỗi, position parameter, labels, nesting, playback. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline) |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: animation liên kết cuộn, pinning, scrub, triggers, refresh, cleanup. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md) | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase, v.v. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins) |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md) | gsap.utils helpers: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils) |
| [gsap-react](gsap-skills/gsap-react/SKILL.md) | React: useGSAP, refs, `gsap.context()`, cleanup, SSR. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react) |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md) | Performance: transforms, will-change, batching, ScrollTrigger tips. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance) |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md) | Vue, Svelte, etc.: lifecycle, scoping selectors, cleanup khi unmount. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks) |

## Đóng góp

Chúng tôi hoan nghênh đóng góp cho các skill mới hoặc cải tiến skill hiện có.

1. Giữ điều kiện kích hoạt rõ ràng và có thể kiểm chứng.
2. Giữ ví dụ ngắn gọn và thiên về thực thi.
3. Nếu một skill phụ thuộc vào công cụ bên ngoài, hãy ghi rõ phụ thuộc đó trong `SKILL.md`.
4. Cập nhật `README.md` và `README.zh-CN.md` khi bạn thêm hoặc đổi tên skill, đồng thời làm mới các README bản dịch khác khi chỉ mục skill công khai thay đổi.

## Giấy phép

Repo này được cấp phép theo [LICENSE](LICENSE).

Một số skill có thêm file giấy phép hoặc ghi nhận nguồn cho tài sản và attribution riêng, bao gồm [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), [`skill-creator/`](skill-creator/) và [`xlsx/`](xlsx/).
