#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

def game_mode():
  game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if game_mode == 'easy':
    return 10
  else:
    return 5

def gameover(total_lives, has_guessed):
  if total_lives == 0 or has_guessed:
    return True
  return False

def guess_game():
  
  start = 1
  end = 100
  target = randint(start, end)
  #print(target)
  
  print(f"I'm thinking of a number between {start} and {end}")
  
  #variables and functions
  has_guessed = False
  
  total_lives = game_mode()
  
  while not gameover(total_lives, has_guessed):
      
    print(f"You have {total_lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    total_lives -=1
  
    if guess < target and total_lives > 0:
      print("Too Low.")
    elif guess > target and total_lives > 0:
      print("Too High.")
    else:
      if guess == target:
        print(f"You got it! The answer was {target}")
      elif(total_lives == 0):
        print(f"You've run out of guesses. The answer was {target}.")
      play_again = input("Would you like to play again? (type 'y' or 'n') ")
      if play_again == "y":
        guess_game()
      break

#main
print(logo)

print("Welcome to the Number Guessing Game!")

guess_game()

print("It was lovely playing with you!")
print("See you around!")
  
