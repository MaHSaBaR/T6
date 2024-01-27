import re

class Soldier:
    def __init__(self, id, x, y, life=100):
        self.id = id
        self.life = life
        self.x = x
        self.y = y

class Archer(Soldier):
    pass

class Melee(Soldier):
    pass

def initialize_game(n):
    arr = [[None for _ in range(n)] for _ in range(n)]
    return arr, {}, {}

def move_soldier(player_dict, arr, id, direction):
    # Implement move functionality
    pass

def new_soldier(player_dict, arr, sol_type, sol_id, sol_x, sol_y):
    # Implement new soldier functionality
    pass

def attack_target(attacker_dict, target_dict, attacker_id, target_id):
    # Implement attack functionality
    pass

def display_soldier_info(player_dict, id):
    # Implement display soldier info functionality
    pass

def who_is_in_the_lead(player1_dict, player2_dict):
    # Implement winner functionality
    pass

def player_turn(player_dict, arr, player_id):
    # Implement player turn functionality
    pass

n = int(input())
arr, player1_dict, player2_dict = initialize_game(n)

turn = [0]

while turn[-1] != 'end':
    if turn[-1] == 0:
        player_turn(player1_dict, arr, 0)
    elif turn[-1] == 1:
        player_turn(player2_dict, arr, 1)
