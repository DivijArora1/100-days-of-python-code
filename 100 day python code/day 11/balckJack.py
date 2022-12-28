import random

def deal_card():
    '''Reeturns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take alist of cards and return the score calculated from cards'''
    if sum(cards) ==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("Loose ,opponent has the black jack" )   
    elif user_score == 0:
        print("win with a black jack")    
    elif user_score>21:
        print("you went over you loose") 
    elif computer_score >21:
        print("compter went over ,you win")
    elif computer_score > computer_score:
        print("You win"  )  
    else:
        print("You loose"   ) 

def play_game():       

    user_cards = []    
    computer_cards = []
    is_game_over = False

    # to add 2 cards to both
    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #this loop is for the user to take card untill the game is over
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards:{user_cards}, current score: {user_score} ")
        print(f" Computer first card: {computer_cards[0]} ")

        if user_score ==0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card , type 'n' to pass")    
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True    


    while computer_score !=0  and computer_score <17:
        #this while loop is for the computer to keep drawing cards 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" Your final hand is  {user_cards}, final score is {user_score} ")
    print(f" computers final hand is  {computer_cards}, final score is {computer_score} ")
    compare(user_score,computer_score)


while input("Do you want to play the game again type 'y' to play or 'n' to exit the game") =='y':
    play_game()
