person = {'name':'Aisha Aliyu', 'age':10, 'friends':['Zainab', 'Zakiya'], 'hobbies':('swimming', 'reading')}
print(person.get('name'))
# METHODS
person2 = person.copy()
person.clear()
print(person)
print(person2)

print(person2.items())
print(person2.keys())

x = person2.pop('name')
print(person2)
print(x)

y = person2.popitem()
z = person2.popitem()
print(person2)
print(y)
print(z)

person2.setdefault('name', 'Omale')
print(person2)

# person2.update([("friends", ["Halima", "Shedrack"]), ('class', 'Primary 6')])
# person2.update({'friends':["Halima", "Shedrack"], 'class':'Primary 6'})
# print(person2)

print(person2.values())
# OPERATIONS

person2['name'] = 'Fred'
person2['friend'] = 'Samuel'

print(person2)
person2['friend'] = 'Ibrahim'
print(person2)
