#check radio button
from tkinter import *

def sel():
   selection = "You selected the option " + str(ans.get())
   label.config(text = selection)

root = Tk()
ans = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=ans, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=ans, value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=ans, value=3,command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()