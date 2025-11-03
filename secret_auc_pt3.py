name= input("What is your name? ")
price = int(input("How much do you want to bid? : $"))
more_bidders = input("Are there more bidders? ")

bidding_dict = {}
bidding_dict[name] = price

print(bidding_dict)

final_bid_price = 0
winner = ""
for bidder in bidding_dict:
    bid_price = name[price]
    if bid_price > final_bid_price:
        final_bid_price = bid_price
        winner = bidder