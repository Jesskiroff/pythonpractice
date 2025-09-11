#Create hangman program
import random

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

display = ""
for letter in word:
    display += "_"
print(display)

users_choice = input("Please pick a letter! \n")
print(users_choice)

display_game = ""
for letter in word:
    if letter == users_choice:
        display_game += users_choice
    else:
        display_game += "_"
print(display_game)