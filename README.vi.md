# OK Skills: bộ AI coding agent skills cho Codex, Claude Code, Cursor, OpenClaw và hơn thế nữa

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | Tiếng Việt | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Bộ sưu tập AI coding agent skills và playbook `CLAUDE.md` / `AGENTS.md` được tuyển chọn cho Codex, Claude Code, Cursor, OpenClaw, Trae và các công cụ khác tương thích với `SKILL.md`.

Kho này hiện gồm **41 skill có thể tái sử dụng**: **33 skill cấp cao nhất** được duy trì trực tiếp trong repo này, cùng với **8 skill animation GSAP được vendored** dưới [`gsap-skills/`](gsap-skills/). Chỉ cần clone vào `~/.agents/skills/ok-skills`; các thư mục bên trong đã khớp với bố cục mà workflow dựa trên `AGENTS.md` mong đợi, và [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) cung cấp agent playbook hướng tới Claude Code.

Nếu bạn đang tìm **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, các playbook **CLAUDE.md / AGENTS.md** có thể tái dùng, hoặc các ví dụ **SKILL.md** thực dụng, repo này được tổ chức để vừa dễ tìm kiếm vừa có thể dùng ngay.

**Các tình huống dùng phổ biến:** tra cứu tài liệu, tự động hóa trình duyệt, debug GitHub Actions, prompt engineering, workflow lập kế hoạch, thiết kế frontend, và xử lý PDF/Word/PPTX/XLSX.

## Repo này phù hợp với ai

- Bạn dùng Codex, Claude Code, Cursor, OpenClaw, Trae hoặc một AI coding agent khác và muốn dùng lại skill thay vì viết prompt ad-hoc.
- Bạn duy trì workflow với `CLAUDE.md` / `AGENTS.md` / `SKILL.md` và muốn có hướng dẫn có thể dùng xuyên nhiều dự án.
- Bạn cần các skill đã được kiểm chứng cho tra cứu tài liệu, tự động hóa trình duyệt, workflow GitHub, lập kế hoạch, prompt engineering, thiết kế frontend, PDF, tài liệu Office, slide deck và bảng tính.

## Bắt đầu từ đây

Nếu lúc đầu bạn chỉ cài vài skill, hãy bắt đầu với những skill sau:

- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch dựa trên file cho tác vụ phức tạp, nghiên cứu và công việc kéo dài.
- [find-docs](find-docs/SKILL.md): lấy tài liệu thư viện mới nhất, tham chiếu API và ví dụ được Context7 hỗ trợ.
- [agent-browser](agent-browser/SKILL.md): tự động hóa trình duyệt cho ảnh chụp màn hình, biểu mẫu, scraping và web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): kiểm tra các check GitHub Actions thất bại và biến log thành kế hoạch sửa lỗi.

## Quick Start trong 1 phút

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Sau khi clone, repo sẽ nằm tại `~/.agents/skills/ok-skills`, và các thư mục bên trong đã theo đúng bố cục mong đợi:

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

Với chỉ dẫn toàn cục cho Claude Code hoặc Codex, hãy bắt đầu từ [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md), rồi sao chép hoặc gộp vào `CLAUDE.md` của Claude Code hoặc `AGENTS.md` của Codex. File này đóng gói workflow Chinese-first, theo KISS, kiểm tra tài liệu/source mới nhất, ưu tiên multi-agent, bật mặc định `caveman` / `planning-with-files` / `karpathy-guidelines`, kỳ vọng TypeScript nghiêm ngặt và quy tắc định tuyến context-mode. Trước khi tái sử dụng, hãy chỉnh phần `语言要求` cho dự án của bạn. Phần `其他注意项` là cấu hình cục bộ theo dự án và có thể chỉnh khi cần.

Thêm các quy tắc kích hoạt đơn giản vào `AGENTS.md` của bạn, hoặc gộp cùng các trigger skill đó vào `CLAUDE.md` / `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- find-docs: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Sau đó bạn có thể yêu cầu một cách tự nhiên:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Duyệt skills theo trường hợp sử dụng

### Nghiên cứu và tài liệu

- [find-docs](find-docs/SKILL.md): workflow Context7 CLI tập trung vào tra cứu tài liệu mới nhất.
- [exa-search](exa-search/SKILL.md): nghiên cứu web, code và công ty bằng các công cụ tìm kiếm Exa.
- [get-api-docs](get-api-docs/SKILL.md): lấy tài liệu API và SDK bên thứ ba mới nhất trước khi viết code.
- [find-skills](find-skills/SKILL.md): khám phá các skill sẵn có khi người dùng cần một năng lực cụ thể.

### Lập kế hoạch và prompting

- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch Markdown bền vững với `task_plan.md`, `findings.md` và `progress.md`.
- [autoresearch](autoresearch/SKILL.md): vòng lặp tự động theo mục tiêu với goal, metric, verify loop và keep/discard gate rõ ràng.
- [diagnose](diagnose/SKILL.md): vong lap chan doan co ky luat cho bug kho va regression hieu nang.
- [grill-me](grill-me/SKILL.md): hoi tung cau de stress-test plan hoac design den khi dat hieu biet chung.
- [grill-with-docs](grill-with-docs/SKILL.md): doi chieu plan voi domain language, `CONTEXT.md`, ADR va cap nhat docs inline.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): tìm cơ hội architecture deepening giúp tăng locality, leverage, testability và AI navigation.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): hướng dẫn hành vi coding giúp giảm overcomplication, giả định ẩn và thay đổi không kiểm chứng được.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migrate `as` type assertions trong test sang `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): test-first red-green-refactor cho tính năng, bugfix, refactor và thay đổi hành vi.
- [systematic-debugging](systematic-debugging/SKILL.md): điều tra có hệ thống nguyên nhân gốc của bug, test lỗi hoặc hành vi bất thường trước khi đề xuất cách sửa.

### Workflow GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): xử lý comment review và issue trên PR hiện tại bằng `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): kiểm tra các check GitHub Actions thất bại, tóm tắt log và lập kế hoạch sửa.

### Tự động hóa và QA

- [agent-browser](agent-browser/SKILL.md): tự động hóa trình duyệt cho điều hướng, biểu mẫu, ảnh chụp màn hình và scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): điều khiển trình duyệt thật của người dùng qua daemon cục bộ để điều hướng, điền biểu mẫu, chụp màn hình, đọc trang và dùng phiên đã đăng nhập.
- [browser-trace](browser-trace/SKILL.md): ghi lại CDP trace, ảnh chụp màn hình và DOM dump cho quá trình gỡ lỗi tự động hóa trình duyệt.
- [opencli](opencli/opencli-usage/SKILL.md): biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI.

- [dogfood](dogfood/SKILL.md): exploratory testing có cấu trúc cùng bằng chứng có thể tái hiện.
- [electron](electron/SKILL.md): tự động hóa ứng dụng Electron desktop qua Chrome DevTools Protocol.

`dogfood/` và `electron/` vẫn được vendored từ `vercel-labs/agent-browser`, nhưng upstream đã chuyển chúng từ `skills/` sang `skill-data/` trong commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` để logic discovery của installer chỉ lộ ra skill bootstrap `agent-browser`. Repo này vẫn giữ các specialized skills đó ở cấp top-level vì upstream vẫn đang duy trì chúng và chúng vẫn hữu dụng trực tiếp.

### Frontend và thiết kế

- [ai-elements](ai-elements/SKILL.md): xây dựng các thành phần UI chat AI cho thư viện `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): dùng khi cần landing page, website, ứng dụng, prototype, demo hoặc UI game có thị giác mạnh.
- [huashu-design](huashu-design/SKILL.md): tạo prototype HTML độ trung thực cao, demo tương tác, slide deck, motion design, biến thể thiết kế, video export và design critique.
- [shader-dev](shader-dev/SKILL.md): kỹ thuật GLSL toàn diện cho hiệu ứng hình ảnh thời gian thực tương thích ShaderToy.
- [better-icons](better-icons/SKILL.md): tìm kiếm, duyệt và lấy icon SVG từ hơn 200 bộ Iconify qua CLI hoặc MCP.
- [`gsap-skills/`](gsap-skills/): 8 skill animation GSAP chính thức (core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks).

### Tiện ích và biên soạn nội dung

- [minimax-docx](minimax-docx/SKILL.md): tạo, chỉnh sửa và định dạng DOCX chuyên nghiệp với OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): tạo, điền và tái định dạng tài liệu PDF bằng hệ thiết kế token.
- [pptx-generator](pptx-generator/SKILL.md): tạo, chỉnh sửa và đọc bản trình bày PowerPoint bằng PptxGenJS, luồng XML hoặc markitdown.
- [huashu-design](huashu-design/SKILL.md): tạo HTML deck, PPTX chỉnh sửa được, MP4/GIF motion pieces và video thiết kế có narration.
- [minimax-xlsx](minimax-xlsx/SKILL.md): mở, tạo, đọc, phân tích, chỉnh sửa và kiểm tra tệp Excel/bảng tính với quy trình XML ít mất mát.

## Gói skill vendored

[`gsap-skills/`](gsap-skills/) chứa một bundle animation được vendored từ [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) tại commit `aed9cfd3277740755f6bfc1155c7aa645403b760`.

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

[`planning-with-files/`](planning-with-files/) dùng [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files) làm upstream baseline. Repo này dùng thư mục upstream đó làm baseline canonical cho skill cục bộ. Khac biet cuc bo chi gom giu ten skill cong khai `planning-with-files` va chuan hoa frontmatter `SKILL.md` de tuong thich `skills-ref`.

## Các điều kiện tiên quyết phổ biến

- Một số skill giả định rằng `gh` đã được cài đặt và đăng nhập.
- Các skill thiên về trình duyệt có thể cần môi trường hỗ trợ Chrome/CDP.
- Các skill tra cứu tài liệu bên thứ ba có thể phụ thuộc vào CLI hoặc công cụ MCP bên ngoài; hãy kiểm tra từng `SKILL.md` để biết chi tiết.

## Chỉ mục đầy đủ của skill

Cột `Source URL` trỏ tới upstream chính thức khi một skill được vendored/imported; nếu không, nó sẽ trỏ tới thư mục skill trong repo này.

### Top-Level Skills

| Skill                                                               | Mô tả                                                                                                                                                                                      | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | CLI tự động hóa trình duyệt cho AI agents: điều hướng, điền biểu mẫu, chụp màn hình, trích xuất và kiểm thử web.                                                                           | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Tạo các thành phần giao diện chat AI mới cho thư viện ai-elements với mô hình composable và quy ước shadcn/ui.                                                                             | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | Engine lặp tự động theo mục tiêu cho workflow modify, verify, keep/discard và repeat.                                                                                                    | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Tìm trong hơn 200 bộ Iconify và lấy icon SVG qua CLI hoặc công cụ MCP.                                                                                                                     | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Điều khiển trình duyệt thật của người dùng qua daemon cục bộ để điều hướng, điền biểu mẫu, chụp màn hình, đọc trang và dùng phiên đã đăng nhập.                                           | [install.sh](https://kimi-web-img.moonshot.cn/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Ghi lại CDP trace, ảnh chụp màn hình và DOM dump để gỡ lỗi tự động hóa trình duyệt.                                                                                  | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Che do giao tiep sieu nen, tra loi kieu nguoi toi co de giam token nhung van giu do chinh xac ky thuat.                                                                                    | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnose](diagnose/SKILL.md)                                   | Vong lap chan doan co ky luat cho bug kho va regression hieu nang.                                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnose)                                |
| [find-docs](find-docs/SKILL.md)                                     | Dùng Context7 CLI để tra cứu tài liệu mới nhất, tham chiếu API và ví dụ mã.                                                                                                                | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Tạo, chỉnh sửa và định dạng DOCX chuyên nghiệp với OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Dùng Exa cho nghiên cứu web, code và công ty.                                                                                                                                              | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Khám phá các skill hiện có khi người dùng cần những năng lực chuyên biệt.                                                                                                                  | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Tạo landing page, website, ứng dụng, prototype, demo hoặc UI game có thị giác mạnh.                                                                                                        | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [huashu-design](huashu-design/SKILL.md)                           | Tạo prototype HTML độ trung thực cao, demo tương tác, slide deck, motion design, biến thể thiết kế, video export và design critique.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [shader-dev](shader-dev/SKILL.md) | Kỹ thuật GLSL toàn diện cho hiệu ứng hình ảnh thời gian thực tương thích ShaderToy. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Lấy tài liệu API hoặc SDK bên thứ ba hiện tại trước khi viết code.                                                                                                                         | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Xử lý comment review PR và issue trên nhánh hiện tại bằng `gh`.                                                                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Kiểm tra các check GitHub Actions thất bại, kéo log và lập kế hoạch sửa.                                                                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [grill-me](grill-me/SKILL.md)                                 | Phong van lien tuc ve plan hoac design cho den khi dat hieu biet chung.                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)                                |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | Stress-test plan voi domain language, `CONTEXT.md`, ADR va cap nhat tai lieu inline.                                                               | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Tìm cơ hội architecture deepening giúp tăng locality, leverage, testability và AI navigation.                                                                                                | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Hướng dẫn hành vi coding giúp giảm overcomplication, giả định ẩn và thay đổi không kiểm chứng được.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migrate file test từ `as` type assertions sang `@total-typescript/shoehorn`.                                                                                                                | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | Lấy mã nguồn của dependency để cung cấp cho AI agents bối cảnh triển khai sâu hơn.                                                                                                         | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI.                                                             | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Kiểm thử web app một cách có hệ thống và tạo báo cáo lỗi có thể tái hiện với ảnh chụp và video.                                                                                            | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Tự động hóa ứng dụng Electron desktop thông qua agent-browser và Chrome DevTools Protocol.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Tạo, điền và tái định dạng tài liệu PDF bằng hệ thiết kế token. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Lập kế hoạch dựa trên file cho các tác vụ phức tạp bằng `task_plan.md`, `findings.md` và `progress.md`.                                                                                    | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | Tạo, chỉnh sửa và đọc bản trình bày PowerPoint bằng PptxGenJS, luồng XML hoặc markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Dùng trước tính năng, bugfix, refactor hoặc thay đổi hành vi; ưu tiên integration-style tests qua public interface.                                                                          | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Dùng khi gặp bug, test lỗi hoặc hành vi bất thường, trước khi đề xuất cách sửa.                                                             | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Mở, tạo, đọc, phân tích, chỉnh sửa và kiểm tra tệp Excel/bảng tính với quy trình XML ít mất mát. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |

Ghi chú:
- `dogfood` và `electron` đến từ `skill-data/` của upstream, không phải `skills/`.
- Upstream đã chuyển các specialized skills này trong commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` để installer discovery chỉ tìm thấy skill bootstrap `agent-browser`.
- Repo này cố ý giữ chúng như các vendored top-level skills vì upstream vẫn duy trì và chúng vẫn hữu dụng trực tiếp.

### Vendored `gsap-skills/` Skills

| Skill                                                         | Mô tả                                                                                           | Source URL                                                                                            |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | Core API: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timeline: sắp xếp chuỗi, position parameter, labels, nesting, playback.                         | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: animation liên kết cuộn, pinning, scrub, triggers, refresh, cleanup.             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase, v.v.                          | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils helpers: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.              | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, refs, `gsap.context()`, cleanup, SSR.                                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Performance: transforms, will-change, batching, ScrollTrigger tips.                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte, etc.: lifecycle, scoping selectors, cleanup khi unmount.                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Đóng góp

Chúng tôi hoan nghênh đóng góp cho các skill mới hoặc cải tiến skill hiện có.

1. Giữ điều kiện kích hoạt rõ ràng và có thể kiểm chứng.
2. Giữ ví dụ ngắn gọn và thiên về thực thi.
3. Nếu một skill phụ thuộc vào công cụ bên ngoài, hãy ghi rõ phụ thuộc đó trong `SKILL.md`.
4. Cập nhật `README.md` và `README.zh-CN.md` khi bạn thêm hoặc đổi tên skill, đồng thời làm mới các README bản dịch khác khi chỉ mục skill công khai thay đổi.

## Giấy phép

Repo này được cấp phép theo [LICENSE](LICENSE).

Một số skill có thêm file giấy phép hoặc ghi nhận nguồn cho tài sản và attribution riêng, bao gồm [`improve-codebase-architecture/`](improve-codebase-architecture/), [`migrate-to-shoehorn/`](migrate-to-shoehorn/), [`huashu-design/`](huashu-design/), [`minimax-docx/`](minimax-docx/) và [`gsap-skills/`](gsap-skills/).
