from .json_file_handling import *
from .validate import *
class StudentClass():

    def __init__(self):
       pass

    def accept_info(self):
        data = {
            "name" : input("Enter name: "),
            "roll_num" : int(input("Enter roll: ")),
            "address" : input("Enter address: "),
            "email" : validate_email(),
            "phone_num" : validate_phone(),
            "marks" : list(input("Enter marks: "))
        }
        write_student(data)

    def display_all(self):
        data = read_student()
        for diction in data:
            for key,val in diction.items():
                if key == "name" or key == "subject" or key == "address" or key == "email" or key == "phone_num" or key == "roll_num" or key == "marks":
                    print(f"{key} : {val}") 

    def search(self,to_search):
        data = read_student()
        for diction in data:
            if to_search in diction.values():
                for key,val in diction.items() :
                    print(f"{key} : {val}")

    def pass_fail_determination(self,student_name):
        data = read_student()
        for diction in data:
            if diction.values() == student_name:
                for key,value in diction:
                    if key == "marks":
                        if all(num > 32 for num in value):
                            return "pass"
                        else:
                            return "fail"
                        
    def Highest_score(self):
        highest = 0
        data = read_student()
        for diction in data:
            if diction.keys() == "marks":
                high = sum(diction.values())
                if highest < high:
                    highest = high
        return highest
    
    def percentage(self,name):
        data = read_student()
        for diction in data:
            if name in diction.values():
                if diction.keys() == "marks":
                    percent = sum(diction.values()) / len(diction.values())
                    return percent
    
    def delete(self,to_delete):
       del_student(to_delete)