# 设计风格库：网页 20 种 + PPT 20 种（HTML 原生优先）

> **2026-06 重构**。基于对全球 10 大网站类型 + 10 大演示类型、各 top5 公认最佳设计（共 100 个真实案例）的调研反推。
> 旧版 20 种「平面/装置设计师哲学」库的致命问题：大胆风格几乎全是 AI-生成-only（粒子/光影/手绘），**用户默认无生图能力、default 全走 HTML 时，大胆半场直接清零，只剩极简——这是「default 千篇一律」的根因**。本库每一种都标了「纯 HTML/CSS 无生图」下的**还原度**。
>
> ⚖️ **但记住定位**：这是**「没思路时翻的弹药」，不是「必须从这里选」的清单**。用户给了内容/品牌/参考，设计就从那里展开，别套库。skill 的职责是帮用户规避最差，不是规定好设计长什么样——好设计从用户的真实需求里长出来。

## 这个库怎么用

1. **先按输出类型选半区**：做网页/落地页/官网 → 网页 20 种；做 PPT/deck/演示 → PPT 20 种。
2. **温度体系**：每种标了 `大胆 / 中性 / 安静`。**故意让大胆款占多数**——模型的确定性偏差天然偏安静极简，库的配比要把它往大胆推。
   - 方向 A（稳妥底盘）从安静/中性里按需求选；方向 B 取不同温度拉反差；**方向 C 由 SKILL 的「秒数轮盘」强制注入大胆款**。
   - ❌ 三个方向不要都落在「米白+留白+一个点缀色」——那是最常见的失败模式。
3. **还原度**：≥90% 闭眼做；70-90% 主体可做、个别细节降级；<70%（如 Memphis 做旧纹理）必须在产出里**明确标注哪部分用纯色块降级**，不假装能做出原版质感。
4. **字体**：每种给了开源替代（Inter/Geist/Manrope/Space Grotesk/Fraunces/Playfair 等），不要写付费字体（Söhne/Circular 等）。
5. 配套：SKILL「设计方向顾问」Phase 3-5 用本库推 3 方向；`assets/showcases/` 有预制截图画廊。

---

## 色彩推导协议（用任何风格前先走这三步）

> ⚠️ **以下所有风格条目里的 hex 是示例锚点，不是配方。** 同一风格用于不同内容，应通过本协议推导出不同色值——直接复制条目 hex，只是在生产品味更好的 slop。为什么：写死配方让 100 个用户拿到 100 份同色产出，色彩的信息量归零；推导让色彩成为「这个内容独有」的证据。
>
> **字体同理**：条目里的字体名也是示例锚点。选定风格后，display+body 配对先过 `references/typography.md` 的配对逻辑与「已被用烂名单」——**名单与条目冲突时以 typography.md 为准**（如条目写 Fraunces，按名单换 Newsreader 等平替）。

### 三步法：采样 → 收敛 → 论证

| 步骤 | 做什么 | 为什么 |
|------|--------|--------|
| **1. 采样** | 主色从三个来源取，不凭空发明：①品牌资产（logo/已有 VI 直接吸色）②内容真图（产品截图/摄影素材里的主导色）③文化语境（内容主题自带的色彩记忆，见下表） | 凭空选色=从模型先验里抽签，抽出来的永远是那几个网红色；从内容里采的色天然带「为什么」 |
| **2. 收敛** | 用 oklch 把调色板压到 **2-3 个有彩色 + 1 组中性色**。中性色写成明度序列（如 L 0.15/0.35/0.65/0.92/0.98），有彩色之间拉开 oklch 色相角 H ≥60° 或明度 L 差 ≥0.3 | 色多必乱；oklch 的 L 通道感知均匀，明度序列写出来就是层级系统，比一堆孤立 hex 可推理 |
| **3. 论证** | 一句话写出「为什么是这个色」，写进产出注释或交付说明。例：「主色取自用户 logo 的赭石，压低 chroma 到 0.08 模拟油墨」 | **写不出这句话=你在抄配方。** 论证是防 slop 的自检门，不是仪式 |

### 印刷色质感：为什么低饱和比纯屏幕色高级

油墨印在纸上永远达不到屏幕 RGB 的最大饱和度——CMYK 色域更窄、纸张吸墨、环境光反射，都会把颜色「压灰」。人眼几十年被印刷品训练出的「高级感」，本质是这层物理灰度。所以屏幕设计里刻意压 chroma，等于借用印刷的质感记忆。

| 用途 | oklch chroma 参考 | 效果 |
|------|------------------|------|
| 大面积底色 | 0.01–0.04 | 纸感、不刺眼 |
| 品牌主色/强调 | 0.08–0.15 | 油墨感，够醒目但不塑料 |
| 小面积点睛（按钮/链接） | 0.15–0.22 | 保留活力，仅限小面积 |
| >0.25 满版铺 | 慎用 | 屏幕荧光感，只适合 Wrapped/糖果这类刻意「电子原生」的风格 |

### 文化语境速查：同一色相，不同语境

选色不只是选色相，是选它背后的文化坐标。同是「红」，落点差之千里：

| 色相 | 语境 A | 语境 B | 差在哪 |
|------|--------|--------|--------|
| 红 | 故宫朱红（偏橙、带灰，oklch 低 L 低 C，比可乐红更暗更浊）→ 传统/庄重 | 可乐红（高饱和正红）→ 消费/兴奋 | chroma 一降，从货架跳到宫墙 |
| 蓝 | 日本蓝染/琉璃绀（深、偏紫灰）→ 手工/沉静 | 科技蓝 #0066FF 系 → SaaS/效率 | 后者是模型最爱的默认蓝，用之前先问自己是不是在抽签 |
| 绿 | 抹茶/苔绿（黄相、低饱和）→ 自然/日式 | 荧光绿 #39FF14 → 终端/hacker | 同为绿，一个喝茶一个敲代码 |
| 黄 | 藤黄/芥末（带棕灰）→ 复古印刷 | 警示黄/Mailchimp 黄 → 醒目/玩味 | 灰度决定它是旧书页还是安全帽 |
| 白 | 奶油纸白 #F5F0E8 → 出版物/暖 | 纯白 #FFF → 实验室/瑞士 | 底色的 2% 色温差就是气质分野 |

---

## 网页风格库(20种)

#### 大胆派

**媒体级粗野主义 Editorial Brutalism（巨号Helvetica压小正文）** `大胆·还原98%`
- 参考:Bloomberg Businessweek（Richard Turley 2010-2014 改版，Code and Theory操刀）；Neue Haas Grotesk谱系
- 适配:媒体/内容出版、AI产品发布、品牌官网hero、调研报告封面、观点型长文头图
- 视觉DNA:配色纯黑#000+纯白#FFF+超链接蓝#0000EE，点缀信号橙红#FF433D/终端绿#00A33E。字体Helvetica/Neue Haas Grotesk，120px+巨号headline左对齐紧字距直接压住14px小正文，极端字号反差。布局模块化网格+1px规则线分栏切割，高信息密度刻意不留白。标志元素：rule line分栏、超链接蓝下划线、黑白底大色块。
- HTML实现:纯CSS可1:1还原。CSS Grid做模块网格+border做规则线分栏，clamp()做超大响应式字号+letter-spacing收紧，系统Helvetica/Arial栈或Inter兜底，超链接直接#0000EE下划线。零素材依赖。
- 字体:Inter（替Helvetica/Neue Haas Grotesk），代码用Geist Mono

**新粗野主义撞色信息流 Neo-Brutalism（粗黑描边卡片+高饱和撞色）** `大胆·还原95%`
- 参考:The Verge 2022 redesign（in-house team，PolySans + Mānuka）
- 适配:媒体/内容站、AI产品聚合页、活动landing、社区榜单页、小红书风信息卡
- 视觉DNA:配色电光紫#5200FF~品红#E1306C高饱和主色+亮黄#F8E000强调+纯黑#08080D+白，大面积撞色块刻意不柔和。字体几何无衬线大标题+衬线正文反差。布局卡片化feed流、2-4px粗黑描边、硬色块分区、近乎无圆角。标志元素：粗描边卡片hover撞色翻转、未完成界面气质。
- HTML实现:纯CSS强项。border:3px solid #000粗描边+box-shadow硬投影偏移(4px 4px 0 #000)+grid/flex卡片流+:hover切换background撞色翻转。无3D/光影障碍。
- 字体:Space Grotesk（替PolySans）+ 任一衬线如Fraunces

**孟菲斯复古拼贴最大化 Memphis Maximalism（撞色块+错位叠放+复古字体）** `大胆·还原72%`
- 参考:Gucci Vault概念店（Alessandro Michele）；Memphis设计运动 / Sagmeister叛逆基因
- 适配:电商概念店、创意活动页、品牌实验campaign、Y2K复古主题、节日营销页
- 视觉DNA:配色复古红/芥末黄/宝蓝/紫/橄榄绿大面积撞色并置+做旧米色暖底，浓烈刻意不和谐。字体复古衬线+装饰字混用、印刷质感、打破网格错位叠放。布局反网格拼贴策展、模块大小不一错落叠压、像逛数字房间。标志元素：撞色块、错位叠放、非常规导航彩蛋。
- HTML实现:transform:rotate()做错位叠放+position:absolute叠压+高饱和background撞色块+复古Google Fonts。真实做旧纹理无法CSS还原，降级为纯色块+mix-blend-mode/contrast滤镜模拟肌理，几何拼贴版成立、archival做旧版会降级。
- 字体:DM Serif Display + Bungee（装饰）+ Space Mono

**糖果色凸起立体按钮游戏化 Friendly Geometric Candy** `大胆·还原85%`
- 参考:Duolingo（Johnson Banks + Monotype，Feather Bold字体）；反硅谷极简
- 适配:教育语言学习、消费级App landing、游戏化产品、面向大众亲和产品、活动报名页
- 视觉DNA:配色Duo绿#58CC02+鸭子黄#FFC800+天蓝#1CB0F6糖果高饱和+白底，圆润友好。字体超粗圆体（Feather Bold感）。布局大圆角卡片、凸起3D按钮（底部硬阴影=可按压感）、吉祥物位+进度气泡。标志元素：3px实底阴影立体按钮、按下位移动画、超圆角。
- HTML实现:纯CSS。box-shadow:0 4px 0生硬底阴影做凸起按钮+:active translateY(4px)消阴影模拟按压，border-radius大圆角，纯色块。吉祥物无生图时用CSS几何形或emoji占位（轻微降级）。
- 字体:Baloo 2 / Nunito（超粗圆体替Feather）

**纯CSS几何插画+响应式变形彩蛋 Pure-CSS Art** `大胆·还原80%`
- 参考:Lynn Fisher（lynnandtonic.com，纯CSS艺术传奇，Adobe专文报道）
- 适配:个人主页、创意404/彩蛋页、品牌玩味landing、技术博客头图、设计师自我展示
- 视觉DNA:配色2-4色高对比扁平面（每个breakpoint换调色）。字体粗几何无衬线标题。布局核心是「图随视口变形」——一组CSS形状在不同断点重组成不同画面（如建筑随屏宽变换层数）。标志元素：纯CSS绘制的几何插画、断点驱动的重排彩蛋、零图片。
- HTML实现:纯CSS的炫技战场，零素材是优势。div+border-radius/clip-path/transform/box-shadow堆叠几何形，@media断点改变形状尺寸位置实现变形。难度在设计构思而非技术，但需要精心手搓每个形状。
- 字体:Rubik / Archivo（粗几何替自定义）

**巨型字黑白高对比时装大字报 Bold Big-Type Editorial** `大胆·还原88%`
- 参考:Jacquemus官网 / Rik Oostenbroek / Domestika；时装杂志大字报
- 适配:电商时尚、作品集、媒体专题、品牌宣言页、视频课程封面、调研报告大字版
- 视觉DNA:配色极简黑白+单一克制点缀色（裸粉#E8C4C0或正红）。字体超大Display无衬线/高反差衬线，标题占满整屏。布局全幅网格、巨字与负空间博弈、图文1:1分割。标志元素：屏占比巨型headline、奢侈级留白、左右对位排版。
- HTML实现:纯CSS完美还原。clamp()巨号字+CSS Grid全幅分割+大量padding留白+vh单位让标题占满视口。无图时用纯色块/文字块替代时装大片占位（轻降级但版式成立）。
- 字体:Archivo Expanded / Anton（Display）+ Playfair Display（高反差衬线）

**复古未来太空图录 Cosmic Retro-Futurism** `大胆·还原75%`
- 参考:Perplexity Comet浏览器发布站（The Brand Identity：Black/Blue/Cream；《2001太空漫游》气质）
- 适配:AI产品发布站、科技品牌宣言页、活动倒计时页、未来感landing、概念发布会
- 视觉DNA:配色纯黑#0A0A0A+奶油纸白cream#F0EAD8+一抹钴蓝-孔雀蓝#2B4F91，低饱和像老式天文图录。字体高反差衬线（古典天文图册感）+留白。布局线描轨道/抛物线SVG、行星圆点、奶油底压黑字、古籍式排印。标志元素：SVG天体轨道线、奶油+蓝+黑三色、复古衬线大字、天文图录质感。
- HTML实现:纯CSS+SVG还原静态版八成气质。SVG path画轨道抛物线+CSS径向定位行星圆点+三色变量+高反差衬线。缺口是「太空落到地球」的全屏视频转场（灵魂部分）——降级为CSS scroll视差+SVG轨道旋转近似。
- 字体:Cormorant Garamond / EB Garamond（高反差衬线）+ Space Mono

**电影感声波可视化 Cinematic Sound-Viz Dark** `大胆·还原72%`
- 参考:ElevenLabs；电影片头title sequence（Saul Bass式极简动态）× 音频工程界面
- 适配:音频/语音AI产品、音乐科技站、播客平台、媒体发布页、影院级品牌hero
- 视觉DNA:配色纯黑#000底+纯白文字+蓝紫渐变accent波形。字体大号无衬线标题Saul Bass式极简。布局全幅暗场、声波/频谱可视化贯穿、巨标题压波形、卡片功能区。标志元素：彩色audio-waveform波形带、电影片头式极简、高对比黑白+单渐变、声音可视化母题。
- HTML实现:纯CSS+SVG还原70%气质（骨架完美，波形是降级点）。SVG polyline画静态波形或多条不等高div柱阵+CSS animation做『假波形』跳动近似。缺口：随声音实时跳动的Web Audio/Canvas频谱不可纯CSS还原，静态版像、动态灵魂还不了。
- 字体:Inter / Sora（大号无衬线）

**像素游戏横版叙事 Pixel-Game Side-Scroller** `大胆·还原70%`
- 参考:Robby Leonardi交互简历（8/16-bit平台动作游戏叙事，致敬任天堂SNES）
- 适配:创意简历/作品集、品牌玩味campaign、游戏化landing、活动彩蛋页、个人趣味主页
- 视觉DNA:配色复古游戏多段分区——森林绿#4CAF50草地+天蓝#5DADE2，过渡太空紫#2C2A4A、火山橙红#E8743B、海底青#1ABC9C，每『关卡』换一套高饱和卡通调色。字体像素字体（8-bit感）+粗无衬线。布局横版/纵向滚动分关卡场景、视差分层、scroll触发位移。标志元素：分关卡换色、像素美学、视差滚动、游戏HUD式UI。
- HTML实现:纯CSS+少量JS还原骨架（原作就是HTML+CSS+jQuery无WebGL）。视差分层position+scroll位移、image-rendering:pixelated、CSS逐帧background-position做sprite动画、分段背景色。缺口：原创角色/场景手绘像素插画——无生图时用CSS方块拼简易像素图标替代（美术降级，技术不降）。
- 字体:Press Start 2P / VT323（像素字）+ Inter


#### 中性派

**包豪斯几何标志+扁平插画系统 Bauhaus Geometric** `中性·还原90%`
- 参考:Khan Academy rebrand（六边形+花瓣logomark + Wonder Blocks设计系统）；Bauhaus几何构成
- 适配:教育课程站、品牌logo系统、信息图、儿童亲和向产品、活动KV
- 视觉DNA:配色三原色谱系——包豪斯红#E63946/黄#FFB703/蓝#0077B6+黑白，纯色块拼接。字体几何无衬线（圆润几何感）。布局圆/三角/方基本几何单元搭建插画，对齐栅格、模块化拼图。标志元素：纯几何形态logomark、扁平无渐变插画、原色块构成。
- HTML实现:纯CSS几何全能。border-radius:50%做圆、clip-path/border三角形、方块div拼几何插画，CSS Grid栅格对齐，纯色fill无需素材。插画用CSS形状或内联SVG几何路径手搓。
- 字体:Poppins / Manrope（几何圆润替Wonder Blocks）

**暗色双色侧栏开发者作品集 Dark Editorial（深底+单荧光accent+等宽字）** `中性·还原96%`
- 参考:Brittany Chiang（brittanychiang.com v4，dev portfolio事实标准）
- 适配:作品集个人主页、开发者向产品、技术品牌站、简历页、AI工具landing
- 视觉DNA:配色深墨绿/海军底#0A192F+板岩灰文字#8892B0+单一荧光青绿accent#64FFDA。字体无衬线正文+等宽字（编号/标签）。布局左固定侧栏导航+右滚动主区双栏，section编号01/02、链接hover下划线滑入。标志元素：单accent色、等宽编号标签、侧栏锚点高亮。
- HTML实现:纯CSS完全还原。position:sticky做固定侧栏+CSS Grid双栏+单accent变量+等宽字标签+:hover下划线transform滑入。零素材，纯版式与微交互。
- 字体:Inter + JetBrains Mono（等宽）

**暖色出版物 Warm Editorial（奶油纸底+赤陶橙+衬线无衬线混排）** `中性·还原97%`
- 参考:Anthropic / Claude（DBCo + Geist Studio，Styrene×Tiempos）；Penguin/Pelican平装书排印
- 适配:AI产品站、品牌官网、长文阅读页、橙皮书电子书、调研报告、培训材料
- 视觉DNA:配色奶油纸底#F5F0E8+赤陶橙#CC785C/#D97757点缀+近黑文字#191919，温暖低饱和。字体衬线标题（Tiempos感）×无衬线正文（Styrene感）混排。布局书籍式单栏阅读流、舒适行高、节制分隔线。标志元素：纸感暖底、赤陶橙、出版级排印节奏。
- HTML实现:纯CSS 100%还原，零素材。背景色变量+衬线无衬线字体栈混排+max-width限制阅读宽度+line-height 1.7舒适行高。这是Anthropic赤陶橙暖色版的安全主场。
- 字体:Fraunces / Newsreader（替Tiempos衬线）+ Inter（替Styrene）

**Linear暗色发光+Bento网格 Glassmorphism Bento** `中性·还原85%`
- 参考:Linear / Cursor（'The Linear Look'现象级流派，Frontend Horse有代码配方）
- 适配:SaaS/AI产品站、开发者工具、技术品牌hero、产品功能展示、深色dashboard演示
- 视觉DNA:配色近黑底#08090A+去饱和蓝紫品牌#5E6AD2+低饱和青紫微光渐变#4EA7FC→#B59AFF。字体几何无衬线负字距紧凑。布局便当盒bento网格分块、发丝分割线、玻璃拟态卡片。标志元素：暗底发光渐变边框、bento分块、流光streamer、磨砂玻璃。
- HTML实现:纯CSS强还原。box-shadow/filter blur+radial-gradient做发光晕，backdrop-filter:blur玻璃拟态，conic/linear-gradient边框，CSS Grid拼bento。缺口仅「真实产品UI截图」——用色块+文字拼简化假UI替代（这部分降级）。
- 字体:Inter / Geist（负字距）+ Geist Mono

**斜切流体渐变带 Angled Fluid Gradient** `中性·还原92%`
- 参考:Stripe（标志性angled gradient banner，Klim定制Söhne字体）
- 适配:SaaS/Fintech落地页、品牌官网hero、产品发布页、活动banner、AI产品营销页
- 视觉DNA:配色多色流体渐变（靛蓝#635BFF→青→粉→橙暖调）做hero背景+纯白内容区+近黑文字。字体精致无衬线（Söhne感）。布局倾斜分割色块（skew切角分区）、渐变hero压结构化栅格正文。标志元素：angled斜切边界、多色流体渐变、理性栅格压表达渐变。
- HTML实现:纯CSS。transform:skewY()或clip-path:polygon()做斜切分区，linear-gradient多色叠加（可加CSS animation缓慢流动）做流体渐变带，Grid做下方结构化正文。零素材。
- 字体:Inter / Hanken Grotesk（替Söhne）

**实用主义彩虹分类文档 Utility-First Colorful Docs** `中性·还原98%`
- 参考:Tailwind CSS Docs（Sky/Cyan品牌色+功能分类彩虹色相条）
- 适配:技术文档、API参考、设计系统站、教程站、开发者knowledge base、SaaS帮助中心
- 视觉DNA:配色Sky蓝#38BDF8品牌+teal→cyan→sky青蓝渐变+Slate灰阶#0F172A/#64748B/#F8FAFC，文档用彩虹色相条区分功能分类（粉#EC4899/紫#A855F7/绿#10B981/橙）。字体清爽无衬线+等宽代码。布局左侧栏导航+中正文+右TOC三栏，彩色高亮代码块、分类色标。标志元素：青蓝渐变hero、彩虹分类色、三栏文档骨架、语法高亮代码块。
- HTML实现:纯CSS 98%还原（它本身就是CSS框架文档）。Grid三栏+linear-gradient青蓝hero+分类色变量+代码块语法色用span着色。Inter开源，唯暗色切换/copy需轻量JS。零光影/3D/手绘。
- 字体:Inter + JetBrains Mono / Fira Code（代码）

**终端核软未来 Terminal-Core Soft-Futurism（等宽字+等距立方）** `中性·还原80%`
- 参考:Cursor (Anysphere)；开发者终端美学 × Teenage Engineering工业极简
- 适配:AI编程工具站、CLI产品landing、开发者基础设施、技术品牌hero、终端类产品
- 视觉DNA:配色炭黑#0B0D14底+暖白文字#F2F0EF+克制蓝紫渐变accent点缀按钮与光晕。字体等宽字为主角（命令行感）+无衬线辅助。布局命令行/代码块前景、bento分区、2.5D等距cube示意。标志元素：等宽字命令行、等距投影立方体、暖白×炭黑、克制渐变光晕、工业极简。
- HTML实现:纯CSS 80%还原。等宽字代码块+暗色bento+box-shadow光晕；2.5D等距cube用CSS 3D transform(rotateX/Y+skew)或SVG等距投影手搓。缺口：可点击切换的多界面demo需JS+假UI拼接。无WebGL刚需。
- 字体:Geist Mono / JetBrains Mono（主角）+ Inter（辅助）


#### 安静派

**功能主义网格社区 Functional Brutalism（灰线分割+系统字+蓝链接）** `安静·还原98%`
- 参考:Are.na / Lobsters / Quartz；Müller-Brockmann栅格数字落地 + Tufte信息密度
- 适配:社区/UGC平台、内容聚合站、文档知识库、移动优先内容流、极客向产品
- 视觉DNA:配色近白底#FBFBFB+黑文字+1px灰分割线#E0E0E0+经典链接蓝#0000EE/已访问紫。字体系统字栈（-apple-system/无装饰）。布局高密度信息列表、细灰线分栏、极小留白、紧凑行距。标志元素：发丝灰分割线、蓝链接、系统字、信息密度优先。
- HTML实现:纯CSS最易还原，这是Brutalist Web的本色。border-bottom:1px灰线列表+system-ui字栈+紧凑padding+蓝链接。几乎不需要任何素材或JS，纯结构。
- 字体:system-ui系统字栈 / IBM Plex Sans（兜底）

**深色画廊裱框 Gallery Dark（深黑负空间+单列大图+EXIF小字）** `安静·还原75%`
- 参考:Glass (glass.photo) / Bottega Veneta；美术馆暗房 + Apple Photos内容至上
- 适配:摄影作品集、奢侈品电商、视觉内容沉浸展示、个人画廊页、高端产品陈列
- 视觉DNA:配色纯黑底#0A0A0A+作品图本身提供唯一色彩+极淡灰EXIF小字#666。字体极细无衬线小字。布局单列居中大图、巨幅负空间裱框、图下metadata小字。标志元素：暗房黑底、内容至上UI退隐、EXIF式小字注脚、大图独占视口。
- HTML实现:纯CSS还原版式骨架。纯黑底+居中max-width单列+巨幅padding裱框留白+小字metadata。缺口是「真实摄影作品」本身——用占位图/纯色块代替则失灵魂，但暗房氛围与版式100%可搭。
- 字体:Inter（细字重300）/ Cormorant（衬线奢侈感可选）

**Swiss极致黑白 Swiss Monochrome（Vercel式纯黑白+Geist+锐利边角）** `安静·还原98%`
- 参考:Vercel / Next.js Docs（自研Geist已开源）；Massimo Vignelli少即是多
- 适配:开发者工具文档、技术品牌官网、AI产品站、SaaS落地页、极简调研报告
- 视觉DNA:配色纯黑#000+纯白#FFF+灰阶#888，零彩色或仅一抹蓝链接。字体Geist几何无衬线+Geist Mono。布局锐利直角（无圆角或极小）、高对比、精密栅格、克制留白。标志元素：纯黑白、锐利边角、Geist字体、三角/箭头几何标记。
- HTML实现:纯CSS 100%还原，Geist开源可直接引。CSS Grid精密栅格+纯黑白变量+border-radius:0锐角+发丝边框。这是HTML最舒适的极简主场，零素材依赖。
- 字体:Geist + Geist Mono（Vercel开源原版）

**日式留白白盒画廊 Kenya Hara White Gallery** `安静·还原80%`
- 参考:Cosmos (cosmos.so) / Aesop伊索官网；原研哉『白』的空寂 + 瑞士网格混血
- 适配:高端电商、创意画廊、内容策展平台、设计师作品集、品牌精品店、moodboard站
- 视觉DNA:配色近全白#FAFAFA底+纯黑文字#0A0A0A+极淡灰分割#EFEFEF，内容图提供全部色彩、UI退到背景。字体极简系统/几何无衬线小字、大字距。布局masonry瀑布网格、极致留白、淡灰发丝分隔、东方空寂。标志元素：白盒美学、奢侈留白、内容至上UI隐退、瀑布流策展。
- HTML实现:纯CSS还原静态版式（与暗色画廊区分在『白』）。CSS columns或Grid做masonry+近白变量+大padding留白+淡灰分隔。缺口是Lenis/GSAP丝滑惯性滚动与图片入场缓动（高级感60%在此），CSS仅基础transition，动效层降级。
- 字体:Inter（细字重）/ Cooper Hewitt（Aesop同款开源）


## PPT风格库(20种)

#### 大胆派

**新瑞士大字报 / Neo-Swiss Billboard Editorial** `大胆·还原98%`
- 参考:Scribe $75M、Flock Safety $47M 等 AI/SaaS 路演 deck 的 Big-Number Editorial 流派；Bloomberg Businessweek 信息图；Pentagram
- 适配:融资路演、QBR/业务回顾、年度趋势复盘、产品发布关键页
- 视觉DNA:配色=纯白(#FFFFFF)或近黑(#0A0A0A)底+单一高饱和强调色(电光蓝#2D5BFF/荧光绿#00E676/品牌橙#FF6B2C)+中性网格线#E5E5E5。字体=超大粗体无衬线，标题占半屏，数字tabular-nums等宽收紧字距。母版=①大色块章节页一个词②巨型数字占半屏(3.2x)+小注③左右分栏对比④全幅扁平折线/柱状。标志=billboarding大字、严格基线网格、大色块章节页
- HTML实现:超大数字用clamp()；严格网格用CSS Grid；大色块章节页background-color；折线柱状用纯div+CSS或内联SVG(比贴图更锐利)；数字对齐font-variant-numeric:tabular-nums。零插画零3D
- 字体:Inter / Geist / Söhne替代Neue Haas Grotesk；数字配Geist Mono

**黑底巨型数字剧场 / Black Big-Number Stage** `大胆·还原97%`
- 参考:Steve Jobs 2007 iPhone Keynote、小米SU7 Ultra雷军发布会、Spotify Wrapped、Presentation Zen(Garr Reynolds)
- 适配:产品发布主题演讲、思想演示、全员town hall、情绪向年度回顾
- 视觉DNA:配色=纯黑#000000底+纯白#FFFFFF字高反差，一页只一个品牌强调色高亮(小米橙#FF6900/Spotify绿#1ED760/Apple蓝#2997FF)。字体=几何无衬线粗体，一屏一词或一个超大数字占满视野，字距收紧。母版=①标题页黑底居中一行大字②数据高潮页巨型数字+单位+一行注③左右参数对比双栏(强调色vs灰)④slogan单页。大量负空间
- HTML实现:黑底白字几行CSS；巨型数字clamp()+flex居中；强调色highlight单独span；左右对比CSS Grid两列+条形高亮；tabular-nums。去掉产品照改纯文字反而更接近Zen本质
- 字体:Geist / Inter / 思源黑替代SF Pro

**高饱和单色品牌撞色海报 / Mono-Brand Type-as-Hero** `大胆·还原96%`
- 参考:Spotify Wrapped视觉系统、Mailchimp Brand Book(Collins)、Netflix红黑现代复刻、COLLINS品牌系统
- 适配:品牌/营销策略、campaign宣讲、town hall文化页、活动主视觉
- 视觉DNA:配色=单一品牌主色满版铺底(Spotify绿#1ED760/Mailchimp黄#FFE01B/Netflix红#E50914)+黑或白反差字，撞色两层。字体=超大字体即主视觉(type-as-hero)顶天立地。母版=①满色块底+反白巨字②双色块上下/左右分割③巨型数字撑满。标志=单色满版、字体当图、高对比撞色
- HTML实现:满版background-color；超大字clamp()占满；双色用两个100vh色块；字体当图靠font-weight900+负letter-spacing。纯色块零素材，HTML原生最爽
- 字体:Inter / Manrope / Archivo(超粗)替代Circular/Cavendish

**全幅渐变宣言版式 / Full-Bleed Gradient Manifesto** `大胆·还原82%`
- 参考:Zuora『Tell a Different Story』销售deck(Andy Raskin拆解)、Nike『Just Do It』campaign、National Geographic跨页
- 适配:销售提案愿景页、品牌宣言、keynote转折页、使命愿景单页
- 视觉DNA:配色=满版CSS渐变(暖橙→品红/深蓝→青)或纯色出血+反白宣言大字+hashtag口号(#shifthappens)。字体=厚重无衬线全大写标语横贯。母版=①满幅渐变+居中反白宣言②应许之地愿景页③客户logo墙。标志=full-bleed出血、反白大标语、hashtag口号
- HTML实现:linear-gradient/radial-gradient满版(不做粒子/光影，纯CSS渐变是允许的)；反白字position居中；logo墙用grid灰度SVG/文字占位。原本靠纪实大照片的部分降级为CSS渐变铺底+大字，照片缺失这一项还原度降约15%
- 字体:Archivo / Anton / Manrope(超粗)

**CS50单概念糖果舞台 / Candy-Color Lecture Stage** `大胆·还原94%`
- 参考:Harvard CS50(David Malan)、Lessig Method/高桥流、Presentation Zen
- 适配:教育课件、技术讲座、概念解释、代码教学
- 视觉DNA:配色=深黑底#0A0A0A+高饱和糖果色大字轮换(品红#FF2D95/青#00E5FF/明黄#FFD500/绿#39FF14)。字体=无衬线超大字漂浮居中，一屏一概念，文字极少。母版=①深黑底单个糖果色大词②等宽代码块语法高亮③舞台聚光感大字。标志=深黑漂浮糖果色大字、等宽代码高亮、强舞台聚光、极少文字
- HTML实现:深黑背景+单色超大字clamp()居中；代码块用pre+等宽字+span上色做语法高亮；聚光感用极淡radial-gradient暗角(非粒子光效)。还原度高
- 字体:Inter超粗 + JetBrains Mono(代码)

**玩味手绘极简 / Playful Maximalist Editorial (Collins式)** `大胆·还原75%`
- 参考:Mailchimp Brand Book(Collins 2018)、New Yorker漫画气质、Cooper圆润衬线、Cavendish荧光黄
- 适配:有态度的品牌deck、创意机构提案、文化向town hall、反SaaS极简的营销页
- 视觉DNA:配色=Cavendish荧光黄#FFE01B大面积+黑+少量撞色，反SaaS极简。字体=Cooper式圆润衬线大标题(playful)+杂志式留白编排。母版=①荧光黄满底+怪诞标题②杂志式不规则留白排版③大字玩梗文案。标志=荧光黄、圆润衬线、playful编排、怪诞手绘气质(降级为几何色块/emoji替代真插画)
- HTML实现:荧光黄background；圆润衬线font-family；杂志留白用非对称Grid。手绘猩猩/插画这一核心元素无AI生图无法做，降级为CSS几何色块+大号emoji+不规则transform旋转的文字块替代，插画缺失还原度降约20%
- 字体:Fraunces(可调圆润)/ Bree Serif替代Cooper；正文Inter

**不羁玩梗流行版 / Irreverent Pop (Reddit式)** `大胆·还原80%`
- 参考:Reddit Ads销售deck(被Dock列为最有性格)、David Carson式不羁排版、90年代web复古、Memphis玩味
- 适配:Z世代品牌、玩梗营销deck、社区/创作者向、敢于不正经的提案
- 视觉DNA:配色=Reddit橙红#FF4500+撞色，90s web复古色。字体=混排/打破网格的David Carson式排版，玩梗口语文案。母版=①fun页玩梗大字②facts页节奏转折严肃数据③口语标题。标志=打破网格混排、橙红、玩梗口语、fun→facts节奏反转、复古web质感
- HTML实现:故意打破网格用transform旋转/重叠定位/混合字号；橙红+撞色块；复古质感用粗黑边border+硬阴影box-shadow(无blur)。自定义meme插画降级为emoji+几何拼贴，但混排排版本身HTML可还原
- 字体:Archivo / Space Grotesk + 混搭Inter制造对比

**Y2K膨胀大字 / Maximalist 3D-Type (Wrapped式)** `大胆·还原78%`
- 参考:Spotify Wrapped 2022/2023/2025、Memphis撞色、Y2K/Maximalism、duotone人像渐变
- 适配:年度回顾(情绪出圈向)、个性化数据卡、社交分享竖屏卡、品牌年终
- 视觉DNA:配色=高饱和撞色满版背景(品红+青+橙)+Spotify绿点睛+duotone双色渐变。字体=顶天立地巨型数字，年份/数字做3D膨胀/金属质感。母版=①撞色满版+巨型膨胀数字②duotone人像/色块底+反白大字③竖屏可分享卡。标志=巨型膨胀3D数字、撞色满版、duotone渐变、年份金属质感、竖屏story卡
- HTML实现:撞色满版background；3D膨胀数字用CSS text-shadow多层叠加+transform:perspective或SVG+stroke制造立体(非真3D渲染)；duotone用mix-blend-mode+渐变叠在灰度图占位块上。金属质感降级为渐变填充文字background-clip:text，还原度降约15%
- 字体:Archivo Black / Anton超粗 + 数字Clash Display


#### 中性派

**Bento便当格模块网格 / Bento Grid** `中性·还原95%`
- 参考:Apple Keynote Bento Grid时代、新一代MBB Bento/Big-Type deck(2024-2026)、Stripe年报指标卡矩阵、Pitch.com QBR模板
- 适配:产品功能汇总、咨询/QBR数据汇报、销售成果页、town hall指标页
- 视觉DNA:配色=浅灰/奶白底(#F5F5F7/cream)或近黑底+品牌主色+1-2强调色，卡片浅色分区底+圆角+微描边/微阴影。字体=超大display标题+常规正文，字重对比强烈，KPI数字tabular figures。母版=①标题页巨型单句+留白②bento页2×2/3列不等高卡片每卡一洞见(数字/线性icon/sparkline)③one-insight超大数字页。标志=不等高卡片网格、圆角微描边、呼吸感
- HTML实现:CSS Grid的grid-template-areas做不等高bento；卡片border-radius+box-shadow微阴影+1px hairline；sparkline用内联SVG；线性icon用inline SVG stroke。零贴图
- 字体:Inter / Geist + 数字Geist Mono

**Neo-Swiss暗色终端美学 / Dark Hairline Terminal** `中性·还原94%`
- 参考:Linear pitch deck、Vercel设计语言、CS50深黑舞台课件；字体Inter Tight+JetBrains Mono
- 适配:开发者工具/技术产品发布、技术路演、工程向汇报
- 视觉DNA:配色=近黑底(#0D0D0F/#111113)+hairline细线#262629网格+单一紫蓝强调(#5B5BD6/#7C7CFF)。字体=Inter Tight大标题+JetBrains Mono做标签/数据。母版=①极简标题页一句话+mono小标②hairline分隔的数据网格③mono标签的特性列表。标志=1px细线网格、mono单等宽标签、极致留白、近黑非纯黑
- HTML实现:近黑背景+border:1px solid的hairline网格；mono标签用等宽font-family；微光用极淡box-shadow/border highlight而非真光效(降级避开赛博霓虹禁区)。注意避开#0D1117深蓝禁区，用中性近黑
- 字体:Inter Tight + JetBrains Mono / IBM Plex Mono

**双字体咨询版 / Two-Font Consulting (Bower式)** `中性·还原90%`
- 参考:McKinsey 2019品牌系统(Wolff Olins设计，Bower衬线+无衬线)、BCG Executive Perspectives、深蓝细线pattern
- 适配:咨询报告、高管汇报、行业研究、权威机构提案
- 视觉DNA:配色=深蓝(#051C2C/McKinsey深蓝)×白二元+单一品牌色高亮(BCG绿#00805A)，暖灰底带呼吸感。字体=characterful衬线大标题(Bower式)与无衬线正文高对比并置。母版=①左上角结论式action-title②蓝色细线pattern装饰③杂志式左右分工(结论文字+视觉)④大数字data-point卡。标志=衬线×无衬线高对比、深蓝细线pattern、action-title、暖灰高级感
- HTML实现:双字体font-family并置(衬线标题+无衬线正文)；细线pattern用repeating-linear-gradient或SVG line；data-point卡纯CSS；照片灰度处理这一项无照片可省。蓝紫edge shimmer降级为纯色边
- 字体:Playfair Display / Fraunces衬线标题 + Inter正文(替代Bower)

**图谱箭头企业版 / Diagram-Driven Isotype** `中性·还原88%`
- 参考:Salesforce销售deck、Isotype(Otto Neurath)谱系、Gene Zelazny《Say It With Charts》、Hans Rosling/Gapminder
- 适配:平台/架构讲解、客户旅程、流程方法论、生态地图
- 视觉DNA:配色=企业蓝色块+产品线分色区分+图标化能力网格。字体=清晰无衬线。母版=①横向客户旅程箭头流②分层平台架构图③图标化能力网格④2×2/瀑布/金字塔结构图。标志=箭头流程、分层架构盒、Isotype图标网格、流程即叙事
- HTML实现:箭头流程用Flexbox+CSS clip-path三角或SVG arrow；架构分层用嵌套带边框div；图标用inline SVG stroke统一描边；瀑布/金字塔用Grid+斜切。气泡图可用CSS圆形+定位。纯矢量绘制
- 字体:Inter / IBM Plex Sans(图表友好)

**单图母图概念图解 / Diagrammatic Minimalism** `中性·还原95%`
- 参考:Simon Sinek黄金圆环(Golden Circle)TED、Bauhaus几何抽象、信息建筑『一图定全场』
- 适配:理论框架讲解、TED式思想传播、模型/方法论可视化、单概念keynote
- 视觉DNA:配色=极简白/浅底+黑+1个强调色，几何纯色。字体=无衬线，标签大写嵌入图形。母版=①唯一几何母图(同心圆/三角/矩阵)承载全部概念②由内向外箭头③对比案例。标志=单一几何母图、嵌套同心圆/三角、大写标签、一图承载概念
- HTML实现:同心圆用border-radius:50%嵌套div或SVG circle；三角用clip-path/SVG polygon；箭头SVG marker；标签absolute定位贴在图形上。纯几何，HTML完美还原
- 字体:Manrope / Futura系(Jost开源替代)几何感

**Sparkline叙事波形 / Narrative Sparkline (Duarte式)** `中性·还原91%`
- 参考:Nancy Duarte《Resonate》Sparkline叙事图谱、Al Gore《An Inconvenient Truth》、Duarte Inc.数据叙事
- 适配:演讲结构设计、变革叙事、before/after对照、数据故事弧线
- 视觉DNA:配色=深底或白底+品牌橙强调转折点+灰化对照。字体=无衬线，annotation标注点。母版=①横贯全屏的振荡波形线②波形上text标注点③上下并置对照波形④全黑底孤悬一条数据线⑤逐步reveal。标志=横贯波形线、波形标注点、橙色转折、对照波形、爬出画面的曲线
- HTML实现:波形线用内联SVG path(平滑贝塞尔)；标注点用SVG circle+text定位；对照波形上下两条path；reveal用CSS动画stroke-dashoffset。纯SVG绘制无素材
- 字体:Inter + 数字Geist Mono


#### 安静派

**断言-证据 / Tufte信息设计** `安静·还原93%`
- 参考:Michael Alley Assertion-Evidence(Penn State实证)、McKinsey/BCG action-title、Edward Tufte数据墨水比、Barbara Minto金字塔原理
- 适配:学术/工程汇报、数据严谨型咨询页、政策研报、技术评审
- 视觉DNA:配色=白/极浅灰底+黑正文+单一克制强调色(深蓝/砖红)。字体=整句话标题(非名词短语)，标题下独占一张图，文字标注嵌进图里。母版=①整句action-title②标题下单图证据③零bullet。标志=整句标题、单图证据、嵌入式标注、零chartjunk、高数据墨水比
- HTML实现:整句标题靠排版层级；图表用纯CSS/内联SVG画极简折线散点(去网格线去图例，标注直接text定位在数据点旁)；零装饰。Tufte的克制正是HTML强项
- 字体:Source Serif / Lora标题 + Inter正文(双字体阅读级)

**瑞士机构极简 / Institutional Swiss Minimal** `安静·还原96%`
- 参考:Sequoia官方10页pitch模板、Airbnb 2009种子轮deck、Müller-Brockmann网格、Massimo Vignelli
- 适配:投资路演、标准商业提案、问题-解法叙事、品牌去装饰提案
- 视觉DNA:配色=纯白底+黑灰正文+单一品牌强调色(Airbnb珊瑚红#FF5A3C/中性蓝)。字体=Helvetica系无衬线，标题中号粗体一句话，正文短句大间距。母版=①居中logo+slogan②顶部一句话标题带+下方3栏对仗(Problem/Solution三点)③TAM大数字分层④2×2竞品矩阵。标志=顶部标题带、三栏对仗、单色强调、2×2矩阵
- HTML实现:Flexbox三栏对仗；2×2矩阵纯CSS Grid+border画；TAM分层用嵌套div或同心方块；一页一信息。几乎纯排版网格，HTML理想对象
- 字体:Inter / Helvetica Now替代Helvetica；正文Inter

**杂志编辑长文流 / Editorial Longform** `安静·还原95%`
- 参考:Stripe Annual Letter($1.9T)、Amazon六页叙事备忘录、Benedict Evans『X eats the world』、Stripe Press
- 适配:年度信/复盘叙事、深度思想长文、内部更新、研报型阅读物
- 视觉DNA:配色=奶白/米白底(#FBFAF8)+深墨字+品牌色点睛(Stripe紫#635BFF)。字体=衬线或高品质无衬线，散文体段落+内联数据卡，超大display数字穿插。母版=①刊头大标题②多栏散文+内联指标卡③超大数字段落锚点。标志=出版物阅读节奏、内联数据卡、克制留白、散文体而非bullet
- HTML实现:多栏column-count或Grid；内联数据卡float/inline-block嵌入正文；衬线正文max-width控制行宽65ch；超大数字穿插。纯排版，零素材
- 字体:Newsreader / Source Serif正文 + Inter辅助；数字tabular

**人文圆角卡片 / Humanist Rounded Cards (Khan式)** `安静·还原80%`
- 参考:Khan Academy Wonder Blocks设计系统、Source Serif Pro衬线、森林绿品牌、友善人文主义
- 适配:教育产品、亲和力课件、公益/非盈利deck、温暖品牌提案
- 视觉DNA:配色=森林绿#14BF96/#0A5C4B+米白底+暖色辅助，柔和不刺眼。字体=Source Serif衬线标题(人文气)+无衬线正文。母版=①圆角卡片组件组②衬线标题+亲和正文③真实摄影位(降级为绿色系几何/圆角色块)。标志=森林绿、衬线标题、大圆角卡片、人文温暖、不完美亲和质感
- HTML实现:大圆角border-radius卡片+柔和box-shadow；衬线标题font-family；暖米白底。真实师生摄影这一项无AI生图，降级为绿色系几何插画块/大圆角纯色占位+emoji人物，照片缺失还原度降约18%
- 字体:Source Serif 4标题 + Nunito Sans / Inter正文(Nunito圆润呼应人文)

**研报密集图表 / Dense Research Report (Meeker式)** `安静·还原92%`
- 参考:Mary Meeker《Internet Trends》(BOND)、CB Insights《State of AI》、McKinsey Global Institute《Year in Charts》、FT/Bloomberg数据新闻
- 适配:趋势研报、行业数据复盘、密集数据汇报、市场地图
- 视觉DNA:配色=白底+品牌色(BOND/CB Insights亮蓝#0066FF)阶梯单色高亮其余灰化，几乎零留白。字体=结论式句子标题，每页1图密度，极小来源脚注。母版=①结论句标题+满页单图②logo网格market map③大数字KPI卡④密集多图网格+脚注。标志=结论句标题、零留白研报感、单色阶梯高亮、logo市场地图、来源脚注规范
- HTML实现:密集图表全用纯CSS/内联SVG画(柱/折线/堆叠/散点)；logo market map用Grid+文字/SVG占位格；KPI卡CSS；脚注小字。极致信息密度正是HTML擅长，零素材
- 字体:Inter + IBM Plex Sans + 数字tabular Geist Mono

**纯文字宣言备忘录 / All-Text Manifesto (Netflix/Amazon式)** `安静·还原97%`
- 参考:Netflix Culture Deck(2009，125页)、Amazon六页叙事备忘录(Bezos)、Tufte反PowerPoint主张、Matthew Carter阅读级排印
- 适配:文化宣言、价值观宣讲、深度备忘录、反PPT的纯文档演示
- 视觉DNA:配色=纯白或纯黑底+单一强调色(Netflix红#E50914)做唯一高亮，极致克制。字体=阅读级排印，一页一观点金句断言/纯散文零bullet零图。母版=①满版底+金句断言②口语化坦诚段落③制度名词高亮(Keeper Test)④六页散文+附录表。标志=纯文字一页一观点、零图零bullet、单色高亮金句、口语坦诚、silent-read文档感
- HTML实现:纯排版：金句用大字clamp()左对齐层级；散文max-width控制行宽；唯一强调色span高亮关键短语；附录用极简table。零素材零图，纯文字是HTML最稳的还原
- 字体:Newsreader / Source Serif(阅读级)或Inter(宣言式)；标题可Archivo超粗


---

## ⚠️ AI 生图专用风格（仅在确认用户有生图能力时才推，default 不可选）

下面这些风格的灵魂在**动态生成视觉 / 3D / 粒子 / 电影级光影 / 手绘插画**，纯 HTML/CSS 无生图下只能做出严重劣化的 mock，**从 default 推荐池剔除**。用户明确有生图能力（走 `huashu-gpt-image`）时才作为候选：

| 风格 | 灵魂 | 为什么 HTML 做不了 |
|------|------|------------------|
| Active Theory（WebGL 粒子） | 3D 粒子系统/实时渲染 | 纯 CSS 无法 |
| Field.io（生成艺术） | 算法生成图形 | 静态 SVG 只能做僵化简化版 |
| Resn（插画交互） | 角色插画+游戏化 | 依赖手绘素材 |
| Zach Lieberman（实时生成） | creative coding 笔触 | 依赖实时生成 |
| Raven Kwok（分形参数） | 递归分形 | CSS 做不出复杂度 |
| Ash Thorp（电影光影） | 电影级体积光/概念美术 | CSS 光影是劣化 |
| Territory Studio（FUI 全息） | 科幻全息界面 | 依赖大量发光层叠素材 |
| Neo Shen（水墨晕染） | 水墨有机晕染 | CSS 渐变≠水墨 |
| Sagmeister & Walsh（色彩爆发） | 手作实物+实验排版 | 撞色骨架可做（已并入网页「Memphis/孟菲斯」与 PPT「单色撞色海报」），手作质感做不了 |

> 这些款不是「不好」，是「载体不对」——它们的原生载体是 AI 直出图，不是浏览器 DOM。

---

## 默认审美禁区（用户可按自己品牌 override）

- ❌ **GitHub-dark 偷懒解**：均匀深蓝底（#0D1117）+ 通用青/紫霓虹 glow——只禁这一种烂大街组合，不是「暗色一律禁」
- ✅ **不在禁区**：电影级戏剧光影、暖色赛博（Ash Thorp 橙/青）、运动诗学暗场叙事——有作者意图的暗色保留（本库「Linear 暗色发光」「黑底数字剧场」「CS50 糖果舞台」都是合法暗色）
- ❌ 激进紫渐变万能公式、emoji 当图标、圆角卡片+左彩 border accent（除非品牌本身用）
- ❌ 封面图加个人署名/水印

---

## 有生图能力时的提示词心法（Mood, Not Layout）

> 仅当走 AI 生图路径时适用；HTML 路径直接按上面各风格的「HTML 实现」写代码。

短提示词 > 长提示词。描述情绪和内容，比堆 30 行布局细节有效。

| 杀死多样性的写法 | 激发创造力的写法 |
|----------------|----------------|
| 指定颜色比例（60%/25%/15%） | 描述情绪（"warm like Sunday morning"） |
| 规定布局位置 | 引用具体美学（"Pentagram editorial feel"） |
| 列出所有视觉元素 | 描述观众应该感受到什么 |

完整 AI 生图方法论 → `huashu-gpt-image` skill。

---

**版本**：v3.0（2026-06 全面重构为 HTML 原生 40 种库）
**适用**：网页/PPT/PDF/信息图/封面/App 等所有视觉设计的 default HTML 路径
