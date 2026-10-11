from units import first_text, add_enteha, add_sarbarg, create_file, recreate_pdf, delete_temp_file, \
	add_question, add_fourchoice, add_multiparts, add_section


first_text = add_sarbarg(first_text, answertime="۹۰ دقیقه", examdate="مهر ۱۴۰۶", teacher="محمد صالح علی اکبری", city="گناباد", schooltitle="دبستان", branch="۱", school="پیشگامان ظهور", grade="چهارم")


# سؤال ۱: درست یا نادرست
first_text = add_multiparts(first_text, text="""درست یا نادرست بودن هر یک از عبارت‌های زیر را مشخص کنید.""",
                            list_part=["در عدد $507083002$ عدد $7$ در مرتبه یکان طبقه میلیون قرار دارد. \\hfill (\\qquad\\qquad)",
                                       r"$423$ ثانیه برابر $8 \dfrac{12}{60}$ دقیقه است که به طور تقریبی آن را $8$ دقیقه در نظر می‌گیریم. \hfill (\qquad\qquad)",
                                       "به متوازی الاضلاعی که زاویه‌های برابر داشته باشد، لوزی می‌گویند. \\hfill (\\qquad\\qquad)",
                                       "عدد $1680$ بر عدد های $7,5,3,2$ بخش پذیر است. \\hfill (\\qquad\\qquad)"],
                            chand=1, barom="1")

# سؤال ۲: جای خالی
first_text = add_multiparts(first_text, text="""در جاهای خالی کلمه مناسب بنویسید.""",
                            list_part=["۵ تا چک پول ۵۰۰ هزار ریالی برابر ...... ریال با ........ تومان",
                                       "اگر دو کسر صورت های برابر داشته باشند کسری کوچک تر است که مخرج .......... باشد.",
                                       r"$3/5$ یعنی ......... تا $0/1$ و ......... $72$ تا $0/1$ می‌باشد.",
                                       "در هر متوازی الاضلاع اندازه ......... روبه‌رو با هم مساوی و ...... روبه‌رو با هم موازی هستند."],
                            chand=1, barom="1.75")

# سؤال ۳: تستی (دو مورد)
first_text = add_question(first_text,
                          text=r"""گزینه صحیح را در هر مورد مشخص کنید: \\[0.3em]
\textbf{۱)} مثلث (م د ج) مثلث متساوی‌الاضلاع است. اندازه زاویه مشخص شده چند درجه است؟ \\
\parbox[c]{0.65\textwidth}{%
\begin{fourchoice}[1]
\choice{$25$ درجه}
\choice{$30$ درجه}
\choice{$35$ درجه}
\choice{$40$ درجه}
\end{fourchoice}%
}\hfill%
\\\\ \parbox[c]{0.3\textwidth}{\centering\includegraphics[scale=0.25]{chaharom_q3_mosalas}} \\[0.5em]
\textbf{۲)} کدام یک از زمان‌های زیر از بقیه طولانی‌تر است؟
\begin{fourchoice}[2]
\choice{$679$ ثانیه}
\choice{$12$ دقیقه و $30$ ثانیه}
\choice{خمس یک ساعت و $40$ ثانیه}
\choice{یک سی‌ام شبانه‌روز}
\end{fourchoice}""",
                          barom="0.5")

# سؤال ۴: ارزش مکانی
first_text = add_multiparts(first_text,
                            text=r"""با توجه به عدد زیر به سوالات پاسخ دهید: \hfill \textbf{\large 89147256}""",
                            list_part=[r"این عدد را به حروف بنویسید: \dotfill",
                                       r"کدام رقم در مرتبه یکان هزار قرار دارد؟ \dotfill",
                                       r"ارزش مکانی عدد ۵ را بنویسید: \dotfill",
                                       r"این عدد را در جدول ارزش مکانی نشان دهید: \dotfill"],
                            chand=1, barom="1", khat=1)

# سؤال ۵: الگو
first_text = add_question(first_text,
                          text=r"""در الگوی زیر شکل هشتم از چند دایره تشکیل شده است؟ (نوشتن رابطه الزامی است) \\[0.3em]
\centering\includegraphics[scale=0.35]{chaharom_q5_olgoo} \\[0.3em]
\raggedright رابطه یا فرمول: \dotfill""",
                          barom="1", khat=1)

# سؤال ۶: مقایسه
first_text = add_multiparts(first_text,
                            text=r"""مقایسه کنید ($>$ یا $<$ یا $=$):""",
                            list_part=[r"$3256 \quad \bigcirc \quad 479$",
                                       r"$\dfrac{3}{5} \quad \bigcirc \quad \dfrac{3}{8}$",
                                       r"$\dfrac{2}{3} \quad \bigcirc \quad \dfrac{5}{12}$",
                                       r"$3\dfrac{3}{4} \quad \bigcirc \quad 3\dfrac{2}{4}$",
                                       r"$6\dfrac{8}{12} \quad \bigcirc \quad 9\dfrac{3}{6}$",
                                       r"$7/1 \quad \bigcirc \quad 6/4$"],
                            chand=3, barom="1.5", khat_beyn=1)

# سؤال ۷: ساده کردن کسرها
first_text = add_multiparts(first_text,
                            text="""کسرهای زیر را ساده کنید:""",
                            list_part=[r"$\dfrac{12}{20} = $",
                                       r"$\dfrac{14}{21} = $"],
                            chand=2, barom="1", khat=1)

# سؤال ۸: مسئله اعشار
first_text = add_question(first_text,
                          text="""کیف فیروزه $4/2$ کیلوگرم و کیف دوستش $3/9$ کیلوگرم وزن دارد. وزن کیف فیروزه چند کیلوگرم بیشتر از وزن کیف دوستش می‌باشد؟""",
                          barom="1", khat=2)

# سؤال ۹: مسئله کسر
first_text = add_multiparts(first_text,
                            text=r"""کشاورزی $\dfrac{3}{6}$ مزرعه‌ی خود را گل آفتابگردان و $\dfrac{3}{18}$ آن را گل رز کاشته است:""",
                            list_part=["چه کسری از زمین را گل کاشته است؟",
                                       "چه کسری از زمین بدون کشت مانده است؟"],
                            chand=1, barom="1", khat=1, khat_beyn=1)

# سؤال ۱۰: ضرب و تقسیم
first_text = add_question(first_text,
                          text=r"""حاصل ضرب و تقسیم زیر را به دست آورید: \\[0.3em]
\centering\includegraphics[scale=0.38]{chaharom_q10_zarb_taghsim}""",
                          barom="2", khat=2)

# سؤال ۱۱: زوایا و هندسه
first_text = add_question(first_text,
                          text=r"""برای هر شکل مقدار (؟) را به دست آورید: \\[0.3em]
\centering\includegraphics[scale=0.4]{chaharom_q11_zaviyeha}""",
                          barom="2", khat=1)

# سؤال ۱۲: مساحت قسمت رنگی
first_text = add_question(first_text,
                          text=r"""مساحت قسمت رنگی را به دست آورید: \\[0.3em]
\centering\includegraphics[scale=0.45]{chaharom_q12_shekl}""",
                          barom="2", khat=2)

# سؤال ۱۳: محیط و مساحت کاربردی
first_text = add_question(first_text,
                          text="""یک زمین کشاورزی مستطیل شکل به طول $20$ متر و عرض $15$ متر داریم. می‌خواهیم دور این زمین را نرده بکشیم به چند متر نرده نیاز داریم؟ اگر برای هر متر مربع از این زمین کشاورزی $3$ کیلوگرم بذر گندم نیاز باشد چند کیلوگرم بذر گندم برای همه‌ی زمین لازم است؟""",
                          barom="2", khat=3)

# سؤال ۱۴: احتمال
first_text = add_multiparts(first_text,
                            text="""تاسی را پرتاب می‌کنیم. برای هر یک از احتمالات زیر یک جمله بنویسید:""",
                            list_part=["احتمال آمدن عدد زوج؟ \\dotfill",
                                       "احتمال آمدن عدد دورقمی؟ \\dotfill",
                                       "احتمال آمدن عدد کمتر از ۷؟ \\dotfill"],
                            chand=1, barom="0.75")

# سؤال ۱۵: آمار و نمودار
first_text = add_question(first_text,
                          text=r"""قیمت نفت در ۵ هفته گذشته به صورت زیر بوده است: \\[0.3em]
\noindent
\begin{tabular}{|c|c|c|c|c|c|}
\hline
هفته & ۱ & ۲ & ۳ & ۴ & ۵ \\ \hline
قیمت & ۱۰۵ & ۱۰۷ & ۱۰۹ & ۱۱۰ & ۱۰۸ \\ \hline
\end{tabular} \\[0.5em]
الف) نمودار خط شکسته مربوط به آن را رسم کنید. \\
ب) در کدام هفته‌ها قیمت کمترین و بیشترین مقدار بوده است؟ \dotfill \\
ج) تغییرات قیمت نفت در کدام هفته از بقیه هفته‌ها کمتر است؟ \dotfill""",
                          barom="1", khat=3)

# سؤال ۱۶: تقریب
first_text = add_multiparts(first_text,
                            text="""عددهای داده شده را با تقریب‌های خواسته شده بنویسید:""",
                            list_part=[r"$476$ با تقریب در دهگان $\longrightarrow$ \dotfill",
                                       r"$23162$ با تقریب در هزارگان $\longrightarrow$ \dotfill"],
                            chand=2, barom="0.5")


first_text = add_enteha(first_text)
esm_emtehan = "امتحان مرور ریاضی چهارم ابتدایی"
esm_emtehan += ".tex"
create_file(first_text, esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)
