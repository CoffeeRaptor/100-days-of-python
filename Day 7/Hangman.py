import random
import hangman_stages
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_stages.logo)

# Debugging line to show the solution (optional, can be removed later)
#print(f'Pssst, the solution is {chosen_word}.')

# Initialize display and guessed words
display = ["_" for _ in range(word_length)]
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the guess has already been made
    if guess in guessed_letters:
        print(f"You already guessed the letter '{guess}', try again.")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"The letter '{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("*********************************************You lose*********************************************")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("*********************************************You win*********************************************")

    # Display the current hangman stage
    print(hangman_stages.stages[lives])
