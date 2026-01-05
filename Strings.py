## Problem 46: String length without len()
# **Input:** hello
# **Output:** Length: 5

n = input()
count = 0
for i in n:
    count += 1
print(count)


## Problem 47: Vowels and consonants
# **Input:** Hello World
# **Output:** Vowels: 3\nConsonants: 7

n = input().lower()
vowels = 0
consonents = 0
for i in n:
    if i != " ":
        if i in "aeiou":
            vowels += 1
        else:
            consonents += 1
print(f"Vowels: {vowels}\nConsonents: {consonents}")


## Problem 48: Count character occurrence
# **Input:** programming\ng
# **Output:** Occurrences: 2

str = input()
chr = input()
print(str.count(chr))

## Problem 49: Reverse string without slicing
# **Input:** python
# **Output:** Reversed: nohtyp

str = input()
rev = ""
for i in str:
    rev = i + rev
print(rev)

## Problem 50: Check palindrome string
# **Input:** Never odd or even
# **Output:** Palindrome

str = input()
rev = str[::-1]
print("palindrome" if str == rev else "not palindrome")

## Problem 51: Check anagrams
# **Input:** listen\nsilent
# **Output:** Anagrams

str1 = input().lower()
str2 = input().lower()
count = 0
for i in str1:
    if i in str2:
        count += 1
print("Anagram" if count == len(str1) else "Not Anagram")


## Problem 52: Remove spaces
# **Input:** Hello World Python
# **Output:** HelloWorldPython

str = input()
res = str.replace(" ","")
print(res)

## Problem 53: Remove digits
# **Input:** a1b2c3 45
# **Output:** abc

str = input()
res = ""
for i in str:
    if i.isalpha():
        res = res + i
print(res)

## Problem 54: Replace vowels with *
# **Input:** Hello World
# **Output:** H*ll* W*rld

str = input()
res = ""
for i in str:
    if i.lower() in 'aeiou':
        res = res + "*"
    else:
        res = res + i
print(res)

## Problem 55: First non-repeating character
# **Input:** sw engineering
# **Output:** w

str = input()
char_count = {}
for i in str:
    char_count[i] = char_count.get(i,0) + 1

for i in str:
    if char_count[i] == 1:
        print(i)
        break


## Problem 56: First repeating character
# **Input:** sw engineering
# **Output:** e

str = input()
char_count = {}
for i in str:
    char_count[i] = char_count.get(i,0) + 1
for i in str:
    if char_count[i] > 1:
        print(i)
        break


## Problem 57: Word count
# **Input:** Python is easy to learn
# **Output:** Number of words: 5

str = input()
res = str.split()
print(len(res))

## Problem 58: Capitalize first letter of each word
# **Input:** hello world python
# **Output:** Hello World Python

str = input()
res = str.title()
print(res)

## Problem 59: Email validation (basic)
# **Input:** user@example.com
# **Output:** Valid email format

str = input()
if '@' in str and '.' in str:
    print("Valid Email Format")
else:
    print("Invalid Email Format")

## Problem 60: Character frequency
# **Input:** hello
# **Output:** h: 1\ne: 1\nl: 2\no: 1

str = input()
char_count = {}
for i in str:
    char_count[i] = char_count.get(i,0)+1
for i,j in char_count.items():
    print(f"{i}: {j}")

## Problem 61: Longest word in sentence
# **Input:** Python is powerful and easy
# **Output:** Longest word: powerful

str = input().split()
longest_word = str[0]
for i in str:
    if len(i) > len(longest_word):
        longest_word = i
print(f"Longest Word: {longest_word}")


## Problem 62: Contains only digits
# **Input:** 12345
# **Output:** Contains only digits

n = input()
count = 0
for i in n:
    if i.isdigit():
        count += 1
print("Contains only digits" if count == len(n) else "Contains Alphabets also")

## Problem 63: Remove consecutive duplicates
# **Input:** aabbccda
# **Output:** abcda

n = input()
res = ""
for i in n:
    if not res or res[-1] != i:
        res += i 
print(res)

## Problem 64: Find all substrings
# **Input:** abc
# **Output:** a ab abc b bc c

s = input()
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])

## Problem 65: Check startswith and endswith
# **Input:** hello world
# **Output:** Starts with 'hello': True\nEnds with 'world': True

str = input()
print("Starts with \'hello\':",str.startswith('hello'))
print("Ends with \'world\':",str.endswith('world'))

## Problem 66: Rotate string by K
# **Input:** abcdef\n2
# **Output:** cdefab

str = input()
k = int(input())
rotate = k % len(str)
print(str[rotate:]+str[:rotate])


## Problem 67: Check if rotation of another string
# **Input:** abcd\ncdab
# **Output:** cdab is rotation of abcd

str1 = input()
str2 = input()
if len(str1) == len(str2) and str2 in str1 + str1:
    print(f"{str2} is rotation of {str1}")
else:
    print(f"{str2} is not rotation of {str1}")

## Problem 68: Run-length encoding
# **Input:** aabbcc
# **Output:** a2b2c2

str = input()
char_count = {}
for i in str:
    char_count[i] = char_count.get(i,0) + 1
run_length = ""
for i,j in char_count.items():
    run_length = run_length + f"{i}" + f"{j}"
print(run_length)


## Problem 69: Longest common prefix
# **Input:** flower flow flight
# **Output:** fl


## Problem 70: Check if isogram
# **Input:** background
# **Output:** Isogram
