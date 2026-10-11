from units import first_text, add_enteha, add_sarbarg, create_file, recreate_pdf, delete_temp_file, \
	add_question, add_fourchoice, add_multiparts, add_section


first_text = add_sarbarg(first_text, answertime="۶۰ دقیقه", examdate="مهر ۱۴۰۶", teacher="محمد صالح علی اکبری", city="گناباد", schooltitle="دبستان", branch="۱", school="پیشگامان ظهور", grade="پنجم")


# سؤال ۱ (تستی)
first_text = add_fourchoice(first_text,
                            text="""در عدد هفت میلیارد و دویست و نود و شش میلیون و پانصد و چهل و سه هزار و پانصد و هفتاد، رقم مرتبه یکان هزار و مرتبه دهگان میلیون کدام گزینه است؟""",
                            list_choice=["یکان هزار ۳، دهگان میلیون ۹",
                                         "یکان هزار صفر، دهگان میلیون ۷",
                                         "یکان هزار ۳، دهگان میلیون ۵",
                                         "یکان هزار ۹، دهگان میلیون ۳"],
                            chand=2, barom="0.5")

# سؤال ۲ (تستی)
first_text = add_fourchoice(first_text,
                            text="""کدام گزینه از خصوصیات لوزی نیست؟""",
                            list_choice=["مساحت لوزی مساوی حاصل‌ضرب دو قطر تقسیم بر ۲",
                                         "قطرها یکدیگر را نصف می‌کنند",
                                         "زاویه‌های روبه‌رو با هم مساوی هستند",
                                         "ضلع‌های روبه‌رو با هم مساوی نیستند"],
                            chand=1, barom="0.5")

# سؤال ۳ (تستی)
first_text = add_fourchoice(first_text,
                            text="""گسترده عدد $3/61$ کدام گزینه است؟""",
                            list_choice=[r"$3 + 0/6 + 0/01$",
                                         r"$3 + 6 + 0/01$",
                                         r"$3 + 0/06 + 1$",
                                         r"$36 + 0/1$"],
                            chand=2, barom="0.5")

# سؤال ۴ (تستی)
first_text = add_fourchoice(first_text,
                            text="""اگر در یک کیسه سه تیله نارنجی و سه تیله سفید داشته باشیم، احتمال بیرون آمدن تیله سفید چقدر است؟""",
                            list_choice=["احتمال بیرون آمدن تیله سفید و نارنجی برابر است",
                                         "احتمال بیشتر تیله سفید در می‌آید",
                                         "احتمال کمتر تیله سفید در می‌آید",
                                         "احتمال خیلی زیاد تیله سفید در می‌آید"],
                            chand=1, barom="0.5")

# سؤال ۵ (تستی)
first_text = add_fourchoice(first_text,
                            text="""کدام گزینه درست است؟""",
                            list_choice=[r"$0/25 = 0/250$",
                                         r"$0/7 > 0/71$",
                                         r"$0/306 > 0/36$",
                                         r"$0/205 = 0/25$"],
                            chand=2, barom="0.5")

# ==================== درست یا نادرست ====================
first_text = add_section(first_text, "درست یا نادرست بودن هر یک از عبارت‌های زیر را مشخص کنید.")

# سؤال ۶
first_text = add_question(first_text,
                          text=r"""مجموع زاویه‌های داخلی یک چهارضلعی $360$ درجه است. \hfill (\qquad\qquad)""",
                          barom="0.5")

# سؤال ۷
first_text = add_question(first_text,
                          text=r"""برای به دست آوردن حجم یک مکعب مستطیل، طول و عرض و ارتفاع را با هم جمع می‌کنیم. \hfill (\qquad\qquad)""",
                          barom="0.5")

# سؤال ۸
first_text = add_question(first_text,
                          text=r"""وقتی نیمساز یک زاویه $150$ درجه را رسم کنیم، دو زاویه $70$ درجه به دست می‌آید. \hfill (\qquad\qquad)""",
                          barom="0.5")

# سؤال ۹
first_text = add_question(first_text,
                          text=r"""$3$ درصد شیر چربی است؛ یعنی از هر $100$ گرم شیر، $3$ گرم چربی است. \hfill (\qquad\qquad)""",
                          barom="0.5")

# سؤال ۱۰
first_text = add_question(first_text,
                          text=r"""یک مربع فقط دو خط تقارن دارد. \hfill (\qquad\qquad)""",
                          barom="0.5")

# ==================== سؤالات تشریحی ====================
first_text += r"\newpage"
# سؤال ۱۱
first_text = add_question(first_text,
                          text=r"""اندازه زاویه (۱) و (۲) را پیدا کنید: \\ \\\\ \\\\ \\ زاویه $(1) = $ \\ زاویه $(2) = $""",
                          barom="1", khat=1)

# سؤال ۱۲
first_text = add_multiparts(first_text,
                            text="""در جاهای خالی عدد مناسب بنویسید.""",
                            list_part=[r"$\dfrac{6}{5} = \dfrac{\framebox[0.7cm]{\vphantom{0}}}{25}$",
                                       r"$\dfrac{\framebox[0.7cm]{\vphantom{0}}}{21} = \dfrac{9}{7}$",
                                       r"$\dfrac{4}{3} = \dfrac{\framebox[0.7cm]{\vphantom{0}}}{12} = \dfrac{20}{\framebox[0.7cm]{\vphantom{0}}}$"],
                            chand=3, barom="1",khat = 1)

# سؤال ۱۳
first_text = add_question(first_text,
                          text="""پدر مریم $500$ تومان به او داد. مریم $60$ درصد پولش را یک جامدادی خرید. چند تومان برایش باقی مانده است؟""",
                          barom="1", khat=4)

# سؤال ۱۴
first_text = add_question(first_text,
                          text=r"""در این الگو شکل چهارم را رسم کنید و فرمول یا رابطه آن را بنویسید: \\ \\\\ \\\\ \\ رابطه یا فرمول = """,
                          barom="1", khat=1)

# سؤال ۱۵
first_text = add_question(first_text,
                          text="""جرم یک کیف مدرسه $1500$ گرم است. اگر در این کیف $3610$ گرم کتاب قرار دهیم، جرم کیف و کتاب‌ها با هم چقدر می‌شود؟""",
                          barom="1.5", khat=3)

# سؤال ۱۶
first_text = add_question(first_text,
                          text=r"""محیط شکل زیر را پیدا کنید: \\ \\\\""",
                          barom="1.5", khat=2)

# سؤال ۱۷
first_text = add_question(first_text,
                          text="""دانش‌آموزان یک کلاس تصمیم گرفتند در جشن عید مبعث از دوستان خود با شربت پذیرایی کنند. اگر گنجایش یک لیوان $200$ سی‌سی باشد و تعداد دانش‌آموزان کلاس $25$ نفر باشد، برای تهیه شربت به یک ظرف چند لیتری نیاز است؟""",
                          barom="2", khat=3)

# سؤال ۱۸
first_text = add_multiparts(first_text,
                            text="""عملیات زیر را انجام دهید:""",
                            list_part=[r"$4/26 \times 200 = $",
                                       r"$3 \div \dfrac{12}{8} = $",
                                       r"$3 \dfrac{2}{3} - 1 \dfrac{2}{5} = $",
                                       r"$7/1 - 3/025 = $"],
                            chand=1, khat=1, barom="2", ltr= True, khat_beyn = 1)


first_text = add_enteha(first_text)
esm_emtehan = "امتحان مرور ریاضی پنجم ابتدایی"
esm_emtehan += ".tex"
create_file(first_text, esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)
