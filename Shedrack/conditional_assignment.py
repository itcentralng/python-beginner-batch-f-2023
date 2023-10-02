X = "STARDOM MUSIC"
print(X.center(30, '^'))
print('AFROBEAT NO.1 MUSIC STREAMING PLATFORM' )
print('afroing music!!!')
print('Sign up!')
f = input("Email:")
g = input("First name:")
h = input("Last name:")
c = input("Create Username:")
d = input("Create Password:")
e = input("Confirm Password:")
if d==e:
    print("Get Ready! Already!")
    print("Now sign in!")
    a = input("Username:")
    b = input("Password:")
    print()

else:
     print('Incorrect username or password, please retry.')

if a==c and b==d and d==e:
     print("Listen Up!")
else:
     print("Please try again later")
#      a1=input("Username")
#      b1=input("Password")
# if a1==a and b1==a:
#      print("Listen Up!")
# else:
#      print("Ooops!!! info not matched")        
