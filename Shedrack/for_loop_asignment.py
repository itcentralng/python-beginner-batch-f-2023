for i in range(0, 16):
    
    if i %3 ==0 and i %5 ==0:
        print('Fizzbuzz')
    elif i %3 ==0:
        print('Fizz')
    elif i %5 ==0:
        print('Buzz')
    else:
        print(i)

# 2.
myname = "shedrack yusuf"
for vowels in myname:
    if vowels=="a" or vowels=="e" or vowels=="i" or vowels=="o" or vowels=="u":
     print(vowels.upper())