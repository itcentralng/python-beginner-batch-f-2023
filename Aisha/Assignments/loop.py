# Q1 - Loop through a list of numbers from 1 - 10 and
# print out all numbers by one.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)

# Q2 - Loop through a list of numbers from 1 -10 and
# print out only the odd numbers.
for oddnum in numbers:
    if oddnum%2 ==1:
       print(oddnum)

# WITH BUILTIN MODULE (range)
for number in range(1, 11):
    print(number)

# Q2 - Loop through a list of numbers from 1 -10 and
# print out only the prime numbers.
for number in range(1, 11):
    if number%2 ==1:
       print(number)


