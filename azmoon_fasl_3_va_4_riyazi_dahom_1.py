#import os

from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="90 دقیقه" , examdate= "18/11/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")
first_text = add_section(first_text , "سؤالات ساده")
first_text = add_fourchoice(first_text , "عدد 4- چند ریشه 8 ام دارد؟", ["0", "1", "2", "8"], chand=4, barom= 0.5)
first_text = add_question(first_text ,"""
		ریشه دوم عدد ۱۶ را حساب کنید.""" , khat = 1 , barom=0.5
)
first_text = add_question(first_text , "در چه مواردی ریشه گیری باعث کوچک شدن مقدار عددی عدد اولیه می‌شود؟", khat = 1, barom= 0.5)
first_text = add_question(first_text , "در چه مواردی ریشه گیری باعث بزرگ شدن مقدار عددی عدد اولیه می‌شود؟", khat = 1 , barom= 0.5)
first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را حساب کنید و تا حد امکان از زیر رادیکال خارج کنید.", ["$\\sqrt[4]{16}\\times\\sqrt[4]{81} = $","$\\sqrt[4]{16}\\times\\sqrt[2]{9} = $","$\\sqrt[4]{b}\\times\\sqrt[4]{a} = $", "$\\sqrt[3]{8}\\times\\sqrt[3]{27} = $", "$\\sqrt[3]{16}\\times\\sqrt[3]{25} = $", "$\\sqrt[3]{16}\\times\\sqrt[3]{36} = $"], ltr = True, chand=3 , barom = 3)
first_text = add_multiparts(first_text , "توان‌های گویای زیر را به شکل رادیکالی و رادیکال‌های زیر را به شکل توان‌های گویا بنویسید. (اگر عبارتی تعریف نمی‌شود آن را بیان کنید.)",
["$\\sqrt[7]{5^3} = $", "$(4)^{\\dfrac{5}{6}} = $" , "$(12)^{\\dfrac{5}{3}} = $" , "$(-\\dfrac{3}{7})^{\\dfrac{5}{8}} = $"], chand=2, ltr = True, barom=1)
first_text = add_question(first_text , "به کمک اتحاد حاصل عبارت زیر را حساب کنید. \\begin {LTR} $9999^2 =$  \\end{LTR}", barom=1.5)
first_text = add_question(first_text , "معادله زیر را به روش مربع کامل حل کنید. \\begin {LTR} $x^2+6x = 2$ \\\\ \\\\ \\\\ \\\\ \\end{LTR}", barom=1)
first_text = add_question(first_text , "معادله زیر را به روش دلتا حل کنید. \\begin {LTR}$x^2+6x = 2$ \\\\ \\\\ \\\\ \\end{LTR}", barom=1)
first_text = add_question(first_text , "معادله زیر را به روش تجزیه به عبارت‌های جبری حل کنید. \\begin {LTR}$x^2+7x + 6= 0$ \\end{LTR}", barom= 1)
first_text = add_multiparts(first_text , "عبارت‌های زیر را ساده کنید." , list_part=["$\\dfrac{x^3-1}{(x-1)^3}$" , "$\\dfrac{x^6+1}{x^4+2x^2+1}$"], ltr=True , barom= 2)

first_text = add_section(first_text , "سؤالات متوسط")
first_text = add_question(first_text , "حاصل عبارت $\\sqrt[4]{\\sqrt[5]{81}}-\\sqrt[5]{96}-\\dfrac{3}{\\sqrt[5]{81}}$ را بدست آورید.", khat=2 , barom = 1)
first_text = add_question(first_text , "اگر $\\sqrt{\\sqrt{3}}= \\sqrt[3]{3\\sqrt{x}}$ باشد مقدار x را بدست آورید.", khat=2 , barom = 1)

first_text = add_question(first_text , "اگر $\\sqrt{x+2}+\\sqrt{x-4} = 3$، حاصل عبارت $\\sqrt{x+2}-\\sqrt{x-4}$ را بدست آورید.", khat= 5 , barom= 1)
first_text = add_multiparts(first_text , "عبارت‌های زیر را در صورت نیاز ابتدا گویا و سپس ساده کنید." , list_part=["$\\dfrac{\\sqrt[3]{x}-2}{\\sqrt{x+1}-3}$", "$\\dfrac{x^3-3x+2}{x^3+3x-4}$ \\\\ \\begin {RTL}عبارت $x-1$ را می‌توان تجزیه کرد. \\end{RTL}"], ltr=True , barom= 2, khat_beyn = 1)

first_text = add_section(first_text , "سؤالات باز پاسخ")
first_text = add_question(first_text , "تفاوت ریشه دوم و رادیکال با فرجه دو را بنویسید." , khat= 3 , barom= 1)
first_text = add_question(first_text , "یک قاعده کلی برای تعداد ریشه‌های nام یک عدد در صورت وجود بنویسید.", khat=2 , barom=2)
first_text = add_question(first_text , """معادل عبارت زیر را به صورتی که علامت منفی در توان نداشته باشیم بنویسید. \\
	\\begin {LTR} $a^{-5}=$ \\\\ \\end {LTR}""", barom=0.5)

first_text = add_enteha(first_text)
esm_emtehan = "آزمون فصل ۳ و ۴ ریاضی دهم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)