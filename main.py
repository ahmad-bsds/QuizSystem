from data import data
from quizBrain import QuizBrain
from uiDesign import Gui

# Creating a quiz system.
quiz = QuizBrain(data)

def true_ans():
    quiz.next_question("True")

def false_ans():
    quiz.next_question("False")

# Creating the GUI interface.
interface = Gui(true_ans, false_ans)

# Loop to run the quiz while there are still questions left.
while quiz.still_has_question():
    # Show the current question on the GUI.
    interface.show_question(quiz.question)
    # Wait for user input (True or False button click).
    interface.screen.wait_variable(interface.true_button['text'])

