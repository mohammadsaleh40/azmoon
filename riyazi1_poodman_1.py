from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۵۰ دقیقه" , examdate= "۰۷/۰۲/۱۴۰۴" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "101", school="شهید دکتر چمران" ,grade= "دهم")

first_text = add_question(first_text=first_text,  text = "$5$ کیلو خیار $35$ هزار تومان به فروش می‌رسد. $7$ کیلو خیار چقدر است؟", khat = 3, barom = 2)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان پودمان 1 درس ریاضی ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)