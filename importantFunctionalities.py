import threading
from time import sleep

# =========== Working with variables and tuples =========== 
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


# =========== Generator =========== 
# [Memory optimized | Returns only required value | don't load all value at once in memory like 'for loop']
# [Function containing 'yield' will be treated as 'generator object' | It can be iterated]
def sumoften():
    i = 1
    while i<=1000:
        yield i
        i += 1

for i in sumoften():
    print(i, " -> Address: ", id(i))


# =========== Lambda [syntax - lambda {parameter}: {opertion on parameter}] =========== 
#Use1 : used to performing certain operation and then return value to variable
squareofnum = lambda x: x*x
print(squareofnum(2))

#Use2 : Used inside a function as a helper function to perform remaining operation
def cubeofnum1(x: int):
    print("Printing cube1")
    print(x * (lambda x: x*x)(x))
    return x * (lambda x: x*x)(x)
print(cubeofnum1(4))

#Use3: Can be passed as an argment into a function to perform more operations
def cubeofnum2(lamb_func, x):
    print("Printing cube2")
    sleep(4)
    print(x * lamb_func(x))
    return x * lamb_func(x)
print(cubeofnum2(lambda x: x*x, 6))


# =========== Threading [Run multiple operations, functions parallely]  =========== 
# [Due to GIL: Python doesn't support threads running parallely, but process can]
t2 = threading.Thread(target=cubeofnum1, args=[10])
t1 = threading.Thread(target=cubeofnum2, args=[lambda x: x*x, 8])

t1.start()
t2.start()
