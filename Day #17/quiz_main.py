#Project: Quiz Game
"""
PRACTISE: Adding Methods to a class and __init__ method practice
PROJECT: the program will ask you 12 close ended questions. 
You need to reply it as True/False. During the game you can see your score. 
After 12 questions, you can see your situation and final score.
"""



from question_model import Question
from data import question_data
from quiz import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")