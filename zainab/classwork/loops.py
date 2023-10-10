#Q1.
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

#Q2: print numbers 1 - 10 using a whle loop

number = 1

while number <= 10:
    if number % 2 == 0 or number %5 == 0:
        print(number)
    number += 1

#number = 10
while number <= 20:
    if number % 2 == 0 or number % 5 == 0:
        print(number)
    number += 1

number = 50 
while number <= 100:
    if number % 2 ==0 or number % 5 ==0:
        print(number)
    number += 1
    