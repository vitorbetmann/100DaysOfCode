############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from random import randint
from art import logo
from replit import clear

def hit_next_card():
  next_card = cards[randint(0, len(cards) - 1)]
  return next_card

def cards_sum(cards_list):
  sum = 0
  for i in range(0, len(cards_list)):
    sum += cards_list[i]
  return sum

def ace_value(cards_list):
  while cards_sum(cards_list) > 21 and 11 in cards_list:
    for i in range(0, len(cards_list)):
      if cards_list[i] == 11:
        cards_list[i] = 1
        if cards_sum(cards_list) <= 21:
          break
        
  return cards_sum(cards_list)
  

def blackjack():
  print(logo)

  player_cards = []
  dealer_cards = []
  
  
  player_cards.append(hit_next_card())
  
  dealer_cards.append(hit_next_card())
  dealer_cards.append(hit_next_card())
  
  hit_card = True
  while hit_card:
    player_cards.append(hit_next_card())
  
    player_sum = ace_value(player_cards)

    if player_sum >= 21:
      break
    
    print(f"    Your cards are {player_cards}, they amount to {player_sum}.")
    print(f"    Dealer's first card is {dealer_cards[0]}")

    if player_sum >= 21:
      hit_card = False
    else:
      hit_card = input("Type 'y' to get another card, type 'n' to pass: ") == "y"

      
  print(f"    Your final hand: {player_cards}, they amount to {player_sum}.")

  dealer_sum = ace_value(dealer_cards)

  if player_sum > 21:
    print(f"    Dealer's final hand: {dealer_cards}, they amount to {dealer_sum}")
    print("You went over 21. You lose.")
    
  else:    
    while dealer_sum < 17:
      dealer_cards.append(hit_next_card())
      dealer_sum = ace_value(dealer_cards)
      

    
    print(f"    Dealer's final hand: {dealer_cards}, they amount to {dealer_sum}")

    if player_sum == dealer_sum:
      print("It's a draw.")
    elif player_sum == 21:
      print("BLACKJACK! You win!")
    elif dealer_sum == 21:
      print("Opponent has Blackjack. You Lose")
    elif dealer_sum > 21:
      print("Opponent went over 21. You Win!")
    elif player_sum > dealer_sum:
      print("You Win!")
    else:
      print("You Lose.")

is_gameover = input("Do you want to play a game of Blackjack? type 'y' or 'n': ") != 'y'

while not is_gameover:
  clear()
  blackjack()
  is_gameover = input("Do you want to play a game of Blackjack? type 'y' or 'n': ") != 'y'
  
print("Thanks for playing!")
  
# is_gameover = input("Do you want to play a game of Blackjack? type 'y' or 'n': ") != 'y'
# clear()


##################### Hints #####################

#Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
