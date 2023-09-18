people = ["Aisha", "Shedrack", "Abdul"]

items = ["Yusuf", ["Zainab", []]]

# METHODS

# append - appends objects to end of list
people.append('Zainab')
print(people)

people.clear()
print(people)

items2 = items.copy()

items3 = items

items.append(1)

print(items2)
print(items3)

scores = [14.5, 16.7, 20, 14.5, 2, 9, 10, 2, 9, 9]
x = scores.count(16.7)
print(x)

print(len(scores))


# OPERATIONS

# name = "Alameen"

# print(people[0])

# print(name[0])

print(scores[:3])
print(scores[3:7])
print(scores[7:])
print(scores)
print(scores.count(16.7))
print(scores.index(16.7))

cars = ["Honda", "Toyota"]
cars2 = ("Volvo", "Benz", "BMW", )

car = "Volvo"

cars.extend(cars2)
print(cars)