# exercice 1 : CATS

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
    def find_oldest_cat(cat1, cat2, cat3):
        all_cat_age = [cat1.age,cat2.age,cat3.age]
        oldest_cat = max(all_cat_age)
        if oldest_cat == cat1.age and oldest_cat != cat2.age and oldest_cat != cat3.age   :
            print(f'The oldest cat is {cat1.name}, and is {oldest_cat} years old')
        elif oldest_cat == cat2.age and oldest_cat != cat1.age and oldest_cat != cat3.age  :
            print(f'The oldest cat is {cat2.name}, and is {oldest_cat} years old')
        elif oldest_cat == cat3.age and oldest_cat != cat1.age and oldest_cat != cat2.age  :
            print(f'The oldest cat is {cat3.name}, and is {oldest_cat} years old')
        elif cat1.age == oldest_cat == cat2.age and oldest_cat != cat3.age:
            print(f'Two of them are oldest cat, {cat1.name} and {cat2.name} are {oldest_cat} years old') 
        elif cat1.age == oldest_cat == cat3.age and oldest_cat != cat2.age:
            print(f'Two of them are oldest cat, {cat1.name} and {cat3.name} are {oldest_cat} years old')
        elif cat2.age == oldest_cat == cat3.age and oldest_cat != cat1.age :
            print(f'Two of them are oldest cat, {cat2.name} and {cat3.name} are {oldest_cat} years old')
        elif oldest_cat == cat1.age and oldest_cat == cat2.age and oldest_cat == cat3.age :
            print(f'They have all {oldest_cat} years old')
        all_cat_name = [cat1.name,cat2.name,cat3.name]
        
cat1 = Cat("bixou", 16)
cat2 = Cat("rexus", 15)
cat3 = Cat("dogus", 16)
old_cat = Cat.find_oldest_cat(cat1,cat2,cat3)

# Exercice 2 : DOGS

# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

class Dog() :
        
    def __init__ (self,name,height) :
        self.name = name
        self.height = height
    
    def bark(self) :
        print("goes woof!")
    
    def jump(self) :
        print(f"jumps {self.height * 2} cm high!")
    
    def compare_Dog_sizes(davids_dog,sarahs_dog) :
        if davids_dog.height == sarahs_dog.height :
            print (f"Height of davids and sarahs are equal, {davids_dog.height} = {sarahs_dog.height}")
        elif davids_dog.height > sarahs_dog.height :
            print (f"davids is heigher than sarahs, {davids_dog.height} > {sarahs_dog.height}")
        else :
            print (f"sarahs is heigher than davids, {sarahs_dog.height} > {davids_dog.height}") 

              
davids_dog = Dog('davids', 140)
sarahs_dog = Dog('sarahs', 140)
print(sarahs_dog.name, sarahs_dog.height)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()
Dog.compare_Dog_sizes(davids_dog,sarahs_dog)


#  Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.

class Song  () :
    def __init__(self,lyrics=[]):
        self.lyrics = lyrics
        print("This is a song class which print lyrics line by line.")


    def sing_me_a_song(self,lyrics):
        for i in range(len(self.lyrics)) :
            print(self.lyrics[i])

lyrics = ["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]
stairway_objet = Song(lyrics)
stairway_objet.sing_me_a_song(lyrics) 

# Exercise 4 : Afternoon at the Zoo
# Goal:

# Create a class to manage animals. The class Zoo should allow adding animals, displaying them, 
# selling them, and organizing them into alphabetical groups.


class Zoo:
    def __init__(self, zoo_name,animals = []):
        self.name = zoo_name
        self.animals = animals

    def add_animal(self, new_animal):
        if new_animal not in self.animals :
                self.animals.append(new_animal)

    def get_animals(self):
        print (f"This is a list of the animals present in this zoo {self.animals}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals :
            self.animals.remove(animal_sold)        

    def sort_animals(self, dico = {}):
        self.animals.sort()
        self.animals
        self.dico = dico
        for i in range(len(self.animals)) :
            if self.animals[i][0].capitalize() not in dico.keys() :
                dico[self.animals[i][0].capitalize()] = list([self.animals[i].capitalize()])
            elif self.animals[i][0].capitalize() in dico.keys() :
                dico[self.animals[i][0].capitalize()].append(self.animals[i].capitalize()) 
        print (self.dico)
        
    def get_groups(self):
     for key, value in self.dico.items() :
        print (f"{key} : {value}")

brooklyn_safari = Zoo("Brooklyn Safari")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()




# for my comprehension 

# liste = ["oiseau", "antilope", "grenouille", "cheval", "brebie","chat"]
# liste.sort()
# print(liste)
# dico  = {}
# dico1 = {liste[i][0].capitalize() : list([liste[i].capitalize()]) for i in range(len(liste))  if liste[i][0].capitalize() not in dico.keys() }
 
# for i in range(len(liste)) :
#     if liste[i][0].capitalize() not in dico.keys() :
#         dico[liste[i][0].capitalize()] = list([liste[i].capitalize()])
#     elif liste[i][0].capitalize() in dico.keys() :
#         dico[liste[i][0].capitalize()].append(liste[i].capitalize()) 
# print (dico)
# print (dico1)




