rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

drawing = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors")
player_play = int(input("What do you choose? Press '0' for Rock, '1' for Paper, or '2' for Scissors\n"))
ai_play = random.randint(0, 2)

print(f"You played {player_play}:")
print(drawing[player_play])
print()
print(f"AI played:")
print(drawing[ai_play])
print()

if player_play == ai_play:
  print("It's a draw.")
elif (player_play == ai_play) or (player_play == 0 and ai_play == 2):
  print("You Won!")
else:
  print("You lost")
