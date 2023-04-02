# From day 17
import html  # to formate question.


class QuizBrain:
    """Quiz brain class to manage quiz system."""
    def __init__(self, q_list):
        # Attributes.
        self.question_number = 0
        self.question_List = q_list
        self.score = 0
        self.question = ''

        # Methods

    def still_has_question(self):  # Check questions end or not.
        """Boolean function to keep system on, until all question are not done."""
        return self.question_number < len(self.question_List)  # It will return True/False.
        # No need to write if else block this will do same work.

    def next_question(self, user_answer):  # Go to next question also check question functionality.
        """Check answer and go for next question."""
        current_question = self.question_List[self.question_number]['question']
        current_answer = self.question_List[self.question_number]['correct_answer']
        # formatting:
        current_question = html.escape(current_question)
        self.question = current_question
        self.question_number += 1  # Go to next question.
        # Checking answer.
        self.check_answer(user_answer, current_answer)

    def check_answer(self, user_answer, correct_answer):  # Check question true or false.
        """Check answer function."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
