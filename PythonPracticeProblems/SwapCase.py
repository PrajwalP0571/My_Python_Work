# Swap Case Problem

def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()

    return result

s = "Hello World!"
output_string = swap_case(s)
print("Original String:", s)
print("Swapped Case String:", output_string)

