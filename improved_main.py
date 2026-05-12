import random
import art
EASY_ATTEMPTS= 10
HARD_ATTEMPTS= 5
def computer_guess():
    """this function helps computer guess a number between 1 and 100"""
    guess_number= random.randint(1,100)
    return guess_number

def difficulty_level():
    """this function gives user the number of attempts based on difficulty"""
    level =input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_ATTEMPTS
    elif level== "hard":
        return HARD_ATTEMPTS
    return -1

def compare_guess(my_guess,c_guess,attempt):
    """this function compares my_guess and c_guess also decrease the attempt"""
    if my_guess > c_guess:
        print("Too high!")
        return attempt-1
    elif my_guess < c_guess:
        print("Too low!")
        return attempt-1
    elif my_guess == c_guess:
        print(f"You got it! The answer was {c_guess}")

    return attempt




def guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Project")
    print("I am thinking of a number between 1 and 100")
    c_guess= computer_guess()
    turns= difficulty_level()
    is_guessed=False

    while not is_guessed:

        print(f"You have {turns} attempts remaining to guess the number.")
        my_guess = int(input("Make a guess: "))
        turns = compare_guess(my_guess, c_guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            is_guessed= True
        elif my_guess == c_guess:
            is_guessed= True
        elif my_guess != c_guess:
            print("Guess again.")

guessing_game()





