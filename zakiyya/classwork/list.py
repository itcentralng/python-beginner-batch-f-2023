#append- appends object to the end of list


#extend - it extend list by appending elements from the iterable
names = ["lawisa", "khadija", "zulaiha"]
names.extend("lawisa")
print(names)

#index - it return first index of value
fruits = ["mango", "apple", "grape"] 
fruits.index("apple")
print(fruits)

#insert- insert object before index
job = ["lecturer", "teacher", "doctor"]
job.insert(1, "pilot") 
print(job)

#remove- remove first occurrence of a value
state = ["kaduna","kano","katsina", "adamawa"]
state.remove("adamawa")
print(state)

#reverse- reverse in place
country = ["nigeria", "malaysia", "america", "sudan"]
country.reverse()
print(country)

#pop- remove and return item at index
gadget = ["iphone", "ipad", "phone"]
gadget.pop(0)
print(gadget) 

#sort -itsort the list in ascending order and return none
stationaries = ["pen", "biro", "eraser"]
stationaries.sort()
print(stationaries) 