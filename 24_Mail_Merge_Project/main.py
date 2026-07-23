#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# Read all invited names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the invitation template
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_text = letter_file.read()
#print(letter_text)

# Create one personalized letter for every name
for name in names:
    clean_name = name.strip()

    personalised_letter = letter_text.replace(PLACEHOLDER, clean_name)
    #print(personalised_letter)

    output_path = (
        f"Output/ReadyToSend/"
        f"letter_for_{clean_name}.txt"
    )

    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(personalised_letter)
