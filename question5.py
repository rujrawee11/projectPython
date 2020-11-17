#Question5
from tkinter import *
def radiobutton():
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
    label2 = Label(frame, text="กระบวนการในการปรับปรุงโปรแกรมที่ทำงานได้ถูกต้องอยู่แล้ว \nเพื่อเพิ่มคุณภาพของโปรแกรมให้ดีขึ้น เรียกว่าอะไร ?", width=50, height = 5, bg="white")
    label2.grid(column=0, row=1, columnspan=3, padx=10,pady=3)
    var = IntVar()
    r1 = Radiobutton(frame, text="Encapsulation", width=15, height=3, variable=var, value=1)#คำตอบแรก
    r1.grid(column=0, row=2, padx=75, pady=30)
    r2 = Radiobutton(frame, text="Generalization", width=15, height=3 ,variable=var, value=2)  # คำตอบสอง
    r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(frame, text="Refactoring", width=15, height=3, variable=var, value=3)  # คำตอบสาม
    r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(frame, text="Map", width=15, height=3, variable=var, value=4)  # คำตอบสาม
    r4.grid(column=1, row=3, padx=15, pady=15)
    var.set(1)
    root.mainloop()
radiobutton()