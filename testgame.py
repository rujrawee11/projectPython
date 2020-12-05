"""check"""
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def game(master):  # user
    # จำนวนครั้งแพ้ชนะแก้เก็บแค่score ต่าสถิติ
    print('game')
    p1_stat = {'WINS': 0, 'LOSSES': 0, 'TIES': 0, 'SCORE': 0}
    def rule(p1_shape, p2_shape):  # ฟังก์ชันสำหรับหาว่าใครชนะใครแพ้
        if p1_shape == p2_shape:
            p1_stat['TIES'] += 1
            return "TIED"
        elif (p1_shape == 'ROCK' and p2_shape == "SCISSORS") or (p1_shape == "PAPER"
            and p2_shape == 'ROCK') or (p1_shape == "SCISSORS" and p2_shape == "PAPER"):
            p1_stat['WINS'] += 1
            p1_stat['SCORE'] += 1
            return "PLAYER WON"
        else:
            p1_stat['LOSSES'] += 1
            if  p1_stat['SCORE'] == 0:
                 p1_stat['SCORE'] = 0
            else:
                 p1_stat['SCORE'] -= 1
            return "PLAYER LOST"

    def on_click(e):
        p1_shape = e.widget['text'].upper()
        print(p1_shape)
        p2_shape = random.choice(shapes).upper()
        print(p2_shape)
        result = rule(p1_shape, p2_shape)
        print(f'result : {result}')
        tv_score.set(f'Score : {p1_stat["SCORE"]}')
        # combolistชื่อ
        tv_result.set(f'PLAYER : {p1_shape} - COM : {p2_shape} -> {result}')
        tv_stat.set(f'{p1_stat["WINS"]} wins, {p1_stat["TIES"]} ties, {p1_stat["LOSSES"]} losses')
    # root = Tk()  # หน้าต่างของรูปที่จะกดปุ่ม
    master.title("GAME")
    master.geometry("500x400")
    master.option_add("*Font", "consolas 11")
    shapes = ['rock', 'paper', 'scissors']
    p1_shape = [ImageTk.PhotoImage(Image.open(f'images/{img}.png')) for img in shapes]
    f1 = Frame(master)
    f1.grid(row=0, column=0)
    f2 = Frame(master)
    f2.grid(row=1, column=0)
    tv_result = StringVar()
    tv_stat = StringVar()
    tv_score = StringVar()
    for i in range(len(p1_shape)):
        # ปุ่มรูปtextไม่แสดงเอาไว้ใช้ในonclick
        w = Button(f1, image=p1_shape[i], text=shapes[i], borderwidth=0)
        w.pack(side=LEFT, padx=15)  # รูปปุ่ม
        w.bind('<Button-1>', on_click)  # คลิ๊กปกติ
        w.pack(padx=15, pady=55)
    Label(f2, textvariable=tv_score, fg="black", width=44,
          height=2, bg='red', font='consolas 13 bold').pack()
    Label(f2, textvariable=tv_result, fg="blue",
          width=50).pack()  # scoreจะใส่bg
    Label(f2, textvariable=tv_stat, fg="blue", width=50,
          bg='gold', height=1).pack()  # จำนวนครั้งที่เล่นไปแล้ว
    Button(master, text="Quit", width=10, height=5, anchor='w', command=master.destroy).pack()
    master.mainloop()

def imge(master):
    #root = Tk()  # สร้างหน้าต่าง
    master.title("Instuction")  # ชื่อเกม
    master.geometry("600x500")
    master.option_add("*font", "tahoma 10 bold")
    canvas = Canvas(master, width=600, height=500)
    canvas.pack()
    photo = ImageTk.PhotoImage(Image.open('Home.png'))
    canvas.create_image(300, 250, image=photo)
    master.mainloop()

class CustomCmd:
    def __init__(self, master):
        self.master = master

    def start(self):
        # self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        game(self.newWindow)
    
    def start1(self):
        # self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        imge(self.newWindow)

def question1():
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

    cmd = CustomCmd(root)
    startBtnImg = ImageTk.PhotoImage(Image.open('images/start.png'))
    startBtn = Button(root, text="Start", bg='#138fa9', image=startBtnImg , borderwidth=0, command=cmd.start, anchor='center')
    canvas.create_window(300, 345, anchor='center', window=startBtn)

    quitBtnImg = ImageTk.PhotoImage(Image.open('images/quit.png'))
    quitBtn = Button(root, text="Quit", bg='#138fa9', image=quitBtnImg , borderwidth=0, command=root.quit, anchor='center')
    canvas.create_window(300, 440, anchor='center', window=quitBtn)

    nextBtnImg = ImageTk.PhotoImage(Image.open('how.png'))
    nextBtn = Button(root, text="Instruction", bg='#138fa9', image=nextBtnImg , borderwidth=0, command=cmd.start1, anchor='s')
    canvas.create_window(150, 485, anchor='s', window=nextBtn)
    root.mainloop()  # แสดงผลหน้าต่าง

menu()