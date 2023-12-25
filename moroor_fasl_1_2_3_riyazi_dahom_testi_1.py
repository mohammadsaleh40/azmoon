from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="80 دقیقه" , examdate= "آذر ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_fourchoice(first_text , "ناحیه رنگی در نمودار ون مقابل، کدام مجموعه را مشخص می‌کند؟ \\\\ \includegraphics[scale = 0.18]{Screenshot from 2023-12-15 04-49-09}", list_choice=["$(A\\bigcup B) \\bigcap C'$" , "$A\\bigcap (B\\bigcup C)'$" ,"$A\\bigcap(B-C)'$", "$(A\\bigcap B)\\bigcap C'$" ], chand=4 , barom=1)
first_text = add_fourchoice(first_text , "اگر مجموعه مرجع $\mathbb{R}$ باشد، $A = [2 , 5]$ و $B = (4 , 8)$، مجموعه $B'-A'$ کدام است؟" ,list_choice=["$(2,4]$" , "$[2,4]$" , "$[2,4]\\bigcup[5,8]$", "$[2,4]\\bigcup(5,8)$"] , barom=1 )
first_text = add_fourchoice(first_text , "مقدار عبارت $A=\\dfrac{\\tan^2 30^\circ + \\tan^245^\circ + \\tan^2 60^\circ }{\cot60^\circ -\cot30^\circ}$ کدام است؟", list_choice=["$\\dfrac{13\\sqrt{3}}{6}$",
                    "$-\\dfrac {13\sqrt {3}}{6}$","$-2\\sqrt{3}$" , "$2\\sqrt{3}$"] , chand=4  , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل، طول طناب ABC بر حسب $\\theta$ کدام است؟ \\\\ \includegraphics[scale = 0.18]{Screenshot from 2023-12-15 06-07-16}" , list_choice=["$\\dfrac{8}{\cos\\theta}$" ,"$\\dfrac{2}{\cos\\theta}$" , "$\\dfrac{6}{\sin\\theta}$","$\\dfrac{3}{sin \\theta}$"] ,chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل زیر، حاصل $\\tan\\alpha$ کدام است؟ \\\\\includegraphics[scale = 0.3]{Screenshot from 2023-12-15 20-26-50}", list_choice=["$\dfrac{5}{3}$","$\dfrac{4}{7}$","$\dfrac{4}{3}$","$\dfrac{3}{8}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل مربع‌های کوچک برابرند. مقدار $\\tan(x) \\tan(y) \\tan(z)$ کدام است؟ \\\\\includegraphics[scale = 0.35]{Screenshot from 2023-12-15 20-31-25}", list_choice=["$1$","$\dfrac{9}{8}$","$\dfrac{27}{16}$","$\dfrac{27}{8}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "مجموع پنج عدد که جملات متوالی دنباله‌ای هندسی هستند برابر ۲ است. اگر عدد وسطی برابر ۱ باشد، مجموع معکوسات این اعداد کدام است؟", list_choice=["$2$","$\dfrac{1}{4}$","$\dfrac{1}{2}$","$1$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل طول ضلع مربع‌های کوچک برابر ۱ است. مقدار $\\cos \\beta +\\sin \\alpha$ کدام است؟ \\\\\includegraphics[scale = 0.31]{Screenshot from 2023-12-15 20-36-57}", list_choice=["$\\dfrac{\sqrt{2}+ \sqrt{5}}{\sqrt{10}}$","$\dfrac{1+\\sqrt{5}}{\\sqrt{10}}$","$\dfrac{1+\\sqrt{2}}{\sqrt{10}}$","$\dfrac{\\sqrt{2}+\\sqrt{3}}{\\sqrt{10}}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل زیر از بالای یک فانوس دریایی به ارتفاع $200$ متر، یک قایق با زاویه $35^{\\circ}$ و قایق دیگری با زاویه $27^{\\circ}$ دیده می‌شود. فاصله دو قایق از یکدیگر چقدر است؟ ($\\tan 35^{\\circ} = 0.7$ و $\\tan 27^{\\circ} = 0.5$)\\\\\includegraphics[scale = 0.3]{Screenshot from 2023-12-15 20-45-31}", list_choice=["$30$","$40$","$20$","$50$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل $\hat{A}= 90^{\circ}، \widehat{ABD}=\widehat{DBC}=30^\circ$ و $AD = 12$. طول $DC$ چقدر است؟ \\\\\includegraphics[scale = 0.31]{Screenshot from 2023-12-15 21-00-26}", list_choice=["$18$","$20$","$24$","$15$"], chand = 4 , barom=1)
first_text = add_fourchoice(first_text , "اگر $[-1 , 5) \\bigcap [a,6) = [2a-1 , 5)$، در بازه $[-a , a]$ چند عدد صحیح وجود دارد؟", list_choice=["$4$","$3$","$2$","$1$"], chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل طول ضلع مربع‌های کوچک برابر ۱ است. مقدار $\\cos \\alpha$ کدام است؟ \\\\\includegraphics[scale = 0.7]{Screenshot from 2023-12-15 21-07-51}", list_choice=["$\\dfrac{2}{\sqrt{13}}$","$\dfrac{1}{\\sqrt{13}}$","$\dfrac{2}{\sqrt{11}}$","$\dfrac{1}{\\sqrt{11}}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل زیر طول ضلع HC چقدر است؟ \\\\\includegraphics[scale = 0.7]{Screenshot from 2023-12-15 21-16-17}", list_choice=["$\\sqrt{3}$","$\dfrac{1}{\\sqrt{13}}$","$\dfrac{2}{\sqrt{11}}$","$\dfrac{1}{\\sqrt{11}}$"] , chand=4 , barom=1)

first_text = add_fourchoice(first_text , "در شکل مقابل $ABCD$ مستطیل است، $DE=4$ و $BC=5$. مقدار $\cot \\alpha$ کدام است؟ \\\\\includegraphics[scale = 0.651]{Screenshot from 2023-12-15 21-16-33}", list_choice=["$\\dfrac{4}{5}$","$\\dfrac{5}{4}$","$\\dfrac{4}{3}$","$\\dfrac{3}{4}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "در شکل مقابل مساحت مثلث ABC کدام است؟ \\\\\includegraphics[scale = 0.65]{Screenshot from 2023-12-15 21-16-50}", list_choice=["$\\dfrac{64}{5}$","$\\dfrac{64}{3}$","$\\dfrac{64}{9}$","$\\dfrac{64}{7}$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "کدام است؟ $\\dfrac{x^2+x+1}{2x^2+5x}\div\\dfrac{x^3-1}{2x^2+3x-5}$", list_choice=["$\\dfrac{2}{1+x}$","$\\dfrac{1}{2-x}$","$x$","$\\dfrac{1}{x}$"], khat =0 , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "اگر $ab=1$ و $a-b=76$ مقدار $\\sqrt[3]{a} - \\sqrt[3]{b}$ کدام است؟", list_choice=["$3$", "$4$", "$5$", "$6$"] , chand=4 , barom=1)
first_text = add_fourchoice(first_text , "معکوس عدد$\\sqrt{2-\\sqrt{2}}$برابر کدام است؟", list_choice=["$\\sqrt{4+\\sqrt{2}}$", "$\\sqrt{1+\\dfrac{\\sqrt{2}}{2}}$", "$\\sqrt{\\sqrt{2}+1}$", "$\\sqrt{\\sqrt{2}-1}$"] , chand=4 , barom=1)
first_text = add_question(first_text , "حاصل $\\dfrac{4+2\\sqrt{3}}{\\sqrt{3}-1}-5$ را محاسبه کنید." , barom=1)
first_text = add_question(first_text , "اگر $\\dfrac{1}{\\sqrt[3]{3}-1} = \\dfrac{1}{2}\\sqrt[3]{9}+\\dfrac{1}{2}\\sqrt[3]{3}+a$ مقدار a را محاسبه کنید." , barom=2)
first_text = add_question(first_text , "حاصل عبارت $A=\\dfrac{\\sqrt{2+\\sqrt{3}}+\\sqrt{2-\\sqrt{3}}}{\\sqrt{2+\\sqrt{3}}-\\sqrt{2-\\sqrt{3}}}$" , barom=1)


first_text = add_enteha(first_text)
esm_emtehan = "مرور ۳ فصل اول ریاضی ۱ تستی_۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)