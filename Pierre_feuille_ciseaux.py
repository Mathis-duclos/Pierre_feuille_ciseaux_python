from random import randint
import time #importer le module qui permet d'attendre du temps entre deux action


def test():
    n = input("Coup à tester")
    if n == 1:
        print("pierre")
    elif n == 2:
        print ("feuille")
    elif n == 3 :
        print ("ciseaux")

def comparer_coups(J1, J2):
    if J1 == 1 and J2== 2 : # 1 a fait pierre et 2 a fait feuille
        print ("J2 a gagné !!")

    elif J1 == 1 and J2 == 3 : # 1 fait pierre et 2 fait ciseaux
        print ("J1 a gagné !!")

    elif J1 == 2 and J2 == 1 : # 1 a fait feuille et 2 a fait pierre
        print ("J1 a gagné !!")

    elif J1 == 2 and J2 == 3 : # 1 a fait feuille et 2 a fait ciseaix
        print ("J2 a gagné !!")

    elif J1 == 3 and J2 == 1 : # 1 a fait  ciseaux et 2 a fait pierre
        print ("J2 a gagné !!")

    elif J1 == 3 and J2 == 2 : # 1 a fait ciseaux et 2 a fait feuille
        print ("J1 a gagné !!")

    elif J1 == J2 : # personne ne gagne
        print ("égalité !")
        print ("Personne ne gagne...")

    else :
        print ("Erreur ! Ressayez en vérifiant que vos coups sont valides.")

    print ("-----------")
    time.sleep(2.0)
    rejouer = input("Voulez-vous recommencer ?")
    time.sleep(2.0)

    if rejouer == "oui" :
        jouer()

    else :
        print ("Au revoir ! :)")


def partie_contre_joueur():
        J1 = input("Coup du J1 :")
        J2 = input("Coup du J2 :")
        J1 = int(J1)
        time.sleep(0.5)
        J2 = int(J2)
        time.sleep(2.0)
        comparer_coups(J1,J2)


def comparer_coups_ia(J1, J2): # la meme fonction mais en remplacant le message "J2 gagne" par "l'ia gagne"
    if J1 == 1 and J2== 2 : # 1 a fait pierre et 2 a fait feuille
        print ("L'ia a gagné !!")

    elif J1 == 1 and J2 == 3 : # 1 fait pierre et 2 fait ciseaux
        print ("J1 a gagné !!")

    elif J1 == 2 and J2 == 1 : # 1 a fait feuille et 2 a fait pierre
        print ("J1 a gagné !!")

    elif J1 == 2 and J2 == 3 : # 1 a fait feuille et 2 a fait ciseaix
        print ("L'ia a gagné !!")

    elif J1 == 3 and J2 == 1 : # 1 a fait  ciseaux et 2 a fait pierre
        print ("L'ia a gagné !!")

    elif J1 == 3 and J2 == 2 : # 1 a fait ciseaux et 2 a fait feuille
        print ("J1 a gagné !!")

    elif J1 == J2 : # personne ne gagne
        print ("égalité !")
        print ("Personne ne gagne...")

    else : # un des coups n'est pas 1 ; 2 ou 3
        print ("Erreur ! Ressayez en vérifiant que votre coup est valide.")

    print ("-----------")
    time.sleep(2.0)
    rejouer = input("Voulez-vous recommencer ?")
    time.sleep(2.0)
    if rejouer == "oui" : #si le joueur marque oui il rejouera sinon, la partie s'arete
        jouer()

    else :
        print ("Au revoir ! :)")


def partie_contre_ia():
    J1 = input("Coup du J1 :")
    J1 = int(J1)
    time.sleep(0.5)
    print("L'ordinateur remplacera le Joueur 2 (J2).")
    o = randint(1,3) # prend un entier random entre 1 et 3
    time.sleep(1.0)
    print ("L'ordinateur choisi sont coup...")
    time.sleep(1.5)
    if o == 1:
        print ("l'ordinateur à choisi pierre")
    elif o == 2:
        print ("l'ordinateur à choisi feuille")
    elif o == 3:
        print ("l'ordinateur à choisi ciseaux")
    comparer_coups_ia(J1,o)


def jouer():
    print ("Appuyer sur a pour jouer seul")
    print ("ou sur une autre touche pour jouer contre quelqu'un")

    J = input("Jouer seul (a) ou a plusieurs ?")
    J = str(J)

    if J == "a":
        partie_contre_ia()
    else :
        partie_contre_joueur()


def regles():
    print  (" ") # pour sauter une ligne et espacer le texte
    print ("Bienvenue dans le Pierre Feuille Ciseaux en Python !")
    time.sleep(1.5) # pour patienter une quelques temps entre les deux messages
    print ("Vous pouvez jouer contre un ami avec la fonction partie_contre_joueur().")
    time.sleep(1.0)
    print ("ou jouer contre l'ordinateur avec la fonction partie_contre_ia() !")
    time.sleep(0.5)
    print("Les coups de l'ordinateur sont entièrement aléatoire, il ne posède aucune stratégie.")
    time.sleep(2.0)
    print (" ")
    print ("Dans ce promgramme 1 équivaut à jouer Pierre, 2 à jouer Feuille et 3 à jouer Ciseaux.")
    time.sleep(2.0)
    print("Bonne chance et amusez-vous bien !!")
    time.sleep(2.5) #pour attenndre 2,5 secondes
    print(" ")
    print("Ne tappez pas votre ami s'il gagne contre vous " "\U0001F606" " " "\U0001F923") # caracteres unicode pour mettre des emojis
    jouer()

regles()