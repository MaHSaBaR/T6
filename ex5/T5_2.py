import re

student_dict = {}
professor_dict = {}
course_dict = {}
menu = 'log in/sign up menu'

class course:
    def __init__(self,name,course_id,capacity,total_students=0):
        self.name = name
        self.course_id = course_id
        self.capacity = capacity
        self.total_students = total_students
    
    
    def course_change(self):
        if self.total_students < int(self.capacity):
            self.total_students += 1
            print('course added successfully!')
        else:
            print('course is full')

def course_display():
    print('course list:')
    for x in course_dict.values():   
        print('{} {} {}/{}'.format(x.course_id,x.name,x.total_students ,x.capacity))



class user:
    def __init__(self,name,id,password,taken_courses=[]):
        self.name = name
        self.id = id
        self.password = password
        self.taken_courses = taken_courses
    
    def get_course(self,course_id):
        if course_id in course_dict.keys():
            if course_id not in self.taken_courses:
                self.taken_courses.append(course_id)
                course_dict[course_id].course_change()
  
            else:
                print('you already have this course')
                return -1
        else:
            print('incorrect course id')
            return -1
    



def add_course(course_name,id,course_capacity):
    
    if re.findall(r' ',course_name) == []:
        if re.fullmatch(r'\d+',id) != None:
            if re.fullmatch(r'\d+',course_capacity) != None:
                if id not in course_dict.keys():

                    course_dict[id] = course(name=course_name,course_id=id,capacity=course_capacity)
                    print('course added successfully!')

                else:
                    print('course id already exists')
            else:
                print('invalid course capacity')
        else:
            print('invalid course id')
    else:
        print('invalid course name')






def sign_up(type,id,name,u_password):
    if type == 'S' or type == 'P':

        if re.fullmatch(r'\d+', id) != None:

            if re.findall(r' ',name) == []:

                if len(u_password) > 3 and re.findall(r'[*.!@$%^&()]',u_password) != [] and re.findall(r' ',u_password) == []:
    
                    if type == 'S':

                        if id not in student_dict.keys() and id not in professor_dict.keys():

                            student_dict[id] = user(name,id,u_password,taken_courses=[])
                            print('signed up successfully!')

                        else:
                            print('id already exists')
                    
                    elif type == 'P':

                        if id not in professor_dict.keys() and id not in student_dict.keys():

                            professor_dict[id] = user(name,id,u_password,taken_courses=[])    
                            print('signed up successfully!')

                        else:
                            print('id already exists')
    
            
                else:
                    print('invalid password')
            else:
                print('invalid name')
        else:
            print('invalid id')
    else:
        print('invalid type')

                
def log_in(id,u_password):


    if id in student_dict.keys():

        if student_dict[id].password == u_password:
                
            print('logged in successfully!\nentered student menu')
            menu = 'student menu'
            
        else:
            menu = 'log in/sign up menu'
            print('incorrect password')
    
    elif id in professor_dict.keys():

        if professor_dict[id].password == u_password:

            print('logged in successfully!\nentered professor menu')
            menu = 'professor menu' 
            
        else:
            menu = 'log in/sign up menu'
            print('incorrect password')

    else:
        menu = 'log in/sign up menu'
        print('incorrect id')

    return menu


   


    


    



command = input().strip()

while command != 'edu exit edu':

    if re.fullmatch(r'edu sign up -.+ -i .+ -n .+ -p .+ edu',command) != None:

        a = re.fullmatch(r'edu sign up -(.+) -i (.+) -n (.+) -p (.+) edu',command)
        sign_up(a.group(1),a.group(2),a.group(3),a.group(4))

        command = input().strip()



    elif re.fullmatch(r'edu log in -i .+ -p .+ edu',command) != None:

        a = re.fullmatch(r'edu log in -i (.+) -p (.+) edu',command)
        menu = log_in(a.group(1),a.group(2))

        if menu != 'log in/sign up menu':

            command = input().strip()
            while command != 'edu log out edu':

                if re.fullmatch(r'edu show course list edu',command) != None:
                    course_display()
                    command = input().strip()


                elif re.fullmatch(r'edu add course -c .+ -i .+ -n .+ edu',command) != None and menu == 'professor menu':

                    b = re.fullmatch(r'edu add course -c (.+) -i (.+) -n (.+) edu',command)
                    add_course(b.group(1),b.group(2),b.group(3))
                    command = input().strip()


                elif re.fullmatch(r'edu get course -i .+ edu',command) != None and menu == 'student menu':

                    b = re.fullmatch(r'edu get course -i (.+) edu',command)
                    student_dict[a.group(1)].get_course(b.group(1))
                    command = input().strip()

    
            
                elif re.fullmatch(r'edu current menu edu',command) != None:
                
                    print(menu)
                    command = input().strip()

                else:
                    print('invalid command')
                    command = input().strip()
                

            print('logged out successfully!\nentered log in/sign up menu')
            menu = 'log in/sign up menu'

            command = input().strip()

        else:
            command = input().strip()
    
    elif re.fullmatch(r'edu current menu edu',command) != None:
        print(menu)
        command = input().strip()

    else:
        print('invalid command')
        command = input().strip()

    