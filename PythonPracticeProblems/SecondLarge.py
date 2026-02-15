# Find second largest number in a list

#from os import remove


def second_largest(s):
    if len(s) < 2:
        return None
    
    unique_numbers = list(set(s))

    unique_numbers.remove(max(unique_numbers))

    print(max(unique_numbers))

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
second_largest(numbers) 

    
                
    
