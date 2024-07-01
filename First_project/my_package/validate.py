from .json_file_handling import *
def validate_email():
    email = input("Enter email: ")
    if "@gmail.com" in email or "@yahoo.com" in email:
        return email
    else:
        print("invalid email")
        validate_email()
    
def validate_phone():
    num = int(input("Enter phone number: "))
    if len(str(num)) == 10 and isinstance(num,int):
        return num
    else:
        print("Invalid number")
        validate_phone()
    
def validate_teacher(name,id):
    data = read_teacher()
    for diction in data:
        if name and id in diction.values():
            return True
        
def validate_id():
    id = int(input("Enter id"))
    data = read_teacher()
    for diction in data:
        if id in diction.values():
            print("Invalid ID")
            validate_id()
        else:
            return id
        
def validate_student(name):
    data = read_student()
    for diction in data:
        if name in diction.values():
            return True
    