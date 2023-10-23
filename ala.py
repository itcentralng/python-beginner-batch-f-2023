#creat a dictionary that contain 5 or mare state 
#initialize a veriabble to keep track of users score 
#iterate through the dictionary item and present the quiz question 
#display the state to the user and prompt for their answer
#check if the user answer matches the correct capital 
#increase the user  score by 1 for each correct answer 
#check if the user answer matches the correctcapital 



# # Create a dictionary that contains 5 or more states and their capitals
# state_capitals = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     # Add more states and capitals as needed
# }

# # Initialize a variable to keep track of the user's score
# score = 0

# # Iterate through the dictionary items and present the quiz questions
# for state, capital in state_capitals.items():
#     # Display the state to the user and prompt for their answer
#     user_answer = input(f"What is the capital of {state}? ").strip()

#     # Check if the user's answer matches the correct capital
#     if user_answer.lower() == capital.lower():
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Sorry, the correct capital of {state} is {capital}.\n")

# # Display the final score
# print(f"Your final score is {score}/{len(state_capitals)}")


# # Create a dictionary that contains 5 or more states and their capitals
# state_capitals = {
#     "kano": "kano",
#     "nasarawa": "lafia",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     # Add more states and capitals as needed
# }

# # Initialize a variable to keep track of the user's score
# score = 0

# # Iterate through the dictionary items and present the quiz questions
# for state, capital in state_capitals.items():
#     # Display the state to the user and prompt for their answer
#     print(f"What is the capital of {state}?")
#     user_answer = input().strip()

#     # Check if the user's answer matches the correct capital
#     if user_answer.lower() == capital.lower():
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Sorry, the correct capital of {state} is {capital}.\n")

# # Display the final score
# print(f"Your final score is {score}/{len(state_capitals)}")



 #Write a State and Capital Game where users are presented with a state
# for which they provide the capital, if they are correct the program
# indicates that and if they are wrong the program corrects them and continues
# until all states are exhausted or the user wants to quit.
# Keep track of users score, if they get it right they get 5 points,
# if they get it wrong, 3 points are deducted.
# At the end of the game you show them how their performance and ask them
# to quit or play again.
# If they choose to play they again, you restart the game, otherwise you quit.
# Also, keep track of the user names



import random

# Create a dictionary that contains states and their capitals
state_capitals = {
    "naija": "mina",
    "nasarawa": "lafia",
    "lagos": "ikeja",
    "kaduna": "kaduna",
    "kano": "kano",
    # Add more states and capitals as needed
}

# Initialize a dictionary to keep track of user scores
user_scores = {}

while True:
    # Prompt the user for their name
    user_name = input("Enter your name: ")

    # Initialize user's score
    user_score = 0

    # Create a list of states to be asked as questions
    states_to_ask = list(state_capitals.keys())

    # Shuffle the list of states for random order
    random.shuffle(states_to_ask)

    for state in states_to_ask:
        capital = state_capitals[state]

        # Ask the user for the capital of the state
        user_answer = input(f"What is the capital of {state}? ").strip()

        # Check if the user's answer matches the correct capital
        if user_answer.lower() == capital.lower():
            print("Correct! You earn 5 points.\n")
            user_score += 5
        else:
            print(f"Sorry, the correct capital of {state} is {capital}. You lose 3 points.\n")
            user_score -= 3

    # Display the user's final score
    print(f"{user_name}, your final score is: {user_score} points")

    # Store the user's score
    user_scores[user_name] = user_score

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

# Display the user scores at the end of the game
print("\n===== Game Over =====")
print("User Scores:")
for user, score in user_scores.items():
    print(f"{user}: {score} points")
