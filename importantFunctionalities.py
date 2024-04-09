import threading
from concurrent.futures import ThreadPoolExecutor
from time import sleep, perf_counter



# ======================  Working with variables and tuples ======================  
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



# ======================  Generator ======================  
# [Memory optimized | Returns only required value | don't load all value at once in memory like 'for loop']
# [Function containing 'yield' will be treated as 'generator object' | It can be iterated]
def sumoften():
    i = 1
    while i<=10:
        yield i
        i += 1

for i in sumoften():
    print(i, " -> Address: ", id(i))



# ======================  Lambda [syntax - lambda {parameter}: {opertion on parameter}] ======================  
#Use1 : used to performing certain operation and then return value to variable
squareofnum = lambda x: x*x
print("Printing squareofnum: ")
print(squareofnum(2))

time1 = perf_counter()  #  Performance counter - used for benchmarking

#Use2 : Used inside a function as a helper function to perform remaining operation
def cubeofnum1(x: int):
    print("Printing cube1")
    sleep(2)
    print(x * (lambda x: x*x)(x))
    return x * (lambda x: x*x)(x)
print(cubeofnum1(4))

#Use3: Can be passed as an argment into a function to perform more operations
def cubeofnum2(lamb_func, x):
    print("Printing cube2")
    sleep(1)
    print(x * lamb_func(x))
    return x * lamb_func(x)
print(cubeofnum2(lambda x: x*x, 6))

time2 = perf_counter()
print("Total time taken to complete cubeofnum1() and cubeofnum2(): ", time2-time1)



# ======================  Threading [Run multiple operations, functions parallelly]  ======================  
# [Due to GIL: Python doesn't support threads running parallely, but process can]

# Usage1
t2 = threading.Thread(target=cubeofnum1, args=[10])
t1 = threading.Thread(target=cubeofnum2, args=[lambda x: x*x, 8])

time1 = perf_counter()  # Performance counter - used for benchmarking

t1.start()
t2.start()
t1.join()               # waiting for t1 to complete
t2.join()               # waiting for t2 to complete

time2 = perf_counter()
print("Total time taken to complete t1 and t2: ", time2-time1)  
# Both thread will run parallely, that's why time to complete will be equal to time taken by bigger thread

# Usage2: Execute multiple threads using ThreadPoolExecutor()
def pooling():
    with ThreadPoolExecutor() as executor:
        task1 = executor.submit(cubeofnum1, 11)
        task2 = executor.submit(cubeofnum2, lambda x: x*x, 12)
    print(task1.result())   # To get return value

pooling()

# Usage3: Execute multiple thread using map() and ThreadPoolExecutor() to shorten code and schedule as a task
def pooling():
    with ThreadPoolExecutor() as executor:
        lists = [1,2,3,4]
        results = executor.map(cubeofnum1, lists)

        for result in results:
            print(result)  # To get return value

pooling()