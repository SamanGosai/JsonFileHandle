import json

def read_teacher():
    with open('./my_package/json_files/teacher.json','r') as file:
            data = json.load(file)
    return data

def write_teacher(data):
    json_data = list(read_teacher())
    json_data.append(data)
    with open('./my_package/json_files/teacher.json','w') as file:
        json.dump(json_data,file,indent=4)

def read_student():
    with open('./my_package/json_files/students.json','r') as file:
            data = json.load(file)
    return data

def write_student(data):
    json_data = list(read_student())
    json_data.append(data)
    with open('./my_package/json_files/students.json','w') as file:
        json.dump(json_data,file,indent=4)

def del_teacher(name_to_del):
     data = read_teacher()
     data = [entry for entry in data if entry.get('name')] != name_to_del
     with open('./my_package/json_files/teacher.json','w') as file:
        json.dump(data,file,indent=4)

def del_student(name_to_del):
     data = read_student()
     data = [entry for entry in data if entry.get('name')] != name_to_del
     with open('./my_package/json_files/students.json','w') as file:
        json.dump(data,file,indent=4)