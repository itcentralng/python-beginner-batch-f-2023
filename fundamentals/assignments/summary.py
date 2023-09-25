"""
**Strings:**
1. What are the different ways to create a string in Python?
2. How do you get the length of a string?
3. How do you split a string into a list of words?
"""
# Write your answers here:

"""
**Lists:**
1. How do you create a list in Python?
2. How do you add an item to a list?
3. How do you remove an item from a list?
"""
# Write your answers here:

"""
**Tuples:**
1. What is the difference between a list and a tuple?
2. How do you create a tuple in Python?
3. How do you access an item in a tuple?
"""
# Write your answers here:

example_tuple = 1, 2, 3, 4
print(example_tuple[0])

"""
**Dictionaries:**
1. How do you create a dictionary in Python?
2. How do you add a key-value pair to a dictionary?
3. How do you get the value for a given key in a dictionary?
"""
# Write your answers here:
example_dict = {'name':'Aisha Shedrack'}
example_dict['age'] = 19
example_dict.setdefault('height', '1.9m')
print(example_dict)

"""
Practice questions:

**Strings:**
1. Write a Python program to reverse a string.
2. Write a Python program to check if a string is a palindrome.
3. Write a Python program to find the most frequent character in a string.
"""
# Write your answers here:
example_string = 'name'
print(example_string[::-1] == example_string)

example_string2 = 'nan'

a = example_string2[0]
b = example_string2[1]
c = example_string2[2]

print(a, example_string2.count(a))
print(b, example_string2.count(b))
print(c, example_string2.count(c))



"""
**Lists:**
1. Write a Python program to find the largest number in a list.
2. Write a Python program to find the sum of all the elements in a list.
3. Write a Python program to remove all duplicates from a list.
"""
# Write your answers here:

numbers = [1, 2, 90, 3, 0, 9, 10, 8, 7]
numbers.sort()
print(numbers[-1])
print(numbers[0])

"""
**Tuples:**
1. Write a Python program to find the length of a tuple.
2. Write a Python program to find the smallest number in a tuple.
3. Write a Python program to sort a tuple in ascending order.
"""
# Write your answers here:

example2 = "Aisha", "Omale", "Shedrack"
print(len(example2))

example3 = 2, 1, 8, 0
example3 = list(example3)
example3.sort()
example3 = tuple(example3)
print(example3[0])


"""
**Dictionaries:**
1. Write a Python program to find the number of key-value pairs in a dictionary.
2. Write a Python program to check if a key exists in a dictionary.
3. Write a Python program to print all the keys in a dictionary.
"""
# Write your answers here:

person = {'name':'Ahmad', 'age':16}
print(len(person))
print(len(person.items()))

print(person.get('age'))
print(person.get('friends'))

print(list(person.keys()))