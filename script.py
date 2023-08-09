#coding:utf-8
"""agePersonne = 20
prix = 45

print("l'age de la personne est {} et le prix est de {} dollars".format(agePersonne, prix))

nomJoueur = input("Entrez votre nom :")

print("Bienvenue :", nomJoueur)

prix = input("Entrez votre prix :")
prix = int(prix)
prixth = prix + (prix * 20/10)
print("le prix th :", prixth)

#condition
identifiant = "Guy"
mot_de_passe = "1234"

print("interface de connexion")

user_id = input("Entrez votre identifiant :")
user_password = input("Entrez votre mot de passe :")

if user_id == identifiant and user_password == mot_de_passe:
    print("vous etes connectes,bienvenue", user_id)
else:
    print("Entrez le bon mot de passe ou l'identid$fuiant")

age = input("Entrez votre age :")
age = int(age)
if age > 18:
    print("vous etes majeur")
elif age < 18:
    print("vous etes mineur")
else:
    print("Entrez votre age")


#boucle
compteur = 0

while compteur < 8:
    print("je suis gdp")
    compteur += 1
print("je suis sorti de la boucle....")

phrase = "Boujour!tout le monde"

for lettre in phrase:
    print(lettre)

#fonction
def dire(nom_personne = "guy",age_personne = 12, message_personne = "salut"):
    print("{} : {} : {}".format(nom_personne,age_personne,message_personne))

dire()

def show_inventory(*list_items):
    for item in list_items:
        print(item)

show_inventory("épée")
show_inventory("épée", "arc", "potion de mana")

def calcul_somme(nombre1, nombre2):
    return nombre1 + nombre2 

print(calcul_somme(5, 15))

def le_plus_grand(nombre1, nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "EGALITE !"
print(le_plus_grand(12, 12))

#fontion lambda

coucou = lambda a, b: a + b

print(coucou(23, 21))

#module

#module mathematisque on fait l'importation math

import math

resultat = math.sqrt(100)
sinus = math.sin(2)
print(resultat, sinus)


import includ.player as player
player.au_revoir()
player.parler("guy", "je vais bien!")


# Gestion d'erreur
# gerer les exception: try/except(+else,finally)
ageUtilisateur = input("entrez votre age :")

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("Vous devez mettre votre age ! ")
else:
    print("Tu as", ageUtilisateur, "ans")
finally:
    print("FIN DU PROGRAMME...")

nombre1 = 150
nombre2 = input("Choisir le nombre pour diviser :")
try:
    nombre2 = int(nombre2)
    print("Resultat = {}".format(nombre1/nombre2))
except ZeroDivisionError:
    print("vous ne pouvez pas diviser un nombre par zero.")
except ValueError:
    print("vous devez entre un chiffre different de zero")
except:
    print("valeur incorrecte.")
else:
    print("Bravo, tu as noté un nombre valide")
finally:
    print("Fin du programme")

types d'erreur :   ValueError
                    NameError
                    TypeError
                    ZeroDivisionError
                    OSError
                    AssertionError
"""    