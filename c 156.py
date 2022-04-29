from tkinter import *
import random
from PIL import ImageTk ,Image

root=Tk()
root.configure(background="orange")
root.title("Endless Pokemon Game")
root.geometry("800x600")
labelplayer1=Label(root,text="player 1",background="red",fg="white")
labelplayer1.place(relx=0.1,rely=0.3,anchor=CENTER)
labelplayer2=Label(root,text="player 2",background="red",fg="white")
labelplayer2.place(relx=0.1,rely=0.4,anchor=CENTER)
labelscore=Label(root)
labelscore.place(relx=0.2,rely=0.5)

root.mainloop()