import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    number_of_tries = 0
    max_tries = 10
    has_guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while number_of_tries < max_tries:
        try:
            player_guess = int(input("Enter your guess: "))
            number_of_tries += 1

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                has_guessed_correctly = True
                break
        except ValueError:
            print("Please enter a valid number.")

    if has_guessed_correctly:
        print(f"Congratulations! You've guessed the number in {number_of_tries} tries.")
    else:
        print(f"Sorry, you've used all {max_tries} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
