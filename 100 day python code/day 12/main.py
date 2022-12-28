import random 
easy_level_turn = 10
hard_level_turn = 5
# function to check users guess against the actual answer 
def check_answer(guess, answer,turns):
    """check answer against guess. returns number of turns remaining"""
    if guess > answer:
        print("too high")
        return turns - 1

    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print("you got it")
       
# function to check the difficulty 
def set_difficulty():
    level = input("choose the difficulty 'easy' or 'hard' ")
    if level == 'easy':
        return easy_level_turn
    elif level == 'hard':
        return hard_level_turn

#choosing a random number between 1 and 100
def game():
    print("Welcome to the number guessing game")
    print("I am thinkimg of a number between 1 and 100")
    answer = random.randint(1,100)
    print(f"The answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns}  turns left ")
        #let the user guess the number
        guess = int(input("enter the number that you guess"))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print("You are out of guesses")
            return #this exits the program when out of guesses..otherwise the loop continues

game()


