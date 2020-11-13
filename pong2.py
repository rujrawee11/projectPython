import random
from tkinter import *


def game(): #user
    p1_stat = {'WINS':0, 'LOSSES':0, 'TIES':0}#จำนวนครั้งแพ้ชนะแก้เก็บแค่score ต่าสถิติ

    def rule(p1_shape, p2_shape): #ฟังก์ชันสำหรับหาว่าใครชนะใครแพ้
        if p1_shape == p2_shape:
            p1_stat['TIES'] += 1
            return "TIED"
        elif (p1_shape == 'ROCK' and p2_shape == "SCISSORS") or (p1_shape == "PAPER" \
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
        tv_result.set(f'PLAYER : {p1_shape} - COM : {p2_shape} -> {result}') #combolistชื่อ
        tv_stat.set(f'{p1_stat["WINS"]} wins, {p1_stat["TIES"]} ties, {p1_stat["LOSSES"]} losses')
    root = Tk() #หน้าต่างของรูปที่จะกดปุ่ม
    root.title("GAME")
    root.geometry("500x400")
    root.option_add("*Font", "consolas 11")
    shapes = ['rock', 'paper', 'scissors']
    p1_shape = [PhotoImage(file=f'{img}.png') for img in shapes]
    f1 = Frame(root)
    f1.grid(row=0, column=0)
    f2 = Frame(root)
    f2.grid(row=1, column=0)
    tv_result = StringVar()
    tv_stat = StringVar()
    tv_score = StringVar()
    for i in range(len(p1_shape)):
        w = Button(f1, image=p1_shape[i], text=shapes[i], borderwidth=0) #ปุ่มรูปtextไม่แสดงเอาไว้ใช้ในonclick
        w.pack(side=LEFT, padx=15) #รูปปุ่ม
        w.bind('<Button-1>', on_click) #คลิ๊กปกติ
        w.pack(padx = 15, pady=55)
    Label(f2, textvariable = tv_score, fg ="black", width=44, height=2, bg='red', font='consolas 13 bold').pack()
    Label(f2, textvariable = tv_result, fg ="blue", width=50).pack() #scoreจะใส่bg
    Label(f2, textvariable = tv_stat, fg ="blue", width=50, bg='gold', height=1).pack() #จำนวนครั้งที่เล่นไปแล้ว
    root.mainloop()

#if __name__ == '__main__':
    #print(rule('rock', 'paper'))
    #print(rule('rock', 'scissors'))
    #print(rule('rock', 'rock'))
