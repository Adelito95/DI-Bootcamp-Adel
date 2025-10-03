"""
Exercise 2 : cat's and dog's years

Instructions : Write a program that will calculate cat’s and dog’s years based on human years:

I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago.
Print their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1 humanYears are whole numbers only

Cat Years 15 cat years for first year +9 cat years for second year +4 cat years for each year after that

Dog Years 15 dog years for first year +9 dog years for second year +5 dog years for each year after that

example of output:

human_years = 10
#output: [10, 56, 64]

human_years = 1
#output: [1, 15, 15]

human_years = 2
#output [2, 24, 24]


test the program with the following values:

human_years = 10
human_years = 1
human_years = 2  

"""
Categories = []
Cat_Years = 0
dog_Years = 0

human_Years = int(input("Enter a positive number OR press 0 to exit: "))

while True :
    if human_Years < 0 :
        human_Years = int(input("Try again with a positive number OR press 0 to exit : "))
    elif human_Years == 1:
        Cat_Years = 15
        dog_Years = 15
        Categories.append (human_Years)
        Categories.append (Cat_Years)
        Categories.append (dog_Years)
        print (Categories)
        Categories = []
        human_Years = int(input("Enter a positive number OR press 0 to exit : "))
    elif human_Years ==2:
        Cat_Years = 24
        dog_Years = 24
        Categories.append (human_Years)
        Categories.append (Cat_Years)
        Categories.append (dog_Years)
        print (Categories)
        Categories = []
        human_Years = int(input("Enter a positive number OR press 0 to exit : "))
    elif human_Years > 2 :
        Cat_Years = (24 +(human_Years-2)*4)
        dog_Years = (24 + (human_Years-2)*5)
        Categories.append (human_Years)
        Categories.append (Cat_Years)
        Categories.append (dog_Years)
        print (Categories)
        Categories = []
        human_Years = int(input("Enter a positive number OR press 0 to exit : "))
    elif  human_Years == 0 :
         print ("Thank you for your participation, Bye !!!! ")
         break

    
