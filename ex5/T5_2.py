import re

class Course:
    def __init__(self, name, course_id, capacity, total_students=0):
        self.name = name
        self.course_id = course_id
        self.capacity = capacity
        self.total_students = total_students

    def course_change(self):
        if self.total_students < int(self.capacity):
            self.total_students += 1
            print('Course added successfully!')
        else:
            print('Course is full')

def course_display(course_dict):
    print('Course list:')
    for course_id, course_obj in course_dict.items():
        print('{} {} {}/{}'.format(course_obj.course_id, course_obj.name,
                                    course_obj.total_students, course_obj.capacity))

class User:
    def __init__(self, name, user_id, password, taken_courses=[]):
        self.name = name
        self.id = user_id
        self.password = password
        self.taken_courses = taken_courses

    def get_course(self, course_id, course_dict):
        if course_id in course_dict.keys():
            if course_id not in self.taken_courses:
                self.taken_courses.append(course_id)
                course_dict[course_id].course_change()
            else:
                print('You already have this course')
        else:
            print('Incorrect course ID')

def sign_up(user_type, user_id, name, user_password, user_dict):
    # Similar implementation for sign-up with validation
    # ...

def log_in(user_id, user_password, user_dict):
    # Similar implementation for login with validation
    # ...

def professor_menu(command, course_dict):
    # Implementation for professor menu commands
    # ...

def student_menu(command, user_id, student_dict, course_dict):
    # Implementation for student menu commands
    # ...

course_dict = {}
student_dict = {}
professor_dict = {}

menu = 'log in/sign up menu'

command = input().strip()

while command != 'edu exit edu':
    # Main loop logic with improved command processing and function calls
    # ...

# Remaining code...
