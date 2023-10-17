#Project: GUI Quiz Game
"""
PRACTISE: Creating GUI question app with OOP.
PROJECT: This is a question app. Request from the Trivia APP API Endpoint.
Those questions from trivia will be shown on the GUI and you can select the correct/wrong answer. 
If your answer is correct, the score will increase and will be shown your max. score.
"""


from question_model import Question
from data import question_data
from quiz import QuizBrain
from ui import QuizInterFace

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterFace(quiz)


print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")