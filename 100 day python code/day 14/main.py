from art import logo,vs
from data import data
import random 
def format_data(account):
    ''' Format account data into printable format.'''
    account_name = account["name"]
    account_name = account["name"]
    account_desr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desr}, from {account_country} "

def check_answer(guess,a_followers, b_followers):
    '''Itake the users guess and follower count and returns wheather it is correct or  not '''
    # if a_followers > b_followers and guess == a:
    if a_followers > b_followers :
        # if guess =='a':
        #     return True
        # else:
        #     return False  
        # other way
        return guess == 'a'  
    else:
        return guess == 'b'

# display art
print(logo)
score = 0
game_should_continue = True
while game_should_continue:
    # Generate a random account from the game data.
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)} ")
    print(vs)
    print(f"Against   B: {format_data(account_b)} ")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # Feedback.
    if is_correct:
        score +=1
        print(f"You are right . Final score {score}")
    else:
        game_should_continue = False
        print(f'Sorry thats wrong. Final score {score} ')    
    # Score Keeping.

    # Make game repeatable.

    # Make B become the next A.

    # Clear screen between rounds.

