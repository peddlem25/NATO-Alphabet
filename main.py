import pandas

# python3 -m venv SnmpPollerVenv
# ls
# mkdir SnmpPollerCode
# ls
# source SnmpPollerVenv/bin/activate
# pip install pandas
# pip install --upgrade pandas
# pip freeze > requirements.txt
# pip install -r requirements.txt

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
