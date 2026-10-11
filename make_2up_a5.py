#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_2up_a5.py
ابزار تبدیل دو صفحه یا دو فایل PDF اندازه A4 به یک برگه افقی A4 (دو صفحه A5 در کنار هم)
مناسب برای چاپ دو نسخه یا دو نمونه آزمون در قطع A5 با چاپگر A4 و برش از وسط.
"""

import os
import sys
import shutil
import tempfile
import argparse
import subprocess

def create_2up_pdf(
    pdf1_path,
    pdf2_path=None,
    output_path=None,
    page1_num=1,
    page2_num=1,
    scale=0.96,
    gap_mm=4,
    cut_line=True,
    rtl=True,
):
    """
    ترکیب دو فایل یا دو صفحه PDF به صورت 2-up در قطع A4 افقی.

    :param pdf1_path: مسیر فایل PDF اول
    :param pdf2_path: مسیر فایل PDF دوم (در صورت خالی بودن، از همان فایل اول استفاده می‌شود)
    :param output_path: مسیر فایل خروجی PDF
    :param page1_num: شماره صفحه مورد نظر از فایل اول (پیش‌فرض: ۱)
    :param page2_num: شماره صفحه مورد نظر از فایل دوم (پیش‌فرض: ۱)
    :param scale: ضریب مقیاس برای حاشیه امن چاپگر (پیش‌فرض: 0.90)
    :param gap_mm: فاصله وسط برگه بین دو صفحه برای خط برش به میلی‌متر (پیش‌فرض: 10)
    :param cut_line: آیا خط‌چین راهنمای برش رسم شود؟ (پیش‌فرض: True)
    :param rtl: ترتیب راست‌به‌چپ (نمونه ۱ در سمت راست و نمونه ۲ در چپ؛ مناسب فارسی)
    :return: مسیر فایل PDF خروجی
    """
    pdf1_path = os.path.abspath(pdf1_path)
    if not os.path.exists(pdf1_path):
        raise FileNotFoundError(f"فایل یافت نشد: {pdf1_path}")

    if pdf2_path:
        pdf2_path = os.path.abspath(pdf2_path)
        if not os.path.exists(pdf2_path):
            raise FileNotFoundError(f"فایل یافت نشد: {pdf2_path}")
    else:
        pdf2_path = pdf1_path

    if not output_path:
        base_name, _ = os.path.splitext(pdf1_path)
        output_path = f"{base_name}_2up_A5.pdf"
    else:
        output_path = os.path.abspath(output_path)

    # ایجاد پوشه موقت برای جلوگیری از تداخل نام‌های فارسی یا فاصله‌دار در LaTeX
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_in1 = os.path.join(tmpdir, "doc1.pdf")
        tmp_in2 = os.path.join(tmpdir, "doc2.pdf")
        shutil.copyfile(pdf1_path, tmp_in1)
        shutil.copyfile(pdf2_path, tmp_in2)

        # ترتیب قرارگیری صفحات در برگه افقی
        # در حالت RTL (پیش‌فرض فارسی): فایل ۱ در راست، فایل ۲ در چپ
        # در دستور includepdfmerge، اولین ورودی در چپ قرار می‌گیرد و دومی در راست
        if rtl:
            merge_args = f"doc2.pdf,{page2_num}, doc1.pdf,{page1_num}"
        else:
            merge_args = f"doc1.pdf,{page1_num}, doc2.pdf,{page2_num}"

        cut_line_tikz = ""
        if cut_line:
            cut_line_tikz = r"""
        \begin{tikzpicture}[remember picture, overlay]
            \draw[dash pattern=on 8pt off 4pt, line width=0.7pt, draw=black!50] 
                (current page.north) -- (current page.south);
            \node[below=3mm, text=black!60, font=\scriptsize] at (current page.north) {\faCut\ \ محل برش \ \faCut};
            \node[above=3mm, text=black!60, font=\scriptsize] at (current page.south) {\faCut\ \ محل برش \ \faCut};
        \end{tikzpicture}%
            """

        tex_content = rf"""\documentclass[a4paper,landscape]{{article}}
\usepackage[margin=0pt]{{geometry}}
\usepackage{{pdfpages}}
\usepackage{{tikz}}
\usetikzlibrary{{calc}}
\usepackage{{xepersian}}
\settextfont{{Yas}}
\usepackage{{fontawesome5}}

\begin{{document}}
\includepdfmerge[
    nup=2x1,
    scale={scale},
    delta={gap_mm}mm 0mm,
    pagecommand={{{cut_line_tikz}}}
]{{{merge_args}}}
\end{{document}}
"""
        tex_path = os.path.join(tmpdir, "impose.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_content)

        # اجرای xelatex
        res = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "impose.tex"],
            cwd=tmpdir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out_tmp_pdf = os.path.join(tmpdir, "impose.pdf")
        if not os.path.exists(out_tmp_pdf):
            print("LaTeX output:\n", res.stdout, file=sys.stderr)
            raise RuntimeError("خطا در ایجاد فایل نهایی با xelatex!")

        shutil.copyfile(out_tmp_pdf, output_path)

    print(f"✓ فایل با موفقیت ساخته شد: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="ترکیب دو آزمون یا دو صفحه A4 در یک برگه A4 افقی (دو A5 کنار هم برای چاپ و برش)"
    )
    parser.add_argument("pdf1", help="مسیر فایل PDF اول")
    parser.add_argument("pdf2", nargs="?", default=None, help="مسیر فایل PDF دوم (اختیاری؛ در صورت خالی بودن، دو نسخه از فایل اول چاپ می‌شود)")
    parser.add_argument("-o", "--output", default=None, help="مسیر فایل خروجی (پیش‌فرض: نام فایل اول + _2up_A5.pdf)")
    parser.add_argument("--page1", type=int, default=1, help="شماره صفحه از فایل اول (پیش‌فرض: ۱)")
    parser.add_argument("--page2", type=int, default=1, help="شماره صفحه از فایل دوم (پیش‌فرض: ۱)")
    parser.add_argument("--scale", type=float, default=0.96, help="ضریب مقیاس (پیش‌فرض: 0.96 جهت پر کردن بهینه صفحه)")
    parser.add_argument("--gap", type=int, default=4, help="فاصله میانی دو صفحه برای برش به میلی‌متر (پیش‌فرض: 4)")
    parser.add_argument("--no-cut-line", action="store_true", help="عدم رسم خط‌چین راهنمای برش")
    parser.add_argument("--ltr", action="store_true", help="ترتیب چپ به راست (فایل ۱ در چپ و فایل ۲ در راست)")

    args = parser.parse_args()

    create_2up_pdf(
        pdf1_path=args.pdf1,
        pdf2_path=args.pdf2,
        output_path=args.output,
        page1_num=args.page1,
        page2_num=args.page2,
        scale=args.scale,
        gap_mm=args.gap,
        cut_line=not args.no_cut_line,
        rtl=not args.ltr,
    )

if __name__ == "__main__":
    main()
