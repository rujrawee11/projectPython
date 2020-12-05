from tkinter import *
from PIL import Image, ImageTk

def question1():
    def sel():
        """1 ans"""
        if str(var.get()) == "1":
            print("no")

        elif str(var.get()) == "2":
            print("no")

        elif str(var.get()) == "3":
            print("yes")

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
    label2 = Label(root, text=" set1 = {'tee', 'noey' ,'por', 'noyna'}", width=38, height = 1)
    canvas.create_window(300, 70, anchor='center', window=label2)
    label3 = Label(root, text="          set2 = {'noey', 'sunthon', 'noyna', 'pop'}", width=38, height = 1)
    canvas.create_window(300, 90, anchor='center', window=label3)
    label4 = Label(root, text="intersec = set1.intersection(set2)", width=38, height = 1)
    canvas.create_window(300, 110, anchor='center', window=label4)
    label5 = Label(root, text="for data in intersec:                           ", width=38, height = 1)
    canvas.create_window(300, 130, anchor='center', window=label5)
    label6 = Label(root, text="print(data)                          ", width=38, height = 1)
    canvas.create_window(300, 150, anchor='center', window=label6)
    #label2.grid(column=0, row=1, columnspan=3, padx=10, pady=3)
    var = IntVar()
    r1 = Radiobutton(root, text="tee         \nsunthon  ", width=15, height=3, variable=var, value=1,
                     bg="white", activebackground='red', command=sel)  # คำตอบแรก active bg = เปลี่ยนสีปุ่มตอนกด
    canvas.create_window(300, 210, anchor='center', window=r1)
    #r1.grid(column=0, row=2, padx=75, pady=30,)
    r2 = Radiobutton(root, text="sunthon  \nnoyna    ", width=15, height=3,variable=var, value=2, bg="white", activebackground='red',command = sel)  # คำตอบสอง
    canvas.create_window(300, 275, anchor='center', window=r2)
    #r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(root, text="noey       \nnoyna     ", width=15, height=3,variable=var, value=3, bg="white", activebackground='green',command = sel)  # คำตอบสาม
    canvas.create_window(300, 340, anchor='center', window=r3)
    #r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(root, text="por       \nnoey     ", width=15, height=3, variable=var,
                     value=4, bg="white", activebackground='red', command=sel)  # คำตอบสาม
    canvas.create_window(300, 405, anchor='center', window=r4)
    #r4.grid(column=1, row=3, padx=15, pady=15)
    label = Label(root)
    label.pack()
    root.mainloop()
question1()
