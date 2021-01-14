import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

input_word = input("Enter a word: ").upper()
word_list = [phonetic_dict[letter] for letter in input_word]

print(word_list)
