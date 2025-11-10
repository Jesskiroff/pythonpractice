import random

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6,7, 8, 9, 10,10,10,10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
is_game_over = False

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the list of cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(11)

    return sum (cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "User has lost, opponent has a blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "you win, computer score went over 21"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


for _ in range (2):
    user_cards.append(deal_card()) #when you want to add a single item to an existing list, you should use append instead of += (which is shorthand for the extend function)
    computer_cards.append(deal_card())


while not is_game_over:
        
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else: 
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))