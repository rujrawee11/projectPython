"""check"""
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
global scores
def game(master):  # user
    # จำนวนครั้งแพ้ชนะแก้เก็บแค่score ต่าสถิติ
    print('game')
    p1_stat = {'WINS': 0, 'LOSSES': 0, 'TIES': 0}

    def rule(p1_shape, p2_shape):  # ฟังก์ชันสำหรับหาว่าใครชนะใครแพ้
        if p1_shape == p2_shape:
            p1_stat['TIES'] += 1
            return "TIED"
        elif (p1_shape == 'ROCK' and p2_shape == "SCISSORS") or (p1_shape == "PAPER"
            and p2_shape == 'ROCK') or (p1_shape == "SCISSORS" and p2_shape == "PAPER"):
            p1_stat['WINS'] += 1
            return "PLAYER WON"
        else:
            p1_stat['LOSSES'] += 1
            return "PLAYER LOST"

    def on_click(e):
        p1_shape = e.widget['text'].upper()
        print(p1_shape)
        p2_shape = random.choice(shapes).upper()
        print(p2_shape)
        result = rule(p1_shape, p2_shape)
        print(f'result : {result}')
        tv_score.set(f'Score : {p1_stat["WINS"]}')
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


class CustomCmd:
    def __init__(self, master):
        self.master = master

    def start(self):
        # self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        game(self.newWindow)


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

    gameTitle = Label(root, text="Rock Paper Scissors Game", bg='#138fa9', fg='white', font=("Helvetica", 30))
    canvas.create_window(300, 60, anchor='center', window=gameTitle)

    cmd = CustomCmd(root)
    startBtnImg = ImageTk.PhotoImage(Image.open('images/start.png'))
    startBtn = Button(root, text="Start", bg='#138fa9', image=startBtnImg , borderwidth=0, command=cmd.start, anchor='center')
    canvas.create_window(300, 345, anchor='center', window=startBtn)

    quitBtnImg = ImageTk.PhotoImage(Image.open('images/quit.png'))
    quitBtn = Button(root, text="Quit", bg='#138fa9', image=quitBtnImg , borderwidth=0, command=root.quit, anchor='center')
    canvas.create_window(300, 440, anchor='center', window=quitBtn)

    root.mainloop()  # แสดงผลหน้าต่าง


menu()
