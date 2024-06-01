from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۸۰ دقیقه" , examdate= "۱۳/۰۳/۱۴۰۳" , teacher= "محمد صالح علی اکبری" , city= "رحمت آباد", schooltitle="متوسطه دوره اول", branch= "", school="مقداد" ,grade= "هفتم")

first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را بدست آورید: ", list_part=["$12 + 15 =$" , "$14 \\times 2 = $" , "$8 \div 2 = $" , "$14 - 8 = $", "$17 - 8 = $" , "$22.5 \div 5 = $" ] , ltr=True, chand=2 , barom=1.5)
first_text = add_multiparts(first_text, "حاصل عبارت‌های زیر را با رعایت اولویت‌های محاسباتی انجام دهید." , list_part=["$14 \div 2 \\times 3 =$" ,"$5 + 2 \\times 3 =$" ,"$12 \\times 2 \div 3 = $" ,"$12 \div 3 - 2 = $"], ltr=True , chand=2 , barom=1)
first_text = add_multiparts(first_text, "حاصل تقسیم‌های زیر را به صورت اعشاری بنویسید." , list_part=["$72 \div 30 = $" , "$15 \div 10 =$"] , ltr= True , barom= 0.5)
first_text = add_question(first_text, "مساحت مثلث زیر را محاسبه کنید. \\\\\includegraphics[scale = 0.7]{triangle-area-ex2-1}" , barom= 1.5)
first_text = add_question(first_text, "در مثلث $ABC$ ضلع‌های $BC = 8$ و $AC = 10$ و ارتفاع‌ $AH = 6$ است. طول ارتفاع $BG$ را بدست آورید. \\\\\includegraphics[scale = 0.7]{mosalas_2gh_2h}" , barom= 2)
first_text = add_multiparts(first_text , "معادله‌های زیر را حل کنید.", list_part=["$4x + 2 = x + 12$" , "$2x + 3 = x + 5$" , "$3x + 2 = x + 5$" , "$2x + 3 = 4x + 1$" , "$3x + 2 = x - 4$" , "$5x - 3 = 12x + 2$"] , chand= 2 , khat_beyn= 3 , khat=5 , barom= 6)
first_text = add_multiparts(first_text , "عبارت‌های زیر را محاسبه کنید." , list_part=["$\sqrt{4}$" , "$\sqrt{16}$" , "$\sqrt{81}$" , "$\sqrt{(-2)^2}$", "$\sqrt{36}$" ], barom= 2.5, chand=3  , ltr=True)
first_text = add_multiparts(first_text , "ریشه دوم عددهای زیر را محاسبه کنید." ,list_part=["$100$" , "$25$" , "$9$" , "$49$" ] , chand= 2 , barom= 2 , khat=1 ,khat_beyn=1)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را بدست آورید." , list_part=["$2^3 - 2^2 = $", "$4^2 \div 2^2 = $", "$2^4 - 3^3 + 1^5 = $"], barom = 3, ltr=True , chand=2  , khat= 1)
first_text = add_section(first_text , "یک سؤال ارفاقی")
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را محاسبه کنید." , list_part=["$(\dfrac{5}{2})^2-(\dfrac{2}{5})^2$" , "$\sqrt{22 + \sqrt{9}} = $"] , chand= 2 , barom= 2 , ltr= True)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت دوم ریاضی کلاس هفتم رحمت آباد"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)