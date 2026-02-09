import array


def min_max(arr):
    if not arr:
        return None
    
    min = arr[0]
    max = arr[0]

    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x

    return min, max

arr = [256, 735, 128, 512, 643, 398, 428]

min, max = min_max(arr)

print("Minimum:", min)
print("Maximum:", max)