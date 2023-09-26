# Answer the followng using only the concepts we've treated in class:
# Q1. Write a python program that asks a user to guess a number and 
# you tell them whether they guessed it right or not

n = "3"
num_1 = input("Guess a number between 1 and 10: ")

print(n == num_1)

# Q2. Write a python program that asks a user to guess if a certain
# fruit exists in a supermarket

supermarket = ["mango", "banana", "orange", "apple"]
fruits = input("Guess a fruit found in a supermarket: ")

print(fruits in supermarket)
