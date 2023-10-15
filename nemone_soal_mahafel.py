from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="120 دقیقه" , examdate= "مهر 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "-", school="شاهد خاکپور" ,grade= "فرا پایه")






first_text = add_question(first_text , "یک سال، ماه ژانویه درست چهار تا جمعه و چهار تا دوشنبه داشت، بیستم ژانویه آن سال چه روزی از هفته بوده است؟ ماه ژانویه ۳۱ روزه است.")
# Screenshot from 2023-10-16 02-03-48
first_text = add_question(first_text , "شکل زیر را به چهار تا شکل طوری تقسیم کنید که هر یک از آن‌ها مشابه شکل اصلی و ابعادش نصف آن باشد. \\\\ \includegraphics[scale = 0.2]{Screenshot from 2023-10-16 02-03-48}")
# Screenshot from 2023-10-16 02-08-32
first_text = add_question(first_text , "در صفحه‌ای یازده چرخ دنده به شکل زیر در یک زنجیره چیده شده‌اند. آیا ممکن ست که همه این چرخ دنده‌ها با هم بچرخند؟ \\\\ \includegraphics[scale = 0.15]{Screenshot from 2023-10-16 02-08-32}")
first_text = add_question(first_text , "پنج قنجان مختلف و سه نعلبکی متفاوت در فروشگاه «مهمانی عصرانه» وجود دارد. به چند طریق می‌توان یک فنجان و یک نعلبکی خرید؟")
first_text = add_question(first_text , "در فروشگاه «مهمانی عصرانه» چهار قاشق چایخوری مختلف هم وجود دارد. به چند طریق می‌توان یک سرویس چایخوری شامل یک فنجان، یک نعلبکی و یک قاشق خرید؟")
first_text = add_question(first_text , "نقاط K , L, M, و N نقاط وسط اضلاع مستطیل ABCD و نقاط O, P, R و S نقاط وسط لوزی KLMN هستند. نسبت مساحت ناحیه‌های سایه خورده به مساحت مستطیل چند است؟ \\\\ \includegraphics[scale = 0.3]{Screenshot from 2023-10-16 02-15-49} " )


first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال محافل ریاضی"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)