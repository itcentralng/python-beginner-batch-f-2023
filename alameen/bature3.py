# numbers=[1,2,3,4,5,6,7,8,9,10]
# # for number in numbers:
# #   print(number*1)

numbers=[1,2,3,4,5,6,7,8,9,10]

for number in numbers:
  if number %2 ==1:
     print(number)
    
# # Define the end number
# number=[1,2,3,4,5,6,7,9,10,]

# #loop through a list of number from 1-10 and  print out only the prime numbers


# # Loop through the numbers from 1 to 10 and print prime numbers
# for number in range(1, 11):
#     if number > 1:
#         is_prime = True
#         for i in range(2, number):
#             if (number % i) == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(number)

# Q1. Loop through numbers between 1 and 15 inclusive.
# for each number, if the number is divisible by 3 print "Fizz"
# if the number is divisible by 5 print "Buzz"
# if the number is divisible by both 3 and 5 print "FizzBuzz"
# Otherwise print the number.

# for number in range(1, 16):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# name = "alamin bature"

# # Define a string containing the vowels
# vowels = "aeiou"

# # Loop through each character in the name
# for char in name:
#     # Check if the character is a vowel and convert it to uppercase if it is
#     if char.lower() in vowels:
#         print(char)

# Output: AAIUAE
