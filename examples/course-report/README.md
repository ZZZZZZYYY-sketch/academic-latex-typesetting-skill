# 匿名课程报告排版示例

这是一个仅展示 LaTeX 基础排版元素的**虚构内容示例**，不包含实验数据、真实学生信息或科研结果。

从该目录执行：

```bash
latexmk -xelatex -interaction=nonstopmode -file-line-error -halt-on-error main.tex
python ../../scripts/check_latex_log.py main.log
python ../../scripts/render_pages.py main.pdf --out-dir render --dpi 160
```

请使用安装了 TeX Live、ctex、biblatex、Biber、TikZ 以及 Poppler 的环境。默认字体由 ctex / 本机字体决定；正式项目中需要按学校或期刊模板调整。

成功编译仅代表工程基本可用；**使用者自己的报告依然要逐页检查 PDF**。示例的 `main.pdf` 是演示成品，正式项目交付时请用真实材料重新生成。
