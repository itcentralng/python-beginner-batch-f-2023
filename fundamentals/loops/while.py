# num = 0
# while num <= 10:
#     print(num)
#     num += 1

#Q1 Use a while loop to print all the odd numbers between 1 and 10 inclusive

# Pseudocode:
# 1 - Kabir - Create a list holding values 1-10
# 2 - Create a while statement that finds odd numbers
# 3 - Create the number that assigns the odd number
# 4 - Print the result

# mylist = [1, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
# while x:
#     print(number )

# 1 - Alameen - Create a variable to hold value 1
# 2 - Create a while and check if the number is less than or equals 10
# 3 - print the variable += 2

# myvariable = 1
# while myvariable <= 10:
#     print(myvariable+=2)


# 1 - Shedrack - Create a variable the value 1
# 2 - Create a while loop and check if the variable is less or equals 10
# 3 - Print the variable 
# 4 - Increase the value of the variable by 2

# myvariable = 1
# while myvariable <= 10:
#     print(myvariable)
#     myvariable+=2

# 1 - Ahmad - Create a variable holding the value 0
# 2 - Create a whileloop that checks if the first variable is less or equals 10
# 3 - print the result of the check
# 4 - if statement to check if the number is divisible by 2

# myvariable = 0
# while myvariable <= 10:
#     print(myvariable)


# 1 - Zainab - Create a variable holding the value 1
# 2 - I really dont know
# 3 - Create a variable
# 4 -

# myvariable = 1
# anothervaribale =

# 1 - Aisha - Create a variable holding 1
# 2 - Create a while loop to check if the value is less or equals 10
# 3 - Create an if statement to check if value is divisble by 2
# 4 - Print the value
# 5 - Increase the value of the variable by 1

# myvariable = 1
# while myvariable <= 10:
#     if myvariable % 2:
#         print(myvariable)
#     myvariable += 1



# Q2 Print all items from a list of 5 integers using while loop
# 1 - Create a list of integers
# mylist = [2, 4, 7, 8, 10]
# index = 0
# while index < len(mylist):
#     print(mylist[index])
#     index += 1
# mylist.reverse()
# while len(mylist) > 0:
#     print(mylist.pop())

firstName = "Ahmad"
lastName = "Usman"

usernames = ["ahus1", "ahus2", "ahus3", "ahus5", "ahus4", "usah1"]

isUnique = False
counter = 1
while not isUnique and counter < 10:
    username = "{}{}{}".format(firstName[:2], lastName[:2], counter)
    username = username.lower()
    if username not in usernames:
        isUnique = True
        usernames.append(username)
    counter += 1

if counter > 10:
    print("Oops!!! user taken")

print(usernames)

firstName = "Ahmad"
lastName = "Usaman"

isUnique = False
counter = 1
while not isUnique and counter < 10:
    username = "{}{}{}".format(firstName[:2], lastName[:2], counter)
    username = username.lower()
    if username not in usernames:
        isUnique = True
        usernames.append(username)
    counter += 1

if counter > 10:
    print("Oops!!! user taken")

print(usernames)

# t = 0
# numbers = []
# while t < 20:
#     if t > 0 and t % 2 == 0:
#         numbers.append(t)
#     t += 1

# print(numbers)