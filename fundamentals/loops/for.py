# numbers = [1, 2, 3, 4, 5]
# name = "Abdullahi"
# people = [{'name':'Ahmad', 'age':12}, {'name':'James', 'age':22}]

# print('1.')
# for number in numbers:
#     print(number*2)

# print('2.')
# for alphabet in name:
#     print('Char: '+alphabet)

# print('3.')
# for person in people:
#     print('Name: {} Age: {}'.format(person.get('name'), person.get('age')))

# print('4.')
# for person in people:
#     print('Name: {name} Age: {age}'.format(name=person.get('name'), age=person.get('age')))

# print('5.')
# for person in people:
#     print('Name: '+person.get('name')+' Age: '+str(person.get('age')))

# # Q1. Loop through a list of numbers from 1 - 10 and 
# # print out all numbers one by one

# # Q2. Loop through a list of numbers from 1 - 10 and 
# # print out only the odd numbers.

# # Q3. Loop through a list of numbers from 1 - 10 and 
# # print out only the prime numbers.
# print("PRIME NUMBERS")
# # Loop through all numbers between 2 and 11 using the builtin range() function
# for number in range(2, 11):
#     # assuming every number is a prime number
#     isPrime = True
#     # confirm our assumption by checking if the current number in loop
#     # is divisible by any other number less than it.
#     # if it is, then our assumption is wrong
#     # otherwise we print the number
#     for n in range(2, number):
#         if number % n == 0:
#             isPrime = False
#     if isPrime:
#         print(number)


# items = "ALAMEEN"
# items = ["ALAMEEN", "ZAINAB"]
# items = ("ALAMEEN", "ZAINAB")
# items = ("JAMIL","AHMAD")
# items = {"ALAMEEN":"FAT", "ZAINAB":"THIN"}

# for item in items:
#     print(items.get(item))


# Q1 - Loop through the string zain
# ab and print all the vowels.

# create a variable to store the string zainab
# create a variable to hold all vowels
# loop through the zainab variable
# check if the current item in loop is in the vowels variable
# if it is, print it.

x = 'zainab'
z = 'aieou'
for i in x:
    if i in z:
        print(i)





# name = "ZAINAB"
# vowels = "aieou"
# for char in name:
#     if char.lower() in vowels:
#         print(char)