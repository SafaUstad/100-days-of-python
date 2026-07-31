# Flashcard - German to English Translation

from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv", encoding="utf-16")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/german_words.csv", encoding="utf-16")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def new_word():
    global flip_timer, current_card
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(card_title, text= "German", fill="black")
    canvas.itemconfig(card_word, text= current_card["German"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False, encoding="utf-16")
    new_word()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "", font=("Arial", 60, "bold"))

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

new_word()

window.mainloop()
