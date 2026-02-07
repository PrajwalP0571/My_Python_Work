import sys

print("Accha time ane wala hai!")

# Global Variables
x = "Mumbai Indians"

def myfunc():
    x = "Royal Challengers Bangalore"
    print("My fav IPL team is " + x)


print("My fav IPL team is " + x)

myfunc()

def myfunc2():
    global y
    y = "Fantastic"
    print("Python is " + y)

myfunc2()
print("Python is " + y)

# 