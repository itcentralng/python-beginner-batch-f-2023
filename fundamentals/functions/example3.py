def total(num1, num2):
    result = num1 + num2
    return result

print(total(5, 2))
print(total(15, 12))

def multiply(num1, num2):
    result=num1*num2
    return result

print(multiply(5, 2))
print(multiply(5000, 12))

def middleName(fullname):
    result = fullname.split()
    return result[1]

print(middleName("Zainab Sani Mohd"))
print(middleName("Omale David"))
print(middleName("Alamin Bature Muhammad"))


def firstName(fullname):
    result = fullname.split()
    return result[0]

print(firstName("Zainab Sani Muhammad"))
print(firstName("Omale David"))

# Write a function that takes a list of colors
# and returns a list of primary colors within
# the list.

# Pseudocode:
# - define the function with a proper name
# - give it a parameter to store list of colors
# - create a list that stores all primary colors
# - create an empty list to store matching colors
# - loop through our colors list:
# - if the current color in loop is found in our
#   primary color list, we add it to our match list
# - we return the match list at the end
# - then we test

def primaryColors(colors):
    primary = ["Red", "Green", "Blue"]
    matching_colors = []
    for color in colors:
        if color in primary:
            matching_colors.append(color)
    return matching_colors

print(primaryColors(["Red", "Orange", "Maroon", "Pink", "Green"]))