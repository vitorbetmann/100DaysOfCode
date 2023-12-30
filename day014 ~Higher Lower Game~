import random
from replit import clear
from game_data import data
from art import logo, vs

random.shuffle(data)
score = 0
for i in range(1, len(data)):
  print(logo)
  
  if score != 0:
    print(f"You're right! your score is {score}.")
    
  print(f"Compare A: {data[i - 1]['name']}, a {data[i - 1]['description']}, from {data[i - 1]['country']}.")
  print(vs)
  print(f"Compare B: {data[i]['name']}, a {data[i]['description']}, from {data[i]['country']}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = data[i - 1]['follower_count']
  b_follower_count = data[i]['follower_count']
  correct_guess = (guess == "a" and a_follower_count > b_follower_count) or (guess == "b" and a_follower_count < b_follower_count)
  
  if correct_guess:
    score += 1
  else:
    print("Sorry, that's wrong.", end="")
    break

  clear()

print(f"Final score: {score}.")
