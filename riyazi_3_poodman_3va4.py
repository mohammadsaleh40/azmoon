from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۵۰ دقیقه" , examdate= "۱۰/۰۲/۱۴۰۴" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "301", school="شهید دکتر چمران" ,grade= "دوازدهم")

first_text = add_question(first_text, text = "نمودار یک تابع با دامنه $(-1,0) \\bigcup (0,1) \\bigcup (1,2)$ به شکل زیر است. آیا این تابع پیوسته است؟ چرا؟  \\\\\includegraphics[scale = 0.45]{Screenshot_۲۰۲۵-۰۴-۲۳-۰۶-۰۲-۲۲-۵۹۸_cn.wps.moffice_eng}", khat=2, barom = 2)

first_text = add_question(first_text, text = "نمودار یک تابع به صورت زیر داده شده است. وجود حد این تابع را در نقطه $-2$ ، صفر، $2$ و $3$ بررسی کنید.  \\\\\includegraphics[scale = 0.45]{peyvasteghi_had}", khat=2, barom = 2)

first_text = add_question(first_text, text="""آیا تابع زیر در $x = 2$ حد دارد؟ \\\\
\\begin{equation}
  f(x)=\\begin{cases}
    2 - x^2, & \\ x <= 2\\\\
    x - 4, & \\ 2 < x
  \end{cases}
\end{equation}
""", khat=2, barom = 3)
first_text = add_question(first_text, text="""آیا تابع زیر با دامنه $\\mathbb{R}$ در $x = 1$ پیوسته است؟ نمودار این تتابع را رسم کنید. \\\\
\\begin{equation}
  f(x)=\\begin{cases}
    1 + x^2, & \\ x < 1\\\\
    0, & \\ x = 1\\\\
    2x, & \\ 1 < x
  \end{cases}
\end{equation}
""", khat=5, barom = 3)

first_text = add_multiparts(first_text, text = "مشتق تابع های زیر را در نقطه $x = 1$ به دست آورید.", list_part=["$g(x) = x$", "$f(x) = x^2$"], ltr=True, khat_beyn= 4, khat= 4 , barom=4)

first_text = add_question(first_text, text="""
مشتق تابع خطی $f(x) = 2x+1$ با دامنه $\\mathbb{R}$ را در نقاط $x=1$, $x=3$ و در نقطه دلخواه a حساب کنید.
""", khat=8, barom = 6)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان پودمان ۳ و ۴ درس ریاضی ۳"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)