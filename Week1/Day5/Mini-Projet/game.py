import random# Escalier
# Partie I - game.py
user_number = 0
totaly = 0
quit = "q"
win_count = 0
loose_count = 0
class Game() :
    def get_computer_item() :
        
        while True :
            choice = "rps"
            user_machine = random.choices(choice) 
            print (user_machine)
            user =(input("Menu :\n (g) Play a new game : \n (x) Show score and exit : "))
            if user != "g" and user != "x":
                print("bye")
                # user =(input("Menu :\n (g) Play a new game : \n (x) Show score and exit : "))
            elif user == "g" :
                print (f"Select (r)ock ,(p)aper, or (s)cissor : ")
Game.get_computer_item ()   
    # else : 
    #     user_number = int(user_number)
    #     if user_number == Number and user_number != quit  :
    #         print (" ➞  Winner !!!!")
    #         print()
    #         win_count +=1
    #         totaly += 1
    #     elif user_number != Number and user_number != quit  :
    #         print (" ➞  Better luck next time !!!!")
    #         print ()
    #         loose_count += 1
    #         totaly += 1

        