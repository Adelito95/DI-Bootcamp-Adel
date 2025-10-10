# Défi quotidien - Cercle
# Instructions:
# L’objectif est de créer une classe qui représente un cercle simple.
# A peut être défini en spécifiant le rayon ou le diamètre.
# L’utilisateur peut interroger le cercle pour son rayon ou son diamètre.Circle

# Autres capacités d’une instance de Circle :

# Calculer l’aire du cercle
# Imprimer les attributs du cercle - utiliser une méthode dunder
# Être capable d’additionner deux cercles et de renvoyer un nouveau cercle avec le nouveau rayon - utilisez une méthode dunder
# Être capable de comparer deux cercles pour voir lequel est le plus grand, et renvoyer une méthode booléenne - utiliser une méthode dunder
# Être capable de comparer deux cercles et voir s’ils sont égaux, et renvoyer une méthode booléenne - utiliser une méthode dunder
# Être capable de les mettre dans une liste et de les trier
# Bonus (non obligatoire) : Installez le module Turtle, et dessinez les cercles triés

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Veuillez spécifier un rayon ou un diamètre.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(rayon={self.radius:.2f}, diamètre={self.diameter:.2f}, aire={self.area:.2f})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
    
# Exemple d’utilisation

c1 = Circle(radius=5)
c2 = Circle(diameter=20)  # équivalent à rayon = 10

print("Cercle 1 :", c1)
print("Cercle 2 :", c2)

# Addition
c3 = c1 + c2
print("Cercle 3 (addition de c1 et c2) :", c3)

# Comparaisons
print("c1 > c2 ?", c1 > c2)
print("c1 == c2 ?", c1 == c2)

# Liste et tri
cercles = [c1, c2, c3, Circle(radius=2)]
cercles.sort()  # utilise __lt__
print("\nCercles triés :")
for c in cercles:
    print(c)

# Bonus
    
import turtle

def draw_circle(circle, t):
    t.circle(circle.radius)

def draw_sorted_circles(circle_list):
    turtle.setup(width=800, height=600)
    t = turtle.Turtle()
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.speed(1)
    
    for circle in circle_list:
        draw_circle(circle, t)
        t.penup()
        t.forward(circle.diameter + 10)
        t.pendown()

    turtle.done()

# Exécuter le dessin
draw_sorted_circles(cercles)