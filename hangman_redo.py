#Create hangman program
from __future__ import annotations
import random
from typing import List, Set

#This is the list of words that the computer will randomly choose from
word_bank = [
    "python",
    "developer",
    "hangman",
    "function",
    "variable",
    "keyboard",
    "iteration",
    "algorithm",
    "computer",
    "dictionary"
]

word = random.choice(word_bank)
print(word)

users_choice = input("Please pick a letter! \n")
print(users_choice)

display = ""
for letter in word:
    display += "_"
print(display)


# display_game = ""
# for letter in word:
#     display_game += users_choice
#     display_game += "_"
# print(display_game)