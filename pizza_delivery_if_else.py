print("Welcome to python pizza ")
size = input("What size pizza do you want? s, m, or l: ").upper()

topping = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()


# topping_cost = 3
# extra_cheese_cost = 2

# if size == "s":
#     price = 10
#     print(f"The price is ${price}")
# elif size == "m":
#     price = 13
#     print(f"The price is ${price}")
# else:
#     price = 15
#     print(f"The price is ${price}")

#     if

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25

if topping =="Y":
    if size =="S":
        bill += 2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print (bill)