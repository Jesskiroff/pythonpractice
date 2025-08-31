import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator!")
numb_of_letters = int(input("How many letters would you like your password to have?\n"))
numb_of_numbers = int(input("How many numbers would you like your password to have?\n"))
numb_of_symbols = int(input("How many symbols would you like your password to have?\n"))

for letter in range(1, numb_of_letters + 1):
    pass_letters = random.choice(letters)
    print(pass_letters)


for number in range(1, numb_of_numbers + 1):
    pass_numbers = random.choice(numbers)
    print(pass_numbers)

for symbol in range(1, numb_of_symbols +1):
    pass_symbols = random.choice(symbols)
    print(pass_symbols)
