id_dict = dict()
time_list = []
visit_list=[]
visit_dict = {}
class patient:
    def __init__(self,id, name, familyname, age, height, weight,btime):
        self.id = id
        self.name = name
        self.familyname = familyname
        self.age = age
        self.height = height
        self.weight = weight
        self.btime = btime

    def add_patient(self):
        if str(self.id) in id_dict.keys():
            print('error: this ID already exists')
        else:
            if int(self.age) < 0 :
                print('error: invalid age')
            else:
                if int(self.height) < 0 :
                    print('error: invalid height')
                else:
                    if int(self.weight) < 0 :
                        print('error: invalid weight')
                    else:
                        id_dict[str(self.id)] = self
                        print('patient added successfully')
    
    def display_patient(self):
        print('patient name:',self.name)
        print('patient family name:',self.familyname)
        print('patient age:',self.age)
        print('patient height:',self.height)
        print('patient weight:',self.weight)
    
    def add_visit(self):
        if int(self.btime) in time_list:
            print('error: busy time')
        else:
            if int(self.btime) < 9 or int(self.btime) > 18:
                print('error: invalid time')
            else:
                print('visit added successfully!')
                time_list.append(int(self.btime))
                visit_list.append('{}:00 {} {}'.format(self.btime,self.name,self.familyname))
                visit_dict['{}:00 {} {}'.format(self.btime,self.name,self.familyname)] = self.id
    
    def delete_patient(self):
        for x in visit_list:
            try:
                if visit_dict[x] == self.id:
                    del visit_dict[x]
            except KeyError:
                pass
        if self.btime in time_list:
            time_list.remove(self.btime)
        del id_dict[str(self.id)]
        print('patient deleted successfully!')
    

            


data = list(filter(None,input().split(' ')))
while len(data) == 0:
    print('invalid command')
    data = list(filter(None,input().split(' ')))

while data != ['exit']:
    if data[0]== 'add' and data[1]== 'patient':
        p = patient(id=data[2],name=data[3],familyname=data[4],age=data[5],height=data[6],weight=data[7],btime=0)
        p.add_patient()
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))

        



    elif data[0]== 'display' and data[1]== 'patient':
        try:
            id_dict[data[2]].display_patient()
        except KeyError:
            print('error: invalid ID')
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))

    
    elif data[0]== 'add' and data[1]== 'visit':
        try:
            id_dict[data[2]].btime = data[3]
            id_dict[data[2]].add_visit()
        except KeyError:
            print('error: invalid id')
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))

    
    elif data[0]== 'delete':
        try:
            id_dict[data[2]].delete_patient()
        except KeyError:
            print('error: invalid id')
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))

    
    elif data[0]=='display' and data[1]=='visit':
        print('SCHEDULE:')
        for x in list(visit_dict.keys()):
            print(x)
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))

    
    else:
        print('invalid command')
        data = list(filter(None,input().split(' ')))
        while len(data) == 0:
            print('invalid command')
            data = list(filter(None,input().split(' ')))


