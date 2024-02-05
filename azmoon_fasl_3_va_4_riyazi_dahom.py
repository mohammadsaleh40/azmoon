#import os

from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts


first_text = add_sarbarg(first_text, grade= "دهم")

first_text = add_fourchoice(first_text , "عدد 4- چند ریشه 8 ام دارد؟", ["0", "1", "2", "8"], chand=4)
first_text = add_question(first_text ,"""
		ریشه دوم عدد ۱۶ را حساب کنید.""" , khat = 1
)
first_text = add_question(first_text , "در چه مواردی ریشه گیری باعث کوچک شدن مقدار عددی عدد اولیه می‌شود؟", khat = 1)
first_text = add_question(first_text , "در چه مواردی ریشه گیری باعث بزرگ شدن مقدار عددی عدد اولیه می‌شود؟", khat = 1)
first_text = add_question(first_text , "یک قاعده کلی برای تعداد ریشه‌های nام یک عدد در صورت وجود بنویسید.", khat=2)
first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را حساب کنید.", ["$\\sqrt[4]{16}\\times\\sqrt[4]{81} = $","$\\sqrt[4]{16}\\times\\sqrt[2]{9} = $","$\\sqrt[4]{b}\\times\\sqrt[4]{a} = $", "$\\sqrt[3]{16}\\times\\sqrt[3]{81} = $"], ltr = True)
first_text = add_question(first_text , """معادل عبارت زیر را به صورتی که علامت منفی در توان نداشته باشیم بنویسید. \\
	\\begin {LTR} $a^{-5}=$ \\\\ \\end {LTR}""")
first_text = add_multiparts(first_text , "توان‌های گویای زیر را به شکل رادیکالی و رادیکال‌های زیر را به شکل توان‌های گویا بنویسید. (اگر عبارتی تعریف نمی‌شود آن را بیان کنید.)",
["$\\sqrt[7]{5^3} = $", "$(4)^{\\dfrac{5}{6}} = $" , "$(12)^{\\dfrac{5}{3}} = $" , "$(-\\dfrac{3}{7})^{\\dfrac{5}{8}} = $"], chand=2, ltr = True)
first_text = add_question(first_text , "به کمک اتحاد حاصل عبارت زیر را حساب کنید. \\begin {LTR} $999^2 =$ \\\\ \\\\ \\\\ \\end{LTR}")
first_text = add_question(first_text , "اگر $\\sqrt{x+2}+\\sqrt{x-4} = 3$، حاصل عبارت $\\sqrt{x+2}-\\sqrt{x-4}$ را بدست آورید.", khat= 5)
first_text = add_question(first_text , "معادله زیر را به روش مربع کامل حل کنید. \\begin {LTR} $x^2+6x = 2$ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\end{LTR}")
first_text = add_question(first_text , "معادله زیر را به روش دلتا حل کنید. \\begin {LTR}$x^2+6x = 2$ \\\\ \\\\ \\\\ \\\\ \\end{LTR}")
first_text = add_question(first_text , "جدول تعیین علامت عبارت زیر را بنویسید. \\begin {LTR} $x^2+6x-2$ \\\\ \\\\ \\\\ \\\\ \\end{LTR}")
first_text = add_multiparts(first_text , "نا معادله‌های زیر را حل کنید.", ["$|\\dfrac{x-1}{2}-1| \\geq 0$" , "$|\\dfrac{x-1}{2}-1| \\geq 3$" , "$x+1 \\leq 5-x < 2x +3$"] , ltr = True )
first_text = add_question(first_text , "با نمودار ون و فلش مثالی برای تابع بزنید." , khat= 2)

first_text = add_question(first_text , "تفاوت ریشه دوم و رادیکال با فرجه دو را بنویسید." , khat= 3)



first_text = add_enteha(first_text)
create_file(first_text , "آزمون فصل ۳ و ۴ دهم.tex")
recreate_pdf("آزمون فصل ۳ و ۴ دهم.tex")
delete_temp_file("آزمون فصل ۳ و ۴ دهم.tex")