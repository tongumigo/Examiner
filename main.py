

import requests


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


def messager(examno):
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

    return HTML


print(messager(190910420550))


def sender():
    pass


def formatter():
    pass


def display():
    pass
