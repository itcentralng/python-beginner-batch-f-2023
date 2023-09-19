people = ["Aisha", "Shedrack", "Abdul"]

items = ["Yusuf", ["Zainab", []]]

# METHODS
#append - adds objects to the end of list
people.append('zainab')
print(people)

#Clear - empties a list
people.clear()
print(people)

#copy - returns a SHALLOW copy of the list
items2 = items.copy()
items3 = items 
items.append(1)

print(items2) 
print(items3)

#count - returns number of occurence of a value
Scores = [14.5, 16.7, 20, 14.5, 2, 9, 10, 2, 9, 9]
x = Scores.count(9)
print(x)

w = len(Scores)
print(w)

#extend 
#Examples
integers = [2, -5, 12, 4]
Scores.extend(integers)
print(Scores)

things = ["cup", "table", "book"]
things.extend('table')
print(things)

#Index
#Example
y = integers.index(-5)
print(y)

#Insert
#Example
things.insert(2, "laptop")
print(things)

#Pop
#Example
integers.pop(2)
print(integers)

#Remove
#Example
Scores.remove(14.5)
print(Scores)

#Reverse
#Example
things.reverse()
print(things)

#sort
#Example
rev = [14.5, 16.7, 20, 14.5, 2, 9, 10, 2, 9, 9]

Scores.sort(reverse=True)
rev.sort(reverse=False)
print(Scores)
print(rev)

#scores=[14, 10, 12, 9]
#scores.pop(10)
#print(scores)
# OPERATIONS