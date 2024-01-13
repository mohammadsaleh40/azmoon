from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۹۰ دقیقه" , examdate= "دی ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "۱", school="مقداد" ,grade= "هفتم")

first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید. (علامت + یا - جواب اهمیت دارد.)",
                            list_part=[ "$1 - 4 = $" ,"$3 - 7 = $" ,"$7 - 4 = $" ,"$17 - 14 = $" ,"$8 - 12 = $" ] ,chand=4 ,ltr=True , barom= 2.5)
first_text = add_question(first_text , "میانگین بارش شهر گیسور و رحمت آباد در آذر ماه به ترتیب ۵ و ۷ میلی متر بوده است. میانگین بارش این دو شهر را محاسبه کنید. \\\\" , barom= 0.5)

first_text = add_multiparts(first_text , "حاصل جمع و تفریق‌های زیر را محاسبه کنید. (علامت + یا - جواب اهمیت دارد.)",
                            list_part=["$-223 - 57 = $" ,"$-167 - 24 = $" ,"$-147 - 67 = $" ,"$-324 - 41 = $" ]  , chand= 3 , khat_beyn= 2 , khat= 1 , ltr=True , barom= 4)

first_text = add_multiparts(first_text , "حاصل تقسیم‌های زیر را محاسبه کنید." ,
                            list_part=[" \includegraphics[scale = 0.18]{تقسیم1}","\includegraphics[scale = 0.18]{تقسیم4}","\includegraphics[scale = 0.18]{تقسیم5}","\includegraphics[scale = 0.18]{تقسیم8}",],chand=4 , barom= 4 , khat=3)
first_text = add_multiparts(first_text , "در $\\bigcirc$ عدد علامت دار مناسب قرار دهید." , list_part=["$-4 + \\bigcirc = 5$" , 
                                                                                                      "$-44 + \\bigcirc = 75$" , 
                                                                                                      "$14 + \\bigcirc = 12$" , 
                                                                                                      "$412 + \\bigcirc = 145$" , 
                                                                                                      "$+4 + \\bigcirc = -1$" , 
                                                                                                      "$+24 + \\bigcirc = -5$" , 
                                                                                                      "$10 + \\bigcirc = 8$" , 
                                                                                                      "$35 + \\bigcirc = 17$" , ], chand = 2 , barom = 4 )
first_text = add_question(first_text , "مساحت شکل زیر را محاسبه کنید. \\\\ \includegraphics[scale = 0.78]{دایره با شعاع ۶} " , barom=1)

first_text = add_multiparts(first_text, "۲ جمله بعدی دنباله‌های زیر را بنویسید و در انتها جمله nام آن را بنویسید. مانند نمونه." ,
                            list_part=["$1 , 3 , 5 , 7 , 9 , 11 , 2n-1 $",
                                       "$4 , 7 , 10 , .... , .... , .... , ....$",
                                       "$3 , 5 , 7 , .... , .... , .... , ....$",
                                       "$8 , 12 , 16 , .... , .... , .... , ....$",
                                       ]
                                       , barom= 4 , ltr=True)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت اول کلاس هفتم رحمت آباد"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)