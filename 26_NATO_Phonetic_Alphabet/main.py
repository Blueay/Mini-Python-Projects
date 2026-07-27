################ Version 1 ########################

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1: Create dictionary in this format:
#key_dict = {new_key:new value for (index, row) in data.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2: Create a list of the phonetic code words form a word that the user inputs
word = input("Enter a word: ").upper()
#key_list = [ new item for item in list]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)



###################### Version 2  ########################


"""
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1: Create dictionary in this format:
alphabet_dict = data.set_index("letter")["code"].to_dict()
print(alphabet_dict)

#alphabet_df = pd.DataFrame(alphabet_dict.items(), columns=["letter", "code"])
#print(alphabet_df)

#TODO 2: Create a list of the phonetic code words form a word that the user inputs
word_input = input("Enter a word: ").upper()
letter_list = list(word_input)
print(letter_list)

phonetic_list = []
for letter in letter_list:
    phonetic_list.append(alphabet_dict[letter])
print(phonetic_list)

"""