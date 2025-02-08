import random
from art import logo

def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7 ,8 ,9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list): 
    """Take a list of cards and return the score calculated from the Cards"""
    if sum(list) == 21 and len(list)==2:
        return 0
    
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(u_score, c_score):
    if u_score == c_score:
        return 'DRAW'
    elif c_score == 0:
        return f'Lose, opponent has a Blackjack'
    elif u_score > 21:
        return 'You went over. You Lose.'
    elif c_score > 21:
        return 'Opponent went over. You Win'
    elif u_score == 0:
        return 'User Win With a Blackjack'
    elif u_score > c_score:
        return 'You Win'
    else:
        return 'You Lose'

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards} and your score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to Pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards} and Your final score is: {user_score}")
    print(f"Computer final hand: {computer_cards} and Computer final score is: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack. Type 'y' for yes and 'n' for no: ") =='y':
    print('\n'*15)
    play_game()

