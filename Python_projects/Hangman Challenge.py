import random

def get_random_word():
    words = ['dragonfruit', 'grape', 'mango', 'apple']
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Current word: {display}")

def hangman():
    word_to_guess = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("guess the fruit")
    print(f"You have {max_incorrect_guesses} incorrect guesses. Good luck!")

    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word_to_guess, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
