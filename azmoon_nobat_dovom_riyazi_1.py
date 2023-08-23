from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="90 دقیقه" , examdate= "02 شهریور 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شهید رجایی" ,grade= "دهم")



first_text = add_question(first_text , "در یک جمع 40 نفره 17 نفر با علی دوست هستند. همچنین 11 نفر با هیچ یک از علی و رضا دوست نیستند و 5 نفر با هر دو دوست هستند. چند نفر در این جمع فقط با رضا دوست هستند؟" , khat= 3 , barom=1.5)

first_text = add_question(first_text , "اگر $\\tan\\theta$ و $\\sin\\theta$ هم علامت باشند، آنگاه $\\theta$ در کدام ربع مثلثاتی قرار دارد؟\
" , barom= 1 , khat= 3)

first_text = add_question(first_text , "به کمک اتحاد حاصل عبارت زیر را حساب کنید. \\begin {LTR} $999^2 =$ \\\\ \\end{LTR}", barom = 1)

first_text = add_question(first_text , "اگر $\\sqrt{x+2}+\\sqrt{x-4} = 3$، حاصل عبارت $\\sqrt{x+2}-\\sqrt{x-4}$ را بدست آورید.", barom= 1.5 ,khat= 5)

first_text = add_question(first_text , "عبارت رادیکالی زیر را به شکل توان گویا ساده کنید. \\\\ \\begin{LTR} $\\sqrt[4]{16}\\times\\sqrt[2]{9} = $ \\end{LTR}" , barom = 1)

first_text = add_question(first_text , "معادله زیر را حل کنید. \\begin {LTR}$x^2+6x = 2$  \\end{LTR}" , barom= 1.5 , khat= 1)

first_text = add_question(first_text , "نا معادله زیر را حل کنید. \\\\ \\begin{LTR} $|\\dfrac{x-1}{2}-1| \\geq 0$ \\end{LTR}"  , barom = 0.5)
first_text = add_question(first_text , "نا معادله زیر را حل کنید. \\\\ \\begin{LTR} $|\\dfrac{x-1}{2}-1| \\geq 3$ \\end{LTR}" ,khat = 3 , barom = 1)
first_text = add_question(first_text , "نا معادله زیر را حل کنید. \\\\ \\begin{LTR} $x+1 \\leq 5-x < 2x +3$ \\end{LTR}", khat = 4  , barom = 1.5)

first_text = add_question(first_text , "یک تانکر گاز از یک استوانه و دو نیم کره به شعاع r در دو انتهای استوانه، تشکیل شده است. اگر ارتفاع استوانه ۳۰ متر باشد، حجم تانکر را بر حسب تابعی از r بنویسید." , khat= 2 , barom= 1)

first_text = add_multiparts(first_text , "مشخص کنید هر یک از متغیرهای زیر از نوع کدام دسته ترتیبی یا اسمی هستند؟" , list_part = ["مراحل رشد یک انسان (نوزاد، کودک، نونهال، نوجوان، جوان، میان سال، کهن‌سال)", "نژاد افراد (سفید پوست، زرد پوست، سیاه پوست)", "رنگ موی افراد (مشکی، قهوه‌ای، طلایی)" , "کیفیت میوه هلو (درجه 1، درجه 2، درجه3)"] , barom= 1 )

first_text = add_question(first_text , "از بین تعدادی کتاب مختلف می‌خواهیم سه کتاب را انتخاب کنیم و در قفسه‌ای بچینیم. اگر تعداد حالت‌های مختلف برای این کار ۲۱۰ تا باشد، تعداد کتاب‌ها چند تا است؟" , barom= 1.5 , khat=2)

first_text = add_section(first_text , "دانش‌ آموزان عزیز جهت کسب 6 نمره از سؤالات 13 تا 20 فقط ۳ سؤال را به دلخواه انتخاب و پاسخ دهید.")

first_text = add_question(first_text , """یک فروشگاه دو نوع کارت اعتباری A و B را می‌پذیرد. اگر 34 درصد از مشتریان کارت نوع A $(P(A) = \dfrac{34}{100})$ و 62 درصد کارت نوع B و 15 درصد هر دو کارت را همراه داشته باشند، چقدر احتمال دارد مشتریان با در اختیار داشتن حداقل یکی از این دو کارت از این فروشگاه خرید کنند؟""" , khat= 3 , barom= 2)

first_text = add_multiparts(first_text , "یک آزمون چندگزینه‌ای شامل 10 سؤال 4 گزینه‌ای و 5 سؤال 2 گزینه‌ای (بله – خیر) است. فردی قصد دارد به سؤال‌‌ها به صورت تصادفی جواب دهد. او به چند روش می‌تواند این کار را انجام دهد اگر:" , list_part=["اگر مجبور باشد به همه سؤال‌ها جواب دهد؟", "بتواند سؤال‌ها را بدون جواب هم بگذارد؟"] , barom= 2 , khat= 2)

first_text = add_multiparts(first_text,"""اگر A و B زیر مجموعه‌هایی از مجموعه مرجع باشند و در مورد تعداد اعضای مجموعه‌ها اطلاعات زیر را داشته باشیم:\\\\
$n(U)=100 ، n(A)=70 ، n(B) =30 ، n(A\\bigcap B)=15$ \\\\
عبارت‌های زیر را حساب کنید.""" , list_part=["$n(A\\bigcap B^{\prime})= $", "$n(A^{\prime}\\bigcap B^{\prime}) =$"], barom = 2 , ltr=True)

first_text = add_multiparts(first_text, """با فرض با معنی بودن هر کسر، درستی هر یک از تساوی‌های زیر را بررسی کنید.""" , list_part=["$\dfrac{1}{\\sin\\theta}\\times\\tan\\theta = \\dfrac{1}{\\cos\\theta}$ \\\\ \\\\",
"$1-\dfrac{\cos^{2}x}{1+\sin x} = \sin x$"], ltr=True , barom = 2, khat=3)

first_text = add_question(first_text , """فرض کنید $\sin75^{\circ} \\simeq 0.96$. مساحت مثلث ABC در شکل زیر را بدست آورید.
\\\\
\includegraphics[scale = 0.3]{Screenshot_2023-08-23-14-40-21-311_cn.wps.moffice_eng}""", khat= 3 , barom = 2)

first_text = add_question(first_text , "جدول تعیین علامت عبارت زیر را بنویسید. \\begin {LTR} $x^2+6x-2$ \\\\ \\\\ \\\\ \\\\ \\end{LTR}" , barom= 2)

first_text = add_question(first_text , "تابع $f(x) = 3x-1$ را که دامنه آن مجموعه $\{\\dfrac{1}{2},0,5\}$ است، رسم کنید. برد این تابع را به‌دست آورید و نمایش زوج مرتبی و نمودار پیکانی آن را ارائه دهید." , barom= 2 , khat= 5)

first_text = add_question(first_text , "نمودار تابع، یک سهمی است که از نقاط $(1 ، -2)$ و $(2، -3)$ می‌گذرد و محور yها را در نقطه‌ای به عرض ۱ قطع می‌کند. نمایش جبری این تابع را بیابید و نمودار آن را رسم و دامنه و برد تابع را مشخص کنید.", barom= 2 , khat= 5)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت دوم ریاضی ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)