#import os

from units import first_text , add_enteha , add_sarbarg , create_file , recreate_pdf , delete_temp_file


first_text = add_sarbarg(first_text)

first_text += """

		\question{%
		در فرایند پیدا کردن عددهای اول بین ۲۰ و ۴۰، ب.م.م. دوومین عدد که در مضرب ۲ خط می‌خورد و ششمین عددی که از مضرب ۳ خط می‌خورد کدام است.
			\\begin{fourchoice}
				\choice{۳}
				\choice{۲}
				\choice{۵}
				\choice{۷}
			\end{fourchoice}
		}
        """


first_text = add_enteha(first_text)


create_file(first_text , "آزمون فصل ۳ و ۴ دهم.tex")
recreate_pdf("آزمون فصل ۳ و ۴ دهم.tex")
delete_temp_file("آزمون فصل ۳ و ۴ دهم.tex")