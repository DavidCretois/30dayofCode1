"""
Day 6 - Aujourd'hui, je travaille sur la création des menus avec Tkinter Python
J'essaye de réaliser des menus pour une simulation d'un microctrôleur comme Raspberry ou Arduino
"""
from tkinter import *

root = Tk()
root.geometry("600x300")
root.title( "Simulation MCU 1.0v" )

menubar = Menu(root,bg="red")

#Menu pour la commande "Fichier"
filemenu = Menu(menubar,tearoff=0,activeborderwidth=10)
filemenu.add_command(label="Créer fichier")
filemenu.add_command(label="Fermer le fichier")
filemenu.add_command(label="Ouvrir le fichier")
filemenu.add_command(label="Ouvrir le dossier")
filemenu.add_command(label="Sauvegarder")
filemenu.add_command(label="Imprimer")
filemenu.add_command(label="Options")
filemenu.add_command(label="Quitter",activebackground="#F13535", command=root.destroy)

#Menu pour la commande "Editer"
editmenu = Menu(menubar,tearoff=0,activeborderwidth=10)
editmenu.add_command(label="Créer une simulation",activebackground="green")
editmenu.add_command(label="Créer un microcontrôleur",activebackground="#965EE9")
editmenu.add_command(label="Raspberry Pi")
editmenu.add_command(label="Couper")
editmenu.add_command(label="Copier")
editmenu.add_command(label="Coller")
editmenu.add_command(label="Supprimer",activebackground="red")

#Menu pour la commande "Microcontrôleurs"
helpmenu = Menu(menubar,tearoff=0,activeborderwidth=5)
helpmenu.add_command(label="Atmel AT91")
helpmenu.add_command(label="ARM Cortex-M")
helpmenu.add_command(label="Atmel AVR")
helpmenu.add_command(label="C167")
helpmenu.add_command(label="Intel 8051")
helpmenu.add_command(label="Intel 8051")
helpmenu.add_command(label="Intel 8085")
helpmenu.add_command(label="Freescal 68HC11")
helpmenu.add_command(label="Freescale 68HC12")
helpmenu.add_command(label="MSP430")
helpmenu.add_command(label="8080")

# Menu pour la commande "Modèles Raspberry Pi"
modelemenu = Menu(menubar,tearoff=0,activeborderwidth=5)
modelemenu.add_command(label="Pico")
modelemenu.add_command(label="400")
modelemenu.add_command(label="B 8GB")
modelemenu.add_command(label="4 B")
modelemenu.add_command(label="3 Model A+")
modelemenu.add_command(label="Zero")
modelemenu.add_command(label="Zero W")
modelemenu.add_command(label="Zero WH")
modelemenu.add_command(label="3")
modelemenu.add_command(label="2")
modelemenu.add_command(label="B")

# Commande Menubar
menubar.add_cascade(label="Fichier",menu=filemenu)
menubar.add_cascade(label="Editer",menu=editmenu)
menubar.add_cascade(label="Microcontrôleurs",menu=helpmenu)
menubar.add_cascade(label="Modèles Raspberry Pi",menu=modelemenu)

root.config(menu=menubar)
root.mainloop() #Et bingo !
