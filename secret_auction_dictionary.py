def questions():
    your_name = input("What is your name? ")
    bid_price = int(input("How much do you want to bid? "))

    the_dictionary = {}
    the_dictionary[your_name] = [bid_price]

    print(the_dictionary)

keep_on_bidding = True
other_bidder = input("is there another bidder? ").lower
if other_bidder == "yes":
    keep_on_bidding = True
else:
    keep_on_bidding = False
while other_bidder:
    questions()