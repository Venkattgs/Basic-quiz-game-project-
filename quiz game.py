# Quiz Game with Scoring System

# Questions and Answers dictionary
questions = {
    "What is the capital of France?": "Paris",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest mammal in the world?": "Blue Whale",
    "What is the powerhouse of the cell?": "Mitochondria"
}

# Function to run the quiz
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")

        # Validate user input and check the answer
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

        print()

    return score, total_questions

# Function to calculate and display user performance
def display_performance(score, total_questions):
    print("Quiz Complete!")
    print(f"Your final score is {score}/{total_questions}")

    percentage = (score / total_questions) * 100
    print(f"You got {percentage:.2f}% of the questions correct.")

# Run the quiz
if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("Try to answer the following questions:")
    print("------------------------------------")

    user_score, total_questions = run_quiz(questions)
    display_performance(user_score, total_questions)
