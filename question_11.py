from tkinter import*
def question11():  
    def sel():
        """1 ans"""
        if str(var1.get()) == 1:
            print("no")

        elif str(var2.get()) == 2:
            print("no")

        elif str(var3.get()) == 3:
            print("no")
            
        elif str(var4.get()) == 4:
            print("YES")

        elif str(var5.get()) == 5:
            print("YES") #11
    root = Tk()
    root.title("checkbox")
    root.geometry("600x500")
    root.option_add("font", 'Opun-Mai-Thin 40 bold')
    frame = Frame(root)
    frame.config(background="#C6E0E0")
    frame.place(width=600, height=500,x=0,y=0)
    root.option_add("*foreground", "navy")
    root.option_add("*background", "white")
    root.option_add("*Label.font", "tahoma 11 bold ")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label2 = Label(frame, text="ข้อใดเป็นตัวแปรชนิด list")
    label1.grid(column=0, row=0, padx=80, pady=15)
    label2.grid(column=0, row=1, padx=80, pady=0.1)
    var1 = IntVar()
    c1 = Checkbutton(frame, text="a = {1, 2, 3, 4, 5}    ", width=50, variable=var1, anchor=CENTER, onvalue=1,
                    bg="white", activebackground='red', command=sel)
    c1.grid(column=0, row=6, padx=80, pady=10)
    var2 = IntVar()
    c2 = Checkbutton(frame, text="a = (1, 2, 3, 4, 5)    ", width=50,variable=var2, anchor=CENTER, onvalue=2,
                    bg="white", activebackground='red', command=sel)
    c2.grid(column=0, row=7, padx=80, pady=10)
    var3 = IntVar()
    c3 = Checkbutton(frame, text="a = <1, 2, 3, 4, 5> ", width=50, variable=var3, anchor=CENTER, onvalue=3,
                    bg="white", activebackground='red', command=sel)
    c3.grid(column=0, row=8, padx=80, pady=10)
    var4 = IntVar()
    c4 = Checkbutton(frame, text="a = [1, 2, 3, 4, 5]    ", width=50, variable=var4, anchor=CENTER, onvalue=4,
                    bg="white", activebackground='green', command=sel)
    c4.grid(column=0, row=9, padx=80, pady=10)
    var5 = IntVar()
    c5 = Checkbutton(frame, text="a = [[1, 2], 3, 4, 5]   ", width=50, variable=var5, anchor=CENTER, onvalue=5,
                    bg="white", activebackground='green', command=sel)
    c5.grid(column=0, row=10, padx=80, pady=10)
    label = Label(root)
    label.pack()
    root.mainloop()
question11()