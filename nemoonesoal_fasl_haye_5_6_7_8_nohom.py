from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="120 دقیقه" , examdate= "شهریور 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شاهد امام (ره)" ,grade= "نهم")
first_text = add_question(first_text , "متناظر با هر یک از ناحیه‌های مشخص شده روی محور، یک نابرابری بنویسید. \\\\ \includegraphics[scale = 0.3]{baze_mehvar_nohom}")
first_text = add_multiparts(first_text , "مجموعه جواب نامعادله‌های زیر را به دست آورید." , list_part=["$2(x-3)+5<5-x$"  , "$3-2x \geq 5(3-2x)$" , "$\dfrac{y-3}{4}-1>\dfrac{y}{2}$" , "$-2-\dfrac{q}{4} \leq \dfrac{1+q}{3}$"] , ltr=True , khat = 1 ,  khat_beyn = 1)
first_text = add_question(first_text , "۵ جواب برای دستگاه معادله خطی زیر بنویسید. \\\\ \includegraphics[scale = 0.3]{moadelekhat}" )
first_text = add_multiparts(first_text , "معادلات خط زیر را رسم کنید." , list_part = ["$y = \dfrac{1}{2}x + 4$" , "$2y = 3 x + 7$" , "$4x + 3 y = 0$" , "$4x + 3y  - 3 = 0$"] , khat_beyn= 2 , khat= 2)
first_text = add_multiparts(first_text , "دستگاه معادلات زیر را حل کنید." , list_part=["$x + y = 5 $ \\\\  $2 x + y = 8$" , "$4 x + y = 4$ \\\\ $2x + 2 y = 3.5$" , "$3x + 3 y + z = 11 \\\\ 2 z + 2 x = 12 \\\\ 4 y + z = 5 + \dfrac{1}{3}$"] , ltr=True , khat_beyn= 2 , khat= 2)
first_text = add_question(first_text , "دستگاه معادلات زیر را به روش رسمی حل کنید. \\\\ $y = x + 1$ \\\\ $y = -x + 3$" , khat= 3)


first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال مرور فصل‌های ۵، ۶، ۷، ۸ ریاضی نهم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)