from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="40 دقیقه" , examdate= "08/08/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۷۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_multiparts(first_text , "معادلات درجه ۱ زیر را حل کنید." ,
list_part=["$3x +2 = 2x + 4.5$",
"$8x + 5 = 2x + 23$",
"$7x + 4 = 18$"] , khat_beyn= 3 , khat=3 , chand= 2 , barom= 3)
first_text = add_question(first_text , "عرض مستطیلی ۷ و محیط آن ۳۴ است. طول این مستطیل چند است؟", barom= 2 , khat= 2)
first_text = add_multiparts(first_text , "معادلات درجه ۲ زیر را حل کنید." ,list_part=[
    "$x^2 = 16$",
    "$(x-1)^2 = 20$",
    "$(x-3)^2 = 4$",
    "$(x-3)(x-4)=0$",
    "$(x-6)^2=0$",
    "$3x^2 + 6x -18 = 0$"
], ltr= True, khat_beyn= 3 , chand=2, khat= 2, barom= 6)
first_text = add_question(first_text,"منحنی $y=3x^2 -8x -18$ و منحنی $z= -x^2 +2x +14$ را رسم می‌کنیم. در دو نقطه هم دیگر را قطع کرده‌اند. طول این دو محل تقاطع چند است؟" , khat=4 , barom=3)




first_text = add_enteha(first_text)
esm_emtehan = "امتحان معادلات درجه ۱ و ۲"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)