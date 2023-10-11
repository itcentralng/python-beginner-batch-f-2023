from random import choice
import random
import json
json.loads

# Q2. Write a State and Capital Game where users are presented with a state
# for which they provide the capital, if they are correct the program
# indicates that and if they are wrong the program corrects them and continues
# until all states are exhausted or the user wants to quit.
# Keep track of users score, if they get it right they get 5 points,
# if they get it wrong, 3 points are deducted.
# At the end of the game you show them how their performance and ask them
# to quit or play again.
# If they choose to play they again, you restart the game, otherwise you quit.
# Also, keep track of the user names

states = [
    {"name":"Kaduna", "capital":"Kaduna"},
    {"name":"Kano", "capital":"Kano"},
    {"name":"Oyo", "capital":"Ibadan"},
    {"name":"zamfara","capital":"gusau"},
    {"name":"Abia","capital":"Umuahia"},
    {"name":"Bauchi","capital":"Bauchi"},
    {"name":"Borno","capital":"Maiduguri"},
    {"name":"Edo","capital":"Benin City"},
    {"name":"Jigawa","capital":"Dutse"},
    {"name":"Kogi","capital":"Lokoja"},

    ]
user = input("|Welcome| Enter your name: ")
user = user.strip()
print(' ')
print(f'Hello!! {user} Would you like to play a game?')
print("\n")    
print("options")
print('If Yes press 1) ')
print('If No press  2) ')
print("\n")
option = input('Select your Option: ')
option=int(option)
if option == 1:
    print("Welcome to the State and Capital Game")
    print('\n')
    print('\n')
if option == 2:
    print("Thank you!....")

score = 0
play = True
correct = []

while play:
    state = random.choice(states)
    if (state.get('name') in correct) == False:
        capital = input(f"{user} Guess the capital of {state.get('name')}: ")
        if capital.lower().strip() == 'q':
            play= False
            break
        elif capital.lower().strip() == state.get('capital').lower().strip():
            print(f"will don!!! {user} you get the currect Answser \n")
            print(f"you are correct! you get 5 points \n")
            score=score+5
            print(f'{user}|{+score} points\n')
            correct.append(state.get('name'))
            
           
        else:
            print("Thats wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))
            print("\n")
            score=score-3
            print(f"Oops! sorry you lost 3 points")
            print(f'{user}|{score} points\n')
            
    else:
        if len(states) == len(correct):




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

print("\n")
print("\n")

# write a function that takes a string and return a dictionary, the dic have three key:
# {"word":"Ahmad sani", "characters":15, "combination":["combination1","combination2","combination3"]}

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



            play = False
            print("Goodbye, you've exhausted our levels")
