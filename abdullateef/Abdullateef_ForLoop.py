
#Q1.
for number in range(2,16):
 if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
 elif number % 3 == 0:
    print('Fizz')
 elif number % 5 == 0:
    print('Buzz')




#Q2.

my_name = 'Abdullateef'
Vowels = ['a', 'e', 'o', 'i', 'u']
for  character in my_name:
    if character in Vowels:
        print(character.upper())
