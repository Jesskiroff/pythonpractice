print("Welcome to Treasure Island. Your mission is to find the treasure! ")

which_door = input("Which door would you like to go in to: left or right. Input r or l.\n").lower()

swim_or_wait_choice = input("Would you like to swim or wait? Input s or w.\n").lower()

door_color_choice = input("Which of the doors do you want to go into: red, blue or yellow? Input r, b, or y\n").lower()

if which_door == "l":
    swim_or_wait_choice
    if swim_or_wait_choice == "s":
      door_color_choice
      if (door_color_choice) == "y":
        print("Congradulations, you've found the treasure!")
      else:
        print("Sorry, you went through the wrong color door :(")
    else:
      print("A shark ate you. You should have waited.")
else: 
    print("You got caught in a trap. You should have went through the left door. ")
# if swim_or_wait_choice == "s":
#     print(door_color_choice)
# else:
#     print("A shark ate you. You should have waited.")
# if (door_color_choice) == "y":
#     print("Congradulations, you've found the treasure!")
# else:
#     print("Sorry, you went through the wrong color door :(")
    # else:
    #     print("A shark ate you. You should have waited.")
# else: 
#     print("You got caught in a trap. You should have went through the left door. ")