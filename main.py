from manager import load_high_score
from quiz import play_quiz

if __name__ == "__main__":
    high_score, score_date = load_high_score()
    print("Welcome to the quiz!\n")

    while True:
        play_game = input("Do you want to play? (y/n): ").strip().lower()
        if play_game == "y":
            high_score = play_quiz(high_score)
        elif play_game == "n":
            print("Thank you! Have a nice day")
            break
        else:
            print("Invalid input. Try again")