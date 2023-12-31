print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
action = input('''There's a sketchy looking forest to your left and a beautiful lake to the right.
Where do you want to go? (type 'right' or 'left')\n''').lower()

if action == "left":
  print("You fell into a hole and died. Game Over! \n(Yo, you need to pay attention to the discriptions... That forest was sketchy as hell)")
else:
  action = input("You get to the shore of a beautiful and enormous lake. Practically impossible to swim across.\nYou see the ferry-person, but they're too far away. It seems you'll have to wait until sunrise to catch a ride... Or you can swim. What do you want to do? (type 'wait' or 'swim')\n").lower()
  if action == "swim":
    print("Like... I pretty much said the lake was impossible to swim across. \nYou know what? You got eaten by an oyster. Yes. That's how you died. Game Over.")
  else:
    action = input("Rewads come to those who wait. It was 5:59am and the sun rose quickly. \nThe ferry-person gives you a ride to Treasure Island. You two had a nice chat on the way.\nUpon arriving on the island, you see a nest of snakes to the left, bear traps to the right, and a treasure chest in front of you. Where do you go? (type'left, 'right', or 'front')\n").lower()
    if action == "left":
      print("I'm not even gonna bother to make it look epic... You were bitten by a snake, fainted, woke up home a few hours later (the ferry-person took you back), \nbut you died of embarassment of taking such a stupid decision a few hours later. Game Over.")
    elif (action == "right"):
      print("You fell on the traps the bears set for unwise adventurers. You became human skewer. Game Over.")
    else:
      print("The moment we've been expecting all along! You open the treasure chest and... It's empty... \nI mean... Of course it is. Nothing in life is that easy. \nBut what matters are the friends along the way. You and the ferry-person go have a beer after returning to land \n(on them, cause you're broke... that's why you wanted the treasure in the first place). \nThe end")
