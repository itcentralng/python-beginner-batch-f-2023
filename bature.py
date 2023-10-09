# 1. Input a year from the user and store it in a variable, let's call it "year".
# 2. If (year is divisible by 4) and ((year is not divisible by 100) or (year is divisible by 400)) then
# 3.     Print "Leap year"
# 4. Else
# 5.     Print "Not a leap year"



year = int(input("Enter a year: "))


if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
