from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="80 دقیقه" , examdate= "07/09/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_question(first_text , "خط $l$ و نقطه $A$ خارج از خط $l$ مفروض است. چند خط از این نقطه می‌گذرد که بر خط $l$ عمود است؟"  , barom = 0.5)
first_text = add_multiparts(first_text , "عکس هر یک از گزاره‌های زیر را بنویسید.", list_part=["عدد $2$ فرد است." ,"مجموع زوایای یک مثلث $180$ درجه است."], barom = 1)
first_text = add_question(first_text , "روش رسم خطی موازی به فاصله ۳ واحد از خطی دیگر به کمک پرگار و خط کش را توضیح دهید." , barom=1.5 )
first_text = add_question(first_text , "فرض کنید که برای لوزی بودن یک چهارضلعی کافی است که قطرهای آن چهارضلعی عمود منصف یک دیگر باشند. لوزی رسم کنید که طول ضلع آن 10 و ارتفاع بزرگ آن دو برابر ارتفاع کوچک آن باشد.(روش رسم با خط کش و پرگار توضیح داده شود.)" , barom= 2)
first_text = add_question(first_text , "اثبات کنید عمود منصف‌های مثلث همرس اند." ,barom=2)
first_text = add_question(first_text , "اثبات کنید نیمسازهای مثلث همرس اند.", barom=2)
first_text = add_question(first_text , "روش پیدا کردن مرکز یک دایره که فقط یک کمان از آن در دسترس است را توضیح دهید. (خط کش و پرگار تنها ابزار در دسترس است)" , barom=2)
first_text = add_question(first_text , "قضیه: اگر در مثلثی دو ضلع نابرابر باشند، زاویه روبه‌رو به ضلع بزرگتر است از زاویه روبه‌رو به ضلع کوچک‌تر. \\\\ \includegraphics[scale = 0.48]{Screenshot from 2023-11-25 20-08-09} \\\\ فرض: $AB<AC$ \\\\ حکم: $\hat{C} < \hat{B}$\\\\الف) قضیه فوق را اثبات کنید.\\\\ب)عکس قضیه فوق را بنویسید.\\\\ج)عکس قضیه فوق را اثبات کنید.", barom=5)
first_text = add_multiparts(first_text , "صحت گزاره‌های زیر را بررسی کنید در صورت اشتباه بودن مثال نقض ارائه کنید.", list_part=["در تمام مثلث‌ها نقطه تقاطع عمود منصف‌ها داخل مثلث است.","در هیچ مثلثی عمودهای مثلث بر اضلاع آن منطبق نمی‌شود.", "میانه ساق‌های مثلث متساوی الساقین‌همیشه هم دیگر را بیرون مثلث قطع می‌کنند.","عمود منصف‌های هر دو وتر از یک دایره فقط در مرکز دایره هم دیگر را قطع می‌کنند."], barom=2 )
first_text = add_question(first_text , "قضیه زیر را به کمک برهان خلف اثبات کنید:\\\\قضیه: از هر نقطه غیر واقع بر یک خط نمی‌توان بیش از $2$ خط بر آن خط عمود رسم کرد.", barom=2)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان فصل اول هندسه ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)