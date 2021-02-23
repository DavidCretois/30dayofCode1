import random
from tkinter import *
from math import *
from time import *
from tkinter import filedialog
from tkinter import font
import tkinter.font as tkFont
import  tkinter as tkr

root = Tk()
root.geometry("800x400")
root.title( "Simulation MCU 1.0v" )
root.config(bg="#ABB2B9")
menubar = Menu(root,bg="red")
global open_status_name
open_status_name = False

# Sauvegarder le fichier
def save_file():
    file = filedialog.asksaveasfile()

# Ouvrir le fichier
def open_file():
    file = filedialog.askopenfile()

# Fermer le fichier
def close_file():
    file = filedialog.asksaveasfilename()

def openAT91():
    new_window = Toplevel(root)
    new_window.geometry("1200x800")
    new_window.config(bg="#ABB2B9")
    new_window.title("Atmel AT91")
    new_window.resizable(True)
    photoMCU = PhotoImage(file='C:\\Users\\NaKoO\Desktop\\Learn To code\\Project Developers\\Tkinter Python\\Project Software\\images\\AT91.png')
    label = Label(new_window, image=photoMCU)
    lbl = Label(new_window, text="Microcontrôleur ATMEL")
    lbl.pack
    pic = "C:\\Users\\NaKoO\Desktop\\Learn To code\\Project Developers\\Tkinter Python\\Project Software\\images\\AT91.png"
    pic1 = new_window.Image.open(pic)
    photo = new_window.PhotoImage(pic1)
    label1 = new_window.Label(root, image=photo)
def ARMCortexM():
    new_window = Toplevel(root)
    new_window.geometry("1200x800")
    new_window.title("ARM Cortex-M")
    new_window.resizable(False)
    lbl = Label(new_window, text="Microcontrôleur ARM")
    lbl.pack
    ButtonExit = Button(new_window, background="blue", text="Annuler", command=lambda: new_window.destroy())
    ButtonExit.place(50, 50)
    ButtonExit.pack()

def AtmelAVR():
    new_window = Toplevel(root)
    new_window.geometry("1200x800")
    new_window.title("Atmel AVR")
    new_window.resizable(True)
    lbl = Label(new_window, text="Microcontrôleur ATMEL")
    lbl.pack
    ButtonExit = Button(new_window, background="blue", text="Annuler", command=lambda: new_window.destroy())
    ButtonExit.place(50, 50)
    ButtonExit.pack()

def C167():
    new_window = Toplevel(root)
    new_window.geometry("1200x800")
    new_window.title("C167")
    new_window.resizable(True)
    lbl = Label(new_window, text="Microcontrôleur C167")
    lbl.pack
    ButtonExit = Button(new_window, background="blue", text="Annuler", command=lambda: new_window.destroy())
    ButtonExit.place(50, 50)
    ButtonExit.pack()


# Les boutons
Button1 = Button(root, text="Atmel AT91", padx=60, pady=8, bg="#6B7A89")
Button1.place(x=10, y =80)


Button2 = Button(root, text="ARM Cortex-M", padx=60, pady=8, bg="#6B7A89")
Button2.place(x=10, y =130)

Button3 = Button(root, text="Atmel AVR", padx=60, pady=8, bg="#6B7A89")
Button3.place(x=250, y =80)

Button4 = Button(root, text="C167", padx=60, pady=8, bg="#6B7A89")
Button4.place(x=250, y =130)

Button5 = Button(root, text="Intel 8051", padx=60, pady=8, bg="#6B7A89")
Button5.place(x=10, y =180)

Button6 = Button(root, text="Intel 8051", padx=60, pady=8, bg="#6B7A89")
Button6.place(x=10, y =230)

Button7 = Button(root, text="Freescal 68HC11", padx=60, pady=8, bg="#6B7A89")
Button7.place(x=250, y =180)

Button8 = Button(root, text="Freescale 68HC12", padx=60, pady=8, bg="#6B7A89")
Button8.place(x=250, y =230)


#Menu pour la commande "Fichier"
filemenu = Menu(menubar,tearoff=0,activeborderwidth=10)
filemenu.add_command(label="Créer fichier")
filemenu.add_command(label="Fermer le fichier", command=close_file)
filemenu.add_command(label="Ouvrir le fichier", command=open_file)
filemenu.add_command(label="Ouvrir le dossier", command=open_file)
filemenu.add_command(label="Sauvegarder", command=save_file)
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
helpmenu.add_command(label="Atmel AT91", command=openAT91,activebackground="#C0392B")
helpmenu.add_command(label="ARM Cortex-M", command=ARMCortexM,activebackground="#E74C3C")
helpmenu.add_command(label="Atmel AVR", command=AtmelAVR,activebackground="#9B59B6")
helpmenu.add_command(label="C167", command=C167,activebackground="#8E44AD")
helpmenu.add_command(label="Intel 8051",activebackground="#2980B9")
helpmenu.add_command(label="Intel 8051", activebackground="#3498DB")
helpmenu.add_command(label="Intel 8085", activebackground="#16A085")
helpmenu.add_command(label="Freescal 68HC11", activebackground="#27AE60")
helpmenu.add_command(label="Freescale 68HC12", activebackground="#F1C40F")
helpmenu.add_command(label="MSP430", activebackground="#F39C12")
helpmenu.add_command(label="8080", activebackground="#D35400")

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
