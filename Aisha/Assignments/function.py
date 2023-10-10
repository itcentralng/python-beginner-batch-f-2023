# Write a function that takes the name and age and print 
# "Hi my name is the-name-goes-here and i am the-age-goes-here years old" 

def name_age(name, age):
    print("Hi, my name is {}, and I am {} years old.".format(name, age))

name_age("Faiza", 19)
name_age("Halima", 22)

# Write a function that takes two lists e.g. list1 = ["name", "age", "height"]
# list2 = ["Ahmad Sani", 15, 1.6] and 
# returns a dictionary e.g. {"name": "Ahmad sani", "Age":15, "height":1.6}




def mydict(list1, list2):
    main_dict = {}
    for lists in list1:
        listdict = {list1.pop(0):list2.pop(0), list1.pop(1):list2.pop(1), list1.pop():list2.pop()}
        main_dict.update(listdict)
        print(main_dict)

list1 = ["name", "age", "height"]
list2 = ["Ahmad Sani", 15, 1.6]

mydict(list1, list2)

    

