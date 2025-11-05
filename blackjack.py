import random

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6,7, 8, 9, 10,10,10,10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range (2):
    user_cards.append(deal_card()) #when you want to add a single item to an existing list, you should use append instead of += (which is shorthand for the extend function)