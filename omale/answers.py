# list
# 1.how do you creat a list in python.
# answers:all you need to do is to make sure the data values are having quotations,seperate by comma and enclosed in a square bracket
# examples 
names=['david','john','peter']
x=names
print(x)

countries=['togo',
           'ghana',
           'mali',]
y=countries
print(y)

# 2.how do you add an item to a list
# answer:you can add an item in a list using some list method which are append listmethod,inset listmethod, and extented listmothed
# note:the right way or the right method to add an item in a list is by using the append listmethod.
# examples for append listmethod
food=['banana','orange',]
food.append('mango')
print(food)

books=['60leaves','40leaves',]
books.append('30leaves')
print(books)

# examples for insert listmethod
computers=['hp',
           'dell',]
computers.insert(1,
                 'applemac')
print(computers)

softdrinks=['pepsi','cocacola']
softdrinks.insert(2,'fanta')
print(softdrinks)

# examples for extend listmethod
colours=['black','blue',]
x=['purple']
colours.extend(x)
print(colours)

names=['john','david',]
y=['musa']
names.extend(y)
print(names)

# how do you remove an item from a list
# answers:there are actually two ways to do that. the remove listmothed and the pop listmethod.
# examples for remove listmethod
# note:the righ way or method of doing this is by using the remove listmethod 
texts=['shoes','clothes','bags']
texts.remove('bags')
print(texts)

phones=['samsung','iphone','tecno','infinix']
phones.remove('iphone')
print(phones)

# examples of pop listmethod
# note:the pop method don't permanetly delete the item in the list and it can return back the initial item removed, you most identify the item you want to remove with an index value
# examples for pop listmethod
clothes=['jeans','t-shirt','cap']
clothes.pop(2)
print(clothes)

clothes=['jeans','t-shirt','cap']
x=clothes.pop(2)
print(x)

names=['shedrack',
       'yusuf',
       'peter']
names.pop(1)
print(names)

names=['shedrack','yusuf','peter']
y=names.pop(1)
print(y)

# tuple 
# what is the  difference between a list and a tuple
# 1.the differnce between a list and a tuple is the brackets.the tuple uses the perentheses bracket() while the list uses the square bracket[] 
# 2.tuple are immutable that's why it only has two methods the count and the index methods while list are mutable because it has some methods that allows modification
# the count method tells you the reoccurance of a particular item in a tuple it also carrys out the same function in a list too
# the index method tells you the postion of the item in a tuple it also carry out the same function to in a list too
# note:as you can see from the two methods you can't edit a tuple and a list with this methods rather it tell you the position of the item and the reoccurance of a particular item

# how do you creat a tuple in python
# answer:you can creat a tuple in python by ensuring it has the following features the quotation sing,comma and the perentheses bracket
# exampleas
tribes=('hausa','igbo','yoruba')
x=tribes
print(x)

phones=('samsung','iphone','techo',['infinix'])
y=phones
print(y)

colours=('white','brown',['green'])
x=colours
print(x)

# how do you access an item in a tuple 
# answer:you can access an item in a tuple by using the index value(positioning) of that item 
# examples
languages=('yuroba','hausa','igbo')
x=languages
print(x[1])

texts=('books','pencile','colours')
y=texts
print(y[0:2])

fruits=('banana','orange','mango')
u=fruits
print(u[0:1])

phones=('iphones','samsung','tecno')
x=phones
print(x[0:1])

# dictionaries
# how do you creat a dictionary in python
# answers:for you to be able to creat a dictionary in a python it most have a key and it value in quotation where the key and value are seperated with column enclosed in a curly bracket{} 
# examples
cars={'toyotal':'black','benz':'white','gmc':'ash'}
x=cars
print(x)

texts={'books':'40leaves',
       'pen':'hbblack',
       'bag':'size10'}
y=texts
print(y)

texts={'name':'omale',
       'surname':'duchesne',
       'middlename':'enemona'}
x=texts
print(x)

colours={'food':'rice',
         'phones':'iphones',
         'countries':['mali','togo','china']}
y=colours
print(y)

# how do you add a key-value pair to a dictionary
# the update method in dictionary add a key-value pair to the dictionary
# examples
texts={'name':'duchesne',
       'middlename':'enemona',
       'years':13}
texts.update({'firstname':'omale'})
print(texts)

texts={'colour':'black',
       'food':'idome',
       'computers':'hp'}
texts.update({'names':'shedrack'})
print(texts)

names={'country':'nigeria',
       'state':'lagos',
       'lg':'ikorodu'}
names.update({'village':'ilo'})
print(names)

#  how do you get the value for a given key in a dictionary
# answers:by using the getmethod
# examples
names={'country':'nigeria',
       'state':'lagos',
       'village':'ilo'}
x=names.get('country')
print(x)
y=names.get('state')
print(y)
z=names.get('village')
print(z)

#  what are the different ways to creat a string
# answer:you  can creat a string in python by using single quotations,double quotation and triple quotaton
# example of single quotation
names='johnson is the first son of mr presient'
x=names
print(x)

# example of double quotation
current_balance="23 30 56 78 90 87 98"
y=current_balance
print(y)

# examples of triple quotation
_50="""happy joy sorrow sadness """"""the people of nigeria are not blacks"""
u=_50
print(u)

# how do you splite a string into a list of words
# examples
_50="""happy#joy#sorrow#sadness """"""the#people#of#nigeria#are#not#blacks"""
u=_50.split('#')
print(u)

current_balance="23#30#56#78#90#87#98"
y=current_balance.split('#')
print(y)

names='johnson&is&the&first&son&of&mr&presient'
x=names.split('&')
print(x)

# how do you get the length of a string ?
# answers: you can get the lenth of a string by using the len() function
# examples
x='good by people'
print(len(x))

z="just make you eat before sunset"
print(len(z))

f="hello world"
g=f
print(len(g))

# practice questions
# Write a Python program to reverse a string.
# examples
k="people of mali are too black "[::-1]
x=k
print(x)

t="the people of ghana are fun of eating pig meat"[::-1]
names=t
print(names)

# Write a Python program to check if a string is a palindrome.
# Write a Python program to find the most frequent character in a string.
# examples
result='2 3 4 5 6 7 8 8 8 8 9 9 0 1 1 2 2'
x=result.count('8')
print(x)

countries='nigeria togo mali ghana brazile'
y=countries.count('togo')
print(y)

# Write a Python program to find the largest number in a list.
countries=max('nigeria','togo','ghana','brazile')
print(countries)

numbers=max('1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 23')
print(numbers)

# Write a Python program to find the sum of all the elements in a list.
numbers=[1,3,4,5,6,7,8,9,]
y=sum(numbers)
print(y)

texts=[3,4,5,7,6,3,5,6,6,5]
x=sum(texts)
print(x)

# Write a Python program to remove all duplicates from a list
# examples
numbers=['john','musa','david','john','yusuf']
numbers=list(dict.fromkeys(numbers))
print(numbers)

food=['orange','banana','coconut','banana','mango']
food=list(dict.fromkeys(food))
print(food)

# Write a Python program to find the length of a tuple.
# example
food=('orange','banana','coconut','banana','mango')
y=food
print(len(y))

countries=('nigeria','china','usa','canada')
z=countries
print(len(z))

# Write a Python program to find the smallest number in a tuple.
numbers=(1,3,4,5,6,2,7,2,5,7)
x=min(numbers)
print(x)

texts=(6,7,3,8,)
z=min(texts)
print(z)

# Write a Python program to sort a tuple in ascending order.
computers=('hp','dell','macbook','lenovo','zick')
x=computers
z=sorted(x)
print(z)

tribes=('igbo','hausa','nupe')
x=tribes
y=sorted(x)
print(y)

# Write a Python program to find the number of key-value pairs in a dictionary.
# examples










