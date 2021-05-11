# handle_turn
# current player
# relation

import random
name = input('Enter your name: ')
player = input(f'rock(R),paper(P),sissor(S)\nchoose one {name}: ')

# gamer turn 
ranNo = random.randint(1, 3)

if ranNo == 1:
    gamer = "R"
if ranNo == 2:
    gamer = "P"
if ranNo == 3:
    gamer = "S"
print(gamer)   
A = True
# gamer turn ^^

def handle_turn(gamer, player):
    if gamer == player:
        return None
    if gamer == "R":
        if player == "P":
            return True
        elif player == "S":
            return False
    if gamer == "S":
        if player == "R":
            return True
        elif player == "P":
            return False
    if gamer == "P":
        if player == "R":
            return False
        elif player == "S":
            return True
 


turn = handle_turn(gamer,player)
if turn == None:
    print("tie")
if turn == True:
    print(f"BOOYAH!!!\nplayer -->> {name} won")
if turn == False:
    print('gamer won the game')