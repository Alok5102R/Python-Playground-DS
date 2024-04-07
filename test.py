b = 5
a = b = b+1
# a = b += 1               # SyntaxError: invalid syntax

print(a, b)

a, b = 8, 9
print(a, b)

a = 7, 0
b = a, 8
c = a + b
print(a, b, c)