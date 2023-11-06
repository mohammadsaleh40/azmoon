from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="20 دقیقه" , examdate= "15/08/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_fourchoice(first_text , "اگر $A = [-\\dfrac{3}{2},\\sqrt{5}]$ و $B = [\\sqrt{3} , \\dfrac{16}{3}]$ باشد. مجموعه $A\\bigcup‌B$  شامل چند عدد صحیح است؟" , list_choice=[
    "$5$",
    "$6$",
    "$7$",
    "$8$",
    
], chand=4 
)

first_text = add_fourchoice(first_text , "اگر $n(A \\bigcup B) = 20$، $n(A\\bigcap B)=5$ و $2n(A) = 3n(B)$، مقدار $n(A)$ کدام است؟", chand=4 , list_choice=[
    "$6$",
    "$9$",
    "$12$",
    "$15$",    
])

first_text = add_fourchoice(first_text , "در دنباله حسابی $a_{1} , a_{2} , ...$ حاصل $\\dfrac{a_3}{a_2+a_4}+\\dfrac{a_4}{a_3+a_5}+...+\\dfrac{a_16}{a_{15}+a_{17}}$ چند است؟" , 
                            list_choice=["$\\dfrac{7}{2}$","$\\dfrac{13}{2}$","$7.5$","$7$"] , chand=4)
first_text = add_fourchoice(first_text , "در یک دنباله، جمله اول برابر ۴ و برای هر $n>1$، $\dfrac{a_n}{a_{n+1}}=2$. جمله دهم این دنباله کدام است؟" , 
                            list_choice=["$\\dfrac{1}{128}$","$\\dfrac{1}{64}$","$1024$","$2048$"] ,chand=4)
first_text = add_fourchoice(first_text , "اگر x , y , 2 , z , t جمله‌های متوالی دنباله‌ای هندسی باشند، حاصل $\\dfrac{x^2t^2}{yz}$ کدام است؟" , list_choice=["$16$" , "$2$", "$4$" , "$8$"] , chand=4)
first_text = add_fourchoice(first_text , "اعداد $2^a$ ، $4\\sqrt{2}$ ، $2^b$ سه چمله متوالی از یک دنباله هندسی اند. واسطه حسابی $a$ و $b$ کدام است؟",
                            list_choice=["$\\sqrt{2}$" , "$1.5$" , "$2$" , "$2.5$"] , chand=4)
first_text = add_fourchoice(first_text , "در شکل زیر مربع‌های کوچک برابرند. مقدار $\\tan\\alpha$ کدام است؟ \\\\ \includegraphics[scale = 0.18]{Screenshot_2023-11-06-06-32-43-456_cn.wps.moffice_eng-edit}" , list_choice=[
    "$\\dfrac{2}{3}$","$\\dfrac{3}{2}$","$\\dfrac{4}{3}$","$\\dfrac{3}{4}$"
], chand=4)
first_text = add_fourchoice(first_text , "در شکل زیر طول ضلع مربع‌های کوچک برابر ۱ است. مقدار $\\tan\\alpha + \\sin\\alpha$ کدام است؟ \\\\ \includegraphics[scale = 0.08]{Screenshot_2023-11-06-06-40-47-663_cn.wps.moffice_eng-edit}" , list_choice=[
    "$\\dfrac{34}{15}$","$\\dfrac{3}{15}$","$\\dfrac{32}{15}$","$\\dfrac{31}{15}$"
], chand=4)

first_text = add_fourchoice(first_text , "در شکل زیر $\\tan \widehat{B} = \\dfrac{1}{2}$ و $c-b=4$. مقدار $a$ کدام است؟ \\\\ \includegraphics[scale = 0.3]{Screenshot_2023-11-06-06-44-17-910_cn.wps.moffice_eng-edit}" , list_choice=[
    "$2\\sqrt{5}$","$4\\sqrt{5}$","$3\\sqrt{5}$","$5\\sqrt{5}$"
], chand=4)

first_text = add_enteha(first_text)
esm_emtehan = "۱۰ تست از فصل ۱ ریاضی ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)