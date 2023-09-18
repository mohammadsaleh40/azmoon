from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="120 دقیقه" , examdate= "شهریور 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شاهد امام (ره)" ,grade= "هشتم")




first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال مرور ریاضی هشتم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)