# Day 3 - Python Password "Confirm" or "Refused"
# Aujourd'hui, je m'interesse un peu aux mot de passe et comprendre
#la logique du python, la prochaine fois, j'apprendrais le module "math"
# dans une série 30DayOfCode, permet de réussir dans la matière mathématiques


while True:                                                  # while True = boucle infinie [Else] Sinon
    Motdepasse = input("Quel est le mot de passe ?")         # "Motdepasse" est une variable, input = pour demander quel mot de passe
    if Motdepasse == "Dave":                                 # Si "Motdepasse" est Dave [ICI : vous choisissez le mot de passe.]
        print("Mot de passe réussie")                        # Donc si vous tapez le bon mot de passe = Dave, c'est "print" = cela veut dire afficher
        break                                                # Stoppez suivant la fonctionn "while True" donc si le mot de passe est bo, pas besoin de redemandez
    else:                                                    # "Else" cela veut dire Sinon, donc si la varible "Motdepasse" n'est pas bon
        print("Mot de passe incorrect")                      # Cela affiche "Mot de passe incorrect"


# Cela peut servir pour un bon début sur le cybersécurité ou les pirates
# Mais j'apprendrais le module plein de choses !