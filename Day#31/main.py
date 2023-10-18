from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
LIGHT_BLUE = "#8ECDDD"
DARK_BLUE = "#22668D"
current_card = {}

#----------------------------------------FLASH CARD CREATION----------------------------------------#

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("/data/words_to_learn.csv", index=False)
    next_card()


#----------------------------------------UI SETUP----------------------------------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

image_reject = PhotoImage(file="images/wrong.png")
image_accept = PhotoImage(file="images/right.png")


button_reject = Button(image=image_reject, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_reject.grid(column=0, row=1)
button_accept = Button(image=image_accept, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
button_accept.grid(column=1, row=1)

next_card()

window.mainloop()



