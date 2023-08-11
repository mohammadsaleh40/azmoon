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

def add_question(first_text, text , khat = 0):
    first_text += """\question{%
    """
    first_text += text

    for i in range (khat):
        first_text += """
\\\\"""

    first_text += "}"
    return first_text

def add_fourchoice(first_text , text , list_choice):
    first_text+="""\\question{%
    """+ text+"""
    """
    first_text+= "\\begin{fourchoice}"
    for i in range(len(list_choice)):
        first_text += f"""\choice{{{list_choice[i]}}}
"""
    first_text += """\end{fourchoice}
    }
"""
    return first_text

def add_multiparts(first_text , text, list_part , ltr = False):
    first_text +="""\\question{%
    """+ text+"""
    """
    if ltr:
        first_text+= """\\begin{LTR}
        """    
    first_text+= "\\begin{parts}"
    for i in range(len(list_part)):
        first_text += f"""\part{{{list_part[i]}}}
"""
    first_text += """\\end{parts}
"""

    if ltr:
        first_text+= """\end{LTR}
        """
    first_text +="""
    }"""

    return first_text
