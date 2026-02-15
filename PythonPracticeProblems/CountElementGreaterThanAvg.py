# Count no of elements greater than average

def count_greater_than_avg(arr):

    total = 0
    count = 0

    for i in arr:
        total += i
    avg = total / len(arr)

    return avg

arr = [1, 2, 3, 4, 5]
result = count_greater_than_avg(arr)
print("Average is:", result)
