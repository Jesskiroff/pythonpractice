import random 
# print("Hello, welcome to Hangman! Please guess your letters to come up with the word! Good luck!")

# empty_word = [" "," "," "," "," "," "," "]
# word=["h","a","n","g","m","a","n"]

# hangman w hints


word_list = ["aardvark", "baboon", "camel"]
# todo 1: randomly choose a word from wordlist. assign it to a viriable called chosen_word
chosen_word = random.choice(word_list)
print(chosen_word)

#4 Create a placeholder w the same number of blanks as the randomly chosen word.
place_holder =""
for letter in chosen_word:
    place_holder+= "_"
print(place_holder)
# 2. ask user to guess letter and assign letter to variable.
guess_letter = input("Guess a letter! \n").lower()
print(guess_letter)
# 3. check if letter that user guessed is one of the letters in chosen_word. print right if right and wrong if wrong
for letter in chosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")


#5 create a display that puts the guess letter in the right positions 5\
