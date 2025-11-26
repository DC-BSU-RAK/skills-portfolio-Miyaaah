# Mia Lovina D. Tabucan CCY2 G2

# Sources
# Background Images Sources:
# start_img: https://www.freepik.com/free-vector/group-laughing-emoji-characters_5893371.htm 
# joke_bg: https://www.istockphoto.com/vector/halftone-starburst-background-gm2054365187-563501066
# icon: https://www.freepik.com/premium-vector/emoticon-laughing-out-loud-lol-sign_7589166.htm
# Edited by me: edited and adjusted colors for Tkinter background

from tkinter import *
import random
from tkinter import messagebox

# Main window
root = Tk()
root.title("Alexa, Tell Me A Joke!")
root.geometry("700x500")
root.config(bg="#ffd905")
root.iconbitmap("app_icon.ico")

# Load two different background images
bg_start = PhotoImage(file="start_bg.png")
bg_joke = PhotoImage(file="joke_bg.png")

# Function to create a frame with a specific background image
def create_frame_with_bg(root, image):
    frame = Frame(root, width=700, height=500)
    frame.place(x=0, y=0)

    bg_label = Label(frame, image=image)
    bg_label.image = image    
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    return frame


#     JOKE FUNCTIONS 

# Read jokes from the txt file
with open("randomJokes.txt", "r", encoding="utf-8") as jokes: # encoding="utf-8" because there are special symbols in the file
    jokes_list = [line.strip() for line in jokes]

# variable
current_joke = ("", "")  


def next_random_joke():
    global current_joke

    joke_line = random.choice(jokes_list).strip()

    setup = joke_line
    punch = ""

    # Try to find the first punctuation to split setup and punchline
    for punctuation in ["?", ".", "!"]:
        if punctuation in joke_line:
            index = joke_line.find(punctuation)
            setup = joke_line[:index+1].strip() 
            punch = joke_line[index+1:].strip()  
            break  

    current_joke = (setup, punch)

    # Update the labels
    joke.config(text=setup)
    punchline.config(text="")

# Reveal punchline
def reveal():
    punchline.config(text=current_joke[1])

def start_game():
    switch_to_frame(joke_frame)
    next_random_joke()  

def switch_to_frame(frame):
    frame.tkraise()
    
# Buttons
def go_home():
    switch_to_frame(start_frame)

def quit_app():
    answer = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if answer:  
        root.destroy()  


# Frames with background
start_frame = create_frame_with_bg(root, bg_start)
joke_frame = create_frame_with_bg(root, bg_joke)

# Start Frame
label1 = Label(start_frame, text="ALEXA,", font=('Comic Sans MS',55,"bold"), bg="#FEF4CF", fg="#ff0000")
label1.place(relx=0.5, y=110, anchor='n')

label2 = Label(start_frame, text="Tell me a joke!", font=('Comic Sans MS',35, "bold"), bg="#FEF4CF", fg="#ff7700")
label2.place(relx=0.5, y=230, anchor='n')

button_play = Button(start_frame, text="PLAY", font=('Comic Sans MS',35,'bold'), bg="#ff9500", fg="#FFFF00", activebackground="#FF3300", activeforeground="#FFFFFF", borderwidth = 4, relief="raised", command=start_game)
button_play.place(relx=0.5, y=340, anchor='n', width=190, height=80)



# Joke Frame
joke = Label(joke_frame, text="", font=('Comic Sans MS',20,'bold'), bg="#ffffff", fg="#000000",wraplength=430)
joke.place(relx=0.5, y=150, anchor='n')

punchline = Label(joke_frame, text="", font=('Comic Sans MS',23,'bold'), bg="#ffffff", fg="#ff7300", wraplength=460)
punchline.place(relx=0.5, y=260, anchor='n')

next_joke = Button(joke_frame, text="Next Joke", font=('Comic Sans MS',20,'bold'), bg="#ffc402", fg="#e4010d", width=15, bd=3, relief="solid", command=next_random_joke)
next_joke.place(relx=0.5, y=65, anchor='n',  width=190, height=60)

reveal_joke = Button(joke_frame, text="Show Punchline", font=('Comic Sans MS',25,'bold'), bg="#804fdb", fg="#FFFFFF", width=15, bd=3, relief="solid", command=reveal)
reveal_joke.place(relx=0.5, y=405, anchor='n',  width=280, height=60)

home_button_quiz = Button(joke_frame, text="🏠", font=('Comic Sans MS',12),bg="#aa1535", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2,  relief="flat" , width=5, height=2, command=go_home)
home_button_quiz.place(x=30, y=20)

quit_button_quiz = Button(joke_frame, text="QUIT", font=('Comic Sans MS',15,'bold'),bg="#aa1535", fg="white", activebackground="#850930", activeforeground="#FFFFFF",  bd=2,  relief="flat" , width=7, height=1, command=quit_app)
quit_button_quiz.place(x=580, y=20)

# Show start frame first
switch_to_frame(start_frame)
root.mainloop()
