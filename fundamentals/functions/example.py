def greet():
    print("Hello guys this is a greeting")

greet()

def greet2(name):
    print("Hello {}, how are you doing?".format(name))

greet2("Zainab")
greet2("Aisha")
greet2("Ahmad")

def getTotal(num1, num2):
    print(num1+num2)

getTotal(2, 3)
getTotal(21, 13)

def getOddNumbers(numbers):
    oddnumbers = []
    for number in numbers:
        if number % 2:
            oddnumbers.append(number)
    print(oddnumbers)

getOddNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
getOddNumbers([100, 200, 349, 4900, 5323, 611, 7, 8, 9, 10, 11, 12, 13])
print(getOddNumbers([100, 200, 349, 4900, 5323, 611, 7, 8, 9, 10, 11, 12, 13]))

def customLength(iterable):
    counter = 0
    for _ in iterable:
        counter+=1
    return counter

print("Result from custom len", customLength([11, 12, 13]))
print("Result from len", len([11, 12, 13]))

def doSum(num1=0, num2=0):
    return num1+num2

print(doSum(1, 2))
print(doSum())
# print(customLength())

def send_email(recipient, subject, body):
    mail = f"""
Subject: {subject}
From: noreplay@python.com
To: {recipient}
____________________________
{body}
"""
    print(mail)
    print("Email sent successfully to ", recipient)

recipients = [
    "ibrahim@gmail.com",
    "alameen@gmail.com",
    "qaseem@gmail.com",
    "bilkis@gmail.com",
]

send_email("ibrahim@gmail.com", "Welcome to Python", """Sample body""")