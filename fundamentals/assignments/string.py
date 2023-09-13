# Assignment 1
# 1. Write a short description of what you understand a string
# to be, in your own words.

# 2. Give 10 examples of strings

# What do you understand by a variable?

# 4. Give 5 examples of bad variables names

# Assignment 2
# 1. For each of the following methods, explain what they do with 2 examples:
# - startswith
name = 'Khadija'
print(name.startswith('a'))
# - format
text = "I have a {animal}"
print(text.format(animal='dog'))
text = "I have a {} and a {}"
print(text.format('dog', 'cat'))
print(text.format('fish', 'cow'))
# - index
school = "islamic learning center"
print(school.index('le'))
# - lower
continent = 'Africa'
print(continent.lower())
# - upper
message = "python is fun"
print(message.upper())
# - isalpha
letters = "english language"
print(letters.isalpha())
# - isalnum
alnum = "iphonepro"
print(alnum.isalnum())
# - islower
footballer = "Ronaldo"
result = footballer.islower()
print(result)
# - isupper
human = "WOMAN"
result = human.isupper()
print(result)
# - replace
david = "Bat Ball"
print(david.replace('Ba', 'Ro'))
x = "rice right rift"
print(x.replace('r', 'l').replace('i', 'a').replace('f', 'p'))
name1 = "Alameen Bature"
print(name1.replace('a', 'i').replace('B', 'P'))
sport = "Football"
print(sport.replace('Foot', 'Basket'))
class_ = "Fight Club"
print(class_.replace('F', 'N'))
# - split
name2 = "Zakiyya,Abdulkadir"
print(name2.split(','))
word = "Fundamentals"
print(word.split('n'))
name5 = "Alameen,Aliyu"
print(name5.split(','))
event = "propeller paragon"
print(event.split(' '))
omale = "Ranger Over"
print(omale.split("R"))

fullname = "Abubakar Sani Balarabe"

firstName = fullname.split()[0]
middleName = fullname.split()[1]
lastName = fullname.split()[2]
# - strip
name = " Ibrahim Saleh "
print(name.strip())
