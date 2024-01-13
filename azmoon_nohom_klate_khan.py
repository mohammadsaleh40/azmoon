from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۹۰ دقیقه" , examdate= "دی ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "۱", school="مقداد" ,grade= "نهم")

first_text = add_multiparts(first_text , "هر یک از مجموعه‌های زیر چند عضو دارند؟", ["\{۴ ، ۶، ۸\}","\{۴ ،۴ ،۲ ، ۳\}","\{۴ ، ۵، ۸\}","$\{\\dfrac{4}{2} , \dfrac{6}{3}, 2\}$"], chand=2 , barom=2)
first_text = add_multiparts(first_text , "مجموعه $S=\{1,2,3,4,5,6,7,8\}$ به این صورت است. برای هر یک از زیر مجموعه‌های این مجموعه که در زیر آمده مانند نمونه یک جمله نظیر کنید." , list_part=["$A=\{8 , 7\}$ مجموعه تمام اعداد عضو S که در تاس وجود ندارند.","$B=\{2 , 3 , 5 , 7 \}$","$C=\{6, 3\}$","$D=\{2, 4, 6, 8\}$","$E=\{1 ,2 ,3 ,4 ,5 ,6\}$",], chand=2 , barom=4)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$ 42 - 60 + 100 = $","$20 - 70 + 10 =$","$ 200 - 100 + 30 = $","$5 -100 + 30 + 70 = $"],chand=2 , barom= 2, ltr=True)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید.", list_part=["$-5 \\times (-3) = $","$-7 \\times (3) = $","$3 \\times (8)  = $","$3 \\times (-4) = $"],chand=2 , barom= 2, ltr=True)


first_text = add_multiparts(first_text , "حاصل تقسیم‌های زیر را محاسبه کنید." ,
                            list_part=[" \includegraphics[scale = 0.18]{تقسیم2}","\includegraphics[scale = 0.18]{تقسیم3}","\includegraphics[scale = 0.18]{تقسیم9}","\includegraphics[scale = 0.18]{تقسیم10}",],chand=4 , barom= 4 , khat=3)
first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید.", list_part=["$\\dfrac{4}{3}-(-\\dfrac{4}{8}) = $","$\\dfrac{1}{2}-\\dfrac{3}{1} = $","$-\\dfrac{8}{4}+\\dfrac{2}{1} = $","$\\dfrac{2}{3}+\\dfrac{2}{7} = $","$-\\dfrac{4}{3}+\\dfrac{1}{9} = $",],ltr=True , barom= 5)
first_text = add_multiparts(first_text , "حاصل ضرب و تقسیم‌های زیر را محاسبه کنید.", list_part=["$+\\dfrac{4}{3}*\\dfrac{1}{8} = $","$\\dfrac{1}{2}*\\dfrac{3}{2} = $","$\\dfrac{8}{4}/\\dfrac{1}{7} = $","$\\dfrac{2}{3}/\\dfrac{4}{7} = $","$\\dfrac{2}{3}/\\dfrac{7}{9} = $",],ltr=True , barom= 5)
first_text = add_multiparts(first_text , "حاصل عبارت‌های زیر را حساب کنید. \\\\ $\\sqrt{2} \\simeq 1.2 \\sqrt{3} \\simeq 1.7 \\sqrt{5} \\simeq 2.2  \\sqrt{6} \\simeq 2.4 \\sqrt{7} \\simeq 2.6 \\sqrt{8} \\simeq 2.8$" , list_part=["$|\\sqrt{2}-4| = $" , "$|\\sqrt{12}-3| = $" , "$|\\sqrt{7}-5| = $" , "$|\\sqrt{4}-2| = $" , "$|-3-2\\sqrt{7}| = $" , "$|1-\\sqrt{2}| = $" , "$|\\sqrt{7} -\\sqrt{2}| = $" , "$|\\sqrt{4} -\\sqrt{5}| = $" ] ,barom=8, ltr= True)
first_text = add_question(first_text , "اگر امروز ۲۳ دی باشد و اسفندماه ۲۹ روزه باشد. تا عید (اول فروردین) چند روز باقی مانده است؟" , barom=2)
first_text = add_question(first_text , "اگر امروز ۱۳ دی باشد و اسفندماه ۱۹ ۲۹ روزه باشد. چند روز تا ۱۵ مهر باقی مانده است؟" , barom=2)
first_text = add_question(first_text ,"محیط و مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 1]{دایره}", barom=2)
first_text = add_question(first_text ,"محیط و مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 1]{متوازی الاضلاع}" , barom= 2)
first_text = add_question(first_text ,"محیط و مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 1]{مستطیل}", barom=2)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت اول کلاس نهم رحمت آباد"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)