# replace 
# replace method replaces a specified phrase with another specified phrase.
sentences1='the young man is sleeping '
y=sentences1.replace('man','boy')
print(y)

# split
# split method it splict a string into a list 
names='john is to young,  to be school'
z=names.split(',')
print(z)

curren_balance='for long now i have being,trying to be nice'
d=curren_balance.split(',')
print(d)

schools='excel academy#first royal lnternational school#univers academy'
u=schools.split('#')
print(u)

# format
# format method is a mothod that format the data values and insert the data value inside a placefolder 
# note:a placefolder is defined using a curly brackets,which can be identify using indexs
text='john is {0} old'
t=text.format(10)
print(t)


names='john bought orange for {price} dollars and other friuts too'
o=names.format(price=40)
print(o)

texts='i bought the banana for {price} dolloars and mango for {costs} dollars too'
e=texts.format(price=10,costs=30)
print(e)

texts='the boys is {weight} kg and that of the girls is {wage} kg '
g=texts.format(weight=30, wage=20)
print(g)

# join
# join method simply means it take all the data values in a tuple which is seperated with a comma and join them as a string.meaning in one sentenc
# by indicatimg it with a seperator

texts=('jo','hn','ce','na')
g='#'.join(texts)
print(g)

texts='john','david','ruth'
u='&'.join(texts)
print(u)

texts='food is', 'for my me in particular'
e='good'.join(texts)
print(e)

# find
# find method finds the first occurrence of the specified data value and also returns -1 if the value is not found.
texts='welcome to my world of peace and happiness'
b=texts.find('to')
print(b)

texts='john loves to  sleep a lot while ken likes to play football a lot'
m=texts.find('sleep')
print(m)

texts='lucy dislikes banana'
k=texts.find('lucy')
print(k)
 
# list methods 

# copy
# copy method it returns a copy of the specified list
texts=['david','jonh','peter']
texts1=texts.copy()
print(texts1)
 
texts=['orange','banana','mango']
r=texts.copy()
print(r)

# index
# index the index method tells you the position of the data value in a particular list
countries=['togo','nigeria','ghana','mali']
d=countries.index('ghana')
print(d)

phones=['samsunggalaxys 20','iphone','tecno','infinix']
x=phones.index('tecno')
print(x)

cars=['toyotal','benz','camry']
o=cars.index('benz')
print(o)

# extend
# extend method simply adds the specified data value to the end of the current list or actual list.
colours=['yello','green','blue','puple']
w=(1,2,3,4,)
colours.extend(w)
print(colours)


computers=['dell','hp','apple','lenovo']
e=('max')
computers.extend(e)
print(computers)

documents=['zaradoc','johndoc','aishadoc','mosesdoc']
c=['omaledoc']
documents.extend(c)
print(documents)

# insert
# insert method it's insert a data value by specifing the position you want the data value to be in the list
animals=['monkey','rabbit','rat'] 
animals.insert(2,'donkey')
print(animals)

names=['lucy','precious','yusuf']
names.insert(1,'ruth')
print(names)

numbers=['1','2','3','4','5']
numbers.insert(2,'7')
print(numbers)

# reverse
# reverse mothod is a type of method that reverses the data vules from behind to the front.meaning the first
# becomes the last and the last becomes the firt.

texts=['laptops','computer','phones','network']
t=texts.reverse()
print(texts)

friuts=['mango','orange','banana']
f=friuts.reverse()
print(friuts)

heights=['23.4','45.3','56.8']
l=heights.reverse()
print(heights)

