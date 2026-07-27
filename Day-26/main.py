# NATO Phonetic Alphabet

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

# Create a dictionary out of the csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index , row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_code_word = [phonetic_dict[letter] for letter in word]
print(phonetic_code_word)


