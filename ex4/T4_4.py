class Patient:
    def __init__(self, id, name, familyname, age, height, weight, btime):
        self.id = id
        self.name = name
        self.familyname = familyname
        self.age = age
        self.height = height
        self.weight = weight
        self.btime = btime

def is_valid_positive_int(value):
    return value.isdigit() and int(value) > 0

def is_valid_age(value):
    return is_valid_positive_int(value) or value.lower() == 'unknown'

def is_valid_time(value):
    return value.isdigit() and 9 <= int(value) <= 18

def is_valid_weight_height(value):
    return is_valid_positive_int(value) or value.lower() == 'unknown'

def add_patient(patient_id, patient_name, patient_familyname, patient_age, patient_height, patient_weight):
    if patient_id in patients:
        print('Error: This ID already exists')
    elif not is_valid_age(patient_age):
        print('Error: Invalid age')
    elif not is_valid_weight_height(patient_height):
        print('Error: Invalid height')
    elif not is_valid_weight_height(patient_weight):
        print('Error: Invalid weight')
    else:
        patients[patient_id] = Patient(patient_id, patient_name, patient_familyname, patient_age, patient_height,
                                      patient_weight, 0)
        print('Patient added successfully')

def display_patient(patient_id):
    try:
        patients[patient_id].display_patient()
    except KeyError:
        print('Error: Invalid ID')

def add_visit(patient_id, visit_time):
    try:
        patient = patients[patient_id]
        if not is_valid_time(visit_time):
            print('Error: Invalid time')
        elif int(visit_time) in busy_times:
            print('Error: Busy time')
        else:
            print('Visit added successfully!')
            busy_times.append(int(visit_time))
            visit_list.append('{}:00 {} {}'.format(visit_time, patient.name, patient.familyname))
            visit_dict['{}:00 {} {}'.format(visit_time, patient.name, patient.familyname)] = patient.id
    except KeyError:
        print('Error: Invalid ID')

def delete_patient(patient_id):
    try:
        patient = patients[patient_id]
        for visit in visit_list:
            if visit_dict[visit] == patient_id:
                del visit_dict[visit]
        if patient.btime in busy_times:
            busy_times.remove(patient.btime)
        del patients[patient_id]
        print('Patient deleted successfully!')
    except KeyError:
        print('Error: Invalid ID')


def display_visits():
    print('SCHEDULE:')
    for visit in list(visit_dict.keys()):
        print(visit)


def is_valid_command(command):
    return len(command) > 0

patients = {}
busy_times = []
visit_list = []
visit_dict = {}

data = list(filter(None, input().split(' ')))
while not is_valid_command(data):
    print('Invalid command')
    data = list(filter(None, input().split(' ')))

while data != ['exit']:
    command = data[0]
    if command == 'add':
        if data[1] == 'patient':
            add_patient(data[2], data[3], data[4], data[5], data[6], data[7])
        elif data[1] == 'visit':
            add_visit(data[2], data[3])

    elif command == 'display':
        if data[1] == 'patient':
            display_patient(data[2])
        elif data[1] == 'visit':
            display_visits()

    elif command == 'delete':
        delete_patient(data[2])

    else:
        print('Invalid command')

    data = list(filter(None, input().split(' ')))
    while not is_valid_command(data):
        print('Invalid command')
        data = list(filter(None, input().split(' ')))
