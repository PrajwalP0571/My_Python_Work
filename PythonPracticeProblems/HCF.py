

# HCF 

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1 , smaller +1):
        if(x%i == 0 and y%i == 0):
            hcf = i
    return hcf

num1 = 48
num2 = 18   
result = hcf(num1, num2)
print("HCF of", num1, "and", num2, "is", result)