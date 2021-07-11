class Quiz_Brain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list

    def next_question(self, question_list):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        input(f"Q{self.question_no}.{current_question}:(True/False)) ")
