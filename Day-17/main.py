from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of questions
question_bank = []
for question in question_data:
    question_model = Question(question["text"], question["answer"])
    question_bank.append(question_model)

# Create an object for class QuizBrain
quiz = QuizBrain(question_bank)

# Loop through all questions
while quiz.still_has_question():
    question = quiz.next_question()

# Display final score
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
