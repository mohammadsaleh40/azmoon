import os
import sys

# Ensure current directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from units import (
    first_text as base_first_text,
    add_sarbarg,
    add_question,
    add_enteha,
    create_file,
    recreate_pdf,
    delete_temp_file,
)

def build_sample_1():
    text = base_first_text
    text = add_sarbarg(
        text,
        answertime="۳۰ دقیقه",
        examdate="۲۵ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان",
        branch="",
        school="شهید جوانبخت",
        grade="هشتم",
    )

    # سؤال ۱: محاسبات عددهای صحیح (۶ نمره)
    q1 = (
        r"\textbf{حاصل هر یک از عبارت‌های زیر را به دست آورید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lll}" + "\n"
        r"الف) $25 + 34 = $ & ب) $84 - 29 = $ & ج) $120 + 230 = $ \\\\[0.5em]" + "\n"
        r"د) $(-12) + (+7) = $ & هـ) $(-8) - (-15) = $ & و) $(-4) - (+9) + (-3) = $" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_ (text, q1, barom="6", khat=0, ltr= True)

    # سؤال ۲: مفاهیم عددهای گویا (۴ نمره)
    q2 = (
        r"\textbf{به پرسش‌های زیر دربارهٔ عددهای گویا پاسخ دهید:}" + "\\\\[0.2em]\n"
        r"الف) عددهای $-\dfrac{3}{4}$ و $+1\dfrac{1}{2}$ را روی محور زیر با رسم شکل یا علامت مشخص کنید:" + "\\\\[0.15em]\n"
        r"\centerline{\begin{tikzpicture}[x=1.35cm]" + "\n"
        r"\draw[<->,thick] (-2.2,0) -- (2.6,0);" + "\n"
        r"\foreach \x in {-2,-1,0,1,2} \draw[thick] (\x,0.12) -- (\x,-0.12) node[below=1pt] {\footnotesize $\x$};" + "\n"
        r"\end{tikzpicture}}" + "\\\\[0.2em]\n"
        r"ب) قرینهٔ عدد $-\dfrac{5}{7}$ برابر است با: \dotfill \quad معکوس عدد $-\dfrac{2}{3}$ برابر است با: \dotfill \\\\[0.3em]" + "\n"
        r"ج) آیا هر عدد صحیح یک عدد گویا است؟ با یک مثال توضیح دهید: \dotfill \\\\[0.3em]" + "\n"
        r"د) در جای خالی علامت مناسب ($>$ یا $<$ یا $=$) قرار دهید: \hfill " + "\n"
        r"$-\dfrac{1}{2} \quad \bigcirc \quad -\dfrac{3}{4}$"
    )
    text = add_question(text, q2, barom="4", khat=0)

    # سؤال ۳: جمع و تفریق عددهای گویا (۵ نمره)
    q3 = (
        r"\textbf{حاصل جمع و تفریق‌های زیر را به دست آورده و در صورت امکان ساده کنید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lll}" + "\n"
        r"الف) $\left(-\dfrac{3}{5}\right) + \left(+\dfrac{1}{5}\right) = $ & " + "\n"
        r"ب) $\left(-\dfrac{2}{3}\right) - \left(+\dfrac{1}{4}\right) = $ & " + "\n"
        r"ج) $2 - \dfrac{3}{7} = $" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_question(text, q3, barom="5", khat=2)

    # سؤال ۴: ضرب و تقسیم و محاسبات ترکیبی (۵ نمره)
    q4 = (
        r"\textbf{حاصل عبارت‌های زیر را به دست آورید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}ll}" + "\n"
        r"الف) $\left(-\dfrac{4}{9}\right) \times \left(+\dfrac{3}{8}\right) = $ & " + "\n"
        r"ب) $\left(-\dfrac{6}{5}\right) \div \left(-\dfrac{3}{10}\right) = $ \\\\[1.8em]" + "\n"
        r"\multicolumn{2}{l}{ج) $\left(-\dfrac{1}{2} + \dfrac{1}{3}\right) \times (-6) = $}" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_question(text, q4, barom="5", khat=1)

    text = add_enteha(text)

    file_tex = "آزمون ریاضی کلاس هشتم مدرسه شهید جوانبخت - نمونه الف.tex"
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)

def build_sample_2():
    text = base_first_text
    text = add_sarbarg(
        text,
        answertime="۵۰ دقیقه",
        examdate="۲۳ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان",
        branch="نمونه ب",
        school="شهید جوانبخت",
        grade="هشتم (نمونه ب)",
    )

    # سؤال ۱: محاسبات عددهای صحیح (۶ نمره)
    q1 = (
        r"\textbf{حاصل هر یک از عبارت‌های زیر را به دست آورید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lll}" + "\n"
        r"الف) $42 + 53 = $ & ب) $75 - 38 = $ & ج) $350 - 120 = $ \\\\[0.5em]" + "\n"
        r"د) $(+18) + (-24) = $ & هـ) $(-14) - (+6) = $ & و) $(-7) - (-11) + (-5) = $" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_question(text, q1, barom="6", khat=0)

    # سؤال ۲: مفاهیم عددهای گویا (۴ نمره)
    q2 = (
        r"\textbf{به پرسش‌های زیر دربارهٔ عددهای گویا پاسخ دهید:}" + "\\\\[0.2em]\n"
        r"الف) عددهای $+1\dfrac{1}{3}$ و $-\dfrac{5}{2}$ را روی محور زیر با رسم شکل یا علامت مشخص کنید:" + "\\\\[0.15em]\n"
        r"\centerline{\begin{tikzpicture}[x=1.15cm]" + "\n"
        r"\draw[<->,thick] (-3.2,0) -- (2.5,0);" + "\n"
        r"\foreach \x in {-3,-2,-1,0,1,2} \draw[thick] (\x,0.12) -- (\x,-0.12) node[below=1pt] {\footnotesize $\x$};" + "\n"
        r"\end{tikzpicture}}" + "\\\\[0.2em]\n"
        r"ب) معکوس عدد صفر چیست؟ چرا؟ \dotfill \quad معکوس $-1\dfrac{1}{4}$: \dotfill \\\\[0.3em]" + "\n"
        r"ج) بین دو عدد گویا $-\dfrac{1}{5}$ و $+\dfrac{2}{5}$ دو عدد گویای دلخواه بنویسید: \dotfill \\\\[0.3em]" + "\n"
        r"د) در جای خالی علامت مناسب ($>$ یا $<$ یا $=$) قرار دهید: \hfill " + "\n"
        r"$-0.6 \quad \bigcirc \quad -\dfrac{3}{5}$"
    )
    text = add_question(text, q2, barom="4", khat=0)

    # سؤال ۳: جمع و تفریق عددهای گویا (۵ نمره)
    q3 = (
        r"\textbf{حاصل جمع و تفریق‌های زیر را به دست آورده و در صورت امکان ساده کنید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lll}" + "\n"
        r"الف) $\left(+\dfrac{5}{8}\right) + \left(-\dfrac{7}{8}\right) = $ & " + "\n"
        r"ب) $\left(-\dfrac{3}{5}\right) - \left(-\dfrac{1}{2}\right) = $ & " + "\n"
        r"ج) $-3 + 1\dfrac{2}{5} = $" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_question(text, q3, barom="5", khat=2)

    # سؤال ۴: ضرب و تقسیم و محاسبات ترکیبی (۵ نمره)
    q4 = (
        r"\textbf{حاصل عبارت‌های زیر را به دست آورید:}" + "\n"
        r"\begin{LTR}" + "\n"
        r"\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}ll}" + "\n"
        r"الف) $\left(-\dfrac{15}{8}\right) \times \left(-\dfrac{4}{5}\right) = $ & " + "\n"
        r"ب) $\left(+\dfrac{7}{12}\right) \div \left(-\dfrac{14}{3}\right) = $ \\\\[1.8em]" + "\n"
        r"\multicolumn{2}{l}{ج) $-\dfrac{2}{3} \times \left(\dfrac{3}{4} - \dfrac{1}{2}\right) = $}" + "\n"
        r"\end{tabular*}" + "\n"
        r"\end{LTR}"
    )
    text = add_question(text, q4, barom="5", khat=1)

    text = add_enteha(text)

    file_tex = "آزمون ریاضی کلاس هشتم مدرسه شهید جوانبخت - نمونه ب.tex"
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)

if __name__ == "__main__":
    print("Building 8th Grade Sample 1 (Alef)...")
    build_sample_1()
    print("Building 8th Grade Sample 2 (Be)...")
    build_sample_2()
    print("Done!")
