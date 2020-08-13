# Day 1 - Python GUI Calculator
#That's means its first project for Python to Beginners

import tkinter
from tkinter import *

val = ""
A = 0
operator = ""

#def, une fonction 
def btn_1_estcliquer():#Bouton pour la 1
    global val
    val = val + "1"
    v.set(val)

def btn_2_estcliquer():#Bouton pour la 2
    global val
    val = val + "2"
    v.set(val)

def btn_3_estcliquer():#Bouton pour la 3
    global val
    val = val + "3"
    v.set(val)

def btn_4_estcliquer():#Bouton pour la 4
    global val
    val = val + "4"
    v.set(val)

def btn_5_estcliquer():#Bouton pour la 5
    global val
    val = val + "5"
    v.set(val)

def btn_6_estcliquer():#Bouton pour la 6
    global val
    val = val + "6"
    v.set(val)

def btn_7_estcliquer():#Bouton pour la 7
    global val
    val = val + "7"
    v.set(val)

def btn_8_estcliquer():#Bouton pour la 8
    global val
    val = val + "8"
    v.set(val)

def btn_9_estcliquer():#Bouton pour la 9
    global val
    val = val + "9"
    v.set(val)

def btn_0_estcliquer():#Bouton pour la 0
    global val
    val = val + "0"
    v.set(val)

def btn_16_estcliquer():#Bouton pour la division
    global val
    val = val + "/"
    v.set(val)

def btn_17_estcliquer():#Bouton pour la égale
    global A
    global operator
    global val
    A = 0
    operator = ""
    val = ""
    v.set(val)

def btn_18_estcliquer():#Bouton pour la 
    global val
    val = val + "x"
    v.set(val)

def btn_20_estcliquer(): #+
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    v.set(val)

def btn_21_estcliquer(): #-
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    v.set(val)

def btn_22_estcliquer(): #x
    global A
    global operator
    global val
    A = int(val)
    operator = "x"
    val = val + "x"
    v.set(val)

def btn_23_estcliquer(): #=
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    v.set(val)

def result():               #Bouton égale
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        v.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        v.set(val)
    if operator == "x":
        x = int((val2.split("x")[1]))
        C = A * x
        val = str(C)
        v.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            v.set(val)
        else:
            C = int(A / x)
            v.set(C)


root = tkinter.Tk()                                                     #Obliger d'utiliser cet balisage pour allumer
root.geometry("250x400+300+300")                                     # Taille de l'onglet et taille de l'interface
root.resizable(0,0)
root.title("Calculatrice")                                           #Titre du logiciel

v = StringVar()          # Mémorise une chaîne de caractères; sa valeur par défaut est ''
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 22),
    textvariable = v,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand= True, fill = "both")


btnrow1 = Frame(root,bg="#000100")                                  # Couleur de background (arrière-plan)
btnrow1.pack(expand = True, fill = "both",)

# Maintenant on fait la deuxième ligne mais en blanc car Frame(root) = Blanche
btnrow2 = Frame(root)                                               # Coleur de background (arrière-plan)
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root)                                                # Couleur de background (arrière-plan)
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root)                                               # Couleur de background (arrière-plan)
btnrow4.pack(expand = True, fill = "both",)

# Maintenant on va cliquer des buttons voici des commandes:
btn1 = Button(
    btnrow1,
    text = "1",                                              # Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,                                             #la bordure = 0, ou 1
    command = btn_1_estcliquer,                             #commande via def = focntion
)

btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(                                                  #Pour bouton numéro 2
    btnrow1,        
    text = "2",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_2_estcliquer,
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(                                                  #Pour bouton numéro 3
    btnrow1,        
    text = "3",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
     relief = GROOVE,
    border = 0,
    command = btn_3_estcliquer,

)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btn4 = Button(                                                  #Pour bouton numéro 4
    btnrow1,        
    text = "+",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_20_estcliquer,
)
btn4.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
    btnrow2,
    text = "4",                                              # Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_4_estcliquer,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(                                                  #Pour bouton numéro 2
    btnrow2,        
    text = "5",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_5_estcliquer,
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(                                                  #Pour bouton numéro 3
    btnrow2,        
    text = "6",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_6_estcliquer,
)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btn4 = Button(                                                  #Pour bouton numéro 4
    btnrow2,        
    text = "-",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_21_estcliquer,
)
btn4.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
    btnrow3,
    text = "7",                                              # Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_7_estcliquer,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(                                                  #Pour bouton numéro 2
    btnrow3,        
    text = "8",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_8_estcliquer
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(                                                  #Pour bouton numéro 3
    btnrow3,        
    text = "9",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_9_estcliquer,
)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btn4 = Button(                                                  #Pour bouton numéro 4
    btnrow3,        
    text = "x",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_22_estcliquer,

)
btn4.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
    btnrow4,
    text = "C",                                              # Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_17_estcliquer,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(                                                  #Pour bouton numéro 2
    btnrow4,        
    text = "0",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = btn_0_estcliquer,
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(                                                  #Pour bouton numéro 3
    btnrow4,        
    text = "=",                                             #Texte
    font = ("Verdana", 22),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 0,
    command = result,
)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btn4 = Button(                                                  #Pour bouton numéro 4
    btnrow4,        
    text = "OFF",                                             #Texte
    font = ("Verdana", 18),                                 # Police, taille pour "font"
    relief = GROOVE,
    border = 1,
)
btn4.pack(side = LEFT, expand = True, fill = "both", )

root.mainloop()                                            #contient notre boucle infinie dont on ne sortira que lorsqu’on fermera la fenêtre.


#Day1 réussi, tests réussi mais la division sera enlevé parce que j'y arrivais pas
#TOTAL : 3h 