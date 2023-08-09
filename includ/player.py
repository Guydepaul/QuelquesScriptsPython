#coding:utf-8
def parler (personnage, message):
    print("{} : {}".format(personnage, message))

def au_revoir():
    print("Au revoir:) !")

if __name__ == "__main__":
    
    parler("guy", "je vais bien!")
    au_revoir()