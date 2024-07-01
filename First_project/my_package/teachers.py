from .json_file_handling import *
from .validate import *
class TeacherClass:
    
    def __init__(self):
        pass

    def accept_info(self):
        data = {
            "name" : input("Enter name: "),
            "id" : validate_id(),
            "subject" : input("Enter subject: "),
            "address" : input("Enter address: "),
            "email" : validate_email(),
            "phone_num" : validate_phone()
        }
        write_teacher(data)

    def display_all(self):
        data = read_teacher()
        for diction in data:
            for key,val in diction.items() :
                if key == "name" or key == "id" or key == "subject" or key == "address" or key == "email" or key == "phone_num" :
                    print(f"{key} : {val}")    

    def search(self,to_search):
        data = read_teacher()
        for diction in data:
            if to_search in diction.values():
                for key,val in diction.items() :
                    print(f"{key} : {val}")

    def delete(self,to_delete):
       del_teacher(to_delete)

