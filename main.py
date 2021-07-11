from question_model import Question
from data import question_data

question_bank = []

for question in range(len(question_data)):
    question_text = question_data[question]["text"]
    question_answer = question_data[question]["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].text)
print(question_bank[0].correct_answer)