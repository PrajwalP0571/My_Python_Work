import sys

# Arithmetic Operators

a = 10
b = 5       

# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication
# print(a / b)  # Division
# print(a % b)  # Modulus
# print(a ** b) # Exponentiation
# print(a // b) # Floor Division  

# Assignment Operators

# c = 20
# c += 5  # c = c + 5 = 25
# print("After c += 5:", c)
# c -= 5  # c = c - 5 = 20
# print("After c -= 5:", c)
# c *= 5  # c = c * 5 = 100
# print("After c *= 5:", c)
# c /= 5  # c = c / 5 = 20
# print("After c /= 5:", c)
# c %= 5  # c = c % 5 = 0
# print("After c %= 5:", c)
# c **= 5 # c = c ** 5 = 0
# print("After c **= 5:", c)
# c //= 5 # c = c // 5 = 0
# print("After c //= 5:", c)

d = 17


d &= 3  # d = d & 3
print("After d &= 5:", d)
d |= 3  # d = d | 3
print("After d |= 5:", d)
d ^= 3  # d = d ^ 3
print("After d ^= 5:", d)
d >>= 2 # d = d >> 2
print("After d >>= 2:", d)
d <<= 2 # d = d << 2
print("After d <<= 2:", d)  


# Comparison Operators

e = 10
f = 20

print(e == f)
print(e != f)
print(e < f)
print(e > f)
print(e <= f)
print(e >= f)

# Logical Operators

print("Logical Operators:")
x = 5
print(x > 3 and x <10)

print(x<3 or x>10)
print(not(x < 3 or x >10))

# Identity Operators

print("Identity Operators:")

g = 10
h = 10
i = 20

print(g is h)  # True
print(g is i)  # False
print(g is not i)  # True

p = [1, 2, 3]
q = [1, 2, 3]

print(p == q)
print(p is q)

# Bitwise Operators

print("Bitwise Operators:")

# Operator Presedence
print("Operator Precedence:")
result = 10 + 5 * 2
print(result)  # Output: 20

