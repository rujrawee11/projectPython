from tkinter import *
def radiobutton():
    """1 ans"""
    root = Tk()
    root.title("question")#ชื่อlikeeee
    root.geometry("600x500")
    root.option_add("*font","Opun-Mai-Thin 10 bold")
    frame = Frame(root)
    frame.config(background="#C6E0E0")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label1.grid(column=0,row=0, columnspan=2,padx=15,pady=30)
    label2 = Label(frame, text="คำสั่งใดใช้รับข้อมูลทางแป้นพิมพ์?", width=50, height = 5, bg="white")
    label2.grid(column=0, row=1, columnspan=3, padx=10,pady=3)
    var = IntVar()
    r1 = Radiobutton(frame, text="print()", width=15, height=3, variable=var, value=1)#คำตอบแรก
    r1.grid(column=0, row=2, padx=75, pady=30)
    r2 = Radiobutton(frame, text="input()", width=15, height=3 ,variable=var, value=2)  # คำตอบสอง
    r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(frame, text="output()", width=15, height=3, variable=var, value=3)  # คำตอบสาม
    r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(frame, text="compute()", width=15, height=3, variable=var, value=4)  # คำตอบสาม
    r4.grid(column=1, row=3, padx=15, pady=15)
    var.set(1)
    root.mainloop()
radiobutton()

