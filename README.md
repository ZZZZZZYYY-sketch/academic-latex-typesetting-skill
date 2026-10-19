# Academic LaTeX Typesetting Skill

**一套给 ChatGPT 使用的中文学术 LaTeX 排版指令**，适合本科生课程大作业、实验报告、课程设计、科研论文、竞赛报告和技术报告。

它不是新的 LaTeX 引擎，也不是“自动美化按钮”。它将实际排版协作中反复出现的高质量 Prompt 整理为流程：**检查资料 → 一次性确认关键条件 → 先展示排版方案 → 用户批准 → 制作工程 → 编译 → 逐页检查 PDF → 修复并交付**。

## 核心特色

- **以排版为主，内容保真**：默认只改明显错别字、病句及编号/排版错误；不改实验数据和技术结论。
- **模板优先**：有课程/学校/竞赛/期刊模板就忠实遵守；无模板才采用克制专业的默认学术风格。
- **细节有明确标准**：中文与英文字体、图文邻近、黑白三线表、数学渲染、图例位置、留白与跨页等。
- **先方案、后制作**：用户审过整体排版方案，才正式生成文件。
- **PDF 视觉检查**：真实编译、逐页检查、问题修复，不因代码能编译就宣告完成。
- **交付可继续编辑的工程**：PDF + `.tex`、图片、参考文献等组成的完整 ZIP。

## 在 ChatGPT 中怎么用

1. 下载本仓库 ZIP（GitHub 右上角 **Code → Download ZIP**），或单独下载 `SKILL.md`。
2. 新建对话，上传 ZIP / `SKILL.md`，同时上传报告原文、模板、截图、代码、图表等资料。
3. 发送以下一句（可直接复制）：

> 请先阅读我上传的 `SKILL.md`，严格按照其中的「先排版方案、后制作、实际编译与逐页 PDF 视觉检查」流程处理本次材料。不要自行改动实验数据、结论或关键原文；先一次性问完必要的问题，再给我审核排版方案。我确认后再生成完整 LaTeX 工程和 PDF。

4. ChatGPT 给出方案后，确认或提出修改意见，再要求其开始制作。

**说明：**上传 ZIP 不必然等于已将 Skill 安装为 ChatGPT 的系统级能力。请明确要求 ChatGPT 阅读 `SKILL.md`；如当前会话不能读取 ZIP，可直接上传 `SKILL.md` 或粘贴其内容。实际编译/渲染取决于该会话可用的文件和代码执行工具，不能假装成功。

## 仓库结构

```text
academic-latex-typesetting-skill/
├── SKILL.md                       # 核心技能指令，最优先阅读
├── README.md                      # 使用指南
├── LICENSE                        # MIT
├── prompts/
│   └── PROMPTS.md                 # 可复制的排版提示词
├── references/
│   ├── STYLE_GUIDE.md             # 不同报告/论文的排版规则
│   └── QA_CHECKLIST.md            # 实际 PDF 终检清单
├── scripts/
│   ├── check_latex_log.py         # LaTeX 日志问题提示（不代替人工检查）
│   └── render_pages.py            # 将 PDF 渲染为逐页图片
└── examples/
    └── course-report/
        ├── main.tex               # 匿名虚构内容的可编译例子
        ├── references.bib
        ├── main.pdf               # 已真实编译的一页示例（仅作展示）
        └── README.md
```

## 常见任务与模板

见 [可复制 Prompt 集](prompts/PROMPTS.md)，包含：通用排版、严格复刻课程模板、Word 转 LaTeX、实验报告、科研论文、竞赛技术报告、图表修复、PDF 逐页验收。

## 本地编译示例

以 Windows + VS Code + TeX Live 为例，配置 LaTeX Workshop 后，在示例目录运行：

```bash
latexmk -xelatex -interaction=nonstopmode -file-line-error -halt-on-error main.tex
python ../../scripts/check_latex_log.py main.log
python ../../scripts/render_pages.py main.pdf --out-dir render
```

前提：TeX Live 含 `ctex`、`biblatex`、Biber；`render_pages.py` 需要可在 PATH 中找到的 `pdftoppm`（Poppler）。不同论文模板可能需要 pdfLaTeX 或 LuaLaTeX，请服从模板说明。

示例中所有内容均为占位演示，不是任何真实学生的报告或实验数据。

## 使用与贡献

- 本项目基于一组常见、可复用的中文排版需求整理；**Prompt 示例是归纳改写，不声称逐字复现私人聊天**。
- 可以按任务修改样式规范；对与学校/期刊模板冲突的默认规则，应优先遵循正式模板。
- 欢迎 Issue / PR 提供可复现的版式问题及其 PDF 截图（注意删除个人与未公开科研信息）。

## License

MIT，见 [LICENSE](LICENSE)。
