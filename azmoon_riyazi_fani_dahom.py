from units import first_text, add_enteha, add_sarbarg, create_file, recreate_pdf, delete_temp_file, \
	add_question, add_fourchoice, add_multiparts, add_section


first_text = add_sarbarg(first_text, answertime="۶۰ دقیقه", examdate="شهریور ۱۴۰۵", teacher="محمد صالح علی اکبری", city="گناباد", schooltitle="هنرستان", branch="۱", school="خوارزمی", grade="دهم")

# ==================== پودمان اول ====================
first_text = add_section(first_text, "پودمان ۱: نسبت و تناسب")

# سؤال ۱ (تستی)
first_text = add_fourchoice(first_text,
                            text="اگر $4$ کارگر بتوانند ساخت یک دیوار کارگاهی را در مدت $6$ روز به پایان برسانند، $8$ کارگر با همان توان کاری، این دیوار را در چند روز می‌سازند؟",
                            list_choice=["۳ روز",
                                         "۱۲ روز",
                                         "۸ روز",
                                         "۲ روز"],
                            chand=4, barom=1, khat=0)

# سؤال ۲ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="نسبت طول به عرض یک صفحۀ فلزی در کارگاه برابر $\\dfrac{5}{3}$ است. اگر عرض این صفحه $12\\text{ cm}$ باشد:",
                            list_part=["طول این صفحه را به دست آورید.",
                                       "محیط و مساحت این صفحه را محاسبه کنید."],
                            chand=1, khat=2, khat_beyn=0, barom=8)

# سؤال ۳ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="در سیستم اندازه‌گیری انگلیسی، هر اینچ معادل $2/54$ سانتی‌متر است.",
                            list_part=["طول یک قطعۀ صنعتی برابر $10$ اینچ است؛ این اندازه معادل چند سانتی‌متر است؟",
                                       "طول یک تختۀ چوب $127$ سانتی‌متر است؛ طول آن را بر حسب اینچ محاسبه کنید."],
                            chand=1, khat=2, khat_beyn=0, barom=8)


# ==================== پودمان دوم ====================
first_text = add_section(first_text, "پودمان ۲: درصد و کاربردهای آن")

# سؤال ۴ (تستی)
first_text = add_fourchoice(first_text,
                            text="قیمت اولیۀ یک ابزار کارگاهی ۱۰۰ هزار تومان بوده است. اگر قیمت آن ابتدا $\\%20$ افزایش و سپس $\\%20$ کاهش یابد، قیمت نهایی چند هزار تومان خواهد بود؟",
                            list_choice=["۱۰۰ هزار تومان",
                                         "۹۶ هزار تومان",
                                         "۱۰۴ هزار تومان",
                                         "۹۸ هزار تومان"],
                            chand=4, barom=2, khat=0)

# سؤال ۵ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="قیمت اصلی یک لباس کار برابر ۴۰۰ هزار تومان است. اگر فروشگاهی $\\%15$ تخفیف برای آن در نظر بگیرد:",
                            list_part=["مبلغ تخفیف چقدر است؟",
                                       "خریدار برای خرید این لباس چه مبلغی باید پرداخت کند؟"],
                            chand=1, khat=2, khat_beyn=0, barom=8)

# سؤال ۶ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="تولید روزانۀ یک کارگاه از $200$ قطعه به $250$ قطعه افزایش یافته است.",
                            list_part=["مقدار افزایش تولید چند قطعه بوده است؟",
                                       "درصد تغییر (درصد رشد) تولید را به دست آورید."],
                            chand=1, khat=2, khat_beyn=0, barom=8)


# ==================== پودمان سوم ====================
first_text = add_section(first_text, "پودمان ۳: معادله‌های درجۀ دوم")

# سؤال ۷ (تستی)
first_text = add_fourchoice(first_text,
                            text="جواب‌های معادلۀ درجۀ دوم $x^2 - 5x + 6 = 0$ کدام گزینه‌ها هستند؟",
                            list_choice=["$x = 2$ و $x = 3$",
                                         "$x = -2$ و $x = -3$",
                                         "$x = 1$ و $x = 6$",
                                         "$x = -1$ و $x = -6$"],
                            chand=4, barom=2, khat=0)

# سؤال ۸ (تشریحی)
first_text = add_question(first_text,
                          text="معادلۀ درجۀ دوم $x^2 - 4x - 5 = 0$ را با استفاده از روش دلتا ($\\Delta$) حل کرده و ریشه‌های آن را بیابید.",
                          khat=1, barom=8)

# سؤال ۹ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="طول یک باغچۀ مستطیل‌شکل $3$ متر بیشتر از عرض آن است. اگر مساحت باغچه برابر $28\\text{ m}^2$ باشد:",
                            list_part=["با در نظر گرفتن عرض باغچه برابر $x$، یک معادلۀ درجۀ دوم برای مسئله بنویسید.",
                                       "عرض و طول باغچه را با حل معادله بیابید."],
                            chand=1, khat=1, khat_beyn=0, barom=8)


# ==================== پودمان چهارم ====================
first_text = add_section(first_text, "پودمان ۴: توان‌رسانی به توان عددهای گویا")

# سؤال ۱۰ (تستی)
first_text = add_fourchoice(first_text,
                            text="حاصل عبارت عددی $8^{\\frac{1}{3}}$ کدام است؟",
                            list_choice=["$2$",
                                         "$4$",
                                         "$16$",
                                         "$64$"],
                            chand=4, barom=2, khat=0)

# سؤال ۱۱ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="حاصل هر یک از عبارت‌های زیر را به ساده‌ترین صورت به دست آورید:",
                            list_part=["$\\sqrt[3]{27} + \\sqrt[2]{16} = $",
                                       "$\\sqrt[3]{-125} = $"],
                            chand=2, khat=1, khat_beyn=0, barom=8)

# سؤال ۱۲ (تشریحی)
first_text = add_question(first_text,
                          text="عبارت تواندار زیر را با استفاده از قوانین پایه‌های مساوی ساده کنید و پاسخ را به صورت یک توان کسری بنویسید: $A = x^{\\frac{3}{2}} \\times x^{\\frac{1}{2}} \\quad (x > 0)$",
                          khat=1, barom=8)


# ==================== پودمان پنجم ====================
first_text = add_section(first_text, "پودمان ۵: نسبت‌های مثلثاتی")

# سؤال ۱۳ (تستی)
first_text = add_fourchoice(first_text,
                            text="در یک مثلث قائم‌الزاویه، طول ضلع مقابل به زاویۀ $\\theta$ برابر ۳ و طول وتر برابر ۵ است. مقادیر $\\sin(\\theta)$ و $\\tan(\\theta)$ به ترتیب کدامند؟",
                            list_choice=["$\\dfrac{3}{5}$ و $\\dfrac{3}{4}$",
                                         "$\\dfrac{4}{5}$ و $\\dfrac{4}{3}$",
                                         "$\\dfrac{3}{5}$ و $\\dfrac{4}{3}$",
                                         "$\\dfrac{4}{5}$ و $\\dfrac{3}{4}$"],
                            chand=4, barom=1, khat=0)

# سؤال ۱۴ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="در یک مثلث قائم‌الزاویه، طول وتر $10\\text{ cm}$ و یکی از زاویه‌های حاده $30^\\circ$ است.",
                            list_part=["طول ضلع مقابل به این زاویه را بیابید ($\\sin 30^\\circ = \\dfrac{1}{2}$).",
                                       "طول ضلع مجاور به این زاویه را بیابید ($\\cos 30^\\circ = \\dfrac{\\sqrt{3}}{2}$)."],
                            chand=1, khat=0, khat_beyn=0, barom=1.5)

# سؤال ۱۵ (تشریحی - چند قسمتی)
first_text = add_multiparts(first_text,
                            text="یک نردبان به طول $6$ متر به دیوار کارگاهی تکیه داده شده است و با سطح زمین زاویۀ $60^\\circ$ می‌سازد.",
                            list_part=["ارتفاع نقطه‌ای از دیوار که نردبان به آن تکیه کرده چقدر است؟ ($\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$).",
                                       "فاصلۀ پای نردبان تا دیوار چقدر است؟ ($\\cos 60^\\circ = \\dfrac{1}{2}$)."],
                            chand=1, khat=0, khat_beyn=0, barom=1.5)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان شهریور دهم فنی خوارزمی ۱۴۰۵"
esm_emtehan += ".tex"
create_file(first_text, esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)
