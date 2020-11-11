from tkinter import*
from tkinter.ttk import Combobox
def comboboxx():
    root = Tk()
    root.title("GUI Example")
    root.geometry("600x500")
    root.option_add("*font","tahoma 10 bold")
    frame = Frame(root)
    frame.config(background="cyan")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="***** color *****", bg="red")
    label1.place(width=400, height=60, x=100, y=50)
    combo1 = Combobox(frame, width=400)
    combo1.place(width=400, height =35, x=100, y=100)
    booklist = ["python", "java", "C", "PHP", "Acess", "Excel"]
    combo1['values'] = booklist
    combo1.current(0)
    root.mainloop()
comboboxx()
