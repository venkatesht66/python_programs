# SECTION 1: BASICS & SYNTAX (1-20)

## Problem 1: Print "Hello, World!"
# **Statement:** Print Hello, World!
# **Input:** None
# **Output:** Hello, World!

# print("Hello, World!")

## Problem 2: Print name and age
# **Statement:** Ask for name and age, print formatted output
# **Input:** Rohit\n21
# **Output:** Name: Rohit, Age: 21

# name = input()
# age = int(input())
# print("Name: {}, Age: {}".format(name,age))

## Problem 3: Sum of two numbers
# **Statement:** Read two integers and print their sum
# **Input:** 5\n7
# **Output:** Sum: 12

# n = int(input())
# m = int(input())
# sum = n + m
# print(sum)

## Problem 4: Swap two variables
# **Statement:** Swap two numbers without third variable
# **Input:** 10\n20
# **Output:** After swap: a = 20 b = 10

# a = int(input())
# b = int(input())
# print("Before swap: a = {} b = {}".format(a,b))
# a = a + b
# b = a - b
# a = a - b
# print("After swap: a = {} b = {}".format(a,b))

## Problem 5: Celsius to Fahrenheit
# **Statement:** Convert C to F: F = C × 9/5 + 32
# **Input:** 37
# **Output:** Temperature in Fahrenheit: 98.6

# c = int(input())
# f = c * 9/5 + 32
# print(f)

## Problem 6: Even or odd
# **Statement:** Check if number is even or odd
# **Input:** 11
# **Output:** Odd

# n = int(input())
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

## Problem 7: Largest of three numbers
# **Statement:** Find maximum of three numbers
# **Input:** 10\n25\n15
# **Output:** Largest: 25

# a = int(input())
# b = int(input())
# c = int(input())

# if a > b and b > c:
#     print("{} is largest number".format(a))
# elif b > c:
#     print("{} is largest number".format(b))
# else:
#     print("{} is largest number".format(c))

## Problem 8: Simple and compound interest
# **Statement:** Calculate SI = P×R×T/100, CI = P(1+R/100)^T - P
# **Input:** 10000\n5\n2
# **Output:** Simple Interest: 1000.0\nCompound Interest: 1025.0

# P = int(input())
# R = int(input())
# T = int(input())
# SI = (P*R*T)/100
# CI = P*(1+R/100)**T - P
# print(f"Simple Interest: {SI}\nCompound Interest: {CI}")

## Problem 9: Multiplication table
# **Statement:** Print multiplication table 1-10
# **Input:** 7
# **Output:** 7 x 1 = 7\n7 x 2 = 14\n...\n7 x 10 = 70

# n = int(input())
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

## Problem 10: Area and circumference of circle
# **Statement:** Calculate A = πr², C = 2πr
# **Input:** 5
# **Output:** Area: 78.53975\nCircumference: 31.4159

# r = int(input())
# area = (22/7)*((r)**2)
# circumference = 2 * (22/7) * r
# print(f"Area: {area}\nCircumference: {circumference}")

## Problem 11: Convert minutes to hours
# **Statement:** Convert total minutes to hours:minutes
# **Input:** 130
# **Output:** Hours: 2, Minutes: 10

# n = int(input())
# print(f"Hours: {n // 60}, Minutes: {n % 60}")

## Problem 12: Check leap year
# **Statement:** Leap if divisible by 400 OR (divisible by 4 AND not by 100)
# **Input:** 2024
# **Output:** Leap year

# year = int(input())
# if (year % 400 == 0) or (year % 4 == 0 and year %  100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

## Problem 13: Vowel or consonant
# **Statement:** Check if character is vowel or consonant
# **Input:** e
# **Output:** Vowel

# vowel = "aeiou"
# char = input().lower()
# if char in vowel:
#     print("Vowel")
# else:
#     print("Consonant")

## Problem 14: Positive, negative, or zero
# **Statement:** Classify a number
# **Input:** -5
# **Output:** Negative

# n = int(input())

# if n == 0:
#     print("Zero")
# elif n > 0:
#     print("Positive")
# else:
#     print("Negative")

## Problem 15: Absolute value without abs()
# **Statement:** Find absolute value using logic
# **Input:** -12
# **Output:** Absolute value: 12.0

# n = float(input())
# if n < 0:
#     n = -n
# print(n)

## Problem 16: Power a^b without **
# **Statement:** Calculate a^b using loop
# **Input:** 2\n5
# **Output:** Result: 32

# n = int(input())
# pow = int(input())
# res = 1
# for i in range(1,pow+1):
#     res = res * n
# print(res)

## Problem 17: Check if three sides form triangle
# **Statement:** Sum of any two sides > third side
# **Input:** 3\n4\n5
# **Output:** Can form a triangle

# a = int(input())
# b = int(input())
# c = int(input())

# if a + b > c and b + c > a and c + a > b:
#     print("Can form a triangle")
# else:
#     print("Cannot form a triangle")

## Problem 18: Classify triangle
# **Statement:** Equilateral/Isosceles/Scalene
# **Input:** 5\n5\n8
# **Output:** Valid triangle\nIsosceles triangle

# a = int(input())
# b = int(input())
# c = int(input())

# if a + b > c and b + c > a and c + a > b:
#     print("Valid Triangle")
#     if a == b == c:
#         print("Equilateral Triangle")
#     elif a == b or b == c or c == a:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
# else:
#     print("Cannot form a triangle")

## Problem 19: Simple calculator
# **Statement:** Perform +, -, *, / operations
# **Input:** 10\n3\n/
# **Output:** Result: 3.3333333333333335

# a = int(input())
# b = int(input())
# operator = input()

# if operator == '+':
#     print(f"Result: {float(a + b)}")
# elif operator == '-':
#     print(f"Result: {float(a - b)}")
# elif operator == '*':
#     print(f"Result: {float(a * b)}")
# elif operator == '/':
#     print(f"Result: {float(a / b)}")

## Problem 20: ASCII value of character
# **Statement:** Print ASCII value of a character
# **Input:** A
# **Output:** ASCII value of A is 65

# char = input()
# print(f"ASCII value of {char} is {ord(char)}")