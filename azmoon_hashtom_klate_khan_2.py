from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۹۰ دقیقه" , examdate= "دی ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "۱", school="مقداد" ,grade= "هشتم")

first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$ 300 - 20 + 30 = $","$5 -80 + 10 + 80 = $"],chand=2 , barom= 1, ltr=True)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$2 \\times (3)  = $","$4 \\times (-7) = $"],chand=2 , barom= 1, ltr=True)


first_text = add_multiparts(first_text , "حاصل تقسیم‌های زیر را محاسبه کنید." ,
                            list_part=[" \includegraphics[scale = 0.18]{تقسیم5}","\includegraphics[scale = 0.18]{تقسیم8}",],chand=4 , barom= 2 , khat=3)
first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید.", list_part=["$\\dfrac{2}{3}+\\dfrac{2}{7} = $","$-\\dfrac{4}{3}+\\dfrac{1}{9} = $","$4.2-5.1 = $","$6.2 - 5.7 = $" ],ltr=True , barom= 4)
first_text = add_multiparts(first_text , "حاصل ضرب و تقسیم‌های زیر را محاسبه کنید.", list_part=["$+\\dfrac{4}{4}\\times\\dfrac{1}{8} = $","$\\dfrac{7}{2}\\times\\dfrac{6}{5} = $"],ltr=True , barom= 2)

first_text = add_multiparts(first_text,"شمارنده‌های اعداد زیر را بدست آورید." , list_part=["$24$","$10$","$4$"] , chand=2 , barom=3)
first_text = add_multiparts(first_text, "ک.م.م. اعداد زیر را بدست آورید." , list_part=["$12 , 6$","$12 , 6$"] , chand=2 , barom= 2)
first_text = add_multiparts(first_text, "ب.م.م. اعداد زیر را بدست آورید." , list_part=["$45 , 15$","$27 , 36$" ], chand= 2 , barom= 2)

first_text = add_question(first_text , "مجموع اعداد زیر را محاسبه کنید. \\\\1+2+3+...+54+55+56 = ",barom=1.5)
first_text = add_question(first_text ,"محیط و مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 1]{مستطیل}", barom=1.5)



first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت اول کلاس هشتم رحمت آباد2"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)