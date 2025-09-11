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
    """Return a random word from the provided bank."""
    return random.choice(word_bank)


def init_display(word: str) -> List[str]:
    """Return a list of underscores, one per letter in the word."""
    return ["_"] * len(word)


def get_guess(guessed: Set[str]) -> str:
    """Prompt the user until they provide a new single alphabetic letter."""
    while True:
        guess = input("Pick a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
            continue
        if guess in guessed:
            print("Already guessed; try a different letter.")
            continue
        return guess


def apply_guess(word: str, display: List[str], guess: str) -> bool:
    """Reveal guessed letter in display; return True if guess hits at least once."""
    hit = False
    for i, ch in enumerate(word):
        if ch == guess:
            display[i] = ch
            hit = True
    return hit


def is_solved(display: List[str]) -> bool:
    """Check if there are no blanks left."""
    return "_" not in display


def play(word_bank: List[str], lives: int = 6, reveal: bool = False) -> None:
    """Run a single game of Hangman.

    Parameters
    ----------
    word_bank: list of candidate words.
    lives: number of wrong guesses allowed.
    reveal: if True, prints the word for debugging.
    """
    word = choose_word(word_bank)
    if reveal:
        print(f"(debug) word: {word}")

    display = init_display(word)
    guessed: Set[str] = set()
    wrong: Set[str] = set()

    print(" ".join(display))

    while lives > 0 and not is_solved(display):
        guess = get_guess(guessed)
        guessed.add(guess)

        if apply_guess(word, display, guess):
            print("Nice!")
        else:
            lives -= 1
            wrong.add(guess)
            print("Nope!")

        print(" ".join(display))
        print(f"Lives: {lives} | Wrong: {', '.join(sorted(wrong)) if wrong else '—'}\n")

    if is_solved(display):
        print(f"You guessed it: {word} 🎉")
    else:
        print(f"Out of lives. The word was '{word}'.")


if __name__ == "__main__":
    play(WORD_BANK)
