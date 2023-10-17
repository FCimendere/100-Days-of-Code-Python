import random
from tkinter import *
import requests
import time
from random import Random
from quiz import QuizBrain

THEME_COLOR = "#FFDEC9"

class QuizInterFace:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzlet_app")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)


        self.score_label = Label(text="Score: 0", fg ="midnightblue", bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text="some question text",
            fill="blue",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="/Users/flypixie/Desktop/Python_Trials/100-Days-of-Code-Python/Day#17/check.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed
                                  )
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file="/Users/flypixie/Desktop/Python_Trials/100-Days-of-Code-Python/Day#17/cross.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
