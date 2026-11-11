import random
import logo
import words

lives = 6

print(logo.logo)
chosen_word = random.choice(words.word_list)

placeholder = ""
lenght = len(chosen_word)
for position in range(lenght):
    placeholder += "_"
print("Word you should guess: " + placeholder)

game_over = False 
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_"
    if guess in display:
        print("You already guessed this letter")
    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word} ***********************YOU LOSE**********************")

    if "_" not in display:
        print("****************************YOU WIN****************************")

    print(logo.stages[lives])
