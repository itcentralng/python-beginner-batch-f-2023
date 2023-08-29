name = "Ahmed"

sentence = """Hi, I am 19 years old"""

age = '19'

# METHODS
person = "_this is an example. and this is another one"

print(person.capitalize())
print(person)

person = "IBRAHIM"
print(person.casefold())

print(person.center(11, '*'))

print(person.count('I'))

person2 = "Hanif"

print(person2.endswith("if"))

print("I go to {school} and it is {pronoun}".format(school="Zamani", pronoun="annoying"))

person3 = "Alameen"
print(person3.find('lameen'))

person4 = "Abdulateef"
print(person4.isalnum())

person5 = "Ahmad"
print(person5.index("a"))

example = "My name is ahmad"

print(example.isalpha())

example2 = "23456"
print(example2.isdigit())

# OPERATIONS

# print(person[0:4])

name = "James Arthur"

print(name[2:5])

print(name.casefold())
print(name.isalpha())

# print(name"a","u",count=2, /)
# print(name.replace(1, ))
print(name.replace('a', 'u').replace('r', 't'))

emails = "ahmad@gmail.com;  anisa@yahoo.com;  hanif@hotmail.com"
# print(emails.split(';')[0].split('@')[1])
# print(emails.split(';')[1].split('@')[1])
# print(emails.split(';')[2].split('@')[1])
print(emails.split(';')[1].strip())

