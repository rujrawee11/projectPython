#color button
import tkinter
 
window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
button_submit = tkinter.Button(window_main, text="Submit", activebackground='#78d6ff', activeforeground = "red")

 
button_submit.pack()
window_main.mainloop()
