# Exercice 1 : Animaux de compagnie
# Sujets clés de Python :

# Héritage
# Instanciation de classe
# Listes
# Polymorphisme

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
            return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

bengal_obj = Bengal("felix" , 10)
chartreux_obj = Chartreux("chatou", 5)
siamese_obj = Siamese("samiou", 6) 
all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)
print (bengal_obj.sing("miaou"))
print (chartreux_obj.sing("grrrrrr !!"))
print (siamese_obj.sing("snif !"))
sara_pets.walk() 

#  Exercice 2 : Chiens
# But: Créez une classe avec des méthodes pour aboyer, courir et se battre.Dog
# 
# class Dog:
#     def __init__(self, name, age, weight):
#         # ... code to initialize attributes ...
#         self.name = name
#         self.age = age
#         self.weight = weight
        

#     def bark(self):
#         # ... code to return bark message ...
#         return f"{self.name} is barking"
    
#     def run_speed(self):
#         # ... code to return run speed ...
#         return f"{self.name} run_speed is : {self.weight / self.age * 10}"

#     def fight(self, other_dog):
#         # ... code to determine and return winner ...
#         dog_peed = ((Dog(self.name,self.age,self.weight).run_speed()) * self.weight)
#         other_dog_speed = other_dog.run_speed() * other_dog.weight
#         if dog_peed > other_dog_speed :
#             return f"{self.name} is the winner"
#         elif other_dog_speed > dog_peed :
#             return f"{other_dog} is the winner"
#         else :
#             return f"{self.name},{other_dog} are equal"

        
# # Step 2: Create dog instances
# dog1 = Dog("rex",7,56)
# dog2 = Dog("spak",9,60)
# dog3 = Dog("fifi",5,45)

# # Step 3: Test dog methods
# print(dog1.bark())
# print(dog3.bark())
# print(dog2.run_speed())
# print(dog3.run_speed())
# print(dog1.fight(dog3))
# print(dog2.fight(dog3)) 

#  Exercice 3 : Chiens domestiqués
# But: Créez une classe qui hérite de la formation et des astuces et qui y ajoute.PetDogDog
# import sys
# sys.path.append('C:\Users\kiars\BOOTCAMP_PSTB\Week1\Day4\ExerciceXP\xp-classdog.py')
import random
from classdog import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self) :
        print(self.bark())
        self.trained = True

    def play(self,*args) : # arg ici est une liste d'instance de chien
            self.args = args
            print(f"{self.args}, are playing togheter")    

    def do_a_trick(self): 
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        print(f"{self.name} {random.choice(tricks)}")           

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


# Exercice 4 : Classes familiales et individuelles
# But:

# Entraînez-vous à travailler avec des classes et des interactions d’objets en modélisant une famille et ses membres.



# Sujets clés de Python :

# Classes et objets
# Méthodes d’instance
# Interaction avec les objets
# Listes et boucles
# Les instructions conditionnelles (if/else)
# Mise en forme des chaînes (f-strings)

# Step 1: Create the Person Class

class Person ():
    def __init__(self,first_name,age,last_name = "") :
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    def is_18(self) :
        if self.age >= 18 :
            return True
        else : 
            return False
person1 = Person("adel", 15, "Zitouni")
print (person1.is_18())

# Step 2: Create the Family Class

class Family():
    def __init__(self,last_name,members = []) :
        self.last_name = last_name
        self.members = members

    def born(self,first_name, age):
        new_person = Person(first_name, age, self.last_name)
        # print(vars(new_person))
        self.members.insert(-1,vars(new_person))
        return self.members
    
    def check_majority(self,first_name) :
        for i in range(len(self.members)):
            # print(self.members[i])
            # print(type(self.members[i]))
            if first_name in self.members[i].values() :
                person = Person(first_name,self.members[i]['age'],self.members[i]['last_name'])
                if (person.is_18()) == True :
                    print(f"{first_name}, You are over 18, your parents Jane and John accept that you will go out with your friends")
                else :
                    print(f"Sorry, {first_name} you are not allowed to go out with your friends.")
        nothing = ""
        return  nothing
    def family_presentation(self) :
        print (f"The {self.last_name}'s family are all listed below  : ") 
        for i in range(len(self.members)):
            if self.last_name in self.members[i].values() :
                print(f"{i+1} : {self.members[i]['first_name']}, {self.members[i]['age']} ans")
        nothing = ""
        return  nothing


person2 = Family("Zitouni")
print (person2.born("adel", 44))
print (person2.born("zz", 46))
print (person2.born("maissene", 14))
print (person2.born("norhene", 10))
print (person2.born("mohade_mohsen", 6))
print (person2.born("ihsene", 3))
print (person2.check_majority("adel"))
print (person2.check_majority("zz"))
print (person2.check_majority("maissene"))
print (person2.check_majority("norhene"))
print (person2.check_majority("mohamed-mohsen"))
print (person2.check_majority("ihsene"))
print (person2.check_majority("norhene"))
print (person2.family_presentation())
