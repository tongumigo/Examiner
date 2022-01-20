from  Exam_funcs import *

#Generate a list of examination numbers
lst =  generator(190910420550,2,5)
lst2 = generator(190910420550,2,99,51)
lst3 = generator(190910420550,3,150,10)
lst4 = generator(190910420550,3,200,151)
lst5 = generator(190910420550,3,250,201)
dic = [lst,lst2,lst3,lst4,lst5]

#Send requests and save results to file
def send_n_save(lst):
    count = 0
    for exam_number in lst:
        count += 1
        print("+ {}\n".format(count),end="")
        html = Requester(exam_number)
        formatted_dict = formatter(html)
        to_file(formatted_dict)
        


#Search for a name
def find(to_search):
    to_search = str(to_search)
    lst = read_file()
    text =  " ".join(lst)
    if to_search in text:
        return True
    else:
        return False



def main():
    for i in dic:
        send_n_save(i)

send_n_save(lst)
