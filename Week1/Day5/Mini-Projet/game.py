import random
# Partie I - game.py
class Game() :

    def __init__(self):
       pass
        
    def get_user_item(self) :

        while True :
            choice = "rps"
            user = input("Select (r)ock ,(p)aper, or (s)cissor : ")
            if user not in choice :
                print ("Enter one of requested letter please !!!")
            else : 
                return user
    
    def get_computer_item(self) :

        choice = "rps"
        user_machine = random.choice(choice) 
        return user_machine
        
    def get_game_result(self, user_item, computer_item) :
        self.user_item = user_item 
        self.computer_item = computer_item 
        if self.user_item == self.computer_item :
            return "draw"
        elif self.user_item != self.computer_item :
            if (self.user_item == "r" and self.computer_item == "s") or (self.user_item == "p" and self.computer_item == "r") or (user_item == "s" and self.computer_item == "p"):
                return "win"
            else :
                return "loss"
            
    def play(self) :
        user = self.get_user_item()
        computer = self.get_computer_item()
        if user == computer :
            print(f"You selected {user}. The computer selected {computer} You draw")
            return "draw"
        elif user != computer :
            if (user == "r" and computer == "s") or (user== "p" and computer == "r") or (user== "s" and computer == "p"):
                print(f"You selected {user}. The computer selected {computer} You win")
                return "win"
            else :
                print(f"You selected {user}. The computer selected {computer} You lost")
                return "loss"

                      
# game = Game()
# user = game.get_user_item()  
# computeur = game.get_computer_item()
# result = game.get_game_result(user,computeur)
# print (result)
# result1 = play
# print(result1)

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

        