name='people'
x=name
print(x)

name='david'
x=name.capitalize()
print(x)

place='Abu'
x=place.casefold()
print(x)

peeple='duchesne'
y=peeple.count('e')
print(y)

name='hello beautiful world!'
x=name.endswith('!')
print(x)

obo='moses'
x=name.endswith('m')
print(x)

# example
names='john is tall'
x=names.replace('john', 'moses')
print(x)
# exampple
school='josh is not from '
y=school.upper()
print(y)
# example
market='ABRAHAM AND MOSES WERE FROM THE SAME SCHOOL N THE YEAR 1999'
z=market.lower()
print(z)
# example
food='carbohyrate, protein,{},{},{} are the classes of food'
x=food.format('banana','apple','orange')
print(x)

# example
text='i am {0}, from {1} state'
y=text.format('duchesne omale enemona','koge ankpa local governmet area')
print(y)

# example
texts='rice cost {0} and beans {1} but the beans has some damages inside of {word}'
f=texts.format( 30,100, word='okay')
print(f)

#examples
texts='duchesne omale enemona'
d=texts.upper()
print(d)

# examples
texts='DUCHESNE OMALE ENEMONA'
f=texts.lower()
print(f)

# examples
texts='duchesne omale enemona'
k=texts.islower()
print(k)

# example
texts='Duchesne Omale Enemona'
k=texts.islower()
print(k)

# example
texts='Duchesne Omale Enemona'
k=texts.isupper()
print(k)

# example
texts='DUCHESNE OMALE ENEMOAN'
k=texts.isupper()
print(k)

# example
text='Duchesne Omale Enemona is 110 years old'
k=texts.isalnum()
print(k)

# examples
texts='duchesne12 omale enemona'
x=texts.isalnum()
print(x)

# examples
texts='Duchesne12OmaleEnemona'
f=texts.isalnum()
print(f)

# examples
rem='duchene omale enemona'
g=rem.replace('duchesne','david')
print(g)

# example
text='duchesne omale enemona'
t=text.replace('duchesne','david')
print(t)

# example
y="Duchesne Omale Enemona duchesne"
o=texts.replace('duchesne','abraham')
print(o)

# examples
texts='duchesne omale enemona {} from the family of {number} and his brothers are 4 in numbers.'
e=texts.format('is',number=10,)
print(e)

# examples
texts= 'moses is from canada'
e=texts.replace('moses','john')
print(e)

# example
texts='camp'
f=texts.center(10,'o')
print(f)

# example
texts='duchesne omale enemona'
r=texts.center(50,'#')
print(r)

# examplenf
texts='duchesne omale omale moses, david jonathan'
d=texts.count('omale')
print(d)

# examples
text='good'
o=text.count('o')
print(o)

# examples
texts='duchesne omale enemona is from the family of mr and mrs omale'
g=texts.count('omale',8,15)
print(g)

# examples
texts=('name','surname','firstname')
x=':'.join(texts)
print(x)

# examples
texts="""hello my name is {}
you are welcome!"""
o=texts.format('duchesne omale enemona')
print(o)
# examples
texts=input('first name :'.upper().format())
zexts=input('surname :'.lower())
pexts=input('phone number :')
lexts=input('email address :'.upper())
print(('welcome to it central' ).upper())

# examples
contacts=input('state of orgine: '.join(','))
texts=input('nationality: '.upper())
texts=input('course of studies: ')
print('welcome'.upper())

# examples
def primarycolors(colors):
    primary=['red','green','blue']
    matching_colors=[]
    for colors in colors:
        if colors in primary:
            matching_colors.append(colors)
        return matching_colors
    
    print(primarycolors(['red','orange','maroon','pink', 'green']))