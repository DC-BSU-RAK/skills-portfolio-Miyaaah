# Mia Lovina D. Tabucan CCY2 G2

# Sources
# Background Images Sources:
# https://www.freepik.com/free-photo/colourful-math-numbers-letters-frame-with-copy-space-top-view_6625068.htm#fromView=keyword&page=1&position=0&uuid=ace1995e-cffd-4f62-91f5-e4fef277358a&query=Addition+subtraction+background
# Edited by me: edited and adjusted colors for Tkinter background design


from tkinter import *
from tkinter import messagebox
import random

# Variables for the quiz
score = 0
question_number = 0
difficulty = ""
a = b = correct_answer = 0
attempt = 1

# Main window
root = Tk()
root.title("Math Quiz")
root.geometry("700x500")
root.config(bg="#ffffff")
root.iconbitmap("math.ico")

bg_image = PhotoImage(file="Background.png")

# Function to create a frame with background image
def create_frame_with_bg(root):
    frame = Frame(root, width=700, height=500)
    frame.place(x=0, y=0)

    bg_label = Label(frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    return frame

# Functions
def reset_quiz():
    global score, question_number, attempt
    score = 0
    question_number = 0
    attempt = 1

def go_home():
    reset_quiz()
    switch_to_frame(start_frame)

def switch_to_frame(frame):
    frame.tkraise()

def on_space_press(event):
    root.unbind("<space>")
    switch_to_frame(quiz_frame)
    next_question()

def enable_spacebar():
    root.bind("<space>", on_space_press)

# Quiz functions
def randomInt(level):
    if level == "easy":
        return random.randint(1, 9)
    elif level == "moderate":
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(["+", "-"])

def next_question():
    global a, b, op, correct_answer, question_number, attempt 

    if question_number == 10:
        displayResults()
        return

    attempt = 1 
    a = randomInt(difficulty)
    b = randomInt(difficulty)
    op = decideOperation()

    if op == "+":
        correct_answer = a + b
    else:
        correct_answer = a - b

    question_number += 1

    question_label.config(text=f"Q {question_number}. / 10)   {a} {op} {b} = ?") #I asked AI's assistance on how to update the questions
    feedback_label.config(text="")
    answer_entry.delete(0, "end")

    if difficulty == "easy":
        level_label.config(text="Level: EASY", fg="#00c12a")
    elif difficulty == "moderate":
        level_label.config(text="Level: MODERATE", fg="#e9a700")
    else:
        level_label.config(text="Level: ADVANCED", fg="#d700a8")

def check_answer():
    global score, attempt

    user_answer = answer_entry.get().strip()
    if user_answer == "":
        messagebox.showinfo("Input Required", "Please enter a number!")
        return

    try:
        user_answer = int(user_answer)
    except ValueError:
        messagebox.showinfo("Invalid Input", "Enter a valid integer number!")
        return

    if user_answer == correct_answer:
        if attempt == 1:
            points = 10
        elif attempt == 2:
            points = 5
        score += points
        feedback_label.config(text=f"🌟 Correct! +{points} points", fg="#00C244")
        quiz_frame.after(1000, next_question)
    else:
        if attempt == 1:
            attempt += 1
            feedback_label.config(text="❌ Try again!", fg="#e50039")
        else:
            feedback_label.config(text=f"❌ Wrong! The correct answer was {correct_answer}.", fg="red")
            quiz_frame.after(1000, next_question)

def displayResults():
    global score
    name = enter_name.get().strip()

    if score >= 90:
        grade = "A+"
        message = f"🌟 Outstanding, {name}!"
    elif score >= 60:
        grade = "B"
        message = f"Nice job, {name}!"
    elif score >= 50:
        grade = "C"
        message = f"Not bad, keep practicing, {name}!"
    else:
        grade = "F"
        message = f"What a bummer! Maybe next time, {name}."

    result_label.config(text=f"{message}\nYour score: {score}/100")
    grade_label.config(text=f"Grade: {grade}")
    switch_to_frame(result_frame)

def set_difficulty(level):
    global difficulty, score, question_number
    difficulty = level
    score = 0
    question_number = 0
    switch_to_frame(instr_frame)
    enable_spacebar()

def start_game():
    name = enter_name.get().strip()
    if name == "":
        messagebox.showwarning("Missing Name", "Enter your name!")
    else:
        switch_to_frame(menu_frame)

# Frames with background
start_frame = create_frame_with_bg(root)
menu_frame = create_frame_with_bg(root)
instr_frame = create_frame_with_bg(root)
quiz_frame = create_frame_with_bg(root)
result_frame = create_frame_with_bg(root)

# Start Frame
label1 = Label(start_frame, text="Plus or Minus +/- \nMath Quiz!", font=('System',35), bg='#ededed', fg="#00a2c7")
label1.place(relx=0.5, y=110, anchor='n')

name1 = Label(start_frame, text="Enter your name:", font=('Roboto',15), bg='#ededed', fg="#0085DD")
name1.place(relx=0.5, y=245, anchor='n')

enter_name = Entry(start_frame, font=('Roboto',12))
enter_name.place(relx=0.5, y=290, anchor='n', width=180, height=30)

button_play = Button(start_frame, text="PLAY", font=('Roboto',15), bg="#00a189", fg="#FFFFFF", activebackground="#003C71", activeforeground="#FFFFFF", bd=2, relief="flat", command=start_game)
button_play.place(relx=0.5, y=340, anchor='n', width=150, height=40)

# Menu Frame
label2 = Label(menu_frame, text="+-- Select Difficulty --+", font=('System',25), bg='#ededed', fg="#f26d00")
label2.place(relx=0.5, y=110, anchor='n')

ez_button = Button(menu_frame, text="EASY", font=('Roboto',15), bg="#11ce50", fg='white', activebackground="#008b7b", activeforeground="#FFFFFF", bd=2, relief="flat", command=lambda: set_difficulty("easy"))
ez_button.place(relx=0.5, y=200, anchor='n', width=200, height=40)

mod_button = Button(menu_frame, text="MODERATE", font=('Roboto',15), bg="#e9c617", fg='white', activebackground="#008b7b", activeforeground="#FFFFFF", bd=2, relief="flat", command=lambda: set_difficulty("moderate"))
mod_button.place(relx=0.5, y=255, anchor='n', width=200, height=40)

adv_button = Button(menu_frame, text="ADVANCE", font=('Roboto',15), bg="#eb5b6c", fg='white', activebackground="#008b7b", activeforeground="#FFFFFF", bd=2, relief="flat", command=lambda: set_difficulty("advanced"))
adv_button.place(relx=0.5, y=310, anchor='n', width=200, height=40)

home_button = Button(menu_frame, text="🏠", font=('Roboto',12), bg="#DD3D03", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2, relief="flat", width=5, height=2, command=go_home)
home_button.place(x=30, y=20)

# Instructions Frame
label3 = Label(instr_frame, text="Numbers Only, Please!", font=('Roboto',30,'bold'), bg='#ededed', fg='#f26d00')
label3.place(relx=0.5, y=100, anchor='n')

instructions = Label(instr_frame, text="Keep it simple: answers should be numbers. No letters or symbols—just type the digits!", font=('Roboto',14), bg='#ededed', fg="#8700b8", wraplength=400)
instructions.place(relx=0.5, y=170, anchor='n')

instructions2 = Label(instr_frame, text="You’ve got 2 tries to get it right, so make them count!", font=('Roboto',12), bg='#ededed', fg="#D10092", wraplength=320)
instructions2.place(relx=0.5, y=245, anchor='n')

note = Label(instr_frame, text="Note: Don't spam the submit button and wait for the next question to appear.", font=('Roboto',10), bg='#ededed', fg="#8759F3", wraplength=400)
note.place(relx=0.5, y=315, anchor='n')

label4 = Label(instr_frame, text="Press the spacebar to continue", font=('Roboto',18), bg='#ffffff', fg='blue')
label4.place(relx=0.5, y=380, anchor='n')

home_button_instr = Button(instr_frame, text="🏠", font=('Roboto',12), bg="#DD3D03", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2, relief="flat", width=5, height=2, command=go_home)
home_button_instr.place(x=30, y=20)

# Quiz Frame
level_label = Label(quiz_frame, text="", font=('Roboto',20 ,'bold'), bg="#ededed")
level_label.place(relx=0.5, y=120, anchor='n')

question_label = Label(quiz_frame, text="", font=('Roboto',20), bg="#ffffff", fg="#2700c2")
question_label.place(relx=0.5, y=190, anchor='n')

answer_entry = Entry(quiz_frame, font=('Roboto',14))
answer_entry.place(relx=0.5, y=245, anchor='n',  width=180, height=35)

submit_button = Button(quiz_frame, text="SUBMIT", font=('Roboto',15), bg='#00a189', fg='white', width=15, bd=2, relief="flat",  command=check_answer)
submit_button.place(relx=0.5, y=305, anchor='n',  width=120, height=40)

feedback_label = Label(quiz_frame, text="", font=('Roboto',18), bg="#ededed", fg='blue')
feedback_label.place(relx=0.5, y=380, anchor='n')

home_button_quiz = Button(quiz_frame, text="🏠", font=('Roboto',12),bg="#DD3D03", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2,  relief="flat" , width=5, height=2, command=go_home)
home_button_quiz.place(x=30, y=20)

# Result Frame
results = Label(result_frame, text="RESULTS", font=('Roboto',40, 'bold'), bg='#ededed', fg="#a800f0")
results.place(relx=0.5, y=100, anchor='n')

result_label = Label(result_frame, text="", font=('Roboto',20), bg='#ededed', fg="#ff00d4")
result_label.place(relx=0.5, y=185, anchor='n')

grade_label = Label(result_frame, text="", font=('Roboto',28, 'bold'), bg='#ededed', fg="#2700c2")
grade_label.place(relx=0.5, y=280, anchor='n')

replay_button = Button(result_frame, text="PLAY AGAIN", font=('Roboto',16,'bold'), bg="#F7B100", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2.5,  relief="flat" , width=13, height=1, command=go_home)
replay_button.place(relx=0.5, y=363, anchor='n')

# Show start frame first
switch_to_frame(start_frame)

root.mainloop()
