# Day 4 - Python Create a Database Design Système élève
#Pour l'instant, j'apprends le design de Tkinter et le fonctionnement
# Ensuite j'apprendrais MySQL pour comprendre les données (databases)
# Faut je regarde les tableaux des couleurs pour faire un jolie couleur dans un logiciel
# J'ai compris qu'à quoi sert vraiment le Tkinter mais faudrait j'apprends davantage beaucoup d'autres que Tkinter

from tkinter import *
import tkinter
from tkinter import messagebox

windo = tkinter.Tk()
windo.geometry("800x450")           # Taille
windo.title("Système élèves")       # Titre

L = Label(windo, text = "Entrez l'élève ID: ",font=('arial',30),fg='black')
# Position
L.grid(row=0,column=0)
E = Entry(windo, bd=10, width=50)
E.grid(row=0,column=1)

L1 = Label(windo, text = "Entrez le nom d'élève: ",font=('arial',30),fg='black')
L1.grid(row=1,column=0)
E1 = Entry(windo, bd=10, width=50)
E1.grid(row=1,column=1)

L2 = Label(windo, text = "Entrez l'adresse d'élève': ",font=('arial',30),fg='black')
L2.grid(row=2,column=0)
E2 = Entry(windo, bd=10, width=50)
E2.grid(row=2,column=1)

#Boutton à cliquer pour "Insérer"
Binsert = tkinter.Button(text='Insérer',fg='black',bg='gray63',font=('arial',15,'bold'))
#Position
Binsert.grid(row=5,column=0)

#Bouton à cliquer pour "Update"
BUpdate = tkinter.Button(text='Update',fg='gray4',bg='gray69',font=('arial',20,'bold'))
BUpdate.grid(row=5,column=1)

# Bouton à cliquer pour "Suprimer"
BDelete = tkinter.Button(text='Suprimer',fg='white',bg='Red3',font=('arial',20,'bold'))
BDelete.grid(row=8,column=0)

# Bouton à cliquer pour "Choisir"
BSelect = tkinter.Button(text='Choisir',fg='lavender',bg='DodgerBlue2', font=('arial',20,'bold'))
BSelect.grid(row=8,column=1)

mainloop()