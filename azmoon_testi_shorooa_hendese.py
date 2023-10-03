from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="25 دقیقه" , examdate= "10/07/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شاهد امام (ره)" ,grade= "دهم")
first_text = add_fourchoice(first_text , ' نقطه A به فاصله ۴ واحد از خط d قرار دارد. نقاط M و M\' روی خط d و به فاصلة ۵ از نقطه A قرار دارند. فاصله MM\' کدام است؟' , list_choice=['6' , '3' , '5' , '4'] , chand = 4)
first_text = add_fourchoice(first_text , "دو نقطه A و B به فاصله ۴ از هم قرار دارند. فقط یک نقطه در صفحه وجود دارد که به فاصله ۳ از A و  $و2a-1$ از B قرار دارد. مقدار a کدام است؟" ,
                            ['1','2','3','1 یا 4'] , chand = 4)
first_text = add_fourchoice(first_text , " نقاط A و B به فاصله ۱۳ از هم قرار دارند. نقاطی که به فاصله ۱۲ از A و به فاصله ۵ از B می‌باشند را معلوم کرده و از آن‌ها به A و B وصل می‌کنیم. مجموع مساحت‌های شکل‌های حاصل کدام است؟" ,
                            ['30','120','60','90'] , chand = 4)
first_text = add_fourchoice(first_text , "مرکز همه دایره‌هایی که از دو رأس A و B از مربع ABCD می‌گذرند. چگونه‌اند؟ (سؤال دو گزینه درست دارد)" ,
                            ['روی دایره‌ای به قطر ضلع AB قرار دارند.','روی خطی موازی ضلع AB قرار دارند.','روی عمودمنصف ضلع CD قرار دارند.','روی خطی عمود بر ضلع AB قرار دارند.'] , chand = 2)
first_text = add_fourchoice(first_text , "مربع ABCD به ضلع ۴ مفروض است. مرکز دو دایره از مجموعه دوایری به شعاع ۵ که همگی از رأس A می‌گذرند روی محیط مربع قرار دارد. فاصله مرکزهای این دو دایره کدام است؟" ,
                            ['2','2','$\\sqrt{3}$','$\\sqrt{2}$'], chand = 4)
first_text = add_fourchoice(first_text , "در شکل مقابل، چهارضلعی ABCD مستطیل است و نقاط M ، N و P که روی اضلاع مستطیل و امتداد آن‌ها هستند به فاصله برابر از رأس A قرار دارند. اگر $BM=7$، $MC=8$ و $DP=10$ باشند. طول پاره‌خط NC کدام است؟ \\\\ \includegraphics[scale = 0.08]{photo_2023-10-02_00-39-47}" ,
                            ['4','3.5','3','2'] , chand= 4)
first_text = add_fourchoice(first_text , "روی محیط مستطیلی به ابعاد ۴ و 8، دو نقطه وجود دارد که به فاصله ۵ از یک رأس آن قرار دارند. فاصله این دو نقطه از هم کدام است؟",
                            list_choice=['$2 \sqrt{7}$' , '$3\sqrt{2}$', '4' , '$2\sqrt{5}$'] , chand=4)

first_text = add_fourchoice(first_text , "نقطه M درون مربع ABCD به ضلع ۴ قرار دارد. اگر نقاط A، B و وسط ضلع CD از نقطه M به یک فاصله باشند. فاصله M تا مرکز مربع کدام است؟",
                            list_choice=['$0.5$' , '1', '$1.5$' , '$2.5$'] , chand=4)

first_text = add_fourchoice(first_text , "خط d بر دایره C مماس است. m نقطه روی دایره وجود دارد که از خط d به فاصله معلوم L هستند. m کدام نمی‌تواند باشد؟",
                            list_choice=['صفر' , '1', '2' , '3'] , chand=4)

first_text = add_fourchoice(first_text , "در شکل مقابل AD نیمساز زاویه A است. اگر $BD=4$ و$S_{ABD} +12 = S_{ADC}$ باشند، طول پاره‌خط CD کدام است؟ \\\\ \includegraphics[scale = 0.08]{photo_2023-10-02_00-39-16}",
                            list_choice=['7' , '$5\sqrt{2}$', '$2\sqrt{13}$' , '8'] , chand=4)




first_text = add_enteha(first_text)
esm_emtehan = "امتحان تستی از مکان هندسی و نیمساز"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)