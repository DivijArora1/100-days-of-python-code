import random     
from hangman_words import word_list
from hangman_art import stages

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
print(f"The chosen word is {choosen_word} ")

lives = 6

from hangman_art import logo
print(logo)
#using for loop to create number of empty spaces 
display = []
for _ in range(word_length):
    display += "_"
# print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # This is going to replace the letter in word chosen with the guess.
    #now in this loop if we choose 'a' and chosen word is camel ,then first it with compare 'c' with a and if dosent match loops runs again ..slly for all
    for position in range(word_length): #0-4
        letter = choosen_word[position] #singel guseed letter in word stored
        if letter == guess: #compares with all letters and our guess
            display[position] = letter
    if guess in display:
      print(f"You have already chosed the leteer {guess}")
        
    if guess not in choosen_word:
      print(f"You have guessed a letter that's not in the list .You loose a life ")
      lives -= 1
      if lives ==0:
        end_of_game =True
        print("You loose")
    #this loop runs untill the ent blanks are filled
    print(f"{''.join(display)} ")
    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives])



