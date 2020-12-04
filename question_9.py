from tkinter import*

def question9():  
    def sel():
        """1 ans"""
        if str(var1.get()) == str(c1):
            print("no")

        elif str(var2.get()) == str(c2):
            print("no")

        elif str(var3.get()) == str(c3):
            print("YES")
            
        elif str(var4.get()) == str(c4):
            print("no")

        elif str(var5.get()) == str(c5):
            print("no")
    root = Tk()
    root.title("checkbox")
    root.geometry("600x500")
    root.option_add("font", 'Opun-Mai-Thin 40 bold')
    frame = Frame(root)
    frame.config(background="#FFC7C7")
    frame.place(width=600, height=500,x=0,y=0)
    root.option_add("*foreground", "#444F5A")
    root.option_add("*background", "#F6F6F6")
    root.option_add("*Label.font", "tahoma 11 bold ")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label2 = Label(frame, text=" set1 = {'tee', 'noey' ,'por', 'noyna'}", width=38, height = 1)
    label3 = Label(frame, text="          set2 = {'noey', 'sunthon', 'noyna', 'pop'}", width=38, height = 1)
    label4 = Label(frame, text="intersec = set1.intersection(set2)", width=38, height = 1)
    label5 = Label(frame, text="for data in intersec:                           ", width=38, height = 1)
    label6 = Label(frame, text="print(data)                          ", width=38, height = 1)
    label1.grid(column=0, row=0, padx=80, pady=15)
    label2.grid(column=0, row=1, padx=80, pady=0.1)
    label3.grid(column=0, row=2, padx=80, pady=0.1)
    label4.grid(column=0, row=3, padx=80, pady=0.1)
    label5.grid(column=0, row=4, padx=80, pady=0.1)
    label6.grid(column=0, row=5, padx=80, pady=0.1)
    var1 = IntVar()
    c1 = Checkbutton(frame, text="tee          ", width=20, height=1, variable=var1, anchor=CENTER,
                bg="white", activebackground='red', command=sel)
    c1.grid(column=0, row=6, padx=80, pady=10)
    var2 = IntVar()
    c2 = Checkbutton(frame, text="sunthon ", width=20, height=1, variable=var2, anchor=CENTER,
                    bg="white", activebackground='red', command=sel)
    c2.grid(column=0, row=7, padx=80, pady=10)
    var3 = IntVar()
    c3 = Checkbutton(frame, text="noey       ", width=20, height=1, variable=var3, anchor=CENTER,
                    bg="white", activebackground='green', command=sel)
    c3.grid(column=0, row=8, padx=80, pady=10)
    var4 = IntVar()
    c4 = Checkbutton(frame, text="noyna     ", width=20, height=1, variable=var4, anchor=CENTER,
                    bg="white", activebackground='green', command=sel)
    c4.grid(column=0, row=9, padx=80, pady=10)
    var5 = IntVar()
    c5 = Checkbutton(frame, text="por          ", width=20, height=1, variable=var5, anchor=CENTER,
                    bg="white", activebackground='red', command=sel)
    c5.grid(column=0, row=10, padx=80, pady=10)
    label = Label(root)
    label.pack()
    root.mainloop()
question9()