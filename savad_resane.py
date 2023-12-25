from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="80 دقیقه" , examdate= "آذر ۱۴۰۲" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۵۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_question(first_text , "متن، زیر متن و فرا متن تبلیغ زیر را تشریخ کنید. \\\\\includegraphics[scale = 0.31]{images}" )
first_text = add_question(first_text , "تصاویر زیر مربوط به دو تبلیغ از بستنی شرکت میهن است. با توجه به این که این تبلیغ برای داخل کشور طراحی شده متن، زیر متن و فرامتن آن را تحلیل کنید. \\\\\includegraphics[scale = 0.15]{Unt5747jytkiyksgitled}\includegraphics[scale = 0.3]{بستنی}", khat=2)
first_text = add_question(first_text , "متن زیر متن و فرامتن تبلیغ زیر را بیان کنید. برداشت شما از کشوری که این تبلیغ در آن استفاده شده است چیست؟ \\\\\includegraphics[scale = 0.31]{Screenshot 2023-12-20 010718}" , khat=2)
first_text = add_question(first_text , "با توجه به این که واکنش‌ها به تبلیغ شرکت میهن قابل پیش بینی بوده است هدف اصلی این شرکت برای هزینه برای این تبلیغ چه بوده است؟ نظر خود را بنویسید.", khat=5)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان متن زیر متن فرامتن سواد رسانه‌ای"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)