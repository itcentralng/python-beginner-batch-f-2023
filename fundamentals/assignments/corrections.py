# Write a function that takes a number and returns a list containing items
# of the length of number. e.g. func(2)=>[12, 32]

import random

# def listGenerator(length):
#     our_list = []
#     for i in range(length):
#         our_list.append(i)
#     return our_list

# def listGenerator(length):
#     our_list = []
#     for i in range(length):
#         our_list.append(random.randint(0, length))
#     return our_list

def listGenerator(length):
    our_list = []
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(length):
        word = ""
        for i in range(length):
            word+=random.choice(characters)
        our_list.append(word)
    return our_list

print(listGenerator(4))


# Write a function that takes a string and returns a dcitionary. 
# The dictionary should have 3 keys. 
# e.g {'word':'the string', 'characters':len_of_string, 'combination':[3 random words from the string]}

# def dictionaryGenerator(word):
#     our_dictionary = {'word':word, 'characters':len(word), 'combination':[]}
#     characters = []
#     combination = []
#     for i in word:
#         characters.append(i)
#     for i in range(3):
#         new_word = ""
#         for i in range(len(word)):
#             new_word+= random.choice(characters)
#         combination.append(new_word)
#     our_dictionary['combination'] = combination
#     return our_dictionary

def dictionaryGenerator(word):
    our_dictionary = {'word':word, 'characters':len(word), 'combination':[]}
    characters = []
    combination = []
    for i in word:
        characters.append(i)
    for i in range(3):
        new_word = ""
        while len(new_word) < len(word):
            char = random.choice(characters)
            if word.count(char) >= (new_word+char).count(char):
                new_word += char
        combination.append(new_word)
    our_dictionary['combination'] = combination
    return our_dictionary

print(dictionaryGenerator("ahmad"))

# Write a function that takes a list words and returns the string
# with the highest number of vowels.