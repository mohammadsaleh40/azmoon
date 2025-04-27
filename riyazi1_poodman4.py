from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts , add_section


first_text = add_sarbarg(first_text, answertime="۵۰ دقیقه" , examdate= "۱۲/۱۲/۱۴۰۳" , teacher= "محمد صالح علی اکبری" , city= "گناباد", schooltitle="متوسطه دوره دوم", branch= "101", school="شهید دکتر چمران" ,grade= "دهم")


first_text = add_fourchoice(first_text, text="حاصل ضرب $3 \\times 3 \\times 3 \\times 3 = ?$ کدام گزینه است؟",
                            list_choice=[
                                "$12$",
                                "$64$",
                                "$27$",
                                "$81$"
                            ], chand=4 , barom= 0.25)

first_text = add_fourchoice(first_text, text="حاصل ضرب $3 \\times 3 \\times 3 \\times 3 = ?$ به چه شکل خلاصه نویسی می‌شود؟",
                            list_choice=[
                                "$3^4$",
                                "$3 \\times 4$",
                                "$3^3$",
                                "$3 \\times 3$"
                            ], chand=4 , barom= 0.25)

first_text = add_fourchoice(first_text, text="حاصل عبارت $7^2$ کدام گزینه است؟",
                            list_choice=[
                                "$14$",
                                "$9$",
                                "$49$",
                                "$42$"
                            ], chand=4 , barom= 0.25)

first_text = add_fourchoice(first_text, text="حاصل $\\sqrt{49} کدام است؟$",
                            list_choice=[
                                "35",
                                "7",
                                "14",
                                "2"
                            ], chand=4 , barom= 0.25)


first_text = add_fourchoice(first_text, text="حاصل $4^3$ کدام است؟",
                            list_choice=[
                                "$12$",
                                "$64$",
                                "$32$",
                                "$16$"
                            ], chand=4 , barom= 0.25)

first_text = add_fourchoice(first_text, text="حاصل $\\sqrt[3]{64}$ کدام است؟",
                            list_choice=[
                                "$4$",
                                "$3$",
                                "$16$",
                                "$2$"
                            ], chand=4 , barom= 0.25)

first_text = add_fourchoice(first_text, text="طول و عرض یک فرش ۱۲ متری به ترتیب ۴ و ۳ است. قطر این فرش چند متر است؟",
                            list_choice=[
                                "$14$",
                                "$12$",
                                "$7$",
                                "$5$"
                            ], chand=4 , barom= 0.5)


first_text = add_question(first_text, text="معادله زیر را به کمک ریشه گیری حل کنید. \\\\ $c^3 = 64$", barom=1, khat=1)
first_text = add_question(first_text, text="معادله زیر را به کمک ریشه گیری حل کنید. پاسخ را فقط به صورت رادیکالی بنویسید. \\\\ $b^2 = 2$", barom=1, khat=2)

first_text = add_question(first_text, text="یک باکتری هر ساعت دوبرابر می‌شود. اگر این باکتری در ساعت ۱ ظهر ۲ گرم باشد به ترتیب در ساعت ۱:۲۰ ظهر، ساعت  ۱:۳۰ ظهر و در ساعت ۲ ظهر چند گرم است؟ جواب را فقط به صورت یک عدد توان دار بنویسید.", barom=1.5, khat=2)

first_text = add_question(first_text, text="قرار هست از یک ساختمان ۱۲ متری در فاصله ۵ متری پای دیوار آن یک میخ کوبیده شود و بین این میخ و بالای دیوار طنابی وصل شود. این طناب چند متر باید باشد؟ تصویری برای این مسئله رسم کنید.", barom=1.5, khat=3)

first_text = add_question(first_text, text="یک شرکت با سرمایه اولیه ۱ میلیارد تومان در سال اول شروع می‌کند. در شروع سال دوم سرمایه آن $1.5$ میلیارد تومان می‌شود. به همین شکل هر سال سرمایه این شرکت $1.5$ برابر می‌شود. در ادامه به شکل اعداد توان دار بگوید در شروع سال ۴ام در شروع سال ۱۱ام و در شروع سال $n$ام سرمایه این شرکت چقدر است؟", barom=1.5, khat=3)

first_text = add_multiparts(first_text, text="حاصل عبارت‌های زیر را در صورت وجود بدست آورید.",list_part=["$\sqrt{\dfrac{1}{49}} = $", "$-2 \\times -2 = $", "$0.0001^{\\dfrac{1}{4}} = $" , "$\\sqrt{-2} =$", "$\\sqrt{-2 \\times 2} =$",  "$\\sqrt{(-3)^2} =$", ] ,barom=1.5, khat=0 , chand=3, ltr=True)




first_text = add_enteha(first_text)
esm_emtehan = "امتحان پودمان 4 درس ریاضی ۱"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)