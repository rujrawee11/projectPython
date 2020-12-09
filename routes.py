from instruction import *
from game import *
from tkinter import messagebox

class WindowRoute: #ข้อมูลหรือตัวแปรที่กำหนดไว้ในคลาส เปรียบเหมือนตัวแปรสาธารณะเข้าถึงได้ทุกคลาส
    def __init__(self, master): #การกำหนดค่าเริ่มต้นให้กับข้อมูลหรือตัวแปรที่รับมาเหมือนข้อมูลทั่วไป
        self.master = master

    def startGame(self):
        self.master.lower()
        self.master.attributes('-topmost', 0)
        self.newWindow = Toplevel(self.master)
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing) # on close window
        game = GameController(self.newWindow)
        game.startRockPaperScissors()
        # gameWindow(self.newWindow)
    
    def instruction(self):
        self.master.lower()
        self.master.attributes('-topmost', 0) 
        self.newWindow = Toplevel(self.master)
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing) # on close window
        instructionWindow(self.newWindow)

    def on_backing(self):
        self.master.lift()
        self.master.attributes('-topmost', 1)
        self.newWindow.destroy()

    def on_closing(self):
        if messagebox.showinfo("Quit", "Do you want to quit?"): #หน้าต่างแยก askokcancel
            self.master.destroy() #คำสั่งปิดหน้าจอ
