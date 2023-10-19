from example import send_email

send_email("aisha@gmail.com", "Testing", "This is a test body")

# Q1. Write a function that takes name and age 
# and print "Hi my name is the-name-goes-here and I am the-age-goes-here years old"

# Q2 Write a function that takes two lists e.g. list1=["name", "age", "height"]
# list2 = ["Ahmad Sani", 15, 1.6] and 
# returns a dictionary e.g. {"name":"Ahmad Sani", "age":15, "height":1.6}

list1=["name", "age", "height"]
list2 = ["Ahmad Sani", 15, 1.6]

def dictMaker(list1, list2):
    # Create an empty dictionary
    # Identify the list that holds values from the list that holds keys
    # Do a loop with the length of any of the lists keeping track of the current index
    # add a new key value pair to our created dictionary using the indexes of the two lists

    newdict = {}
    index = 0
    while index < len(list1):
    # for index in range(len(list1)):
        newdict[list1[index]]=list2[index]
        index += 1
    return newdict

print(dictMaker(list1, list2))

["Omale", "Ahmad", "Mohd"]

[{"name":"Omale", "total":200, "subjects":[{"name":"English", "score":50}]}, {"name":"Ahmd", "total":150, "subjects":[{"name":"English", "score":10}]}, {"name":"Mohd", "total":240, "subjects":[{"name":"Mathematics", "score":100}]}]

