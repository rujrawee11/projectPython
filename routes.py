from instruction import *
from game import *
from tkinter import messagebox

class WindowRoute:
    def __init__(self, master):
        self.master = master

    # สร้างหน้าต่างเกม เป่า ยิง ฉุบ
    def startGame(self):
        self.master.lower() # ยุบหน้าจอ main menu ลง (master คือ หน้าต่าง main menu)
        self.master.attributes('-topmost', 0) # ปรับลำดับหน้าจอ main menu ลงให้ต่ำสุด หรืออยู่ข้างล่าง
        self.newWindow = Toplevel(self.master) # สร้างหน้าใหม่ขึ้นมาซ้อนไว้
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing) # เมื่อมีการปิดหน้าต่างให้ เรียกฟังก์ชัน on_backing ของ class นี้
        game = GameController(self.newWindow) # สร้าง object จาก class GameController ขึ้นมา
        game.startRockPaperScissors() # เรียกฟังก์ชัน startRockPaperScissors เพิ่มแสดงผลหน้าต่างเกม
    
    # สร้างหน้าต่างวิธีเล่น
    def instruction(self):
        self.master.lower()  # ยุบหน้าจอ main menu ลง (master คือ หน้าต่าง main menu)
        self.master.attributes('-topmost', 0) # ปรับลำดับหน้าจอ main menu ลงให้ต่ำสุด หรืออยู่ข้างล่าง
        self.newWindow = Toplevel(self.master) # สร้างหน้าใหม่ขึ้นมาซ้อนไว้
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing)  # เมื่อมีการปิดหน้าต่างให้ เรียกฟังก์ชัน on_backing ของ class นี้
        instructionWindow(self.newWindow) # เรียกฟังก์ชัน instructionWindow เพิ่มแสดงผลหน้าต่างวิธีการเล่น

    # event สำหรับกลับไปจอ main menu
    def on_backing(self):
        self.master.lift()  # ขยายหรือนำหน้าจอ main menu กลับขึ้นมา (master คือ หน้าต่าง main menu)
        self.master.attributes('-topmost', 1) # ปรับลำดับหน้าจอ main menu ลงให้ขึ้นมาบนสุด
        self.newWindow.destroy() # ทำลายหรือปืดหน้าต่างที่เปิดอยู่ เช่น หน้าต่างเกม หน้าวิธีเล่น

    # event สร้าง dialog ให้ยืนยันก่อนปิดหน้าต่าง
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"): # สร้าง dialog ให้ยืนยันก่อนปิดหน้าต่าง
            self.master.destroy() # ทำลาย main menu เพื่อปิดเกม
