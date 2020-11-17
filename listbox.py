from tkinter import *
ans = ""
listbox = ""

def listbox():
    """listbook"""
    #tiger
    root = Tk()
    root.title("question")#ชื่อ
    root.geometry("600x500")
    root.option_add("*font","tahoma 10 bold")
    frame = Frame(root)
    frame.config(background="cyan")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="Book List", font="courier 12 bold", bg="cyan")
    label1.place(width=150, height=30, x=60, y=20)
    listbox1 = Listbox(frame)
    listbox1.place(width=150, height=100, x=60, y=50)
    scrolly = Scrollbar(frame, orient=VERTICAL, command=listbox1.yview)
    scrolly.place(height=100, x=210, y=50)#รูปscroll mouse
    listbox1.config(yscrollcommand=scrolly.set, font="courier 12 bold")
    booklist = ["python", "java", "C", "PHP", "Access", "Excel"]
    for item in booklist:
        listbox1.insert(END, item)
    button()
    root.mainloop()
listbox()