"""
**Strings:**
1. What are the different ways to create a string in Python?
2. How do you get the length of a string?
3. How do you split a string into a list of words?
"""
# Write your answers here:
# 1. To create string in python, put the characters inside a single or double quotation and assign it a
# variable.
 
# 2. To get the length of a string, the 'len' method is used.
#  Example:
example = "There are 26 letters, in the English alphabet."
print(len(example))

# 3.To split a string into a list, the 'split' method is used.
#  Example:
print(example.split(',', 2))

 

"""
**Lists:**
1. How do you create a list in Python?
2. How do you add an item to a list?
3. How do you remove an item from a list?
"""
# Write your answers here:
# 1.The square brackets[] are used to define a list in python which are assigned a variable.

# 2. To add an item to a list, the 'append' method, which adds an item to the end of the list, can be used or
# the 'insert' method, which adds an item to whatever position specified.
# Examples:
#Using the 'append' method;
Mylist = ["fantasy", "thriller", "crime", "historical fiction"]
Mylist.append("paranormal")
print(Mylist)

#Using the 'insert' method;
Mylist.insert(2, 'sci-fi')
print(Mylist)

# 3.The 'remove' method is used to remove an item from a list.
# Example:
Mylist.remove('sci-fi')
print(Mylist)


"""
**Tuples:**
1. What is the difference between a list and a tuple?
2. How do you create a tuple in Python?
3. How do you access an item in a tuple?
"""
# Write your answers here:
# 1. The difference between a list and a tuple is that a tuple is defined using parenthesis while 
# a list is defined using square brackets.

# 2. A tuple is created using parenthesis().

# 3. 

"""
**Dictionaries:**
1. How do you create a dictionary in Python?
2. How do you add a key-value pair to a dictionary?
3. How do you get the value for a given key in a dictionary?
"""
# Write your answers here:
# 1. The curly brackets{} are used to create a dictionary in python which is then assigned a variable.

# 2. To add a key-value pair to a dictionary, the dictionary is first created using the curly brackets.
# The key-value pair is then inputed, each as a string on its own seperated by a colon':'. If there are multiple key-value pairs, 
# a comma is used to seperate them.  
# Example: 
Mydict = {'language':'Hausa', 'food':'Tuwo'}

# 3. To get the value for a given key in a dictionary, you use the 'get' method.
# Example:
print(Mydict.get('food'))

"""
Practice questions:

**Strings:**
1. Write a Python program to reverse a string.
2. Write a Python program to check if a string is a palindrome.
3. Write a Python program to find the most frequent character in a string.
"""
# Write your answers here:

# 1. A python program to reverse a string.
Mystring = "desserts"[8::-1]
print(Mystring)

# 2. A python program to check if a string is a palindrome
pal = "civic"
pal2 = "civic"[5::-1]

if pal==pal2:
    print('True')
else :
    print('False')

ex1="Racecar"
ex2=ex1[::-1]

if ex1==ex2:
    print('True')
else :
    print('False')

x = input("Input word to check if palindrome: ")
print(x) 
x2 = x[::-1]
if x==x2:
    print('True')
else :
    print('False. Not a Palindrome')

# 3. Write a Python program to find the most frequent character in a string.
#Mystring1 = "She sells seashells by the sea shore."
#print(Mystring1)


#print("The most frequent character in this string is" )


"""
**Lists:**
1. Write a Python program to find the largest number in a list.
2. Write a Python program to find the sum of all the elements in a list.
3. Write a Python program to remove all duplicates from a list.
"""
# Write your answers here:
# 1. A Python program to find the largest number in a list.
#Example1
Mylist1 = [12, 13, 40, 4, 30, 2, 36]
print("The largest number in my list is:", max(Mylist1))

# 2. Write a Python program to find the sum of all the elements in a list.
#Example1
print("The sum of the numbers in Mylist1 is:", sum(Mylist1))

# 3. A Python program to remove all duplicates from a list.
Mylist2 = [12, 9, 12, 13, 40, 9, 4, 30, 2, 4, 36, 2]
print("This is Mylist with the duplicates:", Mylist2)
Mylist2 = list(dict.fromkeys(Mylist2))
print("This is Mylist without the duplicates:", Mylist2)

print(set(Mylist2))


"""
**Tuples:**
1. Write a Python program to find the length of a tuple.
2. Write a Python program to find the smallest number in a tuple.
3. Write a Python program to sort a tuple in ascending order.
"""
# Write your answers here:

# 1. A Python program to find the length of a tuple.

words = ("chocolate", "biscuits", "lacasera", "water")
w = str(words)
print(w)
c = len(w)
print(c)

# 2. A Python program to find the smallest number in a tuple.
Mytuple = (11, 4, 5, 3, 6, 20)
print("The smallest number in the above tuple is:", min(Mytuple))

# 3. A Python program to sort a tuple in ascending order.
tup = list(Mytuple)
tup.sort(reverse=False)
print(tup)

"""
**Dictionaries:**
1. Write a Python program to find the number of key-value pairs in a dictionary.
2. Write a Python program to check if a key exists in a dictionary.
3. Write a Python program to print all the keys in a dictionary.
"""
# Write your answers here:

# 1. A Python program to find the number of key-value pairs in a dictionary.

Mydict2 = {"Integer": 3, "factors": [1, 3], "spelling": "three"}
dict1 = str(Mydict2)
print(dict1)
d = dict1.count(':')
print("There are ", d, " key-value pairs in the above dictionary.")

# 2. A Python program to check if a key exists in a dictionary.

print(Mydict2)
exe = input("Input key to be found:")
print(exe)

if Mydict2.get(exe) == None:
    print("Key not found")
else: 
    print("key found")

# 3. A Python program to print all the keys in a dictionary. 
print(Mydict2.keys())
