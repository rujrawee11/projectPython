from tkinter import *

def main():
    question_1_Var = IntVar() #creating a variable to be assigned to the radiobutton

    Yes_1 = Radiobutton(self, text = "Yes", variable = question_1_Var, value=1, height=5, width = 20)
    Yes_1.pack() #creating 'yes' option

    #Here we are assigning values to each option which will be used in the validation

    No_1 = Radiobutton(self, text = "No", variable = question_1_Var, value=2, height=5, width = 20)
    No_1.pack() #creating 'no' option
    def calculate_score_1(self):
        Enter_1.config(state="disabled")
        #self.question_1.config(state="disabled")
        if (question_1_Var.get() == 1) and not (question_1_Var.get() == 2):
            print("calculate score has worked") #test lines
            #score = score + 1
        else:
            print("not worked") #testlines


    Enter_1 = Button(self, text= "Enter", width=10, command = calculate_score_1)
    Enter_1.pack()
main()
