from tkinter import *
from tkinter import messagebox as mb

import json 

class Quiz:
    def __init__(self):
          
        self.ques_no=0
          
        self.display_title()
        self.display_question()
        
        self.option_selected=IntVar()
          
        # output radio button for the current question
        self.opts=self.radio_buttons()
          
        # display options for the current question
        self.display_options()
          
        # the button for next and exit.
        self.buttons()
          
        # Total questions
        self.data_size=len(question)
          
        # keep a counter of correct answers
        self.correct=0
  
  
    def display_result(self):
          
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"No.of Correct answers: {self.correct}"
        wrong = f"No.of Wrong answers: {wrong_count}"
          
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
          
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
  
  
    # checks the Answer after we click on Next.
    def check_ans(self, ques_no):
          
        # checks for if the selected option is correct
        if self.option_selected.get() == answer[ques_no]:
            return True
  
    # To check the answer of the
    # current question by calling the check_ans and question no.
    def next_btn(self):
          
        # Check if the answer is correct
        if self.check_ans(self.ques_no):
              
            self.correct += 1
          
        self.ques_no += 1
          
        if self.ques_no==self.data_size:
              
            self.display_result()
              
            # destroys the GUI
            GUI.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
  
  
    # This method shows the two buttons on the screen.
    def buttons(self):
          
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(GUI, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
          
        # palcing the button  on the screen
        next_button.place(x=350,y=380)
          
        # This is the second button which is used to Quit the GUI
        quit_button = Button(GUI, text="Quit", command=GUI.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
          
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)
  
  
    # This method deselect the radio button on the screen
    def display_options(self):
        val=0
          
        # deselecting the options
        self.option_selected.set(0)
          
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.ques_no]:
            self.opts[val]['text']=option
            val+=1
  
  
    # This method shows the current Question on the screen
    def display_question(self):
          
        # setting the Quetion properties
        ques_no = Label(GUI, text=question[self.ques_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
          
        #placing the option on the screen
        ques_no.place(x=70, y=100)
  
  
    # This method is used to Display Title
    def display_title(self):
          
        # The title to be shown
        title = Label(GUI, text="CodeInPlace QUIZ",
        width=50, bg="yellow",fg="purple", font=("ariel", 21, "bold"))
          
        # place of the title
        title.place(x=1, y=2)
  
  
    def radio_buttons(self):
          
        question_list = []
          
        y_pos = 160
          
        # adding the options to the list
        while len(question_list) < 4:
              
            # setting the radio button properties
            radio_button = Radiobutton(GUI,text=" ",variable=self.option_selected,
            value = len(question_list)+1,font = ("ariel",15))
              
            # adding the button to the list
            question_list.append(radio_button)
              
            # placing the button
            radio_button.place(x = 100, y = y_pos)
              
            y_pos += 40
          
        # radio buttons
        return question_list
  
# Create a GUI Window
GUI = Tk()
  
# set the size of the GUI Window
GUI.geometry("800x450")
  
# set the title of the Window
GUI.title("CodeInPlace QUIZ")

  
# get the data from the json file
with open('data.json') as f:
    data = json.load(f)
  
# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
  
quiz = Quiz()
  
GUI.mainloop()

