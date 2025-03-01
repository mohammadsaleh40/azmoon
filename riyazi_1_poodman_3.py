from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۵۰ دقیقه" , examdate= "۱۲/۱۲/۱۴۰۳" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "101", school="شهید دکتر چمران" ,grade= "دهم")

first_text = add_fourchoice(first_text, text="کدام یک نمودار معادله خط $y = 3x-2$ را نشان می‌دهد؟",
                            list_choice=[
                                "\includegraphics[scale = 0.4]{y__=__0.5x__+__3}",
                                "\includegraphics[scale = 0.4]{y__=__2x__+__3}",
                                "\includegraphics[scale = 0.4]{y__=__3x__+___-_2}",
                                "\includegraphics[scale = 0.4]{y__=___-_3x__-__4}"
                            ],
                            chand=2,barom=0.5)

first_text = add_fourchoice(first_text, text= """این نمودار مربوط به چه معادله خطی است؟
                            \\\\ \includegraphics[scale = 0.4]{y__=___-_3x__+__5}""",
                            list_choice=["$y = 5x + 3$",
                                         "$y = -3x + 5$",
                                         "$y = -3x - 5$",
                                         "$y = 3x + 5$"], chand= 4, barom= 0.5)

first_text = add_fourchoice(first_text, text="با قرار دادن کدام یک از گزینه‌های زیر به جای $x$ معادله $3x -7 = \dfrac{5x - 8}{2}$ برقرار می‌شود؟",
                            list_choice=[
                                "$4$",
                                "$6$",
                                "$8$",
                                "$12$"
                            ],
                            barom= 0.5, chand= 4)

first_text = add_fourchoice(first_text, text="با قرار دادن کدام یک از گزینه‌های زیر به جای $x$ معادله $x^2 - 10x + 24 = 0$ برقرار می‌شود؟",
                            list_choice=[
                                "$4$ و $6$",
                                "$6$ و $12$",
                                "$3$ و $4$",
                                "$8$"
                            ],
                            barom= 0.5, chand= 4)

first_text = add_fourchoice(first_text, 
    text="با قرار دادن کدام یک از گزینه‌های زیر به جای $x$ معادله $x^2 - 8x + 15 = 0$ برقرار می‌شود؟",
    list_choice=[
        "$2$ و $6$",
        "$4$ و $4$",
        "$3$ و $5$",
        "$8$"
    ],
    barom=0.5, 
    chand=4
)
first_text = add_fourchoice(first_text, 
    text="با قرار دادن کدام یک از گزینه‌های زیر به جای $x$ معادله $x^2 - 5x + 6 = 0$ برقرار می‌شود؟",
    list_choice=[
        "$1$ و $6$",
        "$4$ و $5$",
        "$2$ و $3$",
        "$5$"
    ],
    barom=0.5, 
    chand=4
)
first_text = add_fourchoice(first_text, 
    text="با قرار دادن کدام یک از گزینه‌های زیر به جای $x$ معادله $x^2 - 7x + 12 = 0$ برقرار می‌شود؟",
    list_choice=[
        "$3$ و $4$",
        "$4$ و $5$",
        "$2$ و $6$",
        "$7$"
    ],
    barom=0.5, 
    chand=4
)

first_text = add_fourchoice(first_text, text="کدام تصویر مربوط به حل معادله به روش هندسی معادل $3x^2 + x - 6 = 0$ است؟",
                            list_choice=[
                                "\includegraphics[scale = 0.35]{y__=___-_0.5x_+_2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=__1x_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___-_0.3333x__+__2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___+_0.3333x__+__2_and_y__=__x_power_2}"
                            ],
                            chand= 2, barom= 0.5)

first_text = add_fourchoice(first_text, text="کدام تصویر مربوط به حل معادله به روش هندسی معادل $4x^2 + x + 7 = -1$ است؟",
                            list_choice=[
                                "\includegraphics[scale = 0.35]{y__=___+_0.25x__+__2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___+_0.25x__+___-_2_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___-_0.5x_+_3_and_y__=__x_power_2}",
                                "\includegraphics[scale = 0.35]{y__=___-_2x_and_y__=__x_power_2}"
                            ],
                            chand= 2, barom= 0.5)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان پودمان ۳ درس ریاضی ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)