"""check"""
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from question_data import get_rand_question

class GameController:
    def __init__(self, master):
        self.master = master
        self.win_score = 10 # คะแนนที่จะให้ชนะ
        self.shapes = ['rock', 'paper', 'scissors']
        self.p1_stat = {'WINS': 0, 'LOSSES': 0, 'TIES': 0, 'QUESTION': 0, 'SCORE': 0}
        self.tv_result = StringVar()
        self.tv_stat = StringVar()
        self.tv_score = StringVar()

    def startRockPaperScissors(self):
        print('GameController::startRockPaperScissors')
        self.master.title("GAME")
        self.master.geometry("500x400")
        self.master.option_add("*Font", "consolas 11")
        p1_shape = [ImageTk.PhotoImage(Image.open(f'images/{img}.png')) for img in self.shapes]
        f1 = Frame(self.master)
        f1.grid(row=0, column=0)
        f2 = Frame(self.master)
        f2.grid(row=1, column=0)
        
        for i in range(len(p1_shape)):
            # ปุ่มรูปtextไม่แสดงเอาไว้ใช้ในonclick
            w = Button(f1, image=p1_shape[i], text=self.shapes[i], borderwidth=0)
            w.pack(side=LEFT, padx=15)  # รูปปุ่ม
            w.bind('<Button-1>', self.on_click)  # คลิ๊กปกติ
            w.pack(padx=15, pady=55)
        
        Label(f2, textvariable=self.tv_score, fg="white", width=44,
            height=2, bg='red', font='consolas 13 bold').pack()
        Label(f2, textvariable=self.tv_result, fg="blue",
              width=50).pack()  # scoreจะใส่bg
        Label(f2, textvariable=self.tv_stat, fg="blue", width=50,
              bg='gold', height=1).pack()  # จำนวนครั้งที่เล่นไปแล้ว
        Button(master, text="Quit", width=10, height=5, anchor='w', command=self.master.destroy).pack()
        self.master.mainloop()

    def rule(self, p1_shape, p2_shape):
        if p1_shape == p2_shape:
            self.p1_stat['TIES'] += 1
            return "TIED"
        elif (p1_shape == 'ROCK' and p2_shape == "SCISSORS") or (p1_shape == "PAPER"
            and p2_shape == 'ROCK') or (p1_shape == "SCISSORS" and p2_shape == "PAPER"):
            self.p1_stat['WINS'] += 1
            self.p1_stat['SCORE'] += 1
            return "PLAYER WON"
        else:
            self.p1_stat['LOSSES'] += 1
            if  self.p1_stat['SCORE'] == 0:
                self.p1_stat['SCORE'] = 0
            else:
                self.p1_stat['SCORE'] -= 1
            return "PLAYER LOST"

    def on_click(self, e):
        p1_shape = e.widget['text'].upper()
        print(p1_shape)
        p2_shape = random.choice(self.shapes).upper()
        print(p2_shape)
        result = self.rule(p1_shape, p2_shape)
        if result == "TIED":
            self.master.lower()
            self.master.attributes('-topmost', 0)
            self.newWindow = Toplevel(self.master)
            def on_closing():
                self.master.update_idletasks()
                self.master.update()
                self.master.lift()
                self.master.attributes('-topmost', 1)
                self.newWindow.destroy()
            self.newWindow.protocol("WM_DELETE_WINDOW", on_closing) # on close window
            self.questionWindow(self.newWindow)

        self.check_win()
        print(f'result : {result}')
        self.update_all_stat(f'PLAYER : {p1_shape} - COM : {p2_shape} -> {result}')

    def questionWindow(self, newWindow):
        print('questionWindow')
        newWindow.title("Question")  # ชื่อเกม
        newWindow.geometry("600x500")
        newWindow.option_add("*font", "Opun-Mai-Thin 10 bold")
        canvas = Canvas(newWindow, width=600, height=500)
        canvas.pack()

        question = get_rand_question() # get คำถามจากไฟล์ question_data.py แบบสุ่ม 

        photo = ImageTk.PhotoImage(Image.open(f'images/{question["bg"]}.png'))
        canvas.create_image(300, 250, image=photo)
        label2 = Label(newWindow, text=question["text"],width=50, height=5, bg="white")
        canvas.create_window(300, 105, anchor='center', window=label2)

        var = IntVar()

        def on_select_choice():
            choice_id = var.get()
            print('on_select_choice', choice_id)
            answer = next((choice for choice in question["choices"] if choice["id"] == choice_id), None)
            self.p1_stat['QUESTION'] += 1
            if answer["isAnswer"] == True:
                self.p1_stat['SCORE'] += 1
                self.update_all_stat(f'PLAYER : Has answer the question correctly!')
                self.check_win()
            else:
                self.update_all_stat(f'PLAYER : Has answer the question incorrectly!')
            self.master.update_idletasks()
            self.master.update()
            self.master.lift()
            self.master.attributes('-topmost', 1)
            print('questionWindow', self.p1_stat)
            newWindow.destroy()

        pos_y = 190
        for choice in question["choices"]:
            print(choice)
            choice_btn = Radiobutton(newWindow, text=choice["text"], width=15, height=3, variable=var, value=choice["id"],
                            bg="white", activebackground='green', command=on_select_choice)  # คำตอบแรก active bg = เปลี่ยนสีปุ่มตอนกด
            canvas.create_window(300, pos_y, anchor='center', window=choice_btn)
            pos_y += 70

        label = Label(newWindow)
        label.pack()
        newWindow.mainloop()

    def check_win(self):
        if self.p1_stat['SCORE'] >= self.win_score:
            # แสดงผลว่าชนะ
            print('WIN the game!!!!')
            if messagebox.askokcancel("จบเกม", f'คุณชนะแล้ว!!!\nคะแนนที่ได้ {self.p1_stat["SCORE"]}'):
                self.p1_stat = {'WINS': 0, 'LOSSES': 0, 'TIES': 0, 'QUESTION': 0, 'SCORE': 0}
                self.update_all_stat()
                self.master.destroy()
            return True
        else:
            return False

    def update_all_stat(self, result_msg):
        self.tv_score.set(f'Score : {self.p1_stat["SCORE"]}')
        self.tv_result.set(result_msg)
        self.tv_stat.set(f'{self.p1_stat["WINS"]} wins, {self.p1_stat["TIES"]} ties, {self.p1_stat["LOSSES"]} losses, {self.p1_stat["QUESTION"]} answers')