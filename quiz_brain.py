class QuizBrain:

    def __init__(self, qn_list):
        self.qn_no = 0
        self.score = 0
        self.qn_list = qn_list

    def next_question(self):

        current_question = self.qn_list[self.qn_no]
        self.qn_no += 1
        user_answer = input(f"Q.{self.qn_no}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if len(self.qn_list) > self.qn_no:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ")
        else:
            print("You got it wrong")
        print(f"The correct answer was :{correct_answer}")
        print(f"Your score is {self.score}/{self.qn_no}")
        print()





