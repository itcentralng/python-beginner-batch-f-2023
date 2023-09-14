# extend
cars= ['honda', 'toyota', 'bmw', 'lexus','volvo']
cars.extend('volkswagen')
print(cars)
cars.extend('mercedes benz')
print(cars)

# index
d= ["fendi", "gucci", "christain dior", "nike", "adiddas"]
n=d.index("nike")
print(n)
g=d.index('gucci')
print(g)
f=d.index('fendi')
print(f)

# insert
com=['monitor', 'mouse', 'keyboard',]
com.insert(1, "joystick")
print(com)
com.insert(3, 'CPU')
print(com)

# pop
climate = ['summer', 'winter', 'autumn', 'spring']
climate.pop(1)
print(climate)
climate.pop(-1)
print(climate)

#  remove
KUtensinls = ['knife', 'spoon', 'plates', 'siever']
KUtensinls.remove('siever')
print(KUtensinls)
KUtensinls.remove('spoon')
print(KUtensinls)

# reverse
Countries = ['Nigeria', 'Togo', 'Rwanda', 'Cameroon', 'Morroco,' 'South Africa']
Countries.reverse()
print(Countries)
KUtensinls.reverse()
print(KUtensinls)

# sort
food = ['rice', 'beans', 'yam', 'potatoes', 'noodles']
food.sort()
print(food)
food.sort(reverse=True)
print(food)