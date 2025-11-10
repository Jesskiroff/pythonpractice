friends = 1

def increase_friends ():
  
  print(f"Friends inside func {friends}")
  return friends +1
    

friends = increase_friends(friends)
print(f"friends outside func {friends}")

# #Local scope- exists within functions
# def magic_drink():
#     potion_strength = 2
#     print(potion_strength)

# magic_drink()