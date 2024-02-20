#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_filename = "./input/Letters/starting_letter.txt"
guests_filename = "./input/Names/invited_names.txt"

with open(guests_filename) as guest_list:
    guests = guest_list.readlines()
    print(guests)

for guest in guests:
    personal_letter = guest.strip() + "'s invite"

    with open(f"{personal_letter}.txt", "w") as invite:
        with open(letter_filename) as letter:
            lines = letter.readlines()
            lines[0] = lines[0].replace("[name]", guest.strip())

            for line in lines:
                invite.write(line)
