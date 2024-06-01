from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="70 دقیقه" , examdate= "17/11/1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "۱۷۱", school="شاهد امام (ره)" ,grade= "دهم")

first_text = add_question(first_text , "جدول زیر نمایش‌های یک رابطه مشخص شده‌اند. جاهای خالی را پر کنید. \\\\ \\includegraphics[scale = 1]{Screenshot 2024-02-05 220237}",barom = 3)
first_text = add_question(first_text , "اگر رابطه f تابع باشد، در این صورت حاصل $x^2+y^2$ را بدست آورید. \\\\ $f = {(2,x+y), (2,4), (5,2), (3,4) , (5,x-y)}$" , barom=1.5 , khat=2)
first_text = add_multiparts(first_text , "دامنه و برد هر یک از توابع زیر را مشخص کنید." , list_part=["$\\includegraphics[scale = 0.2]{نمودار_معادله}$" , "$\\includegraphics[scale = 0.2]{نمودار_معادله_خطی}$"] , ltr=False , barom=2)
first_text = add_multiparts(first_text , "برد هر یک از توابع زیر را با توجه به ضابطه و دامنه داده شده بدست آورید." , list_part=["$\\includegraphics[scale = 0.35]{Screenshot_2024-02-04-20-41-05-400_com.yygg.note.app}$" , "$\\includegraphics[scale = 0.35]{Screenshot_2024-02-04-20-40-53-370_com.yygg.note.app}$"], khat=2 , barom=1)
first_text = add_multiparts(first_text , "یک شرکت برای تولید x کالا ، $C(x) = 3000+50x$ تومان هزینه می‌کند و هر کالا را $70$ تومان می‌فروشد." , list_part=["تابع سود را تعیین و نمودار آن را رسم کنید." , "این شرکت حداقل چه تعداد از این کالا را باید بفروشد تا سوددهی آغاز شود؟"] , barom=1.5)
first_text = add_question(first_text , "نمودار یک تابع خطی از مبدأ می‌گذرد و $f(2) = 7$ است. در این صورت اختلاف $f(0.1)$ و $f(-0.1)$ را بدست آورید.",khat=2,barom=1)
first_text = add_question(first_text , "ضابطه تابع خطی f را که از نقاط $(2 , 3)$ و $(4,1)$ می‌گذرد، مشخص کنید و نمودار آن را رسم نمایید." , barom=1,khat=2)
first_text = add_question(first_text ,  "معادله خطی که با شیب $1$ که از نقاط $(1,a)$ و $(a,3)$ بگذرد، به چه صورت است؟" , barom=1,khat=2)


first_text = add_enteha(first_text)
esm_emtehan = "ریاضی و آمار تابع"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)