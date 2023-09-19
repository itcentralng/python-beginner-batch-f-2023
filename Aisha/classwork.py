# 1. For each of the following string methods:
#   (a)replace - this string method replaces a specified value with another specified value.
# - Example

Saying = "Knowledge is power"
a = Saying.replace("Knowledge", "Power")

print(a)

#   (b)split - this string method splits a string using a specified seperator and returns the string as a list.
# - Example 
vegetables = "Tomatoes, pepper. Cabbages, lettuce. Carrots, peas"

print(vegetables.split('.'))

#   (c)format - This string method formats specified value(s) and inserts them inside a placeholder,
# which is defined using curly brackets{}.
# - Example
Address = "{name} works at {place}, {state}."
print(Address.format(name = "Salima", place = "Kasu", state = "Kaduna"))

#   (d)join - this string method takes all items in an iterable and joins them into one string.
# - Example
vegetables2 = "Tomatoes, pepper.", "Cabbages, lettuce.", "Carrots, peas"
num = "2"
b = num.join(vegetables2)
print(b)
#   (e)find - this string method finds the first occurence of the specified value. It returns -1 if value is not found.
# - Example
print(vegetables.find("cabbages"))
print(vegetables.find("Cabbages"))

#    - Explain in your own words what the method does and give an example
# 
# 2. For each of the following list methods:
#   (a)copy - this list method returns a copy of the list.
# - Example
course = ["Medicine", "Pharmacy", "Pharmacology"]
course2 = course
course3 = course.copy()

print(course)
print(course2)
print(course3)
course.append("Biochemistry")
print(course2)
print(course)

#   (b)index - this list method returns the position of a specified value at the first occurence.
# - Example
Age = [17, 15, 16, 15, 17, 19, 18, 12]
print(Age.index(15))

#   (c)extend - this list method extends a list by appending elements from the iterable
# - Example
rnumbers = [12, 20, 5.6, 12]
Age.extend(rnumbers)
print(Age)
course.extend('Biochemistry')
print(course)

#   (d)insert - this list method inserts a specified value at a specified index.
# - Example
course3.insert(1, "Anatomy")
print(course3)

#   (e)reverse - this list method reverses the items in a string.
# - Example
Age.reverse()
print(Age)
#    - Explain in your own words what the method foes and give an example
