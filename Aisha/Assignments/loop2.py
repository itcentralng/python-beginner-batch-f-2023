# Write a state and capital game where users are presented with a state for which they provide the capital,
# if correct the program indicates that and if they are wrong the program corrects them and continues until
# all states are exhausted or user want to quit.

# Q1. Write a State and Capital Game where users are presented with a state
# for which they provide the capital, if they are correct the program
# indicates that and if they are wrong the program corrects them and continues
# until all states are exhausted or the user wants to quit.


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
#     elif capital.lower().strip() == state.get('capital').lower().strip():
#         # 4
#         print("Correct")
#     else:
#         print("Thats wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))

# WHILE IMPLEMENTATION
# 1

states = [
    {"name":"Kaduna", "capital":"Kaduna"},
    {"name":"Kano", "capital":"Kano"},
    {"name":"Oyo", "capital":"Ibadan"},
]
import random
score = 0

# 1.2
print("\n\nWelcome to the state and capital game")
print("To quit, enter 'Q' or 'q' at anytime.")
print("For every correct answer given, five points are added to your score. \nThree points are removed for every wrong answer given.\n\n")
#  

playing = True
usedStates = []
username = input("Enter username: ")
while playing:
    state = random.choice(states)
    if (state.get('name') in usedStates) == False:
        capital = input("What is the capital of {}: ".format(state.get('name')))
        # 3
        if capital.lower().strip() == 'q':
            playing = False
            
        elif capital.lower().strip() == state.get('capital').lower().strip():
            # 4
            print("Correct")
            usedStates.append(state.get('name'))
            score += 5
            print("Your new score is: ", score)
        else:
            print("Thats wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))
            score -= 3
            print("Your new score is: ", score)
    elif len(states) == len(usedStates):
            playing = False
            print()
            print(username, "Your overall score is: ", score)
            print("Goodbye, you've exhausted our levels")
            restart = input("Would you like to play again? If yes, Enter 'Yes'. If no, Enter 'Q' or 'q': ").strip().lower()
            if restart == "yes":
                playing = True
                usedStates.clear()
                score = 0
            else:
                print(username,",", "Your final score: ", score)
                print("Goodbye")
                break
           

               
            
            

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