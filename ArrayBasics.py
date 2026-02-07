import sys

# Arrays Basic

arr = [1, 2, 3, 4, 5]

# Array Length
print(len(arr))

# Index Access
print(arr[2])

# Append to Array
arr.append(6)
print(arr)

# Pop from Array
arr.pop() # if no index is specified, it removes the last element
# arr.pop(0) # removes the element at index 0
print(arr)

# Insert into Array
arr.insert(0, 0)
print(arr)

# Remove from Array
arr.remove(0) # removes the first occurrence of 0
print(arr)

# Slice Array
print(arr[1:4]) # prints elements from index 1 to 3

# Concatenate Arrays
arr2 = [7, 8, 9]
arr3 = arr + arr2
print(arr3)

# Iterate through Array
for x in arr3:
    print(x)
