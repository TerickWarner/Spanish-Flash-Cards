from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
known_data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Spanish_Words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    print(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Spanish Flashcards")
window.config(padx=10, pady=10, bg="cyan")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=500)
card_front_img = PhotoImage(file="images/back_card.png")
card_back_img = PhotoImage(file="images/back_card.png")
card_background = canvas.create_image(400, 300, image=card_front_img)
card_title = canvas.create_text(400, 45, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 200, text="", font=("Ariel", 70, "bold"))
canvas.config(bg="cyan", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



x_image = PhotoImage(file="images/wrong_button.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.place(x=100, y=350)

check_image = PhotoImage(file="images/right_button.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.place(x=560, y=350)

next_card()

window.mainloop()