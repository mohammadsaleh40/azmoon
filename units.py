import os

first_text = """
\\documentclass[template=tabling,81pt,headonall]{azmoon}
\\usepackage{xepersian}
\\usepackage{amsfonts}
\\usepackage{graphicx}
\\graphicspath{ {./images/} }
\\settextfont{Yas}
\\setdigitfont{A Iranian Sans}

\\printanswers"""

def add_sarbarg (first_text , teacher = "آقا/خانم معلوم نیست" ,teachertitle = "دبیر" ,
                city = "گناباد", schooltitle = "دبیرستان" , school = "نام مدرسه" ,
                grade = "هشتم" , branch = "شعبه کلاس" , topic = "ریاضی" ,  examdate = "تاریخ امتحان",
                answertime = "70 دقیقه"
                ):
    first_text += f"""
    \\teacher{{{teacher}}}
    \\teachertitle{{{teachertitle}}}
    \\city{{{city}}}
    \\schooltitle{{{schooltitle}}}
    \\school{{{school}}}
    \\grade{{{grade}}}
    \\branch{{{branch}}}
    \\topic{{{topic}}}
    \\examdate{{{examdate}}}
    \\answertime{{{answertime}}}
    \\begin{{document}}
	\\begin{{questions}}
		\\nointerlineskip%
		\\vskip-\\baselineskip
		"""
    return first_text

def add_enteha(first_text):
    first_text += """\end{questions}
    \end{document}
    """
    return first_text

def create_file(first_text , file_path):
    f = open (file_path , "w")
    f.write(first_text)
    f.close()
    os.system(f"xelatex '{file_path}'")

def recreate_pdf(file_path):
    os.system(f"xelatex '{file_path}'")

def delete_temp_file(file_path):
    file_path = file_path[:-4]
    os.system(f"rm '{file_path}.aux'")
    os.system(f"rm '{file_path}.headfootlength'")
    os.system(f"rm '{file_path}.fls'")
    os.system(f"rm '{file_path}.headfootlength'")
    os.system(f"rm '{file_path}.log'")