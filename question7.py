#Question7
from tkinter import *
def question7():  
    def sel():
        """1 ans"""
        if str(var.get()) == "1":
            print("no")

        elif str(var.get()) == "2":
            print("YES")

        elif str(var.get()) == "3":
            print("no")
            
        elif str(var.get()) == "4":
            print("no")
    """1 ans"""
    root = Tk()
    root.title("question")#ชื่อ
    root.geometry("600x500")
    root.option_add("*font","Opun-Mai-Thin 10 bold")
    frame = Frame(root)
    frame.config(background="#FFCDCD")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label1.grid(column=0,row=0, columnspan=2,padx=15,pady=30)
    label2 = Label(frame, text=" คอมพิวเตอร์ใช้ภาษาระดับใด ?", width=50, height = 5, bg="white")
    label2.grid(column=0, row=1, columnspan=3, padx=10,pady=3)
    var = IntVar()
    r1 = Radiobutton(frame, text="python", width=15, height=3, variable=var, value=1,
                    bg="white", activebackground='red', command=sel)#คำตอบแรก
    r1.grid(column=0, row=2, padx=75, pady=30)
    r2 = Radiobutton(frame, text="machine", width=15, height=3 ,variable=var, value=2,
                    bg="white", activebackground='green', command=sel)  # คำตอบสอง
    r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(frame, text="high-level", width=15, height=3, variable=var, value=3,
                    bg="white", activebackground='red', command=sel)  # คำตอบสาม
    r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(frame, text="natural", width=15, height=3, variable=var, value=4,
                    bg="white", activebackground='red', command=sel)  # คำตอบสาม
    r4.grid(column=1, row=3, padx=15, pady=15)
    label = Label(root)
    label.pack()
    root.mainloop()
question7()