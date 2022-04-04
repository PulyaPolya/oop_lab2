from tkinter import *
import random
from numpy.random import choice
from tkinter import messagebox
import numpy as np
def chooseOne(res):
    userInput.delete(0, END)
    userInput.insert(0, res)
    return

def generate():
    set = [1,0]
    r = np.random.choice(set, p = [4/5, 1/5])
    if r == 1:
        string = "Nada! try again"
    else:
        string = "Great! You found the ring"
    return string

def welcomeMessage():
    name = name_Tf.get()
    return messagebox.showinfo('message',f'Hi! {name}, Welcome to python guides.')
ws = Tk()

ws.title("find the ring")
ws.geometry("400x250")
frame = Frame(ws)

userInput = Entry(frame, width=40, justify=CENTER)
userInput.grid(row=0, columnspan=4, padx=5, pady= 10)
title = generate()
Button(frame,text="Box 1",command=lambda:chooseOne(title)).grid(row=1, column=0)
title1 = generate()
Button(frame,text="Box 2 ",command=lambda:chooseOne(title1)).grid(row=1, column=1)
title2 = generate()
Button(frame,text="Box 3",command=lambda:chooseOne(title2)).grid(row=1, column=2)
title3 = generate()
Button(frame,text="Box 4",command=lambda:chooseOne(title3)).grid(row=1, column=3)
title4 = generate()
Button(frame,text="Box 5",command=lambda:chooseOne(title4)).grid(row=2, column=0)

name_Tf = Entry(ws)
name_Tf.pack()
frame.pack()
Button(ws, text="Click Here", command=welcomeMessage).pack()
ws.mainloop()

