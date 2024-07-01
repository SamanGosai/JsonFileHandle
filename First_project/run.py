import my_package as mp

def teacher_entry():
      select = int(input("Enter 1:add teacher,2:add student,3:display teacher,4:display student,5:delete teacher,6:delete student,7:search teacher,8:search student"))
      t1 = mp.TeacherClass()
      s1 = mp.StudentClass()
      if select == 1:
         t1.accept_info()
      elif select == 2:
         s1.accept_info()
      elif select == 3:
         t1.display_all()
      elif select == 4:
         s1.display_all()
      elif select == 5:
         t1.delete(input("Enter teachers name to delete"))
      elif select == 6:
         s1.delete(input("Enter students name to delete"))
      elif select == 7:
         name_to_search = input("Enter name of teacher to search")
         t1.search(name_to_search)
      elif select == 8:
         name_to_search = input("Enter name of students to search")
         s1.search(name_to_search)
      else:
         print("Invalid Input")
         teacher_entry()

def student_entry():
   s1 = mp.StudentClass()
   name = input("Enter your name: ")
   if mp.validate_student(name):
      select = int(input("Enter 1:display,2:check pass or fail,3:check percentage"))
      if select == 1:
         opt = int(input("Display all or yours;Enter 1 to display all"))
         if opt == 1:
            s1.display_all()
         else:
            s1.search(name)
      elif select == 2:
         print(f"You are {s1.pass_fail_determination(name)}")
      elif select == 3:
         print(f"You're percentage is {s1.percentage(name)}")
      else:
         print("Invalid Input")
   else:
      print("You are not verified!!!")
print("Are you a teacher or a student")
choices = int(input("Enter 1:teacher 2:student: "))
if choices == 1:
   name = input("Enter your name: ")
   id = int(input("Enter your id: "))
   if mp.validate_teacher(name,id):
      print("You Are Verified!!!")
      teacher_entry()
   else:
      print("Sorry you are not verified!!")
elif choices == 2:
   student_entry()