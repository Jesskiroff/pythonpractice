import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator!")
numb_of_letters = int(input("How many letters would you like your password to have?\n"))
numb_of_numbers = int(input("How many numbers would you like your password to have?\n"))
numb_of_symbols = int(input("How many symbols would you like your password to have?\n"))


# password = ""

# for letter in range(1, numb_of_letters + 1):
#     pass_letters = random.choice(letters)
#     password += pass_letters
# # print(password)


# for number in range(1, numb_of_numbers + 1):
#     pass_numbers = random.choice(numbers)
#     password += pass_numbers
# # print(password)

# for symbol in range(1, numb_of_symbols +1):
#     pass_symbols = random.choice(symbols)
#     password += pass_symbols
# print(password)

password_list = []
for character in range(0,numb_of_letters ):
    password_list.append(random.choice(letters))

for character in range(0,numb_of_numbers):
    password_list.append(random.choice(numbers))

for character in range(0,numb_of_symbols):
    password_list.append(random.choice(symbols))
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for letter in password_list:
    password+= letter
print(f"Your password is {password}")