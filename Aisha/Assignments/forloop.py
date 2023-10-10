# Q1. Loop through numbers between 1 and 15 inclusive.
# for each number, if the number is divisible by 3 print "Fizz"
# if the number is divisible by 5 print "Buzz"
# if the number is divisible by both 3 and 5 print "FizzBuzz"
# Otherwise print the number.

print("Question 1: ")
for number in range(1, 16):
    if number%3 ==0 and number%5 ==0:
        print("fizzbuzz")
    elif number%3 ==0:
        print("Fizz")
    elif number%5 ==0:
        print("Buzz")
    else:
        print(number)

# Q2. Loop through your name as a string and print only the vowels in uppercase.
print()
print("Question 2:")
Myname = "Aisha Aliyu"
for vowels in Myname:
    if vowels =='a' or vowels =='e' or vowels =='i' or vowels =='o' or vowels =='u' or vowels =='A':
        print(vowels.upper()) 