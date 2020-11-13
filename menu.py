"""check"""
import random
import pong2 as gameon
from tkinter import *
from tkinter import messagebox

def startbutton():
    """start menu in button menu"""
    gameon.game()

def buttonmenu(frame):
    """button menu"""
    buttonstart = Button(frame, text="START", width=20, height=5, fg = "blue", bg = "red", command=startbutton)#fgอักษร, bgพื้นหลังปุ่ม command เรียกคำสั่งใช้ปุ่ม
    buttonstart.pack(padx=30, pady=200)  #ที่วางปุ่มตำเเหน่งเทียบจากframe

def menu():
    """start menu"""
    root = Tk()#สร้างหน้าต่าง
    root.title("MENU")  #ชื่อเกม
    root.geometry("600x500")  #ขนาดจอ
    root.option_add("*font", "tahoma 10 bold")  #font
    frame = Frame(root)#สร้างเฟรม
    frame.config(background="green")#สีพื้นหลัง
    frame.place(width=600, height=500, x=0, y=0)  #จัดวางเฟรม
    #canvas = Canvas(root, width=2014, height=1365)
    #canvas.pack()
    #photo = PhotoImage(file='a.png')
    #canvas.create_image(0, 0, image = photo, anchor = CENTER)
    buttonmenu(frame)#เรียกปุ่มbuttonstart ของframe
    root.mainloop()  #แสดงผลหน้าต่าง
menu()


