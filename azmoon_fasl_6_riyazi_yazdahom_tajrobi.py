
from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file ,\
	add_question , add_fourchoice, add_multiparts


first_text = add_sarbarg(first_text, grade= "یازدهم")

first_text = add_multiparts(first_text , "برای تابع $f(x) = x + [x]$:" ,
                            ["نمودار تابع در بازه $x\in [-1 , 1)$", """جدول زیر را کامل کنید.
\\begin{table}
\centering
\\begin{tabular}{|c|c|}
\hline
ستون ۱ & ستون ۲ \\
\hline
مقدار ۱-۱ & مقدار ۱-۲ \\
مقدار ۲-۱ & مقدار ۲-۲ \\
مقدار ۳-۱ & مقدار ۳-۲ \\
مقدار ۴-۱ & مقدار ۴-۲ \\
مقدار ۵-۱ & مقدار ۵-۲ \\
مقدار ۶-۱ & مقدار ۶-۲ \\
مقدار ۷-۱ & مقدار ۷-۲ \\
مقدار ۸-۱ & مقدار ۸-۲ \\
مقدار ۹-۱ & مقدار ۹-۲ \\
مقدار ۱۰-۱ & مقدار ۱۰-۲ \\
\hline
\end{tabular}
\caption{یک جدول دو در ده}
\end{table}

"""])






first_text = add_enteha(first_text)
esm_emtehan = "نمونه سؤال فصل حد و پیوستگی"
esm_emtehan += ".tex"
create_file(first_text , esm_emtehan)
recreate_pdf(esm_emtehan)
delete_temp_file(esm_emtehan)