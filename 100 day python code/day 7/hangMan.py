import random
from hangman_words import word_list
from hangman_art import stages, logo

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
print(f"The chosen word is {choosen_word} ")

lives = 6
print(logo)
display = []
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in display:
        print(f"You have already chosed the leteer {guess}")

    if guess not in choosen_word:
        print(f"You have guessed a letter that's not in the list .You loose a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")
    print(f"{' '.join(display)} ")
    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])
