import pandas
data = pandas.read_csv('/Users/programing/Desktop/programing/NATO-alphabet-start/nato_phonetic_alphabet.csv')

phon_dict = {row.letter: row.code for (index,row) in data.iterrows()}

#print(phon_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def gen():
    name = input("Write Name \n")
    try: 
        output_dict = [phon_dict[n.upper()] for n in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        gen()
    else:
        print(output_dict)
    
gen()