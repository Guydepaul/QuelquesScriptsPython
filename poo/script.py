#coding:utf-8

# les classe et attributs
"""
class Humain: #classe des etres humains

     #création d'un attribut de classe

    humains_crees = 0

    def __init__(self, c_prenom, c_age): #creation d'un costructeur, self = identifiant qui vise l'objet que l'on crée
        print("Création d'un humain")

        #creation d'un attribut

        #self.prenom = "guy"
        #self.age = 12
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees += 1

print("Lancement du programme")

h1 = Humain("guy", 12) # creation d'un objet
#print("prenom de h1 => {}".format(h1.prenom))
print("Humains existant : {}".format(Humain.humains_crees))
print("prenom de h1 => {}".format(h1.prenom))
print("Age de h1 => {}".format(h1.age))
h2 = Humain("Paul", 13)
#print("age de h2 => {}".format(h2.age))
print("Humains existant : {}".format(Humain.humains_crees))
print("prenom de h2 => {}".format(h2.prenom))
print("age de h2 => {}".format(h2.age))

#12_les methodes
class Humain:

    lieu_habitation = "terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    #methode qui fonction en parallele avec un objet/ methode standard
    def parler(self, message): #self = methode standard
        print("{} a dit : {}".format(self.nom, message))
    
    #methode de classe on va directement travail sur la classe
    def changer_planete(cls, nouvelle_planette): #cls = methode de classe
        Humain.lieu_habitation = nouvelle_planette

    changer_planete = classmethod(changer_planete) #definition d'une methode de classe"

    #methode statique c'est une classe qui peut etre applle dans une classe sans avoir un objet a extensier
    def definition():
        print("un humain c'est un etre-vivant...")
    definition = staticmethod(definition)
#programme principale
#h1 = Humain("guy", 21)
#h1.parler("Boujour mon frere !")
#print("planette actuel : {}".format(Humain.lieu_habitation))

#Humain.changer_planete("Mars")
#print("planette actuel : {}".format(Humain.lieu_habitation))
Humain.definition()

#13_proprietés d'encapsulation

class Humain:

    def __init__(self, nom, age):
        print("création d'un humain...")
        self.nom = nom
        self._age = age #cad que l;atribut a une propriete qui permet de l'acceder
    #lire un attribut
    def _getage(self):
        return self._age
    #modifier un attribut
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age
        #property il peut prendre plusir=eur valeur("getter", "setter", "deleter", "helper") 

    age = property(_getage, _setage)

#programme principal
h1 = Humain("guy", 21)

print(h1.age)

h1.age = -3

print(h1.age)

#14_heritage

#classe mere
class Humain:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def marcher(self):
        print("{} avec ses {} ans est entrain de marcher...".format(self.nom, self.age))
#classe fille
class Homme(Humain):
    def __init__(self, nom, age, tail):
        Humain.__init__(self, nom, age)
        self.tail = tail
    def marcher(self):
        print("{} avec ses {} ans et un tail de {}m est entrain de marcher...".format(self.nom, self.age, self.tail))

#programme principale

p2 = Homme("guy", 21, 1)
p2.marcher()
print(p2.tail, 21)

 #15_chaine de caracteur

ma_chaine = "papa et maman"
 
print(ma_chaine)

ma_chaine = ma_chaine.capitalize()

print(ma_chaine)

#16_liste

#creation d'une liste
inventaire = ["papa", "maman", "frere"]

print(inventaire[:])

inventaire[2]= "soeur" #modification tout comme invetaire.insert(2, "soeur")
print(inventaire[:])

if "papa" in inventaire:
    print("j'ai un papa")
else:
    print("suis orphelin")
inventaire.append("ma go") #ajouter un element a la liste
print(inventaire[:])

inventaire.remove("papa") #supprime tout comme def inventaire[1]
print(inventaire[:])
onjet_a_supprimer = inventaire.index("maman")
del inventaire[onjet_a_supprimer]
print(inventaire[:])

nombre = [2, 4, 11, 1, 6]
nombre.sort() #faire un trie
print(nombre[:])
nombre.reverse()
print(nombre[:])


#17_tuple c'est une maniere d'organise les données

#liste = [1, 2, 3, 4, 5, 6]

#for chose in enumerate(liste): #créer des couple
#    print(chose)
mon_tuple = (23, 21)
print(mon_tuple)

#18_dictionnaire

#création de dictionnaire : dico = {} ici il est vide, dico = {<clé>: <valeur>, <clé2>:<valeur2>}

dico = {1:145, "nom":"guy"}
print(dico[1]) #accés a une dictionnaire

#ajout au dictionnaire ou modification : dico[<clé>] = <valeur>
dico["chien"]= "animal"
print(dico)

#suppresssion 1. dico.pop(<clé>), 2. del dico[<clé>]
dico.pop("chien")
print(dico)

#existance d'une clé s'il existe
if 1 in dico:
    print("oui")
else:
    print("non")

for k,v in dico.items():
    print("clé : {} - valeur : {}".format(k, v))


#19_fichier

Modes d'ouverture : r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    x (lecture et écriture)
                    r+ (lecture/écriture dans un meme fichier)
Lecture           : read(), readline(), readlines()

#LECTURE
#fic = open("docs/donnees.txt", "r")
#content= fic.read() #pour lire 

#print(content)

#autre methode

#with open("docs/donnees.txt", "r") as fic:
   # content= fic.read() #pour lire 
  #  print(content)
    #pas besoin de closse
#print("le reste du programme...")

#ECRITURE
with open("docs/donnees.txt", "w") as fic:
    nombre = 13
    fic.write(str(nombre))
    fic.write("\nBonjour\n")
    fic.write("et les autre...\n")


line = fic.readline()
print(line)

line = fic.readlines()
print(line)
fic.close()


#20_introduction tkinter

import tkinter 
#from tkinter import *

 #on commence par créer un constructeur comme pour les classe qui permet de construire notre fenetre

mainapp = tkinter.Tk() #mainapp est l'objet du constructeur
mainapp.title("Mon premier grogamme fenetre")
#mainapp.minsize(640, 480)
#mainapp.maxsize(1280, 720)
#mainapp.positionfrom("user")

#geometry("XxY+0+0") et centre la fenetre

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 800
window_y = 600

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
mainapp.geometry(geo)


mainapp.mainloop() #mainloop permet de garde la fenetre jusqu'a ce que l'utilisateur la ferme


#21_premiers xidgets

#<nom_variable>= <nom_widget>(<widget_parent, <params>...)


import tkinter

app = tkinter.Tk()

#label_welcome = tkinter.Label(app, text="Bienvenue à tous") #label c'est une classe(de l'objet) avec ses parametres
#label_welcome.configure(text="nouveau message") #change le texte
#message_welcome = tkinter.Message(app, text="Bienvenue à tous") #avec message on a un retour a la ligne imediat
#message_welcome.pack() #pack va separe l'espace en deux partie, affichage

#pour la saisi

#entrez_nom = tkinter.Entry(app, width=45) #Entry gere les input
#entrez_nom.pack()


#widget boutton
def hello():
    print("hello sur teminal")
button_quit = tkinter.Button(app, text="Ok", command=hello)
button_quit.pack()
app.mainloop()



#22_widget avancé

import tkinter

#app = tkinter.Tk()

#*****************************************************************
#cocher une case
#check_widget = tkinter.Checkbutton(app, text="publier", offvalue=2, onvalue=3) #case optionnel genre on peut ou n'est pas la coche

#radio_widget = tkinter.Radiobutton(app, text="homme", value=1) #avec radio on est oblige de selectionner une case
#radio_widget1 = tkinter.Radiobutton(app, text="femme", value=0)

#check_widget.pack()
#radio_widget.pack()
#radio_widget1.pack()
#**************************************************************************
#de curseur
#scale_widget = tkinter.Scale(app, from_=1, to=100, tickinterval=25)
#spin_widget = tkinter.Spinbox(app, from_=1, to = 10)
#scale_widget.pack()
#spin_widget.pack()
#**********************************************************************
#avec une liste et on vait selectionner un element
#lb = tkinter.Listbox(app)
#lb.insert(1, "guy")
#lb.insert(2, "guy")
#lb.insert(3, "guy")
#lb.pack()
#*******************************************************************

#les fenetre modal = c'est tout ce qui est message d'avertissement, message d'errreur,...ici on va devoir importe  un module specifique
from tkinter import messagebox
def show_modal_window():
    messagebox.showerror("ERREUR", "Un problème est survenu !")

    #showinfo(), showwarning(), askquestion(genre voulez vous sortir?), askokcancel(), askyesno(), askretrycancel()

app = tkinter.Tk()
btn = tkinter.Button(app, text="Declancher une erreur", command=show_modal_window)

btn.pack()

app.mainloop()

#***************************__FIN__*****************************************

#***************************__DEBUT__***************************************

#23_VARIABLE CONTROLE

import tkinter

#observateur
#def upadete_label(*args):
    #var_label.set(var_entry.get())
def upadate_observation(*args):
    if var_gender.get():
        var_label_gender.set("c'est un homme")
    else:
        var_label_gender.set("c'est une femme")

#création et parametrage de fenetre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable tkinter")

#Widget...
#var_entry = tkinter.StringVar()
#var_entry.trace("w", upadete_label)
#entry = tkinter.Entry(app, textvariable=var_entry
var_gender = tkinter.IntVar()
var_gender.trace("w", upadate_observation)

#var_label = tkinter.StringVar()
#label = tkinter.Label(app, text="Bonjour ! :)", textvariable=var_label)
radio1 = tkinter.Radiobutton(app, text="homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text="femme", value=0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label = tkinter.Label(app, textvariable= var_label_gender)

#entry.pack()
#label.pack()
radio1.pack()
radio2.pack()
label.pack()

#Boucle principale
app.mainloop()
#***************************FIN********************************

#***************************DEBUT******************************

#24_positionnzmznr widget

import tkinter

#création et parametrage de la fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement widget")

#widgets
    #   widget de cadre qui peut contnir d'aotre widget
#mainfrem = tkinter.Frame(app, width=100, height=100, borderwidth=1)
#mainfrem.pack()

#btn = tkinter.Button(mainfrem, text="DECONNEXION" )
#btn.pack()

#positionnement
label = tkinter.Label(app, text= "un label")
entry = tkinter.Entry(app)
btn = tkinter.Button(app, text="DECONNEXION" )

#label.pack()
#entry.pack()
#btn.pack(expand=1, side="left")

label.grid(row=0, column= 0, padx=20, pady=20)
entry.grid(row=0, column= 2)
btn.grid(row=0, column= 3)
#boucle principale
app.mainloop()
#******************FIN*****************************

#*******************DEBUT**************************

#25_ création de menu

import tkinter

def show_about():
    about = tkinter.Toplevel()
    about.title("A propos de moi")
    lb = tkinter.Label(about, text="Bonjour")
    lb.pack()

#création et parametrage de la fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Creation de menu")

#widgets...
maimenu = tkinter.Menu(app)

first_menu = tkinter.Menu(maimenu, tearoff=0)
first_menu.add_cascade(label="option1")
first_menu.add_cascade(label="option2")
first_menu.add_cascade(label="quitter", command=app.quit)

second_menu = tkinter.Menu(maimenu, tearoff=0)
second_menu.add_cascade(label="commande1")
second_menu.add_cascade(label="commande2")
second_menu.add_separator()
second_menu.add_cascade(label="A propos", command=show_about)

maimenu.add_cascade(label="premier", menu=first_menu)
maimenu.add_cascade(label="second", menu=second_menu)

#boucle principale
app.config(menu=maimenu)
app.mainloop()

#**********************FIN TKINTER************************
#26_gestion de temp

#************************DEBUT****************************

import time

#print("le premier texte")
#time.sleep(5) #on est bloqué de 5sec avant execution du second instruction
#print("le second texte")

#1er janvier 1970 à 00H00
#print(time.time())

begin = time.time()
print("debut")
time.sleep(5)
end = time.time()
print("fin")
print(f"temps executé : {end - begin}s")

              localtime()
(TIMESTAMP) ----------------> structure de temps
            <----------------
                mktime()

print(time.localtime())
print(time.mktime(time.localtime()))

%d : jour (01 à 31)
%m : mois (01 à 21)
%y : année (ex : 2023)
%P : AM/PM

%A: jour semaine/ %a (jour abrégé)
%B : mois
%Z : fuseau horaire (timezone)

#comment avoir une chaine pour manipule le temps

print(time.strftime("%d/%m/%y"))
print(time.strftime("%Z"))
#***************************FIN TIME***********************

#27_gestion de date

#***************************DEBUT DATE**********************

import datetime

#comparer deux date avc temps
d1 = datetime.datetime(2023, 5, 24, 14, 25, 30)
d2 = datetime.datetime(2023, 5, 23, 14, 25, 30)

if d1 < d2:
    print("d1 est plus ancien que d2")
else:
    print("d1 est plus recent que d2")

#pour compare la date seulemlent on utilise "date" a la place de "datetime",mais aussi on peut travail sur le temps seulement est là on remplace avec "time"

#pour voir le temps réel

#from datetime import datetime
#print(datetime.now())

#pour la date seulement

from datetime import date

now = date.today()
print(now)
#**********************FIN****************************
"""
#28_PROGRAMMATION ASYNCHRONE

#*********************DEBUT***************************
import time
import threading # qui permet la programation paralelle

def process_one():
    i = 0
    while i < 4:
        print("aaaaaaaaaaaaaaa")
        time.sleep(0.3)
        i +=1

def process_two():
    i = 0
    while i < 4:
        print("rrrrrrrrrrrrrrrr")
        time.sleep(0.3)
        i +=1
process_one()
process_two()
"""
th1 = threading.Thread(target=process_one) #on crée de thread
th2 = threading.Thread(target=process_two)

th1.start() #on le demarre
th2.start()

th1.join() #on le fait etendre l'un de l'autre
th2.join()

print("Fin du programme")
"""
