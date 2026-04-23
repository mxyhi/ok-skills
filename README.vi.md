# OK Skills: bộ AI coding agent skills cho Codex, Claude Code, Cursor, OpenClaw và hơn thế nữa

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | Tiếng Việt | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Bộ sưu tập AI coding agent skills và playbook `AGENTS.md` được tuyển chọn cho Codex, Claude Code, Cursor, OpenClaw, Trae và các công cụ khác tương thích với `SKILL.md`.

Kho này hiện gồm **40 skill có thể tái sử dụng**: **27 skill cấp cao nhất** được duy trì trực tiếp trong repo này, cùng với **5 skill video HyperFrames được vendored** dưới [`hyperframes/`](hyperframes/README.md) và **8 skill animation GSAP được vendored** dưới [`gsap-skills/`](gsap-skills/). Chỉ cần clone vào `~/.agents/skills/ok-skills`; các thư mục bên trong đã khớp với bố cục mà workflow dựa trên `AGENTS.md` mong đợi.

Nếu bạn đang tìm **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, các playbook **AGENTS.md** có thể tái dùng, hoặc các ví dụ **SKILL.md** thực dụng, repo này được tổ chức để vừa dễ tìm kiếm vừa có thể dùng ngay.

**Các tình huống dùng phổ biến:** tra cứu tài liệu, tự động hóa trình duyệt, debug GitHub Actions, prompt engineering, workflow lập kế hoạch, thiết kế frontend, và xử lý PDF/Word/PPTX/XLSX.

## Repo này phù hợp với ai

- Bạn dùng Codex, Claude Code, Cursor, OpenClaw, Trae hoặc một AI coding agent khác và muốn dùng lại skill thay vì viết prompt ad-hoc.
- Bạn duy trì workflow với `AGENTS.md` / `SKILL.md` và muốn có hướng dẫn có thể dùng xuyên nhiều dự án.
- Bạn cần các skill đã được kiểm chứng cho tra cứu tài liệu, tự động hóa trình duyệt, workflow GitHub, lập kế hoạch, prompt engineering, thiết kế frontend, PDF, tài liệu Office, slide deck và bảng tính.

## Bắt đầu từ đây

Nếu lúc đầu bạn chỉ cài vài skill, hãy bắt đầu với những skill sau:

- [brainstorming](brainstorming/SKILL.md): làm rõ ý tưởng, yêu cầu và thiết kế trước khi bắt đầu triển khai.
- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch dựa trên file cho tác vụ phức tạp, nghiên cứu và công việc kéo dài.
- [context7-cli](context7-cli/SKILL.md): lấy tài liệu thư viện mới nhất và các tham chiếu được Context7 hỗ trợ.
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

- [brainstorming](brainstorming/SKILL.md): làm rõ ý tưởng, yêu cầu và thiết kế trước khi bắt đầu triển khai.
- [planning-with-files](planning-with-files/SKILL.md): lập kế hoạch Markdown bền vững với `task_plan.md`, `findings.md` và `progress.md`.
- [test-driven-development](test-driven-development/SKILL.md): buộc viết test trước khi triển khai.
- [systematic-debugging](systematic-debugging/SKILL.md): điều tra có hệ thống nguyên nhân gốc của bug, test lỗi hoặc hành vi bất thường trước khi đề xuất cách sửa.

### Workflow GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): xử lý comment review và issue trên PR hiện tại bằng `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): kiểm tra các check GitHub Actions thất bại, tóm tắt log và lập kế hoạch sửa.
- [yeet](yeet/SKILL.md): chỉ dùng khi người dùng yêu cầu rõ ràng việc stage, commit, push và mở GitHub pull request trong một luồng dùng `gh`.

### Tự động hóa và QA

- [agent-browser](agent-browser/SKILL.md): tự động hóa trình duyệt cho điều hướng, biểu mẫu, ảnh chụp màn hình và scraping.
- [browser-use](browser-use/SKILL.md): CLI tự động hóa trình duyệt dạng phiên bền vững để điều hướng, kiểm tra trạng thái trang, điền biểu mẫu, chụp màn hình và trích xuất dữ liệu.
- [opencli](opencli/opencli-usage/SKILL.md): biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI.

- [dogfood](dogfood/SKILL.md): exploratory testing có cấu trúc cùng bằng chứng có thể tái hiện.
- [electron](electron/SKILL.md): tự động hóa ứng dụng Electron desktop qua Chrome DevTools Protocol.

`dogfood/` và `electron/` vẫn được vendored từ `vercel-labs/agent-browser`, nhưng upstream đã chuyển chúng từ `skills/` sang `skill-data/` trong commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` để logic discovery của installer chỉ lộ ra skill bootstrap `agent-browser`. Repo này vẫn giữ các specialized skills đó ở cấp top-level vì upstream vẫn đang duy trì chúng và chúng vẫn hữu dụng trực tiếp.

### Frontend và thiết kế

- [ai-elements](ai-elements/SKILL.md): xây dựng các thành phần UI chat AI cho thư viện `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): dùng khi cần landing page, website, ứng dụng, prototype, demo hoặc UI game có thị giác mạnh.
- [shader-dev](shader-dev/SKILL.md): kỹ thuật GLSL toàn diện cho hiệu ứng hình ảnh thời gian thực tương thích ShaderToy.
- [better-icons](better-icons/SKILL.md): tìm kiếm, duyệt và lấy icon SVG từ hơn 200 bộ Iconify qua CLI hoặc MCP.
- [remotion-best-practices](remotion-best-practices/SKILL.md): hướng dẫn Remotion cho công việc video dựa trên React.
- [`gsap-skills/`](gsap-skills/): 8 skill animation GSAP chính thức (core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks).

### Video & Motion

- [hyperframes](hyperframes/hyperframes/SKILL.md): create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and scene transitions.
- [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md): scaffold, lint, preview, render, transcribe, and troubleshoot HyperFrames projects.
- [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md): install registry blocks and components, then wire them into compositions.
- [gsap](hyperframes/gsap/SKILL.md): HyperFrames-focused GSAP reference for timelines, easing, effects, and performance.
- [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md): capture a website and turn it into a scripted HyperFrames promo or product video.

### Tiện ích và biên soạn nội dung

- [minimax-docx](minimax-docx/SKILL.md): tạo, chỉnh sửa và định dạng DOCX chuyên nghiệp với OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): tạo, điền và tái định dạng tài liệu PDF bằng hệ thiết kế token.
- [pptx-generator](pptx-generator/SKILL.md): tạo, chỉnh sửa và đọc bản trình bày PowerPoint bằng PptxGenJS, luồng XML hoặc markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): mở, tạo, đọc, phân tích, chỉnh sửa và kiểm tra tệp Excel/bảng tính với quy trình XML ít mất mát.

## Gói skill vendored

[`gsap-skills/`](gsap-skills/) chứa một bundle animation được vendored từ [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) tại commit `03d9f0c3dbf91e0b60582b64ed040c8911ca0174`.

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

| Skill                                                               | Mô tả                                                                                                                                                                                      | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | CLI tự động hóa trình duyệt cho AI agents: điều hướng, điền biểu mẫu, chụp màn hình, trích xuất và kiểm thử web.                                                                           | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Tạo các thành phần giao diện chat AI mới cho thư viện ai-elements với mô hình composable và quy ước shadcn/ui.                                                                             | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | Tìm trong hơn 200 bộ Iconify và lấy icon SVG qua CLI hoặc công cụ MCP.                                                                                                                     | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Biến ý tưởng thành thiết kế và đặc tả đã được xác nhận thông qua đối thoại cộng tác trước khi triển khai.                                                                                | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | CLI tự động hóa trình duyệt dạng phiên bền vững để điều hướng, kiểm tra trạng thái trang, điền biểu mẫu, chụp màn hình và trích xuất dữ liệu.                                              | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Che do giao tiep sieu nen, tra loi kieu nguoi toi co de giam token nhung van giu do chinh xac ky thuat.                                                                                    | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | Dùng Context7 CLI để tra cứu tài liệu, quản lý skill và thiết lập MCP.                                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | Tạo, chỉnh sửa và định dạng DOCX chuyên nghiệp với OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Dùng Exa cho nghiên cứu web, code và công ty.                                                                                                                                              | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Khám phá các skill hiện có khi người dùng cần những năng lực chuyên biệt.                                                                                                                  | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Tạo landing page, website, ứng dụng, prototype, demo hoặc UI game có thị giác mạnh.                                                                                                        | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Kỹ thuật GLSL toàn diện cho hiệu ứng hình ảnh thời gian thực tương thích ShaderToy. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Lấy tài liệu API hoặc SDK bên thứ ba hiện tại trước khi viết code.                                                                                                                         | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Xử lý comment review PR và issue trên nhánh hiện tại bằng `gh`.                                                                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Kiểm tra các check GitHub Actions thất bại, kéo log và lập kế hoạch sửa.                                                                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Lấy mã nguồn của dependency để cung cấp cho AI agents bối cảnh triển khai sâu hơn.                                                                                                         | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Biến website thành lệnh CLI bằng cách tái sử dụng phiên đăng nhập trình duyệt, truy cập API công khai và sinh adapter bằng AI.                                                             | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Kiểm thử web app một cách có hệ thống và tạo báo cáo lỗi có thể tái hiện với ảnh chụp và video.                                                                                            | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Tự động hóa ứng dụng Electron desktop thông qua agent-browser và Chrome DevTools Protocol.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Tạo, điền và tái định dạng tài liệu PDF bằng hệ thiết kế token. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Lập kế hoạch dựa trên file cho các tác vụ phức tạp bằng `task_plan.md`, `findings.md` và `progress.md`.                                                                                    | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | Tạo, chỉnh sửa và đọc bản trình bày PowerPoint bằng PptxGenJS, luồng XML hoặc markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Best practices để xây dựng video trong React với Remotion.                                                                                                                                 | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [test-driven-development](test-driven-development/SKILL.md)         | Dùng trước khi triển khai bất kỳ tính năng hay bugfix nào.                                                                                                                                 | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Dùng khi gặp bug, test lỗi hoặc hành vi bất thường, trước khi đề xuất cách sửa.                                                             | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Mở, tạo, đọc, phân tích, chỉnh sửa và kiểm tra tệp Excel/bảng tính với quy trình XML ít mất mát. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Chỉ dùng khi người dùng yêu cầu rõ ràng việc stage, commit, push và mở GitHub pull request trong một luồng dùng `gh`.                                                                      | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Ghi chú:
- `dogfood` và `electron` đến từ `skill-data/` của upstream, không phải `skills/`.
- Upstream đã chuyển các specialized skills này trong commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` để installer discovery chỉ tìm thấy skill bootstrap `agent-browser`.
- Repo này cố ý giữ chúng như các vendored top-level skills vì upstream vẫn duy trì và chúng vẫn hữu dụng trực tiếp.

### Vendored `hyperframes/` Skills

| Skill | Description | Source URL |
| --- | --- | --- |
| [hyperframes](hyperframes/hyperframes/SKILL.md) | Create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and transitions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes) |
| [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md) | CLI workflow for HyperFrames: init, lint, preview, render, transcribe, TTS, and environment diagnosis. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-cli) |
| [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md) | Install registry blocks/components and wire them into HyperFrames compositions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-registry) |
| [gsap](hyperframes/gsap/SKILL.md) | HyperFrames-focused GSAP reference for timelines, easing, effects, and performance. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/gsap) |
| [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md) | Capture a website and turn it into a HyperFrames video workflow with design, script, storyboard, voiceover, and build steps. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/website-to-hyperframes) |

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

Một số skill có thêm file giấy phép hoặc ghi nhận nguồn cho tài sản và attribution riêng, bao gồm [`minimax-docx/`](minimax-docx/) và [`gsap-skills/`](gsap-skills/).
