#  # Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples



# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input("Entrer un nombre : ")) # Asking the user for a number.
length = int(input("Entrer une longueur : ")) # Asking the user for a length.
list_of_multiples = [] # Creation of an empty list
for i in range(length+1) : # Loop on the range of the lenght + one
    if i > 0 : # 0 non include
        multiples = number*i # Mathematique operation
        list_of_multiples.append(multiples) # Adding the result of the operation at a liste
print (f"number: {number} - length {length} ➞  {list_of_multiples}") # Printing of list of multiples of the user given number until the list length reaches the user given length.

# # Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"


# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

user_string = input("Entrer un mot : ") # Asking the user for a string caracter.
user_string_corrected = "" # Corrected varaible of user_string
for elem in user_string: # Iteration Loop on user_string 
    if user_string_corrected.endswith(elem) !=True : # Duplicate consecutive element is not allowed 
        user_string_corrected += elem # Adding the character parsed on the user_string_corrected variable
print(f"user's word : \"{user_string}\" ➞  \"{user_string_corrected}\"") # Printing of the result without duplicate consecutive letter in the given word
