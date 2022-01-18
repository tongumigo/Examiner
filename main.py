


def generator(exam_no, remove, stop, start = 0):
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
    exam_num   = str(exam_no) [:-remove] 

    for i in range(start, stop + 1):
        additive = str(i)
        additive = additive.rjust(remove,"0") 
        exam_num = exam_num + additive

        list_exams.append(exam_num)
        exam_num = str(exam_no) [:-remove] 

    return list_exams 
       

        
def messager():
    pass



def sender():
    pass


def formatter():
    pass




def display():
    pass