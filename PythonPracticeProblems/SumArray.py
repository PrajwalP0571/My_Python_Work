# sum of array elements

def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total

arr = [1, 2, 3, 4, 5]
result = sum_array(arr)
print("Sum of array elements is:", result)  