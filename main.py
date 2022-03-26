import os
# import logo
from art import logo
print(logo)
print("Welcome to the secret auction program.")
# create a dictonary which store all the name and price
auction_data = {}
is_end = False
while not is_end:
    name = input("What is your name ?: ")
    bid_price = int(input("What's your bid ?: $"))
    # add above data into auction_data
    auction_data[name] = bid_price
    user_choice = input("Are there any other bidder's ? Type 'yes' or 'no'. ")
    if(user_choice.lower() == 'yes'):
        os.system("cls")
        continue
    else:
        is_end = True

# store maximum bid's price
max_bid = 0
# store user name who bid's highest
max_bid_user = ""

for name in auction_data:
    # getting bid price of each user
    user_bid = auction_data[name]
    if user_bid > max_bid:
        max_bid = user_bid
        max_bid_user = name

# Finally tell to user who win's the bid
os.system("cls")
print(f"The winner is {max_bid_user} with a bid of ${max_bid}. ")
