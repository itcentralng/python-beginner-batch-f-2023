person = {"name":"Ahmad", "age":15, "address":"38 Kinkino Road, Kawo Kaduna", "landmark":"DNA Labs", 'hobbies':['Swimming', 'Gyming'], 'category':'Fiction'}

informaiton = {"address":"Malali"}

# METHODS
x = informaiton.copy()
informaiton.clear()
print(informaiton)
print(x)

print(person.get('category', 'all'))

print(person["category"])
print(person.items())
print(person.keys())

x = person.pop("landmark")
print(x)

y = person.popitem()
print(y)
y = person.popitem()
print(y)

person.setdefault('friend', 'Bello')

person['address'] = "13 Ribado Crecent"
person['x'] = "Test"

print(person)

print(person)

person.update({'school':'Capital School', 'class':'JSS1'})
person.update([['school','Capital School'], ['class','JSS1']])

print(person.values())

# OPERATIONS

person2 = {'name':'Hanif school', 'age':10}
print(person2.get('Hanif', 'Amina'))
print(person2['name'])