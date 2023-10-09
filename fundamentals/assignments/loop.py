# Q1. Write a State and Capital Game where users are presented with a state
# for which they provide the capital, if they are correct the program
# indicates that and if they are wrong the program corrects them and continues
# until all states are exhausted or the user wants to quit.

import random
# people = ["Abdul", "Alameen", "Shedrack"]
# print(random.choice(people))


# PSUEDOCODE:

# 1 - Create a list of dictionaries that contains states and capitals
# 1.2 Welcome the user to the game and show them the rules.
# 1.3 Using a for Loop, loop through the list of dictionaries
# 2 - Display a the state from the current dict in the loop to the user
#  and request for the capital
# 3 - Check if the capital entered by the user is same as the capital in 
# the dictionary
# 4 - if the input indicates that the user wants to quit we end the game
#  else If correct, print "Corret" otherwise we print 
# "Thats wrong, the capital of x is y"

# # FOR IMPLEMTATION
# # 1
# states = [
#     {"name":"Kaduna", "capital":"Kaduna"},
#     {"name":"Kano", "capital":"Kano"},
#     {"name":"Oyo", "capital":"Ibadan"},
# ]
# # 1.2
# print("\n\nWelcome to the state and capital game")
# print("To quit, enter 'Q' or 'q' at anytime\n\n")
# #  

# for state in states:
#     # 2
#     capital = input("What is the capital of {}: ".format(state.get('name')))
#     # 3
#     if capital.lower().strip() == 'q':
#         break
#    elif capital.lower().strip() == state.get('capital').lower().strip():
#         # 4
#         print("Correct")
#     else:
#         print("Thats wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))

# WHILE IMPLEMENTATION
# 1
states = [
    {"name":"Jigawa", "capital":"Dutse"},
    {"name":"Kebbi", "capital":"Birnin kebbi"},
    {"name":"Oyo", "capital":"Ibadan"},
]

print("\n\nWelcome to the state and capital game")
print("To quit, enter 'Q' or 'q' at anytime\n\n")
print()
  
scores=0
playing = True
usedStates = []
while playing:
    state = random.choice(states)

    if (state.get('name') in usedStates) == False:
        capital = input("What is the capital of {}: ".format(state.get('name')))
        
        if capital.lower().strip() == 'q':
            playing = False
        elif capital.lower().strip() == state.get('capital').lower().strip():
            
            print("Correct you earned 5 points" )
            scores += 5
    
            usedStates.append(state.get('name'))
        else:
            print("Thats wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))
            scores= -3   
    else:
        if len(states) == len(usedStates):
            playing = False
            print("Goodbye, you've exhausted our levels")
        else:
            

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