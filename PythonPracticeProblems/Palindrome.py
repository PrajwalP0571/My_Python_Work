# Palindrome 

def isPalindrome(self, x: int) -> bool:

    if x < 0:
        return False
    
    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10        

    return original == reversed_num

x = int(input("Enter a number: "))
if isPalindrome(x):
    print(f"{x} is a palindrome.")
else:    print(f"{x} is not a palindrome.") 
  
