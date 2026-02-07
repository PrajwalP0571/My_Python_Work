import sys

# quote inside a string
print("What a Beautiful Day, isn't it?")
print('Hey, My name is "Johnny"')

# Multiline Strings

a = """ Ye re ye re pavsa,
Tula deto paisa,
Paisa zala khota,
Pause ala motha"""

print(a)
print(a[6])

# Looping through a string
for x in "Apple":
    print(x)

# String Length
b = "I am The best"
print(len(b))

# Check String
txt = "I will get hired in IBM definitely"
print("definitely" in txt)

if ("definitely" in txt):
    print("Yes, 'definitely' is in the text.")

print("ibm" not in txt)

# String Slicing
c = "I will do Hard Work and get Success"
print(c[10:19])

print(c[:6])
print(c[4:])

# Negative Indexing
print(c[-3:-7])

# Modify Strings

d = "  Consistency is the  key "
print(d.upper())
print(d.lower())
print(d.capitalize())

# remove whitespace
print(d.strip())

# Replace String
print(d.replace("key", "chabi"))
print(d.split(" , "))

# string concatenation
e = "I am "
f = "the Best"

print(e+f)

# string format
age = 24
txt = f"My age is {age}"
print(txt)

price = 83
txt2 = f"the price of a dollor is {price:.2f} rupees"
print(txt2)

# placeholder
txt3 = f"The price of a 10 dollers is {10 * 82} rupees"
print(txt3)

# Escape Characters
g = "The \"IBM Campus\" is not so far from my place"
print(g)

# String Methods
word = "I can do it"
print(word.capitalize())
print(word.casefold())
print(word.center(60))
print(word.count("i"))
print(word.encode())
