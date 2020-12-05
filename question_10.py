from tkinter import*
from PIL import Image, ImageTk
def question10():  
    def sel():
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
    root.title("checkbox")
    root.geometry("600x500")
    root.option_add("font", 'Opun-Mai-Thin 40 bold')

    canvas = Canvas(root, width=600, height=500)
    canvas.pack()

    photo = ImageTk.PhotoImage(Image.open('Q2.png'))
    canvas.create_image(300, 250, image=photo)
    # frame = Frame(root)
    # frame.config(background="#F9ACC0")
    # frame.place(width=600, height=500,x=0,y=0)
    # root.option_add("*foreground", "navy")
    # root.option_add("*background", "white")
    # root.option_add("*Label.font", "tahoma 11 bold ")
    label1 = Label(root, text='word = "IT_KMITL"', width=40, height = 3, bg="white")
    canvas.create_window(300, 90, anchor='center', window=label1)
    label3 = Label(root, text="ต้องprint()อย่างไรเพื่อที่จะแสดงผลลัพธ์ตัวสุดท้าย", width=40, height = 3,  bg="white")
    canvas.create_window(300, 120, anchor='center', window=label3)
    # label1.grid(column=0, row=0, padx=80, pady=15)
    # label2.grid(column=0, row=1, padx=80, pady=0.1)
    # label3.grid(column=0, row=2, padx=80, pady=0.1)
    var = IntVar()
    r1 = Radiobutton(root, text="word[-1]     ",  width=15, height=3, variable=var, value=1,
                    bg="white", activebackground='green', command=sel)
    canvas.create_window(300, 190, anchor='center', window=r1)
    # c1.grid(column=0, row=6, padx=80, pady=10)
    # var2 = IntVar()
    r2 = Radiobutton(root, text="word[6:8]    ",  width=15, height=3, variable=var, value=2,
                    bg="white", activebackground='green', command=sel)
    canvas.create_window(300, 260, anchor='center', window=r2)
    # c2.grid(column=0, row=7, padx=80, pady=10)
    # var3 = IntVar()
    r3 = Radiobutton(root, text="word[4:]      ",  width=15, height=3, variable=var, value=3,
                    bg="white", activebackground='green', command=sel)
    canvas.create_window(300, 330, anchor='center', window=r3)
    # c3.grid(column=0, row=8, padx=80, pady=10)
    # var4 = IntVar()
    r4 = Radiobutton(root, text="word[3:8]    ",  width=15, height=3, variable=var, value=4,
                        bg="white", activebackground='red', command=sel)
    canvas.create_window(300, 400, anchor='center', window=r4)
    # c4.grid(column=0, row=9, padx=80, pady=10)
    label = Label(root)
    label.pack()
    root.mainloop()
question10()