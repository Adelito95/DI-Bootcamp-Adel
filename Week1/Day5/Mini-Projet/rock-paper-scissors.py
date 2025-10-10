from game import Game

def get_user_menu_choice() :
    user = input("Menu :\n (g) Play a new game : \n (x) Show score and exit : \n")    
    return user
    
def print_results(results) :
    print(f"Game result :\nYon win : {results["win"]} times\nYou lost : {results["loss"]} times\nYou draw : {results["draw"]} times\n\n \
Thank you for playing !!!")

def main() :
    win_count = 0
    loss_count = 0
    draw_count = 0
    while True :
        user_choice = get_user_menu_choice()
        if user_choice == "g":
            game = Game()
            resu = game.play()
            if resu == "win" :
                win_count += 1
            elif resu == "loss" :
                loss_count += 1
            elif resu == "draw" :
                draw_count += 1
        elif user_choice == "x":
            results = {"win": win_count,"loss":loss_count,"draw": draw_count }
            return print_results(results)

if __name__ == "__main__":
    main()
                           
                

                
# play = Play()   
# print(play.get_user_menu_choice())
# self.user_item = user_item 
#         self.computer_item = computer_item 
#         win_count = 0
#         loose_count = 0
#         drew_count = 0
#         if self.user_item == self.computer_item :
#             drew_count += 1
#             return f"you choose : {self.user_item}, the computer chose : {self.computer_item}, result : draw"
#         elif self.user_item != self.computer_item :
#             if (self.user_item == "r" and self.computer_item == "s") or (self.user_item == "p" and self.computer_item == "r") or (user_item == "s" and self.computer_item == "p"):
#                  win_count += 1
#                  return f"you choose : {self.user_item}, the computer chose : {self.computer_item}, result : win" 
#             else :
#                 loose_count += 1
#                 return f"you choose : {self.user_item}, the computer chose : {self.computer_item}, result : loose" 


    # 
    #   if user not in new_game :
    #         print ("Enter one of requested letter please !!!")
    #     else :