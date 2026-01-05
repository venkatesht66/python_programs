## Problem 111: Simple function
# **Input:** 5
# **Output:** Square: 25

def square(n):
    return n * n

n = int(input())
print(square(n))

## Problem 112: Function with multiple parameters
# **Input:** 10\n3
# **Output:** 10 + 3 = 13\n10 - 3 = 7\n10 * 3 = 30\n10 / 3 = 3.33

def calculator(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

a = int(input())
b = int(input())
calculator(a, b)

## Problem 113: Function returning multiple values
# **Input:** 36\n60
# **Output:** GCD: 12, LCM: 180


## Problem 114: Default parameter values
# **Input:** 5
# **Output:** Power(5, 2) = 25

def pow(n, exp = 2):
    return n ** exp

n = int(input())
print(pow(n))

## Problem 115: Variable length arguments (*args)
# **Input:** 1 2 3 4 5
# **Output:** Sum: 15

def sum_len(*args):
    sum = 0
    for i in args:
        sum += i
    return f"Sum: {sum}"

print(sum_len(1,2,3,4,5))

## Problem 116: Keyword arguments (**kwargs)
# **Input:** name Alice age 25 city NYC
# **Output:** name=Alice, age=25, city=NYC

def key_args(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}: {j}")

key_args(name="Alice",age= 25,city="NYC")

## Problem 117: Factorial using recursion
# **Input:** 5
# **Output:** Factorial: 120

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))

## Problem 118: Fibonacci using recursion
# **Input:** 7
# **Output:** Fibonacci(7) = 13

def fibonacci(n):
    if n == 0 or n == 1:
        return  n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

## Problem 119: Power using recursion
# **Input:** 2\n5
# **Output:** 2^5 = 32

def power(n,exp):
    if exp == 0:
        return 1
    return n * (power(n, exp - 1))

n = int(input())
exp = int(input())
print(power(n, exp))

## Problem 120: Sum of N numbers using recursion
# **Input:** 5
# **Output:** Sum: 15

def sum_n_natural_num(n):
    if n == 1:
        return 1
    return n + sum_n_natural_num(n-1)

n = int(input())
print(sum_n_natural_num(n))

## Problem 121: Lambda function (anonymous)
# **Input:** [1, 2, 3, 4, 5]
# **Output:** Squares: [1, 4, 9, 16, 25]

l = [int(i) for i in input().split()]
res = list(map(lambda x: x * x, l))
print(res)


## Problem 122: Map function
# **Input:** [1, 2, 3, 4]
# **Output:** Doubled: [2, 4, 6, 8]

l = [int(i) for i in input().split()]
res = list(map(lambda x : x + x, l))
print(f"Doubled: {res}")

## Problem 123: Filter function
# **Input:** [1, 2, 3, 4, 5, 6, 7, 8]
# **Output:** Even: [2, 4, 6, 8]

l = [int(i) for i in input().split()]
res = list(filter(lambda x : x % 2 == 0, l))
print(f"Even: {res}")

## Problem 124: Reduce function (sum using reduce)
# **Input:** [1, 2, 3, 4, 5]
# **Output:** Sum: 15

from functools import reduce
l = [int(i) for i in input().split()]
res = reduce(lambda x, y : x + y, l )
print(res)

## Problem 125: Decorator function
# **Input:** hello world
# **Output:** Function called with: hello world

def decorator(func):
    def wrapper(*args):
        print(f"Function called with: {args}")
        return func(*args)
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")