from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۸۰ دقیقه" , examdate= "۱۳/۰۳/۱۴۰۳" , teacher= "محمد صالح علی اکبری" , city= "رحمت آباد", schooltitle="متوسطه دوره اول", branch= "", school="مقداد" ,grade= "هشتم")

first_text = add_multiparts(first_text , "حاصل تقسیم‌های زیر را تا ۲ رقم اعشار محاسبه کنید." , list_part=["$\dfrac{25}{2} = $", "$\dfrac{14}{28} = $" , "$\dfrac{18}{6} = $"] , ltr=True , chand= 3 , barom= 1.5 , khat= 1)
first_text = add_question(first_text , "مقدار $x$ و $y$ را با توجه به خطوط و زوایای زیر بدست آورید. \\\\ \includegraphics[scale = 0.5]{دو خط موازی} \\\\ \includegraphics[scale = 0.5]{زاویه بین دو خط موازی}" , barom=2)
first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید." , list_part=["$\dfrac{3}{5}+\dfrac{7}{5} = $","$\dfrac{1}{5}-\dfrac{4}{5} = $","$\dfrac{2}{5}-\dfrac{2}{3} = $","$\dfrac{2}{7}+\dfrac{4}{6} = $"] , chand= 1 , barom=3 , khat=1 , khat_beyn=1 , ltr= True)
first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را محاسبه کنید.", list_part=["$\sqrt{16} =$" , "$\sqrt{36} =$" ], ltr=True , chand= 2 , barom= 1)
first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را محاسبه کنید.", list_part=["$3^3 =$" , "$2^4 =$" ], ltr=True , chand= 2 , barom= 1)
first_text = add_multiparts(first_text, "معادله‌های زیر را محاسبه کنید." , list_part=["$4x + 3 = 2x + 5$" , "$2x + 3 = 3x + 1$" ,"$22x + 5 = 13x - 4$","$12x + 15 = 3x - 14$"] , ltr=True , khat=2 , khat_beyn=2, chand=2 , barom=3)
first_text = add_multiparts(first_text, "معادله‌های زیر را محاسبه کنید." ,list_part=["$-\dfrac{3}{8}x+5=\dfrac{1}{6} $" , "$\dfrac{5}{12}x - \dfrac{7}{18} = 2$" , "$\dfrac{1}{2}-\dfrac{2x-1}{4} = \\dfrac{3}{4}$", "$4x + \dfrac{2}{7} = \dfrac{3}{2}x$"], chand=2,khat= 4 , khat_beyn=4 , ltr=True , barom=4)
first_text = add_multiparts(first_text , "کوچک ترین مضرب مشترک جفت اعداد زیر را محاسبه کنید." , list_part=["$[12 , 8] = $" , "$[6 , 4] = $"] , ltr=True , barom= 1 , chand= 2)
first_text = add_multiparts(first_text , "بزرگ ترین مقسوم علیه مشترک جفت اعداد زیر را محاسبه کنید." , list_part=["$(12 , 8) = $" , "$(16 , 4) = $"] , ltr=True , barom= 1 , chand= 2)
first_text = add_question(first_text , "یک 7 ضعلی مجموع زوایای داخلی اش چقدر است؟" ,khat=2 ,barom=1)
first_text = add_question(first_text , "اندازه زاویه داخلی یک ۵ ضلعی منتظم چقدر است؟" , khat= 3 , barom=1.5)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت دوم ریاضی کلاس هشتم رحمت آباد"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)