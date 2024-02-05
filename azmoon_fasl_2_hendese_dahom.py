#import os

from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="60 دقیقه" , examdate= "18/11/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_fourchoice(first_text , "اگر $AB$ = cm$20$ و $A'B'$ = m$2$، نسبت اندازه‌ی پاره خط $AB$ به اندازه $A'B'$ کدام است؟", ["$0.2$", "$\\dfrac{1}{10}$", "$1$", "$10$"], chand=4, barom= 0.5)
first_text = add_fourchoice(first_text , "اگر $\\dfrac{a}{b} = \\dfrac{c}{d}$، حاصل $\\dfrac{a+c}{b+d}$ برابر است با (مخرج‌ها صفر نیستند):" , list_choice=["$\\dfrac{a-c}{d-b}$","$\\dfrac{ab}{cd}$","$\\dfrac{a-c}{b-d}$","$\\dfrac{ab}{bc}$",], chand= 4 , khat = 1 , barom= 1)
first_text = add_question(first_text , "اگر $ (z\\neq 0) , \\dfrac{z}{6} = \\dfrac{y}{3} = \\dfrac{x}{2}$ حاصل $\\dfrac{x+y}{z}$ را بدست آورید." , barom= 1)
first_text = add_question(first_text , "طول دو ضلع مثلثی $8$ و $10$ است و طول ضلع سوم آن واسطه‌ی هندسی طول‌های این دو ضلع است. طول ضلع سوم این مثلث کدام است؟" , barom = 1 , khat= 2)
first_text = add_question(first_text , "در شکل زیر $\\dfrac{CD}{CB} = \\dfrac{3}{4}$ و $2AB = AC$ نسبت $\\dfrac{DF}{DI}$ را بدست آورید.  \\\\ \includegraphics[scale = 0.5]{Screenshot from 2024-02-05 11-08-12}", khat= 1 , barom= 2)
first_text = add_question(first_text , "در شکل مقابل MN||BC. حاصل x+y چقدر است؟  \\\\ \includegraphics[scale = 0.5]{Screenshot from 2024-02-05 11-17-20}", khat= 1 , barom= 2)
first_text = add_question(first_text , "در شکل مقابل دو مثلث ABD و ACB متشابه‌اند. مقدار AD+AB چقدر است؟ \\\\ \includegraphics[scale = 0.5]{Screenshot from 2024-02-05 12-21-16}", barom= 2 )
first_text = add_question(first_text , "در شکل زیر مقدار x را بدست آورید.\\\\ \includegraphics[scale = 0.5]{Screenshot from 2024-02-05 12-24-26}", barom= 1 , khat= 1)
first_text = add_question(first_text , "در شکل مقابل $ABCD$ متوازی الاضلاع است. اگر $AF = \\dfrac{1}{4}AC$، طول پاره خط $BE$ چقدر است؟ \\\\ \includegraphics[scale = 0.5]{Screenshot from 2024-02-05 12-33-05}", barom= 2 )


first_text = add_enteha(first_text)
esm_emtehan = "آزمون فصل ۲ هندسه دهم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)