import random 

friends = [ "Alice",
    "Benjamin",
    "Clara",
    "David",
    "Elena",
    "Frank",
    "Grace",
    "Henry",
    "Isabella",
    "Jack"]

who_pays_the_bill = random.choice(friends)
print(who_pays_the_bill)


#how to get the number value of items in a list
print(len(friends))

number_of_friends = len(friends)
#if i try to print the last state by printing (friends(number_of_friends)), then I iwll get an 
# error bc my last index would be 50 bc that's the length. 
# the last index is always len- 1

print(friends[number_of_friends - 1])