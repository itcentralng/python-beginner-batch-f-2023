# Some string methods and their examples

# replace()
# This string method is used to replace a value with another.
sent = "Shedrack Yusuf is one of the greatest Fashion Designers"
print(sent.replace('Fashion Designer',"Software Developer"))
# ==> Shedrack Yusuf is one of the greatest Software Developers

# split()
# This string method is used to remove characters in a string.
v = "Knowledge££Power££Money££Information"
print(v.split("££"))
# ==> ['Knowledge', 'Power', 'Money', 'Information']

# format()
# This string method is used to insert a specified value into a specified placeholder.
fnw = "this car is a {cname} brand. it's been in use for {age} years now"
print(fnw.format(cname='volkswagen',age= '15'))
# ==> this car is a volkswagen brand. it's been in use fo 15 years now

# join()
# This method is used to join the iterable elements to the end of a string contained.
abc = ['fendi', 'balenciaga', 'nike', 'addidas', 'versace']
xyz = "$$"
print(xyz.join(abc))
# ==> fendi$$balenciaga$$nike$$addidas$$versace

# find()
# This method is used to find the occurence of a value from a string.
dsp = "Life is like a movie. A movie about africa would be nice."
print(dsp.find('movie'))
# ==> 15

# Some list methods and their examples.
# copy()
# This method returns a new list, which does not modify the original list.
bdy = ["Head", "Shoulder", "Knees", "Toes"]
bdy2 = bdy.copy
print(bdy)
print(bdy2)
# ==> ['Head', 'Shoulder', 'Knees', 'Toes']
# ==> ['Head', 'Shoulder', 'Knees', 'Toes']

# index()
# This method returns the position of the first occurrence of a specified value.
mood = ['happy', 'sad', 'anxcious', 'rude', 'angry']
print(mood.index('anxcious'))
# ==> 2

# extend()
# This method enlarges the list by adding elements of a list, tuple and dictionary or chars of strings to another list.
noun = ['name', 'place', 'thing']
noun.extend('animal')
print(noun)
# ==>['name', 'place', 'thing', 'a','n','i','m','a','l',]
verb =("eating", "dancing", "running")
noun.extend(verb)
print(noun)
# ==> ['name', 'place', 'thing', 'a','n','i','m','a','l', 'eating', 'dancing', 'running']
part = {"noun&verb":'examples' }
noun.extend(part)
print(noun)
# ==> ['name', 'place', 'thing', 'a','n','i','m','a','l', 'eating', 'dancing', 'running', 'noun&verb']

# insert()
# This method is used to add an element to the list.
room = ["desk", "fan", 'chair']
room.insert(2,'bed')
print(room)
# ==> ['desk', 'fan', 'bed', 'chair' ]
room.insert(0,'table')
print(room)
# ==> ['table', 'desk', 'fan', 'bed', 'chair']

# reverse()
# This method returns the list from the element it endswith to the element it begins with.
car = ['tyre', 'burnet', 'boot', 'seat', 'dashboard', 'brake', 'clutch', 'engine', 'windscreen']
car.reverse()
print(car)
# ==> ['windscreen', 'engine', 'clutch', 'brake', 'dashboard', 'seat', 'boot', 'burnet', 'tyre']