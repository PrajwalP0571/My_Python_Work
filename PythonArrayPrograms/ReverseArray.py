import array

# Reverse an array

def reverse_array(arr):
    left = 0
    right = len(arr) -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

arr = [256, 735, 128, 512, 643, 398, 428]
reversed_arr = reverse_array(arr)   
print("Reversed Array:", reversed_arr)


arr2 = [23, 45, 67, 89, 12, 11]
reversed_arr2 = reverse_array(arr2)
print("Reversed Array 2:", reversed_arr2)
