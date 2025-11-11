import random 

list_of_numbers = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                   41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                   51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                   61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                   71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
                   81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
                   91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# print("Welcome to the number guessing game! \n I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ") 

number_chosen = int(random.choice(list_of_numbers)) #computer automatically generates a number to be guessed by the user

number_of_attempts = 0
if difficulty_level == "hard":
    number_of_attempts = 5
else:
    number_of_attempts = 10
print(number_of_attempts)

for x in range(1, number_of_attempts + 1):
    answer_attempt = int(input (f"Guess a number. You have {number_of_attempts} guesses."))
    number_of_attempts -= 1
    if answer_attempt == number_chosen:
        print(f"You guessed it! the answer is {answer_attempt}")
    else:
        print(f"Nope, you have {number_of_attempts} guesses left")
        if answer_attempt > number_chosen:
            print ("Hint: It's lower")
        else:
            print ("Hint: It's higher")
