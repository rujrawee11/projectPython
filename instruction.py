from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def instructionWindow(master):
    #root = Tk()  # สร้างหน้าต่าง
    master.title("Instuction")  # ชื่อเกม
    master.geometry("600x500")
    master.option_add("*font", "tahoma 10 bold")
    canvas = Canvas(master, width=600, height=500)
    canvas.pack()
    photo = ImageTk.PhotoImage(Image.open('images/instruction.png'))
    canvas.create_image(300, 250, image=photo)
    master.mainloop()