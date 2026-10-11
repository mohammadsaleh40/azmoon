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
        answertime="۳۵ دقیقه",
        examdate="۲۵ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان",
        branch="نمونه ۱",
        school="شهید جوانبخت",
        grade="هفتم (نمونه ۱)",
    )

    # سؤال ۱: مشترک (مسئله ساختمان)
    q1 = (
        "یک ساختمان $5$ طبقه ساخته شده است. بالاترین طبقهٔ آن $2$ واحد دارد، "
        "اما هر یک طبقه که پایین می‌رویم، $2$ واحد به تعداد واحدها اضافه می‌شود.\\\\\n"
        "الف) چه الگویی بین تعداد واحدها در طبقه‌های این ساختمان وجود دارد؟\\\\\n"
        "ب) این ساختمان در کل چند واحد دارد؟"
    )
    text = add_question(text, q1, khat=4)

    # سؤال ۲: مسئله قورباغه (سؤال ۲ اولیه)
    q2 = (
        "قورباغه‌ای می‌خواهد از یک دیوار بالا برود. او با هر جهش $3$ متر بالا می‌رود و "
        "هر بار $2$ متر سُر می‌خورد و پایین می‌آید. اگر ارتفاع دیوار $9$ متر باشد، "
        "او با چند جهش به بالای دیوار می‌رسد؟ (رسم شکل یا نوشتن مراحل راه‌حل الزامی است)"
    )
    text = add_question(text, q2, khat=7)

    # سؤال ۳: مسئله چوب‌کبریت (سؤال ۴ اولیه)
    q3 = (
        "با توجه به الگوی چوب‌کبریت‌های زیر:\\\\[0.3em]\n"
        r"\noindent" + "\n"
        r"\begin{minipage}[c]{0.50\linewidth}" + "\n"
        r"الف) شکل دهم با چند چوب‌کبریت ساخته می‌شود؟ \\\\[0.8em]" + "\n"
        r"ب) چرا؟ (رابطه یا روش خود را توضیح دهید)" + "\n"
        r"\end{minipage}\hfill" + "\n"
        r"\begin{minipage}[c]{0.48\linewidth}" + "\n"
        r"\centering" + "\n"
        r"\includegraphics[width=\linewidth]{haftom_choob_kebrit}" + "\n"
        r"\end{minipage}"
    )
    text = add_question(text, q3, khat=5)

    text = add_enteha(text)
    
    file_tex = "آزمون ریاضی کلاس هفتم مدرسه شهید جوانبخت - نمونه ۱.tex"
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)

def build_sample_2():
    text = base_first_text
    text = add_sarbarg(
        text,
        answertime="۳۵ دقیقه",
        examdate="۲۵ مهر ۱۴۰۵",
        teacher="محمد صالح علی اکبری",
        city="گناباد",
        schooltitle="دبیرستان",
        branch="نمونه ۲",
        school="شهید جوانبخت",
        grade="هفتم (نمونه ۲)",
    )

    # سؤال ۱: مشترک (مسئله ساختمان)
    q1 = (
        "یک ساختمان $5$ طبقه ساخته شده است. بالاترین طبقهٔ آن $2$ واحد دارد، "
        "اما هر یک طبقه که پایین می‌رویم، $2$ واحد به تعداد واحدها اضافه می‌شود.\\\\\n"
        "الف) چه الگویی بین تعداد واحدها در طبقه‌های این ساختمان وجود دارد؟\\\\\n"
        "ب) این ساختمان در کل چند واحد دارد؟"
    )
    text = add_question(text, q1, khat=4)

    # سؤال ۲: مسئله انگشتان دست (سؤال ۳ اولیه)
    q2 = (
        "با انگشتان یک دست به $5$ صورت می‌توان عدد $1$ را نشان داد. "
        "به چند صورت می‌توان عدد $2$ را نشان داد؟ (تمام حالت‌های مختلف و روش خود را بنویسید)"
    )
    text = add_question(text, q2, khat=4)

    # سؤال ۳: مسئله دوچرخه و سه‌چرخه (سؤال ۵ اولیه)
    q3 = (
        "$20$ دستگاه دوچرخه و سه‌چرخه در یک پارکینگ وجود دارد. "
        "اگر تعداد کل چرخ‌های آن‌ها $45$ عدد باشد، "
        "چند دوچرخه و چند سه‌چرخه در توقفگاه وجود دارد؟ (راه‌حل یا جدول حدس و آزمایش را کامل بنویسید)"
    )
    text = add_question(text, q3, khat=9)

    text = add_enteha(text)

    file_tex = "آزمون ریاضی کلاس هفتم مدرسه شهید جوانبخت - نمونه ۲.tex"
    create_file(text, file_tex)
    recreate_pdf(file_tex)
    recreate_pdf(file_tex)
    delete_temp_file(file_tex)

if __name__ == "__main__":
    print("Building Sample 1...")
    build_sample_1()
    print("Building Sample 2...")
    build_sample_2()
    print("Done!")
