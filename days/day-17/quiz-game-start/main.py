

from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain

question_bank =[]

for que in question_data:
    question_text = que["text"]
    question_answer = que["answer"]
    new_question=QuestionModel(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You Have completed your quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")