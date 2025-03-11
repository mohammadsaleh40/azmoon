from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۵۰ دقیقه" , examdate= "۲۱/۱۲/۱۴۰۳" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "101", school="هنرستان خوارزمی" ,grade= "دهم")

first_text = add_fourchoice(first_text, text= """قرینه عدد 5 چند است؟""",
                            list_choice=["$5$",
                                         "$-5$",
                                         "$-\dfrac{1}{5}$",
                                         "$\dfrac{1}{5}$"], chand= 4, barom= 1)

first_text = add_fourchoice(first_text, text="حاصل عبارت $\dfrac{4 - \sqrt{36-11}}{2} = $ کدام است؟",
                            list_choice=[
                                "$-3$",
                                "$5$",
                                "$-\dfrac{1}{2}$",
                                "$\dfrac{1}{2}$"
                            ],
                            barom= 1, chand= 4)

first_text = add_fourchoice(first_text, text="حاصل عبارت $\dfrac{6 + 4}{2} = $ کدام است؟",
                            list_choice=[
                                "$5$",
                                "$8$",
                                "$7$",
                                "$10$"
                            ],
                            barom= 1, chand= 4)

first_text = add_fourchoice(first_text, text="نمودار زیر محل تقاطع دو نمودار $y_1 = -2x$ و $y_2 = -x^2$ جواب معادله $-2x = -x^2$ چند است؟ \\\\ \includegraphics[scale = 0.6]{y__=___-_2x_and_y__=___-_1x_power_2}",
                            list_choice=[
                                "$1$",
                                "$-4$",
                                "$3$ و $-1$",
                                "$2$ و $0$"
                            ],
                            chand=4,barom=1)

first_text = add_fourchoice(first_text, text="نمودار زیر محل تقاطع دو نمودار $y_1 = -\dfrac{1}{4}x+2$ و $y_2 = -\dfrac{1}{4}x^2+\dfrac{3}{4}x+4$ جواب معادله $-\dfrac{1}{4}x+2 = -\dfrac{1}{4}x^2+\dfrac{3}{4}x+4$ چند است؟ \includegraphics[scale = 0.4]{y__=___+_0.25x_+_2_and_y__=___-_0.25x_power_2__+_0.75x__+_4}",
                            list_choice=[
                                "$3$",
                                "$-3$",
                                "$4$ و $-2$",
                                "$-4$ و $2$"
                            ],
                            chand=4,barom=1)


first_text = add_fourchoice(first_text, text="برای حل معادله $x^2 + 3x - 4 = 0$ آن را به کدام یک از عبارت‌های زیر می‌توان تبدیل کرد؟ (در حال حل معادله به روش هندسی هستیم)",
                            list_choice=[
                                "$x^2 = +3x + 4$",
                                "$x^2 = +3x - 4$",
                                "$x^2 = -3x + 4$",
                                "$x^2 = -3x - 4$"
                            ],
                            barom= 1, chand= 4)


first_text = add_fourchoice(first_text, text="کدام تصویر مربوط به حل معادله به روش هندسی معادل $3x^2 + x - 6 = 0$ است؟",
                            list_choice=[
                                "\includegraphics[scale = 0.35]{y__=___-_0.5x_+_2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=__1x_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___-_0.3333x__+__2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___+_0.3333x__+__2_and_y__=__x_power_2}"
                            ],
                            chand= 2, barom= 1)

first_text = add_fourchoice(first_text, text="جواب‌های معادله $x^2 - 6 = 0$ در کدام گزینه وجود دارد؟.",
                            list_choice=[
                                "$\\sqrt{6}$ و $\\sqrt{-6}$",
                                "$\\sqrt{6}$ و $-\\sqrt{6}$",
                                "$\\sqrt{-36}$ و $\\sqrt{36}$",
                                "$\\sqrt{0}$ و $\\sqrt{36}$"
                            ], chand=4 , barom= 1)

first_text = add_question(first_text,"معادله $x^2 -2x = 0$ را به کمک روش هندسی حل کنید.", khat=7, barom = 2.5)
# سؤال در مورد جمع دو عدد 20 و ضرب شون 106 این دو عدد چه اعدادی هستند؟
first_text = add_question(first_text, "اگر جمع دو عدد 3 و ضرب آنها -10 باشد، این دو عدد چه اعدادی هستند؟ راهنمایی باید معادله $x^2 -3x -10$ را حل کنید.", khat=6 , barom=3)
first_text = add_question(first_text, text="از معادله $2(x+y)=100$ مقدار x را بر حسب y محاسبه کنید.", barom=1.5, khat=4)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان پودمان ۳ درس ریاضی ۱ مدرسه خوارزمی"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)