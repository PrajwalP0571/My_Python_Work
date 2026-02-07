import sys

# Array Iteration

arr = [1, 2, 3, 4, 5]

#for x in arr:
    #print(x)

for i in range(len(arr)-1):
    print(arr[i])

# Smallest and Largest Element in Array

arr2 = [33, 45, 67, 12, 89]
smallest = arr2[0]
largest = arr2[0]

for x in arr2[1:]:
    if x < smallest:
        smallest = x
    if x > largest:
        largest = x

print("Smallest element:", smallest)
print("Largest element:", largest)



