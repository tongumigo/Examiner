

from re import I
from tokenize import String
import requests
import bs4


def generator(exam_no, remove, stop, start=0):
    """
    *******************************************************
    |+ e.g generator(190910420550, 2, 10) start => default 0
    |+ return a [list of strings]
    |+ (start and stop) is the value to which values will
    |+ be generated exam_no is the full examination number
    |+ Remove is the positional places from the end at
    |+ old is removeed and the new values are added
    ********************************************************
    """

    list_exams = []
    exam_num = str(exam_no)[:-remove]

    for i in range(start, stop + 1):
        additive = str(i)
        additive = additive.rjust(remove, "0")
        exam_num = exam_num + additive

        list_exams.append(exam_num)
        exam_num = str(exam_no)[:-remove]

    return list_exams


def Requester(examno):
    """
    *******************************************************
    |+ This function receives the examination number and
    |+ sends a post request to the ecz portal.
    |+ Arguements are a string => messager(190910420550)
    |+ Returns a string of html
    ********************************************************
    """

    HTML = ""
    url = "https://eservices.exams-council.org.zm/e-sor/g9_int_statement_can.php"
    payload_2 = {'examno': examno, 'submit': 'Continue >'}

    try:
        res = requests.post(url, files=payload_2)
        HTML = res.text
    except:
        print("Problem occured")

    t = open("index.html", 'a')
    t.write(HTML)
    t.close()

    return print(HTML)


Requester("190910420530")


def to_file(wat_to_rit):
    """
    *******************************************************
    |+ Saves the txt to a file
    |+ input string => output txt file
    ********************************************************
    """

    txt = open("Exam_result.txt", 'a')
    txt.write(wat_to_rit)
    txt.close()


def formatter(html_txt):
    """
    *******************************************************
    |+ This function take in a string html and parses it 
    |+ returning a dictionary of key and values pairs
    ********************************************************
    """

    details = bs4.BeautifulSoup(html_txt, "html.parser")
    item = details.select("td")

    Examin_num, name, Aggre_score, sub_passed = item[0], item[2], item[5], item[6]

    Examin_num = Examin_num.get_text()
    name = name.get_text()
    Aggre_score = Aggre_score.get_text()
    sub_passed = sub_passed.get_text()

    lst = [Examin_num, name, Aggre_score, sub_passed]
    tionary = {}

    for item in lst:
        for i in range(2):
            temp_list = item.split(" : ")
            tionary[temp_list[0]] = temp_list[1]

    return tionary


# print(formatter(Requester(190910420550)))


def display(name):
    Examin_num = ""
    name = ""
    Aggre_score = ""
    sub_passed = ""

    txt = "+----------------------------------------+\n{}\n{}\n{}\n{}\n+----------------------------------------+ \n".format(
        Examin_num, name, Aggre_score, sub_passed)
