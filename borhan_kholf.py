from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="60 دقیقه" , examdate= "۱۴۰۲/۱۰/۰۴", teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_question(first_text , "فرض کنید که برای لوزی بودن یک چهارضلعی کافی است که قطرهای آن چهارضلعی عمود منصف یک دیگر باشند. لوزی رسم کنید که طول ضلع آن 10 و قطر بزرگ آن دو برابر قطر کوچک آن باشد.(روش رسم با خط کش و پرگار توضیح داده شود.)" , barom=2)
first_text = add_multiparts(first_text ,"نقیض گزاره زیر را بنویسید.",list_part=["عدد $\\sqrt{2}$ گنگ است."] , barom=0.5)
first_text = add_multiparts(first_text, "برای هر یک از گزاره‌های زیر مثال نقضی ارائه کنید." , list_part=["تمام اعضای مجموعه $\{2k +1|k \\in \mathbf{Z} \}$ زوج هستند." , "عمود منصف‌های هر دو وتر از یک دایره فقط در مرکز دایره هم دیگر را قطع می‌کنند."] , barom= 1)

first_text = add_question(first_text , "اثبات کنید $\\sqrt{2}$ گنگ است. (راهنمایی از برهان خلف استفاده کنید.) \\\\" , barom=1.5)
first_text = add_question(first_text ,"در شکل زیر اثبات کنید نسبت مساحت مثلث ACD به ABC برابر $\\dfrac{3}{2}$. (خط d با پاره خط BC موازی است. $\\dfrac{AD}{BC}=\\dfrac{3}{2}$) \\\\ \\includegraphics[scale = 0.31]{Screenshot from 2023-12-25 06-17-21}" , barom=2)
first_text = add_question(first_text ,"صورت قضیه تالس را بنویسید و اثبات کنید. \\\\", barom= 2)
first_text = add_question(first_text , "اگر خطی دو ضلع مثلثی را در دو نقطه قطع کند و با ضلع سوم آن موازی باشد، مثلثی پدید می‌آید که اندازه ضلع‌های آن با اندازه ضلع‌های ملث اصلی متناسب اندک مثلا در شکل زیر داریم:\\\\$\\dfrac{AD}{AB}=\\dfrac{AE}{AC}=\\dfrac{DE}{BC}$\\\\\includegraphics[scale = 1]{Screenshot from 2023-12-25 06-07-15} \\\\در شکل مقابل، $MNQB$ متوازی‌الضلاع است. اگر مساحت مثلث $PNM$، $60$ درصد مساحت مثلث $AMN$ باشد، نسبت $QC$ به $MN$ را محاسبه کنید. \\\\\includegraphics[scale = 0.8]{تالس خاص}" , barom=2)



first_text = add_enteha(first_text)
esm_emtehan = "امتحان هندسه مرور مباحث"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)