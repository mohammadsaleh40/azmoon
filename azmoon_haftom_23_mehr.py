#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

# Ensure current directory is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

from units import (
    first_text as base_first_text,
    add_sarbarg,
    add_question,
    add_enteha,
    create_file,
    recreate_pdf,
    delete_temp_file,
)
from make_2up_a5 import create_2up_pdf

def build_sample_1():
    text = base_first_text
    text = add_sarbarg(
        text,
        answertime="۴۰ دقیقه",
        examdate="۲۳ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان دوره اول",
        branch="نمونه ۱",
        school="شهید جوانبخت",
        grade="ریاضی هفتم (نمونه ۱)",
        topic="فصل ۱: راهبردهای حل مسئله",
    )

    # سؤال ۱: راهبرد الگویابی و تفکر جبری
    q1 = (
        r"در الگوی زیر، چوب‌کبریت‌ها برای ساختن مربع‌های به هم چسبیده به کار رفته‌اند:" + "\n\n"
        r"\noindent\textbf{شکل (۱):} $4$ چوب‌کبریت \hfill \textbf{شکل (۲):} $7$ چوب‌کبریت \hfill \textbf{شکل (۳):} $10$ چوب‌کبریت" + "\n\n"
        r"الف) شکل چهارم با چند چوب‌کبریت ساخته می‌شود؟ \\" + "\n"
        r"ب) رابطهٔ جبری بین شمارهٔ شکل ($n$) و تعداد چوب‌کبریت‌ها را بنویسید. \\" + "\n"
        r"ج) شکل بیستم ($20$) از چند چوب‌کبریت تشکیل شده است؟"
    )
    text = add_question(text, q1, khat=3)

    # سؤال ۲: راهبرد رسم شکل و کسرها
    q2 = (
        r"کشاورزی نصف زمین خود را گندم کاشته و $\frac{1}{3}$ از باقی‌ماندهٔ زمین را جو کاشته است. "
        r"اگر پس از این کارها، مساحت زمین باقی‌مانده برابر با $400$ متر مربع باشد، کل مساحت زمین کشاورزی چقدر است؟ "
        r"\textbf{(حل مسئله با «رسم شکل» و نوشتن توضیحات الزامی است)}"
    )
    text = add_question(text, q2, khat=5)

    # سؤال ۳: راهبرد حدس و آزمایش
    q3 = (
        r"در یک پارکینگ در مجموع $18$ دستگاه خودرو و موتورسیکلت پارک شده است. "
        r"اگر تعداد کل چرخ‌های آن‌ها روی هم $56$ عدد باشد، در این پارکینگ چند خودرو و چند موتورسیکلت وجود دارد؟ "
        r"\textbf{(جدول حدس و آزمایش را با حداقل سه حدس رسم کرده و پاسخ نهایی را بنویسید)}"
    )
    text = add_question(text, q3, khat=5)

    # سؤال ۴: راهبرد الگوسازی و حذف حالت‌های نامطلوب
    q4 = (
        r"حاصل‌ضرب سن دو برادر برابر $48$ است. اگر بدانیم مجموع سن آن‌ها کمترین مقدار ممکن است، "
        r"سن هر کدام از برادرها چند سال است؟ "
        r"\textbf{(جدول حالت‌های مختلف ضرب را به صورت نظام‌دار بنویسید و حالت مطلوب را مشخص کنید)}"
    )
    text = add_question(text, q4, khat=4)

    text = add_enteha(text)

    file_tex = os.path.join(CURRENT_DIR, "آزمون ریاضی هفتم گزینه دو ۲۳ مهر - نمونه ۱.tex")
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)
    pdf_out = file_tex[:-4] + ".pdf"
    return pdf_out

def build_sample_2():
    text = base_first_text
    text = add_sarbarg(
        text,
        answertime="۴۰ دقیقه",
        examdate="۲۳ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان دوره اول",
        branch="نمونه ۲",
        school="شهید جوانبخت",
        grade="ریاضی هفتم (نمونه ۲)",
        topic="فصل ۱: راهبردهای حل مسئله",
    )

    # سؤال ۱: راهبرد الگویابی و تفکر جبری
    q1 = (
        r"در الگوی زیر، چوب‌کبریت‌ها برای ساختن مثلث‌های به هم چسبیده به کار رفته‌اند:" + "\n\n"
        r"\noindent\textbf{شکل (۱):} $3$ چوب‌کبریت \hfill \textbf{شکل (۲):} $5$ چوب‌کبریت \hfill \textbf{شکل (۳):} $7$ چوب‌کبریت" + "\n\n"
        r"الف) شکل چهارم با چند چوب‌کبریت ساخته می‌شود؟ \\" + "\n"
        r"ب) رابطهٔ جبری بین شمارهٔ شکل ($n$) و تعداد چوب‌کبریت‌ها را بنویسید. \\" + "\n"
        r"ج) شکل بیست و پنجم ($25$) از چند چوب‌کبریت تشکیل شده است؟"
    )
    text = add_question(text, q1, khat=3)

    # سؤال ۲: راهبرد رسم شکل و کسرها
    q2 = (
        r"توپی از ارتفاع $18$ متری رها می‌شود. این توپ پس از هر بار برخورد به زمین، تا $\frac{2}{3}$ ارتفاع قبلی خود بالا می‌آید. "
        r"این توپ پس از برخورد سوم به زمین، تا چه ارتفاعی بالا خواهد آمد؟ "
        r"\textbf{(حل مسئله با «رسم شکل جهش‌ها» و نوشتن مراحل محاسبه الزامی است)}"
    )
    text = add_question(text, q2, khat=5)

    # سؤال ۳: راهبرد حدس و آزمایش
    q3 = (
        r"در یک مزرعه در مجموع $20$ رأس مرغ و گوسفند نگهداری می‌شود. "
        r"اگر تعداد کل پاهای آن‌ها روی هم $58$ عدد باشد، در این مزرعه چند مرغ و چند گوسفند وجود دارد؟ "
        r"\textbf{(جدول حدس و آزمایش را با حداقل سه حدس رسم کرده و پاسخ نهایی را بنویسید)}"
    )
    text = add_question(text, q3, khat=5)

    # سؤال ۴: راهبرد الگوسازی و حذف حالت‌های نامطلوب
    q4 = (
        r"مجموع سن سارا و خواهرش برابر $16$ سال است. اگر حاصل‌ضرب سن آن‌ها بیشترین مقدار ممکن باشد، "
        r"سن هر کدام چند سال است؟ "
        r"\textbf{(جدول حالت‌های ممکن جمع را به صورت نظام‌دار بنویسید و حالت مطلوب را مشخص کنید)}"
    )
    text = add_question(text, q4, khat=4)

    text = add_enteha(text)

    file_tex = os.path.join(CURRENT_DIR, "آزمون ریاضی هفتم گزینه دو ۲۳ مهر - نمونه ۲.tex")
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)
    pdf_out = file_tex[:-4] + ".pdf"
    return pdf_out

def main():
    print("1. Creating Sample 1...")
    pdf1 = build_sample_1()
    print(f"Sample 1 generated: {pdf1}")

    print("2. Creating Sample 2...")
    pdf2 = build_sample_2()
    print(f"Sample 2 generated: {pdf2}")

    print("3. Creating 2-up A5 side-by-side on A4...")
    out_2up = os.path.join(CURRENT_DIR, "آزمون ریاضی هفتم گزینه دو ۲۳ مهر - دو نمونه در یک برگه A4.pdf")
    create_2up_pdf(
        pdf1_path=pdf1,
        pdf2_path=pdf2,
        output_path=out_2up,
        scale=0.96,
        gap_mm=4,
        cut_line=True,
        rtl=True,
    )
    print(f"All done! Final 2-up PDF: {out_2up}")

if __name__ == "__main__":
    main()
