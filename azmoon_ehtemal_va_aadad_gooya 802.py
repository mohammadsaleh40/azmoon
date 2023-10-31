from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="40 دقیقه" , examdate= "آبان 1402" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره اول", branch= "-", school="شاهد خاکپور" ,grade= "هشتم")

first_text = add_section(first_text , "۳ سؤال از ۶ سؤال زیر را انتخاب کنید و به آن‌ها پاسخ دهید.")
first_text = add_multiparts(first_text , "عبارت‌های زیر را حساب کنید." , list_part = [
    "$\\dfrac{10^{-3}\\times0.122\\times10^{6}}{61\\times0.25}$",
    "$\\dfrac{16\\times6.022\\times10^{23}}{64}$"
], ltr=True , barom= 1 , khat_beyn= 1 , khat= 1 )
first_text = add_question(first_text, "یک فروشنده بعد از یک معامله پر خطر که کل سرمایه کاری اش در آن بود ۲۰ درصد سود می‌کند. او که از این نتیجه خوشحال بود دوباره کل سرمایه اش را درگیر معامله می‌کند. این بار ۲۰ درصد زیان می‌کند. در نهایت این فروشنده چند درصد سود یا زیان کرده است؟", barom= 1 , khat=3)
first_text = add_question(first_text , "یک ساندویچی برای این که جذب مخاطب بیشتری کند طرح $4+1$ را شروع کرده است. یعنی در ازای برگرداندن هر ۴ پلاستیک نشان دار آن ساندویچی ۱ ساندویچ دیگر به صورت رایگان به مشتری می‌دهند. برای سال آینده این ساندویچی براورد کرده است هر ساندویچ را باید به قیمت $45000$ تومان بدون طرح $4+1$ بفروشد. این ساندویچی می‌خواهد این طرح $4+1$ را ادامه دهد و هرچقدر هم که فروش داشته باشد و تمام پلاستیک‌ها در حال برگشت باشند باز هم زیان نکند قیمت جدید هر ساندویچ چند تومان باید باشد؟" ,khat=6, barom=1)
first_text = add_multiparts(first_text , "احتمال وقوع هر یک از وقایع زیر را بدست آورید." , list_part=[
    "یک تاس را دوبار بیندازیم. حاصل ضرب دو عددی که رو آمدند 18 باشد.",
    "دو سکه می‌اندازیم. احتمال این که یکی رو و یکی پشت بیایید چقدر است؟"
] , khat_beyn= 1 , khat=1 , barom=1)
first_text = add_question(first_text , "حاصل عبارت $6x - 4y +1$ به ازای $x = 3a$ ، $y = -\\frac{1}{4}a$ بر حسب $a$ بدست آورید؟"  , khat= 3)
first_text = add_question(first_text , "تعدادی باکتری در ظرفی شیشه‌ای گذاشته شده‌اند. یک ثانیه بعد هر باکتری به دو تا تقسیم می‌شود، یک ثانیه بعد از آن هر یک از باکتری‌های حاصل هم به دو باکتری تقسیم می‌شود و همین طور تا آخر. بعد از یک دقیقه ظرف پر می‌شود. چه وقت نصف ظرف پر شده است؟", khat=2 , barom=1)

first_text = add_enteha(first_text)
esm_emtehan = "۸۰۲ امتحان ریاضی فصل ۱ هشتم"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)