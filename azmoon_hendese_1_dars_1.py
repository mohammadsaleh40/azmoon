from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="40 دقیقه" , examdate= "08/08/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_question(first_text , "خط $l$ و نقطه $A$ خارج از خط $l$ مفروض است. چند خط از این نقطه می‌گذرد که بر خط $l$ عمود است؟" ,khat=1 , barom = 0.5)
first_text = add_question(first_text , "روش رسم خطی موازی به فاصله ۳ واحد از خطی دیگر به کمک پرگار و خط کش را توضیح دهید." , barom=1.5 , khat= 4)
first_text = add_question(first_text , "فرض کنید که برای لوزی بودن یک چهارضلعی کافی است که قطرهای آن چهارضلعی عمود منصف یک دیگر باشند. لوزی رسم کنید که طول ضلع آن 10 و ارتفاع بزرگ آن دو برابر ارتفاع کوچک آن باشد.(روش رسم با خط کش و پرگار توضیح داده شود.)" , barom= 2 , khat= 6)
first_text = add_question(first_text , "اثبات کنید عمود منصف‌های مثلث همرس اند.", khat= 4 , barom=2)
first_text = add_question(first_text , "روش پیدا کردن مرکز یک دایره که فقط یک کمان از آن در دسترس است را توضیح دهید. (خط کش و پرگار تنها ابزار در دسترس است)" , khat= 4 , barom=2)
first_text = add_section(first_text , "سؤال با نمره اضافه")
first_text = add_question(first_text , "در مثلث $ABC$ عمود منصف ضلع $AB$ و $AC$ را رسم کرده‌ایم. حول نقطه $B$ دایره‌ای رسم کرده‌ایم و این دایره با شعاع $2.5$ واحد محل تقاطع دو عمود منصف رسم شده را بر روی ضلع $AB$ قطع کرده است و ضلع $BC$ را نیز در فاصله $1.5$ واحد از رأس $C$ قطع کرده است. مساحت مثلث $ABC$ را بدست آورید." , barom= "+4" , khat= 5)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان درس اول هندسه ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)