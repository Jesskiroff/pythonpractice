from __future__ import annotations
import random
from typing import List, Set

WORD_BANK: List[str] = [
"python",
"developer",
"hangman",
"function",
"variable",
"keyboard",
"iteration",
"algorithm",
"computer",
"dictionary",
]

def choose_word(word_bank: List[str]) -> str:
    return random.choice(word_bank)

def initial_display(word: str) -> List[str]:
    return["_"] * len(word)

def get_guess(guessed: Set[str]) -> str:
    while True:

         guess = input("Pick a leter: ").strip().lower()
         if len(guess) != 1 or not guess.isalpha():
             print("Enter a single letter. ")
             continue
         if guess in guessed:
             print("Already guessed, please try a different letter. ")
             continue
         return guess
    
def apply_guess(word: str, display: List[str], guess: str) -> bool:
    hit = False 
    for i, ch in enumerate(word):
        if ch == guess:
            display[i] = ch
            hit = True 
    return hit

def is_solved(display: List[str]) -> bool:
    return "-" not in display

def play(word_bank: List[str], lives: int = 6, reveal:bool = False) -> None:

    word = choose_word(word_bank)
    if reveal:
        print(f"(debug) word: {word}")
