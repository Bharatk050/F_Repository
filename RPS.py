<<<<<<< HEAD
import random
name = input('Enter your name: ')

=======
# handle_turn
# current player
# relation

from ast import Break
import random
name = input('Enter your name: ')

print("Disclaimer:\t Play until you win")

>>>>>>> ce35c7939a2a59f9a8d1f7b570906d8a56c7b212

while True:

    player = input(f'rock(R),paper(P),sissor(S)\nchoose one {name}: ')

    ranNo = random.randint(1, 3)

    if ranNo == 1:
        gamer = "R"
    if ranNo == 2:
        gamer = "P"
    if ranNo == 3:
        gamer = "S"


    if player not in ['R', 'S', 'P']:
        print("Invalid!!")

    # gamer turn 
    def handle_turn():
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

    turn = handle_turn()

    if turn == None:
        print("tie")
        print(gamer)
    if turn == True:
        print(f"BOOYAH!!!\nplayer -->> {name} won")
        print(gamer)
        break
    if turn == False:
        print('Computer won the game')
        print(gamer)
