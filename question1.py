from tkinter import *
from PIL import Image, ImageTk

def question1():
    def sel(): #ฟังก์ชัน
        """1 ans"""
        if str(var.get()) == "1":
            print("YES")

        elif str(var.get()) == "2":
            print("no")

        elif str(var.get()) == "3":
            print("no")

        elif str(var.get()) == "4":
            print("no")

    root = Tk()
    root.title("question")  # ชื่อ
    root.geometry("600x500")
    root.option_add("*font", "Opun-Mai-Thin 10 bold")

    canvas = Canvas(root, width=600, height=500)
    canvas.pack()

    photo = ImageTk.PhotoImage(Image.open('Q2.png'))
    canvas.create_image(300, 250, image=photo)
    #frame = Frame(root)
    #frame.config(background="#FFCDCD")
    #frame.place(width=600, height=500, x=0, y=0)
    #root.option_add("*foreground", "navy")
    # label1 = Label(root, text="QUESTION ?", width=15, height=2, bg="white")
    # canvas.create_window(300, 40, anchor='center', window=label1)
    #label1.grid(column=0, row=0, columnspan=2, padx=15, pady=30)
    label2 = Label(root, text="ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?",width=50, height=5, bg="white")
    canvas.create_window(300, 105, anchor='center', window=label2)
    #label2.grid(column=0, row=1, columnspan=3, padx=10, pady=3)
    var = IntVar()
    r1 = Radiobutton(root, text="19", width=15, height=3, variable=var, value=1,
                     bg="white", activebackground='green', command=sel)  # คำตอบแรก active bg = เปลี่ยนสีปุ่มตอนกด
    canvas.create_window(300, 190, anchor='center', window=r1)
    #r1.grid(column=0, row=2, padx=75, pady=30,)
    r2 = Radiobutton(root, text="33", width=15, height=3,variable=var, value=2, bg="white", activebackground='red',command = sel)  # คำตอบสอง
    canvas.create_window(300, 260, anchor='center', window=r2)
    #r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(root, text="22", width=15, height=3,variable=var, value=3, bg="white", activebackground='red',command = sel)  # คำตอบสาม
    canvas.create_window(300, 330, anchor='center', window=r3)
    #r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(root, text="-11", width=15, height=3, variable=var,
                     value=4, bg="white", activebackground='red', command=sel)  # คำตอบสาม
    canvas.create_window(300, 400, anchor='center', window=r4)
    #r4.grid(column=1, row=3, padx=15, pady=15)
    label = Label(root)
    label.pack()
    root.mainloop()
question1()
