from tkinter import *                     #est la façon la plus courante faire appel à ce système d'importation,
import time                                 #import TIME, connait le widget

root = Tk()                                      #Crée un widget Tkinter
root.title('Time.com')                              #Nom d'un Widget ou application
root.geometry("400x200")                            #Taille 

def clock():
    hour = time.strftime("%H")                           # Heure %H
    minute = time.strftime("%M")                         # Minute %M
    second = time.strftime("%S")                            # Seconde %S
    day = time.strftime("%A")                               # Jour %A
    time_zone = time.strftime("%Z")                         # Location %Z

    my_label.config(text=hour + ":" + minute + ":" + second)            # Heure + Minutes + Secondes
    my_label.after(1000, clock)                                             #Commencer l'heure

    my_label2.config(text=time_zone + " " + day)                        #Pour affciher la location et le jour

def update():
    my_label.config(text="New Text")                             #Pour affciher le variable "my_label_config" aussi Label c'est pour afficher !

# Pour Label n°1, pour afficher l'heure
my_label = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=40) #taille par dessus du haut

# Pour Label2 = Créer un bloc pour affciher la location et le jour
my_label2 = Label(root, text="", font=("Helvetica", 14))    
my_label2.pack(pady=1)

clock()                                                                     # Affciher la focntion "l'heure" = def clock

my_label.after(5000, update)                                                # Afficher la focntion Update !

root.mainloop()                                                             # Contient des infinies boucles jusqu'a on arrête le Tkinter