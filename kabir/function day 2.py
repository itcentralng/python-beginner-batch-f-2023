from example import send_email



send_email("aisha@gmail.com", "Testing", "This is a test body")

# Q1. Write a function that takes name and age 
# and print "Hi my name is the-name-goes-here and I am the-age-goes-here years old"


print("kabir")
def details1(name , age):
    print("hi my name is {} and im  {} years old".format(name,age))
details1('kabir', 20)




# Q2 Write a function that takes two lists e.g. list1=["name", "age", "height"]
# list2 = ["Ahmad Sani", 15, 1.6] and 
# returns a dictionary e.g. {"name":"Ahmad Sani", "age":15, "height":1.6}

print('kb')
list1=["name",'age',"height"]
list2=["ahmad sani",15,1.6]
def dictmaker(list1,list2):
    newdict={}
    index= 0
    while index < len(list1):
        newdict[list1[index]]=list2[index]
        index +=1
    return newdict
print(dictmaker(list1,list2))    



# write a function that takes a string and return a dictionary, the dic have three key:
# {"word":"Ahmad sani", "characters":15, "combination":["combination1","combination2","combination3"]}

print("\n")
print("kb")

icon1=["name",'age','hobbies']
icon2=['Ahmad sani',15,['chess',"snoker","football"]]
def schoolar(icon1,icon2,):
    empty={}
    counter=0
    while counter<len(icon1):
        empty[icon1[counter]]=icon2[counter]
        counter+=1
        
    return empty
print(schoolar(icon1,icon2))

print("\n")

