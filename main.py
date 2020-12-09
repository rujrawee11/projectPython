import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from routes import *


def menu():
    """start menu"""
    root = Tk()  # สร้างหน้าต่าง
    root.title("Rock Paper Scissors Game")  # ชื่อเกม
    root.geometry("600x500")  # ขนาดจอ
    root.option_add("*font", "tahoma 10 bold")  # font
    canvas = Canvas(root, width=600, height=500)
    canvas.pack()
    
    photo = ImageTk.PhotoImage(Image.open('images/bg.png'))
    canvas.create_image(300, 250, image=photo)

    gameTitle = Label(root, text="Rock Paper Scissors Game", bg='#138fa9', fg='white', font=("Adobe Gothic Std B", 30))
    canvas.create_window(300, 60, anchor='center', window=gameTitle)

    route = WindowRoute(root)
    startBtnImg = ImageTk.PhotoImage(Image.open('images/start_btn.png'))
    startBtn = Button(root, text="Start", bg='#138fa9', image=startBtnImg , borderwidth=0, command=route.startGame, anchor='center')
    canvas.create_window(300, 345, anchor='center', window=startBtn)

    quitBtnImg = ImageTk.PhotoImage(Image.open('images/quit_btn.png'))
    quitBtn = Button(root, text="Quit", bg='#138fa9', image=quitBtnImg , borderwidth=0, command=route.on_closing, anchor='center')
    canvas.create_window(300, 440, anchor='center', window=quitBtn)

    nextBtnImg = ImageTk.PhotoImage(Image.open('images/instruction_btn.png'))
    nextBtn = Button(root, text="Instruction", bg='#138fa9', image=nextBtnImg , borderwidth=0, command=route.instruction, anchor='s')
    canvas.create_window(150, 485, anchor='s', window=nextBtn)

    root.protocol("WM_DELETE_WINDOW", route.on_closing) # on close window
    root.mainloop()  # แสดงผลหน้าต่าง

menu()