"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Hamda
Delivery Date : 22/06/2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
import uuid
class Course:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.course_id = str(uuid.uuid4())



class Student:
    # TODO 3 define static variable indicates total student count
    total_student_count = 0
    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, name, age, number):
        self.student_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.number = number
        self.course_list = []
        self.marks = []
        self.std_sum = 0
        Student.total_student_count += 1

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self):
        course = Course()
        course.name = input("Enter course name:")
        course.mark = input("Enter course mark:")
        self.course_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        print("student courses with their marks")

    # method to get student_average as a value
    def get_student_average(self):
        if not self.marks:
            print("There are no marks for this student")
            return 0
        self.std_sum += 1
        marks_sum = sum(self.marks)
        std_avg = self.std_sum / len(self.marks)
        return std_avg

        # TODO 7 return the student average



# in Global Scope
# TODO 8 declare empty students list
student_list = []
i = 1
while i != 6:
    if i == 1 :
    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit\n"
                          "Enter your option:" ))


    if i == 6:
        break
        i += 1


        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 11 create student object and append it to students list
        student = Student(student_name, student_age, student_number)

        student_list.append(student)
        print("Student Added Successfully")




    elif selection == 2:
        student_number = input("Enter Student Number")
        find_std = False
        for student in student_list:
            if student.number == student_number:
                student_list.remove(student)
                find_std = True
                break
        if find_std :
            print("student Not Exist")

        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        find_std = False
        for student in student_list:
            if student.number == student_number:
                print("The Student's name is :", student.name)
                print("The Student's age is:", student.age)
                print("The Student's number is:", student.number)
                find_std = True
                break
        if find_std :
            print("student Not Exist")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        find_std = False
        for student in student_list:
            if student.number == student_number:
                student.get_student_average()
                find_std = True
                break
        if find_std :
            print("student Not Exist")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        course_name = input("Enter course name: ")
        course_mark = input("Enter course mark: ")
        course = Course(course_name, course_mark)
        for student in student_list:
            student.course_list.append(course)
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses


    else:
     import sys
     def exit_program():
         print("Exist")
         sys.exit(0)



        # TODO 16 call a function to exit the program



