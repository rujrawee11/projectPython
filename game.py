"""check"""
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def game(master):  # user
    # จำนวนครั้งแพ้ชนะแก้เก็บแค่score ต่าสถิติ
    print('game')
    p1_stat = {'WINS': 0, 'LOSSES': 0, 'TIES': 0}
    #สวัสดีไทยเเลนด์
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
    Button(master, text="Quit", command=master.destroy).pack()
    master.mainloop()


class StartButton:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.b = Button(self.frame, text="START", width=20, height=5, fg="blue", bg="red", command=self.startbutton)
        self.b.pack(padx=30, pady=200)
        self.frame.pack()

    def startbutton(self):
        # self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        game(self.newWindow)


def startbutton(self):
    """start menu in button menu"""
    # game()
    self.master.withdraw()
    self.newWindow = Toplevel(self.master)
    

def buttonmenu(frame):
    """button menu"""
    buttonstart = Button(frame, text="START", width=20, height=5, fg="blue", bg="red", command=startbutton)  # fgอักษร, bgพื้นหลังปุ่ม command เรียกคำสั่งใช้ปุ่ม
    buttonstart.pack(padx=30, pady=200)  # ที่วางปุ่มตำเเหน่งเทียบจากframe


def menu():
    """start menu"""
    root = Tk()  # สร้างหน้าต่าง
    root.title("MENU")  # ชื่อเกม
    root.geometry("600x500")  # ขนาดจอ
    root.option_add("*font", "tahoma 10 bold")  # font
    frame = Frame(root)  # สร้างเฟรม
    frame.config(background="green")  # สีพื้นหลัง
    frame.place(width=600, height=500, x=0, y=0)  # จัดวางเฟรม
    # buttonmenu(frame)#เรียกปุ่มbuttonstart ของframe
    StartButton(root)
    root.mainloop()  # แสดงผลหน้าต่าง


menu()
