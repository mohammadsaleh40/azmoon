from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="120 دقیقه" , examdate= "شهریور 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شاهد امام (ره)" ,grade= "هفتم")



first_text = add_multiparts(first_text , """عبارت‌های زیر راحساب کنید.""" , list_part=["$-73 + (-82) \\times 2 + 7 -43 \\times (-3) = $" , "$\\dfrac{\\dfrac{32}{-2}}{\\dfrac{-30}{6}}$"] , ltr=True , khat= 1 , khat_beyn=1)
first_text = add_question(first_text , "در تصویر دهم چند چوب کبریت وجود دارد؟ \\\\ در شکل n ام چند چوب کبریت وجود دارد؟ \\\\ \includegraphics[scale = 0.3]{donbale_choob_kebriti}" , khat = 2)
first_text = add_multiparts(first_text , "معادله‌های زیر را حل کنید:" , khat_beyn= 2 , khat= 3 , list_part=["$8x - 4 = 27$" , "$3x = 6x - 7$"] , ltr= True)
first_text = add_multiparts(first_text , "عبارت‌های زیر را در صورت امکان \\underline{به کمک توان} ساده کنید." , list_part=["$3+3+3$" , "$2 \\times 2 \\times 2 \\times 2 =$"], ltr=True)
first_text = add_multiparts(first_text , "تساوی‌های زیر را کامل کنید.(به شکل عبارت توان دار بنویسید.)" , list_part=["$(x + y) ( x + y ) = $" , "$\\dfrac{y \\times y \\times y \\times y \\times y}{x \\times x \\times x} =$"], khat_beyn= 1 , khat= 1 , ltr= True)
first_text = add_multiparts(first_text , "با رعایت اولویت‌های محاسباتی عبارت‌های زیر را حساب کنید." , list_part=["$2 \\times 3^{2} - (2^{2} + 2)$" , "$\\dfrac{10 \div (8 - 6)+9 \\times 4}{2^{5}+3^{5}}$"] , ltr= True , khat_beyn= 1)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید." , list_part=["$\\sqrt{\\dfrac{9}{25}}$" , "$-\sqrt{49}$"] ,khat_beyn= 0 , khat= 1 , chand=2 , ltr= True)
first_text = add_multiparts(first_text , "هر یک از اعداد زیر بین کدام دو عدد صحیح متوالی قرار دارد؟ توضیح دهید." , list_part=["$\\sqrt{7}$" , "$\\sqrt{60}$" , "$-\\sqrt{42}$"] , ltr=True)
first_text = add_question(first_text , """بردار $\\begin{bmatrix} -3 \\\\ 2 \\end{bmatrix}$ را در محور مختصات زیر رسم کنید که ابتدای بردار نقطه $\\begin{bmatrix} 3 \\\\ -2 \\end{bmatrix}$ باشد.
\\\\ مختصات نقطه انتهای آن را بنویسید. \\\\
باتوجه به شکل مختصات نقطه‌ها و بردارهای زیر را بنویسید. \\\\
$A = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\ $B = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\ $\overrightarrow{AB} = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\ $D = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\ $C = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\ $\overrightarrow{CD} = \\begin{bmatrix} \\ \\ \\ \\\\  \\end{bmatrix}$ \\
\\\\
\includegraphics[scale = 0.3]{mokhtasat_haftom}""")
first_text = add_multiparts(first_text , """مختصات مورد نظر (مقدار x و y ) را بدست بیاورید. \\\\""" , 
list_part=[" $\\begin{bmatrix} x \\\\ y \\end{bmatrix} + \\begin{bmatrix} -1 \\\\ 2 \\end{bmatrix} = \\begin{bmatrix} 2 \\\\ -1 \\end{bmatrix}$" ,
"$\\begin{bmatrix} -4 \\\\ 3 \\end{bmatrix} + \\begin{bmatrix} 2 \\\\ -1 \\end{bmatrix} = \\begin{bmatrix} x \\\\ -y \\end{bmatrix}$" ] , khat_beyn= 2 ,ltr = True ,  khat= 2
)
first_text = add_multiparts(first_text,"شمارنده‌های اعداد زیر را جلوی آن‌ها بنویسید." , list_part=["شمارنده‌های 12" , "شمارنده‌های 18" , "شمارنده‌های 25" , "شمارنده‌های 53"] )

first_text = add_multiparts(first_text,"با تجزیه کردن (نوشتتن عدد به صورت ضرب عامل‌های اول) عددهای صورت و مخرج، کسرها را تا حد امکان ساده کنید. در واقع شمارنده‌های مشترک صورت و مخرج را ساده کنید." , list_part=["$\\dfrac{126}{39}$" , "$\\dfrac{50}{20}$" , "$\\dfrac{81}{32}$" , "$\\dfrac{42}{21}$"], ltr= True , khat_beyn=1 , chand= 2 , khat= 1)
first_text = add_multiparts(first_text , "ب.م.م. و ک.م.م. های زیر را حساب کنید." , list_part=["$[12 , 18]$", "$[25 , 35]$", "$(35 , 28)$" , "$(7 , 3 , 5)$" , "$[100 , 25 , 4]$" , "$(32 , 28)$" , "$(70 , 6)$" , "$[30 , 7 , 6]$" , "$(30 , 7 , 6)$"] ,ltr= True, chand= 3 , khat=2 , khat_beyn=3)


first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال مرور ریاضی هفتم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)