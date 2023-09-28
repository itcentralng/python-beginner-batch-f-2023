# Q1. Write a program that simulates the login page of a website.
# Users will be allowed to login with their email and password.
# If their credentials are correct, you welcome them by their names.
# If either of their credentials are wrong, you notify them appropraitely.
# OPTIONAL: You can ask users to register first.
# NOTE: Create a database that stores information about users
# Information about users can be name, email and password or more

print("Hello there! Welcome to Booklovers. To register, please enter your credentials in the space below:")
print()

a = input("Create username: ")
b = input("create password: ")
c = input("Confirm password: ")

if c==b:
    print("Congratulations", a, "! Your registration was successful. Please login to access our books.")
    print()
    print("Dearest booklover, enter credentials below.")
    d = input("Booklover username: ")
    e = input("Booklover password: ")

    print()

else: 
    print("Passwords do not match. Please try again.") 
    d = input("Create username: ")
    e = input("create password: ")
    c = input("Confirm password: ")
    if e==c:
        print("Congratulations", a, "! Your registration was successful. Please login to access our books.")
        print()
        print("Dearest booklover, enter credentials below.")
        d = input("Booklover username: ")
        e = input("Booklover password: ")

    else:
        print("Please try again later.")

print()
if d==a and e==b and b==c:
    print("Have fun dearest booklover! Hope you love our books.")
else:
    print("Your password or username is incorect. Please try again.")
    d = input("Booklover username: ")
    e = input("Booklover password: ")

if d==a and e==b:
    print("Have fun dearest booklover! Hope you love our books.")

else: 
    print("Dearest booklover, please try again later.")




