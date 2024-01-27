import re

class soldier:
    def __init__(self,id,x,y,life=100):
        self.id = id
        self.life = life
        self.x = x
        self.y = y
    


n = int(input())


turn = [0]

arr = []
for i in range(n):
    arr.append([])
for i in range(n):
    for j in range(n):
        arr[i].append(None)

player1_dict = {}
player2_dict = {}

class archer(soldier):
    pass

class melee(soldier):
    pass


def winner():

    n = 0
    for sol_id in player1_dict.values():
        n += sol_id.life
    
    m = 0
    for sol_id in player2_dict.values():
        m += sol_id.life
    
    if m > n:
        print('player  2')
    elif n > m:
        print('player  1')
    else:
        print('draw')



def player1_turn():

    def move(id,direction):

        if direction == 'up':
            if player1_dict[id].y > 0:
                arr[player1_dict[id].y][player1_dict[id].x] == None
                arr[player1_dict[id].y-1][player1_dict[id].x] == player1_dict[id].id
                player1_dict[id].y -= 1
                turn.append(1)
            else :
                print('out of bounds')
        elif direction == 'down':
            if player1_dict[id].y < n:
                arr[player1_dict[id].y][player1_dict[id].x] == None
                arr[player1_dict[id].y+1][player1_dict[id].x] == player1_dict[id].id
                player1_dict[id].y += 1
                turn.append(1)
            else :
                print('out of bounds')
        elif direction == 'right':
            if player1_dict[id].x < n:
                arr[player1_dict[id].y][player1_dict[id].x] == None
                arr[player1_dict[id].y][player1_dict[id].x+1] == player1_dict[id].id
                player1_dict[id].x += 1
                turn.append(1)
            else :
                print('out of bounds')
        elif direction == 'left':
            if player1_dict[id].x > 0:
                arr[player1_dict[id].y][player1_dict[id].x] == None
                arr[player1_dict[id].y][player1_dict[id].x-1] == player1_dict[id].id
                player1_dict[id].x -= 1
                turn.append(1)
            else :
                print('out of bounds')

    
    def new_soldier(sol_type,sol_id,sol_x,sol_y):

        if sol_id not in player1_dict.keys():
            if sol_type == 'archer':
                player1_dict[sol_id] = archer(id = sol_id, x = sol_x, y = sol_y)
                arr[sol_y][sol_x] = sol_id

            elif sol_type == 'melee':
                player1_dict[sol_id] = melee(id = sol_id, x = sol_x, y = sol_y)
                arr[sol_y][sol_x] = sol_id
            
            turn.append(1)
        else:
            print('duplicate tag')


    def attack(attacker_id,target_id):
    
        if type(player1_dict[attacker_id]) == melee:

            d = ((player1_dict[attacker_id].x - player2_dict[target_id].x)**2 + (player1_dict[attacker_id].y - player2_dict[target_id].y)**2)**0.5

            if d <= 1:
                player2_dict[target_id].life -= 20
                turn.append(1)
            else:
                print('the target is too far')
        

        elif type(player1_dict[attacker_id]) == archer:

            d = ((player1_dict[attacker_id].x - player2_dict[target_id].x)**2 + (player1_dict[attacker_id].y - player2_dict[target_id].y)**2)**0.5

            if d <= 2:
                player2_dict[target_id].life -= 10
                turn.append(1)
            else:
                print('the target is too far')
        
        
        if player2_dict[target_id].life == 0:

            print('target eliminated')
            del player2_dict[target_id]


    def info(id):

        if id in player1_dict.keys():
            print(f'health:   {player1_dict[id].life}')
            print(f'location:   {player1_dict[id].x}   {player1_dict[id].y}')
            turn.append(1)

        else:
            print('soldier does not exist')
    

    command = input()

    if re.fullmatch(r'new .+ .+ .+ .+',command) !=  None:

        a = re.fullmatch(r'new (.+) (.+) (.+) (.+)',command)
        new_soldier(a.group(1),int(a.group(2)),int(a.group(3)),int(a.group(4)))

    
    elif re.fullmatch(r'move .+ .+',command) !=  None:

        a = re.fullmatch(r'move (.+) (.+)',command)
        move(int(a.group(1)),a.group(2))
            

    elif re.fullmatch(r'attack .+ .+',command) !=  None:

        a = re.fullmatch(r'attack (.+) (.+)',command)
        attack(int(a.group(1)),int(a.group(2)))


    elif re.fullmatch(r'info (.+)',command) !=  None:

        a = re.fullmatch(r'info (.+)',command)
        info(int(a.group(1)))


    elif re.fullmatch(r'who is in the lead\?',command) !=  None:

        winner()

    
    elif command == 'end':

        turn.append('end')



def player2_turn():

    def move(id,direction):

        if direction == 'up':
            if player2_dict[id].y > 0:
                arr[player2_dict[id].y][player2_dict[id].x] == None
                arr[player2_dict[id].y-1][player2_dict[id].x] == player2_dict[id].id
                player2_dict[id].y -= 1
                turn.append(0)
            else :
                print('out of bounds')
        elif direction == 'down':
            if player2_dict[id].y < n:
                arr[player2_dict[id].y][player2_dict[id].x] == None
                arr[player2_dict[id].y+1][player2_dict[id].x] == player2_dict[id].id
                player2_dict[id].y += 1
                turn.append(0)
            else :
                print('out of bounds')
        elif direction == 'right':
            if player2_dict[id].x < n:
                arr[player2_dict[id].y][player2_dict[id].x] == None
                arr[player2_dict[id].y][player2_dict[id].x+1] == player2_dict[id].id
                player2_dict[id].x += 1
                turn.append(0)
            else :
                print('out of bounds')
        elif direction == 'left':
            if player2_dict[id].x > 0:
                arr[player2_dict[id].y][player2_dict[id].x] == None
                arr[player2_dict[id].y][player2_dict[id].x-1] == player2_dict[id].id
                player2_dict[id].x -= 1
                turn.append(0)
            else :
                print('out of bounds')

    
    def new_soldier(sol_type,sol_id,sol_x,sol_y):

        if sol_id not in player2_dict.keys():
            if sol_type == 'archer':
                player2_dict[sol_id] = archer(id = sol_id, x = sol_x, y = sol_y)
                arr[sol_y][sol_x] = sol_id

            elif sol_type == 'melee':
                player2_dict[sol_id] = melee(id = sol_id, x = sol_x, y = sol_y)
                arr[sol_y][sol_x] = sol_id
            
            turn.append(0)
        else:
            print('duplicate tag')


    def attack(attacker_id,target_id):
    
        if type(player2_dict[attacker_id]) == melee:

            d = ((player2_dict[attacker_id].x - player1_dict[target_id].x)**2 + (player2_dict[attacker_id].y - player1_dict[target_id].y)**2)**0.5

            if d <= 1:
                player1_dict[target_id].life -= 20
                turn.append(0)
            else:
                print('the target is too far')
        

        elif type(player2_dict[attacker_id]) == archer:

            d = ((player2_dict[attacker_id].x - player1_dict[target_id].x)**2 + (player2_dict[attacker_id].y - player1_dict[target_id].y)**2)**0.5

            if d <= 2:
                player1_dict[target_id].life -= 10
                turn.append(0)
            else:
                print('the target is too far')
        
        
        if player1_dict[target_id].life == 0:

            print('target eliminated')
            del player1_dict[target_id]


    def info(id):

        if id in player2_dict.keys():
            print(f'health:   {player2_dict[id].life}')
            print(f'location:   {player2_dict[id].x}   {player2_dict[id].y}')
            turn.append(0)

        else:
            print('soldier does not exist')
    

    command = input()

    if re.fullmatch(r'new .+ .+ .+ .+',command) !=  None:

        a = re.fullmatch(r'new (.+) (.+) (.+) (.+)',command)
        new_soldier(a.group(1),int(a.group(2)),int(a.group(3)),int(a.group(4)))

    
    elif re.fullmatch(r'move .+ .+',command) !=  None:

        a = re.fullmatch(r'move (.+) (.+)',command)
        move(int(a.group(1)),a.group(2))
            

    elif re.fullmatch(r'attack .+ .+',command) !=  None:

        a = re.fullmatch(r'attack (.+) (.+)',command)
        attack(int(a.group(1)),int(a.group(2)))


    elif re.fullmatch(r'info (.+)',command) !=  None:

        a = re.fullmatch(r'info (.+)',command)
        info(int(a.group(1)))


    elif re.fullmatch(r'who is in the lead\?',command) !=  None:

        winner()

    
    elif command == 'end':

        turn.append('end')


while turn[len(turn)-1] != 'end':

   
    if turn[len(turn)-1] == 0:

        player1_turn()

    elif turn[len(turn)-1] == 1:

        player2_turn()
