name = input("Enter your name: ")

class Score:
    score = 0
    def Runs(self):
        game_is_still_on = True
        score = 0
        while game_is_still_on:
            import random
            list = [1, 2, 3, 4, 6]
            ranNo = random.choice(list)
            if ranNo == 1:
                bharat = 1
            if ranNo == 2:  
                bharat = 2
            if ranNo == 3:
                bharat = 3
            if ranNo == 4:
                bharat = 4
            if ranNo == 6:
                bharat = 6
            # print(bharat)
            ask = int(input("Score your runs carefully: "))
            if bharat == ask:
                game_is_still_on = False
                print(f"One wicket down \n player - {name} \n Score - {score}")

            if bharat != ask:
                score += ask
                print(f"player - {name}\nScore - {score}")
            
            if ask > 6 or ask < 1:
                game_is_still_on = False
                score = 0
                print(f"player - {name}\n Score - {score}")
                print("your score became zero due to invalidity")

            if ask == 5 :
                print("This is not valid score")
                score -= 5

        return score
f = Score()
a = f.Runs()
print(a)