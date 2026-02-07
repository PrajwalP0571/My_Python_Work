import sys

# Two Pointer Sliding Window

arr = [5, 9, 3, 7, 2, 8, 1, 4, 6]

arr.sort()

print("Sorted array:", arr)

i, j = 0, len(arr) - 1
target = 6

while i < j:
    s = arr[i] + arr[j]

    if s == target:
        print("Pair found:", arr[i], arr[j])
        
        i += 1
        j -= 1
    
    elif s < target:
        i += 1
    else:
        j -= 1




