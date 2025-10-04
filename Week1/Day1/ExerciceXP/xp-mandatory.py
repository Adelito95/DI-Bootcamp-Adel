# # Exercise 1 : Hello World
# # Print the following output in one line of code:

# # Hello world
# # Hello world
# # Hello world
# # Hello world
for i in range(4) : # Boucle for pour réitérer 4 fois l'impression de Hello world
    print ("Hello world") # Affichage du résultat

# # Exercise 2 : Some Math
# # Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
Nombre = 99 # Déclaration de la constante
result = (Nombre**3)*8 # Calcul mathématique
print (result) # Affichage du résultat

# #  Exercise 3 : What’s your name ?
# # Write code that asks the user for their name and determines whether or not you have the same name,
# # print out a funny message based on the outcome.

my_name = "adel" # Déclaration du nom cible
user_name= input("What is your name ? : ") # Demande à l'user d'entrer son nom
user_name = user_name.lower() # Convertion du nom en caractère minuscule 
if user_name == my_name : # condition de validation
    print("You're my Man BRO !!!!") # Affichage de la satisfation
elif user_name != my_name : # Condition de non validation 
    print("My name is better than yours, get it !!!") # Affichage de la non-satisfation

# #  Exercise 4 : Tall enough to ride a roller coaster
# # Write code that will ask the user for their height in centimeters.
# # If they are over 145cm print a message that states they are tall enough to ride.
# # If they are not tall enough print a message that says they need to grow some more to ride.

tall_enouth = "145" # Instantition de la variable recommandée
tall = input("To see if you can ride, please enter your tall : ") # Demande à l'User sa taille 
if tall >= tall_enouth : #condition de validation
    print ("Good new, your tall is enough to ride, here we go !!!") # Affichage de la validation
else : #Condition de non validation
    print ("sorry, but you need to eat more vegetebale, your tall is not enough to ride") # Affichage de la non-validation

# # Exercise 5 : Favorite Numbers
# # Key Python Topics:

# # Sets
# # Adding/removing items in a set
# # Set concatenation (using union)


# # Instructions:

# # Create a set called my_fav_numbers and populate it with your favorite numbers.
# # Add two new numbers to the set.
# # Remove the last number you added to the set.
# # Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# # Note: Sets are unordered collections, so ensure no duplicate numbers are added.
my_fav_numbers = {1,3,7,11,36,70,56,59} # Creétion du set avec les nombre favoris
my_fav_numbers.update([99,100]) # Ajout de deux autres nombre favoris
print(my_fav_numbers) # Affichage du set après ajout des deux derniers nombres
friend_fav_numbers ={6,5,14,58,65,95,105,106} # Creétion du set avec les nombre favoris de mon ami
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) # Union des deux sets
print(our_fav_numbers) # Affichage du set Uni

# #  Exercise 6: Tuple
# # Key Python Topics:

# # Tuples (immutability)


# # Instructions:

# # Given a tuple of integers, try to add more integers to the tuple.
# # Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
mon_premier_tuple = (3,2,9,6,4) # Crétion du premier Tuple
mon_second_tuple = (96,45,42) # Crétion du second Tuple
mon_new_tuple = mon_premier_tuple + mon_second_tuple # Concaténation des deux Tuples pour contourner la non muttabilité du Tuple
print(mon_new_tuple) # Affichage du nouveau Tuple
# # we can not change a tuple after his creation but we can concatenate it with an other one to create a new one

# # Exercise 7: List Manipulation
# # Key Python Topics:

# # Lists
# # List methods: append, remove, insert, count, clear


# # Instructions:

# # You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # Remove "Banana" from the list.
# # Remove "Blueberries" from the list.
# # Add "Kiwi" to the end of the list.
# # Add "Apples" to the beginning of the list.
# # Count how many times "Apples" appear in the list.
# # Empty the list.
# # Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"] # Création de la liste de fruits
basket.remove(basket[0]) # Remove "Banana" from the list
basket.remove(basket[-1]) # Remove "Blueberries" from the list.
basket.append("kiwi") # Add "Kiwi" to the end of the list.
basket.insert(0,"Apples") # Add "Apples" to the beginning of the list.
basket.count("Apples")# Count how many times "Apples" appear in the list.
basket.clear() # Empty the list.
print(basket) # Print of the final state of the list

# #  Exercise 8 : Sandwich Orders
# # Using the list below :

# # sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].

# # The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.
# # We need to prepare the orders of the clients:

# # Create an empty list called finished_sandwiches.

# # One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# # After all the sandwiches have been made, print a message listing each sandwich that was made, such as:


# # I made your tuna sandwich
# # I made your avocado sandwich
# # I made your egg sandwich
# # I made your chicken sandwich

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich",\
                   "Chicken sandwich", "Pastrami sandwich"] # Liste des différents sandwichs
while "Pastrami sandwich" in sandwich_orders : #Suppression du Pastrami sandwich car plus de bastrami en reserve
        sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches =[] # Céation d'une nouvelle liste vide
for i in range(len(sandwich_orders)) : # Boucle for pour la preparation des sandwichs
        finished_sandwiches.append(sandwich_orders[0]) # Ajout des sandwichs finis dans la liste appropriée
        sandwich_orders.remove(sandwich_orders[0]) # Suppression des sandwichs déja préparés de la liste de commande
        print(f"I made your {finished_sandwiches[i]} sandwich") # Information client de la preparation de leurs sandwichs
        