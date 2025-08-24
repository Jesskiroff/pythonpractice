import random

users_choice = input("Which do you choose? Type 0 for rock, 1 for paper, or 2 for scissors \n")

computers_choice = random.randint(0,2)
computers_choice_str = str(computers_choice)

print(f"You chose {users_choice}")
print(f"the computer chose {computers_choice_str}")



if users_choice == "0" and computers_choice_str == "1":
    print("You lose")
elif users_choice == "1" and computers_choice_str == "2":
    print("You lose")
elif users_choice == "2" and computers_choice_str == "0":
    print("You lose")
elif users_choice == "1" and computers_choice_str == "0":
    print("You win!")
elif users_choice == "2" and computers_choice_str == "1":
    print("You win!")
elif users_choice == "0" and computers_choice_str == "2":
    print("You win!")
else:
    print("The game is tied")