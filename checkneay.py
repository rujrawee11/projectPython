"""check"""
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


"""def scores():
    global score
    global ans
    ans = score + 3
    print(ans) """
global score
global count
global ans
score = 0
count = 0
ans = 0

def q1():
    def a():
        global score
        global count
        global ans
        if str(var.get()) == "1":
            print("0", var.get())
            count += 1
            ans = 1
            if count >= 1:
                ans = 0
                count = 0
            click()
            score += ans
            print(count)
            print(ans)
            print(score)
            
            

        elif str(var.get()) == "2":
            print("1", var.get())
            count += 1
            ans = 0
            if count >= 1:
                ans = 0
                count = 0
            click()
            score += ans
            print(count)
            print(ans)
            print(score)

        elif str(var.get()) == "3":
            print("2", var.get())
            count += 1
            ans = 0
            if count >= 1:
                ans = 0
                count = 0
            click()
            score += ans
            print(count)
            print(ans)
            print(score)

            click1()

        elif str(var.get()) == "4":
            print("3",var.get())
            count += 1
            ans = 0
            if count > 1:
                ans = 0
                count = 0
            click()
            score += ans
            print(count)
            print(ans)
            print(score)
            click1()

    root = Tk()
    root.title("question")  # ชื่อ
    root.geometry("600x500")
    root.option_add("*font", "Opun-Mai-Thin 10 bold")
    canvas = Canvas(root, width=600, height=500)
    canvas.pack()

    photo = ImageTk.PhotoImage(Image.open('Q2.png'))
    canvas.create_image(300, 250, image=photo)

    label2 = Label(root, text="ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?",
                   width=50, height=5, bg="white")
    canvas.create_window(300, 105, anchor='center', window=label2)
    var = IntVar()

    r1 = Radiobutton(root, text="19", width=15, height=3, variable=var, value=1,
                     bg="white", command=a)  # คำตอบแรก active bg = เปลี่ยนสีปุ่มตอนกด
    canvas.create_window(300, 190, anchor='center', window=r1)

    r2 = Radiobutton(root, text="33", width=15, height=3, variable=var,
                     value=2, bg="white", command=a)  # คำตอบสอง
    canvas.create_window(300, 260, anchor='center', window=r2)

    r3 = Radiobutton(root, text="22", width=15, height=3, variable=var,
                     value=3, bg="white", command=a)  # คำตอบสาม
    canvas.create_window(300, 330, anchor='center', window=r3)

    r4 = Radiobutton(root, text="-11", width=15, height=3, variable=var,
                     value=4, bg="white", command=a)  # คำตอบสาม
    canvas.create_window(300, 400, anchor='center', window=r4)
    
    label = Label(root)
    
    label.pack()
    def click():
        submitBtn = Button(root, text="SUBMIT", bg='#138fa9', borderwidth=0, command=root.quit,activebackground='green' ,anchor='center')
        canvas.create_window(400, 300, width=40, height=60, anchor='center', window=submitBtn)
    def click1():
        submitBtn = Button(root, text="SUBMIT", bg='#138fa9', borderwidth=0, command=root.quit, activebackground='red' ,anchor='center')
        canvas.create_window(400, 300,width = 40, height = 60,anchor='center', window=submitBtn)
    
    root.mainloop()
q1()
print(score)
#ans = q1()
"""def sel():
    score += ans.a()"""

