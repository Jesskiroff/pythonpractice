import random 

word_list = [
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

generate_word = random.choice(word_list)

word = generate_word
print(word)

pick_letter = input("Pick a letter: ").lower()

users_choice = pick_letter


display = ""
for letter in word:
    display += "_"
print(display)


word_is = ""

while "_" in word_is:
    for char in word:
        if char == users_choice:
            word_is += char
        else:
            word_is += "_"
print(word_is)


'''Rule of thumb
- Use a for loop when iterating over a list, string, range, generator
- use while loop when you do not know how many times you'll loop (run it until condition changes, user quits, or challenge is solved)
- use for... else / while ... else when you want a block that runs only if the loop didn't break (e.g. "not found" case)
- Write a fumction when you want to name a task, reuse it, test it, or hide details (validation state, updates, formatting


Decision guide:

- if iterating an item in collecton, use a for loop
- if looping until a game state changes or input is valid
- if searching until found, else handle not found use for-while... else
-if logic repeats or is complex, then use a function
- if cross-product/ nested data use nested loops or itertools.product)'''

