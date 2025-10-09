#  Exercice 2 : Chiens
# But: Créez une classe avec des méthodes pour aboyer, courir et se battre.Dog

class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...
        self.name = name
        self.age = age
        self.weight = weight
        

    def bark(self):
        # ... code to return bark message ...
        return f"{self.name} is barking"
    
    def run_speed(self):
        # ... code to return run speed ...
        return f"{self.name} run_speed is : {self.weight / self.age * 10}"

    def fight(self, other_dog):
        # ... code to determine and return winner ...
        dog_peed = ((Dog(self.name,self.age,self.weight).run_speed()) * self.weight)
        other_dog_speed = other_dog.run_speed() * other_dog.weight
        if dog_peed > other_dog_speed :
            return f"{self.name} is the winner"
        elif other_dog_speed > dog_peed :
            return f"{other_dog} is the winner"
        else :
            return f"{self.name},{other_dog} are equal"

        
# Step 2: Create dog instances
dog1 = Dog("rex",7,56)
dog2 = Dog("spak",9,60)
dog3 = Dog("fifi",5,45)

# Step 3: Test dog methods
print(dog1.bark())
print(dog3.bark())
print(dog2.run_speed())
print(dog3.run_speed())
print(dog1.fight(dog3))
print(dog2.fight(dog3))