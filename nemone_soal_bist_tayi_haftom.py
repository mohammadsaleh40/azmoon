from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="120 دقیقه" , examdate= "مهر 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "-", school="شاهد خاکپور" ,grade= "هفتم")






first_text = add_fourchoice(first_text , "حاصل عبارت $6x - 2y +1$ به ازای $x = 3a$ ، $y = -\\frac{1}{4}a$ بر حسب $a$ کدام است؟"  ,
                            ["$\\frac{37}{2}a+1$"  , "$\\frac{19}{2}a+1$" , "$\\frac{37}{4}a-1$" , "$\\frac{19}{4}a+1$"]  , chand = 4)
first_text = add_fourchoice(first_text , "حاصل عبارت $\\frac{3(a-b)-2(a+b)}{-\\frac{1}{2}(-2+10b)}$ کدام است؟" ,
list_choice=["$-1$" , "$1$" , "$\\frac{1}{2}$" , "$2$"] , chand=4)
first_text = add_fourchoice(first_text , "سن پدری پنج برابر سن پسرش است. هشت سال بعد سن پدر سه برابر سن پسر خواهد شد. سن فعلی پسر کدام است؟" ,
list_choice=["$6$","$8$","$10$","$12$"] , chand= 4 )
first_text = add_fourchoice(first_text , "مقدار a در تساوی $((a-3)^{2})^{a-1}=1$ کدام است؟" ,
list_choice=["$2$ و $4$","$1$ و $4$","$1$ و $2$ و $4$","$1$ و $3$ و $4$"] , chand= 4 )
first_text = add_fourchoice(first_text , "اگر $3^a = 10$ باشد مقدار $(\\frac{1}{9})^{s-1}$ برابر است با:" ,
list_choice=["$0.27$","$0.09$","$0.81$","$0.03$"] , chand= 4)
first_text = add_fourchoice(first_text , "حاصل $\\frac{(0.04)^{-3}\\times(0.5)^{-6}}{4^{-3}\\times(0.5)^6}$ با کدام یک از گزینه‌های زیر برابر است؟" ,
list_choice=["$50^6$","$100^6$","$100^3$","$50^9$"] , chand= 4)
first_text = add_fourchoice(first_text , "اگر میانگین اعداد $x_1 , x_2 , x_3 , ... , x_n$ برابر $y$ باشد میانگین اعداد $3x_n +n , ... , 3x_2 + 2 , 3x_1 + 1$ کدام است؟" ,
list_choice=["$3y+\\frac{n}{2}$","$3y+\\frac{n(n+1)}{2}$","$3y+\\frac{n+1}{2}$","$3y+n$"] , chand= 4)
first_text = add_fourchoice(first_text , "تعدادی باکتری در ظرفی شیشه‌ای گذاشته شدهاند. یک ثانیه بعد هر باکتری به دو تا تقسیم می‌شود، یک ثانیه بعد از آن هر یک از باکتری‌های حاصل هم به دو باکتری تقسیم می‌شود و همین طور تا آخر. بعد از یک دقیقه ظرف پر می‌شود. چه وقت نصف ظرف پر شده است؟", 
list_choice=["01:1" , "59:0" , "30:1" , "30:0"] , chand=4)



first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال هشت تایی هفتم و خلاقیت ریاضی"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)