# For each of the following methods, explain what they do with 2 examples:

# - startswith; this is a function that returns true if the string starts with a specified value, otherwise false.
# Examples;

text1= "I love badminton."
text2= "The number one is not an integer"

print(text1.startswith('I'))
print(text2.startswith('M'))

# - format; This string method formats specified value(s) and inserts them inside a placeholder,
# which is defined using curly brackets{}.

text3= "I live in {state}, in {place}."
text4= "My name is {name}, I am a {job}."

print(text3.format(state= "Kaduna", place= "malali"))
print(text4.format(name= "Shedrack", job= "teacher"))

# - index; this string method returns the position of the value specified at the first occurence in a list. 
# Examples;

text5= [9, 13, 17, 18, 19, 25]
text6= ["jug", "spoons", "cups", "plates"]
texte= [10, 19, "apple", 4.75, "banana"]
x= texte.index(4.75)
name = "Ibrahim"


a = "Shedrack"
print(a.index("d"))


print(text5.index(17))
print(text6.index('jug'))
print(x)
print(f"My name is {name}")

# - lower; This is a string method that converts each uppercase character in a string to lowercase.
#Examples; 
text7= "HELlo EVeryOnE!"
text8= "LeBrON IS a BAskeTBAllEr."

w=text7.lower()
y=text8.lower()

print(w)
print(y)

# - upper; this is a string method that converts each lowercase character in a character to uppercase.
#Examples;
a=text7.upper()
b=text8.upper()


print(a)
print(b)

# - isalpha; this string method returns true if all characters in a string are alphabets, otherwise false.
#Examples;
text9= "Is Daniel 47 years old?"
text10="The number one is not a prime number."
text11= "thenumberoneisnotaprimenumber"

print(text9.isalpha())
print(text10.isalpha())
print(text11.isalpha())

# - isalnum; this string method returns true if all characters in a string are alphanumeric.
#Examples;
text12= "Danielis47yearsold"
text13= "33 multiplied by 2 is 66"
text14= "33multipliedby2is66"
alnum= "Danielisyearsold"

print(text12.isalnum())
print(text13.isalnum())
print(text14.isalnum())

# - islower; This string method returns true if all characters in the string are lowercase, otherwise false.
#Examples;

print(text11.islower())
print(text8.islower())

# - isupper; This string method returns true if all characters in the string are uppercase, otherwise false.
#Examples;

text15= "ILOVESPAGHETTI"
text16= "SwEEt SixTEEn."

print(text15.isupper())
print(text16.isupper())

# - replace; This string method replaces a specified value with another specified value in a string.
#Examples;

print(text12.replace('Daniel', 'Michael'))
q= text1.replace('badminton', 'Basketball')
print(q)

# - split; This string method splits a string into list.
#Examples;

text17= "I want to eat a Mango, an apple, a biscuit, and an orange."

print(text10.split())
print(text17.split(','))
print(text17.split(',', 2))

# - strip; This string method removes all whitespace or specified characters, at the beginning and end of the string.
#Examples;

text18="    banana is his favorite fruit      "
text19= "..... he was waiting for her at...the park"
text20= "gggggrrrr....out!rrrrgggg...."
l= text18.strip()
k= text19.strip(".")
j= text20.strip("gr.")

print(l)
print(k)
print("Get", j)



