# How the works

# Create a class
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # Looks to see if the question number is less then the length of the question list.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # current Question is equal to question number from list
        current_question = self.question_list[self.question_number]
        # Question number + 1
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check to see if thr users answer matches the right answer
        self.check_answer(user_answer, current_question.answer)

    # Checks the users answer to the correct answer
    def check_answer(self, user_answer, correct_answer):
        # Make users input lower case
        if user_answer.lower() == correct_answer.lower():
            # if correct add one to the score
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
