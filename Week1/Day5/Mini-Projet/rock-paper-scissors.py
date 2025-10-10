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