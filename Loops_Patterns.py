# ## Problem 21: Print numbers 1 to N
# **Input:** 5
# **Output:** 1\n2\n3\n4\n5

# n = int(input())
# for i in range(1, n+1):
#     print(i)


# ## Problem 22: Even numbers 1 to N
# **Input:** 10
# **Output:** 2 4 6 8 10

# n = int(input())
# for i in range(1, n+1):
#     if i%2 == 0:
#         print(i)

# ## Problem 23: Sum of first N natural numbers
# **Input:** 10
# **Output:** Sum: 55

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

# ## Problem 24: Factorial using loop
# **Input:** 5
# **Output:** Factorial: 120

# n = int(input())
# fact = 1
# for i in range(n,0,-1):
#     fact = fact * i
# print(fact)

# ## Problem 25: Count digits in number
# **Input:** 12345
# **Output:** Number of digits: 5

# n = int(input())
# count = 0
# while n > 0:
#     count = count + 1 
#     n //= 10
# print(count)

# ## Problem 26: Sum of digits
# **Input:** 2514
# **Output:** Sum of digits: 12

# n = int(input())
# sum = 0 if n != 0 else 1
# while n > 0:
#     sum = sum + n % 10
#     n = n // 10
# print(sum)

# ## Problem 27: Reverse a number
# **Input:** 12340
# **Output:** Reversed number: 4321

# n = int(input())
# negative = n < 0
# n = abs(n)
# rev = 0
# while n > 0:
#     rev = rev * 10 + (n % 10)
#     n //= 10
# if negative:
#     rev = -(rev)
# print(rev)

# ## Problem 28: Check palindrome number
# **Input:** 1221
# **Output:** Palindrome

# n = int(input())
# negative = n < 0
# n1 = abs(n)
# rev = 0
# while n1 > 0:
#     rev = rev * 10 + (n1 % 10)
#     n1 //= 10
# if negative:
#     rev = -(rev)
# if n == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# ## Problem 29: Armstrong number (3-digit)
# **Input:** 153
# **Output:** Armstrong number

# n = int(input())
# n1 = n
# sum = 0
# while n1 > 0:
#     sum = sum + (n1 % 10) ** 3
#     n1 //= 10
# if sum == n:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")

# ## Problem 30: Fibonacci series up to N terms
# **Input:** 7
# **Output:** 0 1 1 2 3 5 8

# n = int(input())
# a = 0
# b = 1
# for i in range(n):
#     if i == 0:
#         print(a,end=" ")
#     elif i == 1:
#         print(b,end=" ")
#     else:
#         c = a + b
#         print(c,end=" ")
#         a = b
#         b = c


# ## Problem 31: Count even and odd digits
# **Input:** 205431
# **Output:** Even digits: 3\nOdd digits: 3

# n = int(input())
# even = 0
# odd = 0
# while n > 0:
#     if (n%10) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n //= 10

# print(f"Even digits: {even}\nOdd digits: {odd}")


# ## Problem 32: GCD using Euclidean algorithm
# **Input:** 36\n60
# **Output:** GCD: 12

# ## Problem 33: LCM using GCD
# **Input:** 12\n15
# **Output:** LCM: 60

# ## Problem 34: All prime numbers in range
# **Input:** 10\n25
# **Output:** 11 13 17 19 23

# n = int(input())
# m = int(input())
# for i in range(n,m+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i,end=" ")

# ## Problem 35: Check if prime
# **Input:** 29
# **Output:** Prime

# n = int(input())
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# ## Problem 36: Left-aligned star pyramid
# **Input:** 4
# **Output:** *
#             **
#             ***
#             ****

# n = int(input())
# for i in range(1, n+1):
#     print('*'*i)


# ## Problem 37: Center-aligned pyramid
# **Input:** 4
# **Output:**    *
#               ***
#              *****
#             *******

# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# ## Problem 38: Inverted pyramid
# **Input:** 4
# **Output:** ****
#             ***
#             **
#             *

# n = int(input())
# for i in range(n,0,-1):
#     print("*"*(i))

# ## Problem 39: Numeric triangle
# **Input:** 5
# **Output:** 1
#             22
#             333
#             4444
#             55555

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# ## Problem 40: Floyd's triangle
# **Input:** 5
# **Output:** 1
#            2 3
#           4 5 6
#          7 8 9 10
#       11 12 13 14 15

# n = int(input())
# num = 1
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num += 1
#     print()

# ## Problem 41: Pascal's triangle
# **Input:** 5
# **Output:**      1
#                 1 1
#                1 2 1
#               1 3 3 1
#              1 4 6 4 1

# ## Problem 42: Multiplication tables 1-10

# for i in range(1, 11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

# ## Problem 43: Harmonic series sum
# **Input:** 5
# **Output:** Sum: 2.283333333333333


# ## Problem 44: Sum of squares
# **Input:** 4
# **Output:** Sum of squares: 30

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i**2
# print(sum)

# ## Problem 45: All factors of number
# **Input:** 12
# **Output:** 1 2 3 4 6 12

# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end=" ")