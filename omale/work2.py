#3 example
texts=['A','H','M','A','D']
print(texts[0:2])

#4 examples
texts=['A','H','M','A','D']
print(texts[::-1])

#5 example
texts1=['D','A','M','H','A']
x="".join(texts1)
print(x)

#6 example
texts2=[]
texts2.extend(texts1)
print(texts2)

# example
texts3=['D','A','M','H','A']
texts3.pop()
print(texts3)

#1 example
d="apple","orange","banana"
x=texts
print(x)

# 2 example
x="".join(d)
print(x)

# 3 example
s=[]
s.extend(d)
print(s)

#4 example
s.append(x.upper())
print(s)

#5 example
e=[]
e.append(x[-1].lower())
print(e)


# exercise
# create a variable to hold "AZ"
q="A2Z"
print(q)
# create a new string to hold the middle item from the above string
w=q[1:2]
print(w)

# create a tuple of the two strings above
t=(q,w)
print(t)

# create a list to hold the item from the above tuple
r=[q,w]
print(r)

# add two boolen values to the end the new list one true and the other for false 
r.extend([True,False])
print(r)


# create an integer to store the current year
v=2023

# create a float to store your exagerated weight
h=34.90

# add the above integer and float to the previous list
r.append(v)
r.append(h)
print(r)


# create a new list to hold the last 4 items from the old list
r.clear()
r.append(v)
r.append(h)
r.extend([True,False])
print(r)

 # revsers the new list with a method and reverse it back without a method
r.reverse()
print(r)
print(r[::-1])

# # excercise
# #1 create an empty dictionary
# f={}
# print(f)
# #2 use a method to add a new value for the key "name"
# f.update({"name":"abraham joshua"})
# print(f)
# #3 create a new variable and store a tuple of the  current key value pair from our dictionary
# #   such  that the dictionary now become empty.
# l=("name","abraham joshau")
# f.clear()
# print(f)
# #4 use the appropraite method to update the dictionary back to its original form using our new variable holding 
# #   its original values.
# g=f
# f.setdefault(l[0],l[1])
# print(g)
# #5  using the right method to get and print out the "name" from the  restored dictionary
# print(g.get("name"))

# #6 using operation similar to list,add values for each of  the following keys into the dictionary
# g["age"]=100
# g["height"]=67.45
# g["weight"]=59.23
# g["hobbies"]='gaming','sleeping',"cooking"
# print(g)
# #    "age", "height" "weight" "hobbies"
# #7 create a new variable to store the values returned from removing hobbies
# d=g.popitem()
# print(d)
# #8 use the appropraite method to remove all the items from the dictionary
# g.clear()
# print(g)
# #9 repeaat Q2-Q6 HERE
# f.update({"name":"abraham joshua"})

# l=("name","abraham joshau")
# f.clear()
# print(f)

# g=f
# f.setdefault(l[0],l[1])
# print(g)

# g["age"]=100
# g["height"]=67.45
# g["weight"]=59.23
# g["hobbies"]='gaming','sleeping',"cooking"
# print(g)










