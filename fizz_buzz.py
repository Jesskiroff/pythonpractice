# sum = 0
# for number in range(1,101):
#     sum+=number
# print(sum)

start = 0
for number in range(1,101):
    start = number
    
    if start % 15 ==0:
        print("fizzbuzz")
    elif start % 5 == 0:
        print("buzz")
    elif start % 3 == 0:
        print("fizz")
    else:
        print(start)

