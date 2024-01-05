from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    question = Question(entry["text"], entry["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
