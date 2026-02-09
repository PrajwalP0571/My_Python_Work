import array

def second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')

    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif largest > x > second_largest:
            second_largest = x

    return second_largest

arr = [256, 735, 128, 512, 643, 398, 428]

result = second_largest(arr)

print("Second Largest:", result)
    

    
