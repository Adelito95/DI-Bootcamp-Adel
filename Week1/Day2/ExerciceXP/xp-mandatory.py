# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions

# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.



# Lists:
# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dico = dict(zip(keys, values)) 
print(dico)


# Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
for k,v in family.items() :
    if v > 12 :
        price += 15
    elif v >3 and v < 12 :
        price += 10
print (price)

# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family_name_list = []
family_age_list = []
price = 0
dico_price = {}
print("Enter your family's name and age and press q when you finished : ")
while True :
    family_name = (input("Enter the name : "))
    family_name_list.append(family_name)
    family_age = int(input("Enter the age : "))
    family_age_list.append(family_age)
    is_it_finished = input("To continue presse c, to finish press q : ")
    if is_it_finished == "c" :
        continue
    if is_it_finished == "q" :
        dico_price = dict(zip(family_name_list, family_age_list))
        for k,v in dico_price.items() :
            if v > 12 :
                price += 15
            elif v >3 and v < 12 :
                price += 10
        print (f"You have to paie ${price}")
        break 

# Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions

# Create and manipulate a dictionary that contains information about the Zara brand.



# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ("men", "women", "children", "home"),
"international_competitors": ("Gap", "H&M", "Benetton"),
"number_stores": 7000,
"major_color":{
    "France": "blue", 
    "Spain": "red", 
    "US": ("pink", "green")
}
    }
brand["number_stores"] = 2
for k, v in brand.items() :
    if k == "type_of_clothes" :
        print(f"{brand["name"]}'s client are {v[0]}, {v[1]} and also {v[2]} !")
brand["country_creation"] = "Spain"
if "international_competitors" in brand :
    brand["international_competitors"] +=  ("Desigual",)
del brand["creation_date"]
print (brand["international_competitors"][-1])
print (brand["major_color"]["US"])
print(len(brand.keys()))
print(brand.keys())

# Bonus:

# Create another dictionary called with more_on_zaracreation_datenumber_storesbrand 
# and Merge this dictionary with the original dictionary 
# and print the result.
    
more_on_zaracreation_datenumber_storesbrand = {"average_monthly_salary": 1790,
"headquarters": "Arteixo",
"country": "Spain",
"type_of_clothes": ("men", "women", "children", "home"),
"workforce_in 2018" : 171839,
}

brand_merged_solution1 = brand|(more_on_zaracreation_datenumber_storesbrand)
brand_merged_solution2 = {**brand,**more_on_zaracreation_datenumber_storesbrand}
print(brand_merged_solution1)
print(brand_merged_solution2) 

#  Exercise 4 : Some Geography
# Goal: Create a function that describes a city and its country.

# Key Python Topics:

# Functions with multiple parameters
# Default parameter values
# String formatting


# Step 1: Define a Function with Parameters

# Define a function named .describe_city()
# This function should accept two parameters: citycountry and country
# Give the parameter country a default value, such as “Unknown”.


# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.

# Step 3: Call the Function

# Call the function describe_city() with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: and .describe_city("Reykjavik", "Iceland")describe_city("Paris")


# Expected Output:

# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(citycountry,country="Unknown") :
    print(f"{citycountry} is in {country}")
describe_city("Alger", "Algeria")
describe_city("Tanger", "Morroco")
describe_city("Madrid")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Exercise 5 : Random
# Goal: Create a function that generates random numbers and compares them.

# Key Python Topics:

# random module
# random.randint() function
# Conditional statements (if, else)


# Step 1: Import the random Module

# At the beginning of your script, use to access the random number generation functions.import random


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.


# Step 3: Generate a Random Number

# Inside the function, use to generate a random integer between 1 and 100.random.randint(1, 100)


# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100.


# Expected Output:

# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

import random
def random_compare(number) :
    if 1 <= number <= 100:
        random_number = random.randint(1, 100)
        if number == random_number :
            print (f"Success !  ")
        else :
            print(f"Fail !   Your number : {number}, Random number : {random_number}")
    else:
        print ("Erreur : Le nombre doit être compris entre 1 et 100.")

random_compare(25) 

# Exercise 6 : Let’s create some personalized   !
# Goal: Create a function to describe a shirt’s size and message, with default values.

# Key Python Topics:

# Functions with parameters and default values
# Keyword arguments


# Step 1: Define a Function with Parameters

# Define a function called .make_shirt()
# This function should accept two parameters: size and text


# Step 2: Print a Summary Message

# Set up the function to display a sentence summarizing the shirt’s size and message.


# Step 3: Call the Function



# Step 4: Modify the Function with Default Values

# Modify the function so that has a default value of “large” and has a default value of “I love Python”.make_shirt()sizetext


# Step 5: Call the Function with Default and Custom Values

# Call to make a large shirt with the default message.make_shirt()
# Call to make a medium shirt with the default message.make_shirt()
# Call to make a shirt of any size with a different message.make_shirt()


# Step 6 (Bonus): Keyword Arguments

# Call using keyword arguments (e.g., ).make_shirt()make_shirt(size="small", text="Hello!")


# Expected Output:

# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

def make_shirt(size = "large", text = "I love Python") :
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("56 cm","it's too late")
make_shirt()
make_shirt(size = "medium")
make_shirt(size = "small", text = "small but STRONG !!!") 

# Exercise 7 : Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Key Python Topics:

# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)


# Step 1: Create the get_random_temp() Function

# Create a function called that returns a random integer between -10 and 40 degrees Celsius.get_random_temp()


# Step 2: Create the main() Function

# Create a function called . Inside this function:main()
# Call to get a random temperature.get_random_temp()
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”


# Step 3: Provide Temperature-Based Advice

# Inside , provide advice based on the temperature:main()
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


# Step 4: Floating-Point Temperatures (Bonus)

# Modify to return a random floating-point number using for more accurate temperature values.get_random_temp()random.uniform()


# Step 5: Month-Based Seasons (Bonus)

# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify to return temperatures specific to each season.get_random_temp()


# Expected Output:

# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

def get_random_temp() : 
    random_int_number = (random.randint(-10, 40))
    print(f"The temperature right now is {random_int_number} degrees Celsius.")
    return random_int_number

def main() :
    temperature = get_random_temp()
    if temperature < 0 :
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<= temperature <= 16 :
        print("Quite chilly! Don’t forget your coat")
    elif 16<= temperature <= 23 :
        print("Nice weather")
    elif 24<= temperature <= 32 :
        print("A bit warm, stay ted")
    elif 32<= temperature <= 40 :
        print("It’s really hot! Stay cool")

main()

def get_random_temp_Floating_Point() : 
    random_float_number = float(random.uniform(-10, 40))
    print(f"The temperature right now is {random_float_number} degrees Celsius.")
    return random_float_number
def main_Floating_Point() :
    temperature = get_random_temp_Floating_Point()
    if temperature < 0.0 :
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0.0<= temperature <= 16.0 :
        print("Quite chilly! Don’t forget your coat")
    elif 16.0<= temperature <= 23.0 :
        print("Nice weather")
    elif 24.0<= temperature <= 32.0 :
        print("A bit warm, stay ted")
    elif 32.0<= temperature <= 40.0 :
        print("It’s really hot! Stay cool")

main_Floating_Point()

def get_month_saison() : 
    month_list = [(1,"January"),(2,"February"),(3,"March"),(4,"April"),(5,"May"),(6,"June"),(7,"July"),(8,"August"),\
                  (9,"September"),(10,"October"),(11,"November"),(12,"December")]
    list_string_month = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    chosen_month = (input("Enter a number between 1 and 12 if you want to know the season : "))
    chosen_month = int(chosen_month)
    if chosen_month in range(1,13) :
        for a,b in month_list :
            if a == chosen_month :
                if chosen_month in [12,1,2] :
                    print(f"You have choose {b} and it's in Winter season " )
                    season = "winter season"
                    
                elif chosen_month in [3,4,5] :
                    print(f"You have choose {b} and it's in Spring season " )
                    season = "Spring season"
                        
                elif chosen_month in [6,7,8] :
                    print(f"You have choose {b} and it's in Summer season " )
                    season = "Summer season"
                        
                elif chosen_month in [9,10,11] :
                    print(f"You have choose {b} and it's in Autumn season ")
                    season = "Autumn season"
                        
    return season

def main() :
    temperature = get_month_saison()
    if temperature == "winter season" :
        print("Between -4°C and 5°C -> It's cold.")
    elif temperature == "Spring season" :
        print("Between 6°C and 15°C -> Quite chilly! Don’t forget your coat.")
    elif temperature == "Autumn season" :
        print("Between 16°C and 6°C -> Prepare your coat")
    elif temperature == "Summer season" :
        print("Between 32°C and 40°C -> It’s really hot! Stay cool.")

main()

# Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types . 'quit'
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
toppings_list = []
topping_adds = 2.50
base_price = 10
price = 0
while True :
  toppings = (input("Enter your pizza toppings one by one : "))
  toppings = toppings.lower()
  if toppings != "q" :
    toppings_list.append(toppings)
    price = base_price + topping_adds
    print(f"Adding {toppings} to your pizza.")
  elif toppings == "q":
    print(f"You added those {len(toppings_list)} toppings :")
    print(toppings_list)
    print(f"This will cost ${price} ")
    break

