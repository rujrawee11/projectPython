from tkinter import*
def question12():  
    def sel():
        """1 ans"""
        if str(var1.get()) == "1":
            print("YES")

        elif str(var2.get()) == "2":
            print("no")

        elif str(var3.get()) == "3":
            print("YES")
            
        elif str(var4.get()) == "4":
            print("YES")

        elif str(var5.get()) == "5":
            print("no") #12
    root = Tk()
    root.title("checkbox")
    root.geometry("600x500")
    root.option_add("font", 'Opun-Mai-Thin 40 bold')
    frame = Frame(root)
    frame.config(background="#C6E0E0")
    frame.place(width=600, height=500,x=0,y=0)
    root.option_add("*foreground", "navy")
    root.option_add("*background", "white")
    root.option_add("*Label.font", "tahoma 11 bold")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label2 = Label(frame, text="ข้อใดมีผลลัพธ์ True?")
    label1.grid(column=0, row=0, padx=80, pady=10)
    label2.grid(column=0, row=1, padx=80, pady=0.1)
    var1 = IntVar()
    c1 = Checkbutton(frame, text="True and True or False and True       ", width=50, variable=var1, anchor=CENTER,
                    bg="white", activebackground='green', command=sel)
    c1.grid(column=0, row=2, padx=80, pady=10)
    var2 = IntVar()
    c2 = Checkbutton(frame, text="False and True or False and True      ", width=50,variable=var2, anchor=CENTER,
                    bg="white", activebackground='red', command=sel)
    c2.grid(column=0, row=3, padx=80, pady=10)
    var3 = IntVar()
    c3 = Checkbutton(frame, text="True or (8-5 == 3) and True or False", width=50, variable=var3, anchor=CENTER,
                    bg="white", activebackground='green', command=sel)
    c3.grid(column=0, row=4, padx=80, pady=10)
    var4 = IntVar()
    c4 = Checkbutton(frame, text="(2 >= 0) or (-5 <= -8)                         ", width=50, variable=var4, anchor=CENTER,
                    bg="white", activebackground='green', command=sel)
    c4.grid(column=0, row=5, padx=80, pady=10)
    var5 = IntVar()
    c5 = Checkbutton(frame, text="not(9 != 2)                                           ", width=50, variable=var5, anchor=CENTER,
                    bg="white", activebackground='red', command=sel)
    c5.grid(column=0, row=6, padx=80, pady=10)
    label = Label(root)
    label.pack()
    root.mainloop()
question12()