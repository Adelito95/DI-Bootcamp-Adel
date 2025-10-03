"""Examen 1 : Jeu 🎲 de devinettes de nombres (obligatoire)

Construisez un jeu amusant de devinettes de nombres en Python ! 🐍 
Le programme choisit un nombre aléatoire entre 1 et 100, et vous avez 7 tentatives pour le deviner. 
Obtenez des indices si vous êtes trop haut 📈 ou trop bas 📉 ! Parfait pour pratiquer les boucles 🔄, 
les conditionnels et la ❓ saisie ⌨️ utilisateur."""

import random #Import de la librairie nécessaire
Nombre = random.randint(1, 100) # Assignation de la valeur aléatoire à la variable 
tentative = 0
compte = 0
print (Nombre)
print("""Venez tenter votre chace de gagner à notre jeu, il vous suffit de taper un chiffre entre 1 et 100. 
Vous avez le droit à 7 tentatives pour deviner le bon chiffre et gagner contre l'ordinateur """)
for essai in range (7) :
    tentative = int(input("Entrer un chiffre entre 1 et 100 : "))
    compte += 1
    if Nombre == tentative :
        print ("Congretulations, You Win !!!")
        break
    elif tentative > Nombre and compte !=7 :
        print (f"Vous êtes trop haut, plus que {int(7)-compte} chance de gagner, Try again !!!" )
    elif tentative < Nombre and compte !=7 :
        print (f"Vous êtes trop bas, plus que {int(7)-compte} chance de gagner, Try again !!! " )
    elif Nombre != tentative and compte == 7 :
        print ("You lose, see you next time !!!")
