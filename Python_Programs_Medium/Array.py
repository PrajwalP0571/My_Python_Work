import sys
import array

# Arrays

print("Array")
my_array = [1, 2, 3, 4, 5]
print(my_array[3])

for x in my_array:
    print(x)

my_array.reverse()
print(my_array)

my_array.insert(0, 6)
print(my_array)

my_array.sort()
print(my_array)