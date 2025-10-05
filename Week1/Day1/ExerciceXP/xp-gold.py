# Exercise 1: What is the Season?

# Ask the user to input a month (1 to 12).
# Display the season of the month received:
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
month_list = [(1,"January"),(2,"February"),(3,"March"),(4,"April"),(5,"May"),(6,"June"),(7,"July"),(8,"August"),\
                  (9,"September"),(10,"October"),(11,"November"),(12,"December")]
Winter = [12,1,2]
Spring = [3,4,5]
Summer = [6,7,8]
Autumn = [9,10,11]
list_string_month = ["1","2","3","4","5","6","7","8","9","10","11","12"]
quit = "q"
while True :
    chosen_month = (input("Tape a number between 1 and 12 if you want to know his season or press q to exit : "))
    if chosen_month not in list_string_month and chosen_month != quit:
        print ("Choise a number between 1 and 12 or press q to exit : ")
    elif chosen_month == quit :
        break
    else : 
        chosen_month = int(chosen_month)
        if chosen_month < 1 or chosen_month > 12:
            print ("Choise a number between 1 and 12 or press q to exit : ")
        elif chosen_month in range(1,13) :
            for a,b in month_list :
                if a == chosen_month :
                    if chosen_month in Winter :
                        print(f"You have choose {b} and it's in Winter season " )
                    
                    elif chosen_month in Spring :
                        print(f"You have choose {b} and it's in Spring season " )
                    
                    elif chosen_month in Summer :
                        print(f"You have choose {b} and it's in Summer season " )
                    
                    elif chosen_month in Autumn :
                        print(f"You have choose {b} and it's in Autumn season ")

# Exercise 2: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a loop to print all numbers from 1 to 20, inclusive. for
# Write another loop that prints every number from 1 to 20 where the index is even. for

for nombre in range (1,21) :
    print (nombre)
print()
for nombre in range (1,21) :
    if nombre%2 == 0 :
        print (nombre)

# Exercise 3: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Write a loop that keeps asking the user to enter their name. while
# Stop the loop if the user’s input is your name.
my_name = "adel" # Déclaration du nom cible

while True :
    user_name= input("What is your name ? : ") # asking the user to enter their name.
    user_name = user_name.lower() # convert to lowercase to make it not case sensitive
    if user_name == my_name : # condition of validation
        break # validation ok, exit of the loop

# Exercise 4: Check the index
# Using this variable:

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their , if their name is in the names list print out the index of the first occurrence of the name.name

# Example: if input is we should be printing the index 1Cortana
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name= input("What is your name ? : ") # asking the user to enter their name.
user_name = user_name.capitalize()
if user_name in names :
    for first_occurence in names :
        if first_occurence == user_name :
            index = names.index(user_name)
    print(f"The Index of your name in my names list is {index}")
else :
    print("Your name is not in my names list")

# Exercise 5: Greatest Number
# Ask the user for 3 numbers and print the greatest number.

# Test Data:

# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87
user_first_number = input("Input the 1st number: ") # asking the user to enter a 1st number.
user_second_number = input("Input the 2nd number: ") # asking the user to enter a 2nd number.
user_third_number = input("Input the 3rd number: ") # asking the user to enter a 3rd number.
list = [user_first_number, user_second_number,user_third_number] # Create a list of the 3 given numbers
greatest_number = max(list) # Puting the greatest number on a variable 
print (f"The greatest number is {greatest_number}" ) # Printing the result

# Exercise 6: Random number
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says “Winner”.
# If the user guesses the wrong number print a message that says “Better luck next time.”
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost. 


import random #Import de la librairie nécessaire
list_string_number = ["1","2","3","4","5","6","7","8","9"]
user_number = 0
totaly = 0
quit = "q"
win_count = 0
loose_count = 0

while True :
    Number = random.randint(1, 9) # Assignation de la valeur aléatoire à la variable
    # print (Number) 
    user_number =(input("Enter a number between 1 and 9 or press q to quit : "))
    
    if user_number not in list_string_number and user_number != quit:
        print ("Enter a number between 1 and 9 or press q to exit : ")
    elif user_number == quit :
        print (f"Score : Total : {totaly}, win : {win_count}, loose : {loose_count}")
        print ("See you soon !!! ")
        break
    else : 
        user_number = int(user_number)
        if user_number == Number and user_number != quit  :
            print (" ➞  Winner !!!!")
            print()
            win_count +=1
            totaly += 1
        elif user_number != Number and user_number != quit  :
            print (" ➞  Better luck next time !!!!")
            print ()
            loose_count += 1
            totaly += 1
