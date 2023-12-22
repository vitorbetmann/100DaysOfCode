import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  result = ""
  
  shift = shift % 26
  if shift < 0:
    shift += 26
  
  for i in range(len(text)):
    if text[i] not in alphabet:
      result += text[i]
    else:
      letter_position = alphabet.index(text[i])
      if direction == "encode":
        new_letter = letter_position + shift - 26
      elif direction == "decode":
        new_letter = letter_position - shift
      result += alphabet[new_letter]
  
  print(f"The {direction}d text is {result}")
      #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
   

#TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

keep_playing = "yes"

while keep_playing == "yes":
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).


  caesar(direction, text, shift)
  input("Wanna keep playing? (type 'yes' to keep playing of 'no' to quit)")

print("Thanks for using Caeser Cypher! See you around")
