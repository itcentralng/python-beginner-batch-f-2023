people = [ ]
friends = ["Hanif", "Ahmed", "Alameen", "Abdulateef"]
items = [1, 1.7, "Ahmed", 1, [1, 1, 1, 2, 3, [1.5, 5.1]]]

a = "5.1"
b = "True"
c = 5.1
d = [False]
e = (False, True)
f = {"status":True}

# METHODS
friends.append('Anisa')
print(friends)

friends.clear()
print(friends)

items2 = items.copy()

print(items2)
items2.append('Anisa')
print(items2)
print(items)

print(items.count(1))

print(items[2].startswith('A'))
print(items)
print(items.pop(2).startswith('A'))
print(items)

alphas = ['B', 'C', 'D']
alphas.extend('EFGHAA')
print(alphas)

print(alphas.index('A'))

alphas.insert(0, 'A')

print(alphas)

x = alphas.pop()
y = alphas.pop()

print(x, y)
# alphas.remove('A')
# alphas.remove('A')
# alphas.remove('A')
print(alphas)

alphas.reverse()

# OPERATIONS