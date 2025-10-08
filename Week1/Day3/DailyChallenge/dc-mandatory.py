# Daily challenge: Old MacDonald’s Farm

# Instructions: Old MacDonald’s Farm

# You are given example code and output. 
# Your task is to create a Farm class that produces the same output.



class Farm () :

        def __init__(self,farm_name,nameanimals = {}):
            self.name = farm_name
            self.animals = nameanimals
        
        def add_animal(self,animal_type,count = 1) :
            self.animal_type = animal_type
            self.count = count
            if animal_type in self.animals :
                self.animals[animal_type] += 1
            else :
                self.animals[animal_type] = count
            
        def get_info(self) :
            print (f"{self.name}")
            print ("")
            print ("")
            for  k, v in self.animals.items() :
                print (f"{k : <5} : {v : <5}")
            print ("")
            print ("")
            phrase = "E-I-E-I-0!"
            print(f"{phrase: <5}")

        def get_animal_types (self, sorted_list = []):
            self.sorted_liste = sorted_list
            for  k, v in self.animals.items() :
                  sorted_list.append(k)
            print(sorted(sorted_list))
        
        def get_short_info(self) :
             for k, v in self.animals.items() :
                  if v > 1:
                    for i in range(len(self.sorted_liste)) :
                         if self.sorted_liste[i]  == k :
                          self.sorted_liste[i] += "s" 
             print (self.sorted_liste) 
             print(f"{self.name}’s farm has {self.sorted_liste[0]}, {self.sorted_liste[1]} and {self.sorted_liste[2]}")
     

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types()) 
print(macdonald.get_short_info())                     
                
