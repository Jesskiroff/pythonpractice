# multiple if statements
# if cond 1   vs    if cond 1
#do A                  do A
# elif cond 2  vs   if cond 2
# do B                  do B
# else         vs   if cond 3:
#  do C                    do C

#with multiple if nstatement scenario, if all 3 conditions are true, then A,k B, and C will add be executed

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <=12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age<=18:
       bill = 10
       print(f"youth tickets are ${bill}")
    else:
        bill = 15
        print(f"Adult tickets are ${bill}.")
    
    photo_included = input("Do you want to have a photo taken? Type Y for yes and N for no. ")
    if photo_included == "y":
        #add $3 to their bill
        bill += 3
        print(f"Your final bill is ${bill}")
    
else: 
    print("You need to grow taller before you can ride the rollercoaster. ")