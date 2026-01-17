import random
from manager import save_high_score
from questions import questions

def ask_question(quiz):
    options = quiz['options'].copy()
    random.shuffle(options)

    print(quiz['question'])
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")


    while True:
        user_answer = input(f"Choose an option (1-{len(options)}): ").strip()
        if not user_answer.isdigit():
            print("Please enter a number.")
            continue

        user_answer = int(user_answer)
        if user_answer < 1 or user_answer > len(options):
            print("Invalid option.")
            continue
        break

    if options[user_answer - 1] == quiz['answer']:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. Correct answer: {quiz['answer']}\n")
        return False

def play_quiz(high_score):
    quiz_questions = questions.copy()
    random.choice(quiz_questions)
    score = 0

    for q in quiz_questions:
        if ask_question(q):
            score += 1

    print(f"Your final score: {score} / {len(quiz_questions)}")

    if score > high_score:
        print("New High Score!")
        save_high_score(score)
        high_score = score
    else:
        print(f"High Score to beat: {high_score}")

    return high_score