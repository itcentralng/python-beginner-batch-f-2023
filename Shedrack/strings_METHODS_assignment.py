# capitalize()
stm ="my name is krucial"
print(stm.capitalize())

# casefold()
btc = 'her name is HAdiZa sULEiMAN'
print(btc.casefold())

# center()
agent = 'kong'
print(agent.center(16, "$"))

# count()
x = "i am sleeping. i slept well yesterday. i love sleeping"
print(x.count("sleeping", 3, 50))

# find() is used to search for the occurence of a specific letter in a string.
y = 'great people always work hard and smart. i work hard'
print(y.find('work', 25, 50))

# endswith() is used to check if it is true or false, a string endswith a specific value.
obj = "a fool at faulty"
print(obj.endswith('faulty'))

# expandtabbs() is used to set tab size.
stm = 'C\to\tl\tl\te\tg\te'
print(stm.expandtabs())
print(stm.expandtabs(2))
print(stm.expandtabs(4))

# index() is used to find the index of the first ocurrence of a specific value.
_class = 'life is like a movie'
print(_class.index('e'))
print(_class.index('e', 5, 15))

# isalnum() returns true if all the char in the strings are alpha-numeric, else false is returned.
vng = "Krucial7LetarzStardom"
print(vng.isalnum())

# isalpha() returns true if all the char in the strings are alphabets only, else false.
cd = "contermination"
print(cd.isalpha())

# isdecimal() returns true if all the char in the strings are decimals only, else false.
num = '72'
print(num.isdecimal())

# isdigit() returns true if all the char in the strings are digits only, else false.
Num = '7463848'
print(Num.isdigit())

# isdentifier() returns true if the string is an identifier, else false.
fb = 'commonpersonha24shoes'
print(fb.isidentifier())

# islower() returns true if all the char in the strings are lower case, else false.
food = 'rice, bean and kpomo'
print(food.islower())

# isnumeric() returns true if all the char in the strings are numeric, else false.
pic = '0123456789'
print(pic.isnumeric())

# isprintable() this method returns true if all the char in the strings are alphabet.
bro = "Sylvanus Yusuf"
print(bro.isprintable())

# isspace() returns true if all the char in the strings are wide spaces, else false.
space = "  "
print(space.isspace())

# istitle() returns true if the first char of a value in a string is an UPPERCASE, else false.
d = "Yusuf Garba"
print(d.istitle())

# isupper() returns true if all the char in the strings are in UPPERCASE, else false.
fka = 'FOOTBALL'
print(fka.isupper())

# join() is used to join the iterable elements to the end of a string contained.
xyz = ["Fave", "Kasy", "Abelo", "Ayinlo", "Nina", "MCoco"]
abc = "$$"
print(abc.join(xyz))

# lower() is used to convert UPPERCASE data in the string to lowercase.
hank = "The Black Man From The Atlantic Side"
print(hank.lower())

# lstrip() is used to remove char from the left of the string.
py = "*********EDUCATION IS KEY"
print(py.lstrip('*')) 

# replace() is used to replace a value with another.
hi = 'Who is Shedrack Yusuf. Shedrack Yusuf is a Software Developer'
print(hi.replace("Shedrack", 'Saviour',))
hi2 = hi.replace("Software Developer", 'Fashion Designer')
print(hi2)

# rfind is used to find the last occurence of a value from a string.
kit = 'Black is beautiful. Black is a colour.'
print(kit.rfind('beautiful'))
print(kit.rfind('colour'))

# rindex() is used to get the index of the last occurence of a specific value.
col = "it is a box. that is my box. why is aisha carrying my box"
print(col.rindex("box"))

# rjust() is used to return a right justified string and fill chars to the left.
bb ="Nigerian Mafia"
print(bb.rjust(30, "N"))

# rsplit() is used to split a string begining from the right, which returns a list.
aa= 'gemini, dell, samsung, lenovo, zinux, tesla'
print(aa.rsplit(",", 3))

# rstrip() is used to remove chars from the rigth of a string..
cc = "CRAZY THINGS ARE HAPPENING£££££££££"
print(cc.rstrip("£"))

# split() is used to remove chars in a string.
vv= "Time$$Money$$Fame$$Power"
print(vv.split('$$',2))

# splitlines() is used to split a string into a list.
fam = "Ten\nHen\nMen\nPen\nBen"
print(fam.splitlines(False))

# startwith() returns True if string begins with a particular value, else False is returned.
jaam = 'The country is hard and we all are passing through hard times'
print(jaam.startswith('is',12))

# swapcase() is used to swap the case, from either lowercase to UPPERCASE, otherwise.
crw = "A cLasS FilLeD wItH exCitING peoPLE"
print((crw.swapcase()))

# title() this is used to convert the first letter of every word to UPPERCASE.
stm = "the dream of a star"
print(stm.title())

# upper() is used to convert lowercase data in the string to UPPERCASE.
hank1 = "the black man from the atlantic side"
print(hank1.upper())

# zfill() is used to fill zeros in the begining of the string.
hp = "Volvo"
print(hp.zfill(9))

hp2 = "734.4747"
print(hp2.zfill(15))

# strip() is used to remove spaces in the begining and end of a string.
ss = "     3.98,    1.4,      12.67   "
print(ss.strip(" "))
()