# Insertion Sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(arr)
print("Sorted array is:", sorted_array)