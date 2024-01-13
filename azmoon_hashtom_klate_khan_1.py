from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۹۰ دقیقه" , examdate= "دی ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "۱", school="مقداد" ,grade= "هشتم")

first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$ 72 - 60 + 100 = $","$60 - 70 + 40 =$"],chand=2 , barom= 1, ltr=True)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$-6 \\times (-2) = $","$-4 \\times (5) = $"],chand=2 , barom= 1, ltr=True)


first_text = add_multiparts(first_text , "حاصل تقسیم‌های زیر را محاسبه کنید." ,
                            list_part=[" \includegraphics[scale = 0.18]{تقسیم6}","\includegraphics[scale = 0.18]{تقسیم4}",],chand=4 , barom= 2 , khat=3)
first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید.", list_part=["$\\dfrac{4}{9}-(-\\dfrac{7}{2}) = $","$-\\dfrac{8}{4}+\\dfrac{2}{1} = $","$5.7 + 4.5 = $" , "$4.2 + 2.5 =$"],ltr=True , barom= 4)
first_text = add_multiparts(first_text , "حاصل ضرب و تقسیم‌های زیر را محاسبه کنید.", list_part=["$\\dfrac{9}{2}\\div\\dfrac{4}{9} = $","$\\dfrac{4}{3}\\div\\dfrac{3}{4} = $",],ltr=True , barom= 2)

first_text = add_multiparts(first_text,"شمارنده‌های اعداد زیر را بدست آورید." , list_part=["$24$","$10$","$4$"] , chand=2 , barom=3)
first_text = add_multiparts(first_text, "ک.م.م. اعداد زیر را بدست آورید." , list_part=["$12 , 3$","$21 , 14$" ] , chand=2 , barom= 2)
first_text = add_multiparts(first_text, "ب.م.م. اعداد زیر را بدست آورید." , list_part=["$24 , 18$","$20 , 10$"], chand= 2 , barom= 2)
first_text = add_question(first_text , "مجموع اعداد زیر را محاسبه کنید. \\\\1+2+3+...+50+51+52 = ", barom=1.5)

first_text = add_question(first_text ,"محیط و مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 1]{مستطیل}", barom=1.5)



first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت اول کلاس هشتم رحمت آباد1"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)