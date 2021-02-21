from tkinter import *
from tkinter.ttk import *
import time

def start():
    import time
    for i in range(1,100,1):
        progress['value'] = 1
        root.update_idletasks()
        label1.config(text=str(i)+"%")
        time.sleep(0.05)
    progress['value'] = 100

def stop():
    root.destroy()

root = Tk()

label1 = Label(root,font="arial 15 bold")
label1.pack(padx=100,pady=5)

s = Style()
s.configure("IProgressbar", foreground = "black", background="green", thickness=40)

progress = Progressbar(length=400, mode="determinate")
progress.pack(padx=10,pady=10)

button = Button(text="Start", command=start)
button.pack(pady=10)

button1 = Button(root, text="Stop", command=stop)
button1.pack(pady=10)

root.title("Loading")
root.mainloop()
