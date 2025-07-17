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

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <=12:
        print("Child tickets are $5")
    elif age<=18:
       print("youth tickets are $10")
    else:
        print("Adult tickets are $15.")

else: 
    print("You need to grow taller before you can ride the rollercoaster. ")