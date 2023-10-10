"""
**Strings:**
1. What are the different ways to create a string in Python?
2. How do you get the length of a string?
3. How do you split a string into a list of words?
"""
# Write your answers here:
# 1.
a = 'b'
a = "b"
a = """b"""
# 2. The length of a string is gotten by calling the function len(), on th variable. Eg.
Colour = "Ash, Black, Blue, Green, Maroon, Red, Pink, Yellow"
print(len(Colour))
# ==> 50

# 3. A list is splitted by a method split(). Eg.
Colour = "Ash, Black, Blue, Green, Maroon, Red, Pink, Yellow"
print(Colour.split())
# ==> ['Ash', 'Black', 'Blue', 'Green', 'Maroon', 'Red', 'Pink', 'Yellow']

"""
**Lists:**
1. How do you create a list in Python?
2. How do you add an item to a list?
3. How do you remove an item from a list?
"""
# Write your answers here:
# 1. A list in python is created when values of various data types are enclosed in a square brackets, which converts to elements. Eg.
Name = ['Shedrack Yusuf', 'Yusuf Garba', 'Garba Fadason', 'Fada Kaka']
print(Name)
# ==> ['Shedrack Yusuf', 'Yusuf Garba', 'Garba Fadason', 'Fada Kaka']

# 2. An item is added to a list by two methods, insert() and append().
# --The insert() method is used to add an element at any position of a list. Eg.
com=['monitor', 'mouse', 'keyboard',]
com.insert(1, "joystick")
print(com)
# ==> ['monitor', 'joystick', 'mouse', 'keyboard']
com.insert(3, 'CPU')
print(com)
# ==> ['monitor', 'joystick', 'mouse', 'CPU', 'keyboard'] 
# --The append() method is used to add an element to the end of a list. Eg..
cv = ["shoe, shirt, trouser, cap"]
cv.append("necklace")
print(cv)
# ==> ['shoe, shirt, trouser, cap', 'necklace']

# 3. We use two methods to remove and element from a list.
# --remove(): This method permanently deletes an element from a list. Eg.
brkfst = ['bread', 'milk', 'sugar', 'water', 'honey', 'egg']
brkfst.remove('sugar')
print(brkfst)
# ==> ['bread', 'milk', 'water', 'honey', 'egg']

# --pop(): This method is a temporary delete that can be undone. Using the index of the specific element to be deleted.
brkfst2 = ['bread', 'milk', 'sugar', 'water', 'honey', 'egg']
brkfst2.pop(2)
print(brkfst2)
print('sugar')
# ==> ['bread', 'milk', 'water', 'honey', 'egg']
# ==> sugar

"""
**Tuples:**
1. What is the difference between a list and a tuple?
2. How do you create a tuple in Python?
3. How do you access an item in a tuple?
"""
# Write your answers here:
# 1. There are two two differences between a list and a tuple(Physical and Functional).
#                      LIST                                 ||             TUPLE
# Physical diff: elements are in square brackets. *[]*      || elements are in parenthesis brackets.*()*
# Functional diff: can be modified while program is running.|| cannot be modified while program is running.
# Examples
# LIST ===> _class = ['Jss1', 'Jss2', 'Jss3']
# Tuple ==> _class = ('Jss1', 'Jss2', 'Jss3')

# 2. A tuple is created when values of various data types are enclosed in parenthesis brackets, which converts to elements. Eg.
people = ("Infants",('0-1'), 'Children',('1-13'), "Teenagers",('13-20'), 'Adults',('20-70'), 'Old',('70-demise'))
print(people)
# ==> ('Infants', '0-1', 'Children', '1-13', 'Teenagers', '13-20', 'Adults', '20-70', 'Old','70-demise')

# 3. An item in a tuple is accessed by using index() method to find its position or count() method to know the number of its occurrence in a tuple. Eg.
# index()
Countries = ('Nigeria', 'Togo', 'Rwanda', 'Cameroon', 'Morroco', 'South Africa')
b = Countries.index('Togo')
print(b)
# ==> 1
c = Countries.index('Morroco')
print(c)
# ==> 4

# count()
Countries = ('Nigeria', 'Togo', 'Rwanda', 'Cameroon', 'Morroco', 'Togo', 'South Africa')
print(Countries.count('Togo')) 
print(Countries.count('Nigeria'))
# ==> 2
# ==> 1

"""
**Dictionaries:**
1. How do you create a dictionary in Python?
2. How do you add a key-value pair to a dictionary?
3. How do you get the value for a given key in a dictionary?
"""
# Write your answers here:
# 1. Dictionary in python is created by adding items in a curly bracket in Key and Pair values. Eg.
Dash = {'School' : 'Nigerian Army University Biu'}
print(Dash)
# ==> {'School : Nigerian Army University Biu'}

# 2. A Key-Value pair can be added to a dictionary by using a column.
# Eg. Variable = {Key : Value}

# 3. The value of a given key in a dictionary can be gotten, by using the get() method. this will return its value. Eg.
Dash = {'School' : 'Nigerian Army University Biu'}
print(Dash.get('School'))
# ==> Nigerian Army University Biu

"""
Practice questions:

**Strings:**
1. Write a Python program to reverse a string.
 2. Write a Python program to check if a string is a palindrome.
3. Write a Python program to find the most frequent character in a string.
"""
# Write your answers here:
# 1. 
stm = "Everyday is Holiday"
print(stm[::-1])
# ==> yadiloH si yadyrevE

# 2. 
a = '121121'
reverse =  a[::-1]
if(a == reverse):
    print('this is a palindrome')
else:
  print('this is not a palindrome')
# ==> this is a palindrome

b = input("enter value here:")
if b == b[::-1]:
   print('String is palindrome')
else:
   print('String is not palindrome')

# 3.
sy = """Artificial Intelligence"""
print(max(sy, key=sy.count))
# ==> i
sy = """Fatigue """
print(max(sy, key=sy.count))
# ==> F
"""
**Lists:**
1. Write a Python program to find the largest number in a list.
2. Write a Python program to find the sum of all the elements in a list.
3. Write a Python program to remove all duplicates from a list.
"""
# Write your answers here:
# 1. There are two methods of finding the largest number in a list; *by sorting list in ascending order or using max() method to find the largest number.
mylist = [50, 70, 30, 90, 42, 55]
mylist.sort()
print(mylist)
# ==> [30, 42, 50, 55, 70, 90]
print('smallest number is:', mylist[0])
print("largest number is:", mylist[-1])
# ==> smallest number is: 30
# ==> largest number is: 90

mylist = [50, 70, 30, 90, 42, 55]
print('smallest number is:', min(mylist))
print('largest number is:', max(mylist))
# ==> smallest number is: 30
# ==> largest number is: 90
# 2.
mylist2 = [50, 70, 30, 90, 42, 55]
total = 0
for i in range(0,len(mylist)):
   total=total+mylist2[i]
   print("Sum of all numbers is:", total)
   # ==> Sum of all nummbers is: 120
   # ==> Sum of all nummbers is: 150
   # ==> Sum of all nummbers is: 240
   # ==> Sum of all nummbers is: 282
   # ==> Sum of all nummbers is: 337

total=sum(mylist2)
print('Sum of all numbers in given list:', total)
# ==> Sum of all numbers in given list: 337

# 3.
Num = [7,9,2,5,7,2,5,3,4,1,8]
Num = set(Num)
print(list(Num))
# ==> [1, 2, 3, 4, 5, 7, 8, 9]

"""
**Tuples:**
1. Write a Python program to find the length of a tuple.
2. Write a Python program to find the smallest number in a tuple.
3. Write a Python program to sort a tuple in ascending order.
"""
# Write your answers here:
# 1.
mytup = ('head', 'ear', 'eye', 'nose', 'mouth', 'hair')
print(len(mytup))
# ==> 6

# 2.
mytup2 = (58, 40,14,27,78,32,66,12,17)
print(min(mytup2))
# ==> 12

# 3. I thinnk it's impossible to sort a tuple.
mytup3 = (58,40,14,27,78,32,66,12,17)
tup = list(mytup3)
tup.sort(reverse=False)
print(tup)


"""
**Dictionaries:**
1. Write a Python program to find the number of key-value pairs in a dictionary.
2. Write a Python program to check if a key exists in a dictionary.
3. Write a Python program to print all the keys in a dictionary.
"""
# Write your answers here:
# 1.
student = {'name':'Zayyad Umar', 'age': 27, 'courses': ['math', 'computer science', 'physics']}
print(len(student))
# ==> 3

# 2.
student = {'name':'Zayyad Umar', 'age': 27, 'courses': ['math', 'computer science', 'physics']}
print(student['courses'])
# ==> ['math', 'computer science', 'physics']
print(student.get('grades', 'Not found'))
# ==> Not found

# 3.
student = {'name':'Zayyad Umar', 'age': 27, 'courses': ['math', 'computer science', 'physics']}
print(student.keys())
# ==> dict_keys(['name', 'age', 'courses'])