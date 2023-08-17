from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts


first_text = add_sarbarg(first_text, answertime="90 دقیقه" , examdate= "24 مرداد 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "-", school="شهید رجایی" ,grade= "یازدهم")

first_text = add_question(first_text , "جدول زیر را کامل کنید. \\\\ \includegraphics[scale = 1]{جدول_گزاره‌ها}", barom=2)
first_text = add_question(first_text , "5 افراز مختلف از مجموعه $A = \{1,2,3,4\}$ را بنویسید.", khat= 2, barom= 1)
first_text = add_question(first_text , "اگر $A = \\mathbb{N}$ و $B = [1,4]$ باشد مطلوب است نمودار حاصل از ضرب‌های $A \\times B$ و $B \\times A$." , khat= 4, barom = 1)
first_text = add_multiparts(first_text , "اگر $p(A) = \dfrac {2}{5}$ ، $P(B') = \dfrac {3}{7}$ و $P(A \cap B) = \dfrac{1}{5}$ مطلوب است: " , list_part=["$P(A-B)$","$P(A \cup B)$"] , ltr= True , barom = 1.5)
first_text = add_question(first_text , "در پرتاب یک سکه ناسالم، احتمال آمدن رو، نصف احتمال آمدن پشت است. در پرتاب این سکه احتمال ظاهر شدن «رو» و احتمال ظاهر شدن «پشت» را بدست آورید." , khat = 2, barom = 1.5)
first_text = add_question(first_text , "در یک شرکت بسته بندی کالا، درصد محصولات تولیدی با سه دستگاه A و B و C به ترتیب 30، 45 و 25 است. اگر 1 درصد محصولات A و 2 درصد محصولات B و 4 درصد محصولات C معیوب باشند و یک کالا به تصادف از بین محصولات شرکت انتخاب کنیم، احتمال اینکه کالا سالم باشد چقدر است؟", khat = 4 , barom= 1.5)
first_text = add_multiparts(first_text , "احتمال آنکه امیر در کنکور قبول شود $0.7$ و احتمال آنکه علی در کنکور قبول شود $0.6$ می‌باشد. مطلوب است احتمال آنکه:" , list_part = ["هیچکدام از آن‌ها در کنکور قبول نشوند؟","فقط یکی از آن‌ها در کنکور قبول شوند؟"], khat = 3, barom = 2)
first_text = add_multiparts(first_text , "در یک امتحان تستی 4 گزیه‌ای 10 سؤال مطرح شده است. اگر دانش‌آموزی به همه سؤالات پاسخ دهد. احتمال حالت‌های زیر را بدست بیاورید.: (نیازی به محاسبه جواب آخر نیست)",
                        list_part= ["اجتمال پاسخ صحیح به همه سؤالات.","احتمال پاسخ صحیح به نیمی از سؤالات."], khat = 4, barom = 1.5)
first_text = add_question(first_text , "جدول زیر درصد فراوانی نسبی گروه خونی افراد یک جامعه است. در نمودار دایره‌ای، زاویه سطح مربوط به گروه خونی O چند است؟  \\\\ \includegraphics[scale = 1]{جدول_فراوانی_نمودار_دایره‌ای}" , khat = 2 , barom = 1)
first_text = add_question(first_text , "طبق نمرات زیر معدل دانش‌آموزان کلاسی در درس آمار $16.95$ است. نمره دانش‌آموزی که با x‌نشان داده شده است را محاسبه کنید. \\\\ X , $17.5$, 19, 17, 16, 20, 16, 15, 18,18", khat = 2, barom = 1)
first_text = add_question(first_text , "در جدول فراوانی مقابل به تمام داده‌ها $1.5$ واحد اضافه می‌شود، میانگین داده‌های جدید ۱۰ می‌شود. فراوانی دسته سوم چقدر است؟ \\\\ \includegraphics[scale = 1]{جدول_فراوانی_s11}" , khat = 1, barom= 1)
first_text = add_question(first_text , "برای اعداد زیر، واریانس، انحراف معیار، ضریب تغییرات را بدست بیاورید. \\\\ 63 ، 50 ، 64 ، 23 ، 45 ، 17 ، 74 ، 53 ، 26 ، 59 ، 32" , khat = 4, barom = 1.5)
first_text = add_question(first_text , "نمودار حعبه‌ای داده‌های زیر را رسم کنید. \\\\ 2 ، 1 ، 5 ، 5 ، 2 ، 2، 2 ، 2 ، 3 ، 1 ، 1 ، 1 ، 2, 4, 7, 1, 4, 6, 8, 3, 4, 7" , khat = 4, barom = 2)
first_text = add_question(first_text , "فرق بین داده و متغیر چیست؟" , khat=2 , barom = 0.5)
first_text = add_multiparts(first_text , "اصطلاحات زیر را تعریف کنید." , list_part= ["نمونه گیری سیستماتیک" , "نمونه گیری تصادفی ساده."] , barom=1)

first_text = add_enteha(first_text)
esm_emtehan = "امتحان نوبت دوم آمار و احتمال یازدهم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)