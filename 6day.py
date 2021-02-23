from tkinter import *
import tkinter.font as tkFont
import  tkinter as tk
from tkinter import PhotoImage

root = Tk()
root.geometry("800x400")
root.title( "Simulation MCU 1.0v" )
root.config(bg="#100e17")
menubar = Menu(root,bg="red")

# Les boutons
Button1 = Button(root, text="Atmel AT91", padx=50, pady=8, bg="#6B7A89")
Button1.place(x=10, y =80)

Button2 = Button(root, text="ARM Cortex-M", padx=50, pady=8, bg="#6B7A89")
Button2.place(x=10, y =130)

Button3 = Button(root, text="Atmel AVR", padx=50, pady=8, bg="#6B7A89")
Button3.place(x=250, y =80)

Button4 = Button(root, text="C167", padx=50, pady=8, bg="#6B7A89")
Button4.place(x=250, y =130)

Button5 = Button(root, text="Intel 8051", padx=50, pady=8, bg="#6B7A89")
Button5.place(x=10, y =180)

Button6 = Button(root, text="Intel 8051", padx=50, pady=8, bg="#6B7A89")
Button6.place(x=10, y =230)

Button7 = Button(root, text="Freescal 68HC11", padx=50, pady=8, bg="#6B7A89")
Button7.place(x=250, y =180)

Button8 = Button(root, text="Freescale 68HC12", padx=50, pady=8, bg="#6B7A89")
Button8.place(x=250, y =230)


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
