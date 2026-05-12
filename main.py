import random
import art

def computer_guess():
    guess_number= random.randint(1,100)
    return guess_number
attempt_easy= 11
attempt_hard= 6
def difficulty_level(level):
    global attempt_easy
    global attempt_hard
    if level == "easy":
        attempt_easy-=1
        return attempt_easy
    elif level== "hard":
        attempt_hard-=1
        return attempt_hard
    return -1

def guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Project")
    print("I am thinking of a number between 1 and 100")
    c_guess= computer_guess()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

    guessed= False

    while not guessed:
        attempt = difficulty_level(difficulty)
        if attempt != 0:
            print(f"You have {attempt} attempts remaining to guess the number.")
            my_guess = int(input("Make a guess: "))

            if my_guess > c_guess:
                print("Too high!")
            elif my_guess < c_guess:
                print("Too low!")
            elif my_guess == c_guess:
                print(f"You got it! The answer was {c_guess}")
                guessed= True
        elif attempt==0:
            print("You've run out of guesses. Refresh the page to run again.")
            guessed= True

guessing_game()





