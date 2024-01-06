from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

#variables
has_next_bidder = True
bids_dictionary = {}
winner_name = ""
winner_bid = 0

#collect bids in a dictionary
while has_next_bidder: 
  name = input("What's your name? ").title()
  bid = int(input("What's your bid? $"))
  
  bids_dictionary[name] = bid
  #print(bids_dictionary)
  
  has_next_bidder = input("Are there any other bidders? type 'yes' or 'no'.\n") == "yes"
  clear()

#find highest bidder
for key in bids_dictionary:
  if bids_dictionary[key] > winner_bid:
    winner_name = key
    winner_bid = bids_dictionary[key]

print(f"The winner is {winner_name} with a bid of ${winner_bid}")
