# What You’ll learn
# In this challenge, you will enhance your understanding of Python dictionaries, string manipulation, and working with list data structures. You’ll practice iterating over strings, updating dictionaries, and handling data types, all fundamental skills in programming.



# 🛠️ What you will create
# You will create a Python script that processes user input to map the positions of each letter in a given word into a dictionary. This will involve string indexing, dictionary manipulation, and ensuring data types are appropriately handled.



# Challenge
# Ask a user for a word.
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list, and those lists are values.

# Examples
# “dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
# “froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
# “grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3], “e”: [4], “s”: [5] }
#  dicos = {}
dico = {}
user_word = input("Enter a word please : ")
for i in range(len(user_word)):
    if user_word[i] not in dico.keys() :
        dico[user_word[i]] = list([i])
    elif user_word[i] in dico.keys() :
        dico[user_word[i]].append(i)
print (dico)
# # Créer un dictionnaire de carrés
# carres = {x: x**2 for x in range(1, 6)}
# print(carres)   # Affiche : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# dicos = {user_word[i] :  list([i]) for i in range(len(user_word)) if user_word[i] not in dicos.keys()}
# # dicos.update({user_word[i] :  dicos[user_word[i]].append(i)  for i in range(len(user_word)) if user_word[i] in dicos.keys()})
# for i in range(len(user_word)-1):
#     if user_word[i] in dicos.keys() :
#         dicos[user_word[i]].append(i)
# print (dicos)