## Problem 96: Create and display dictionary
# **Input:** name: Alice, age: 25, city: NYC
# **Output:** {'name': 'Alice', 'age': 25, 'city': 'NYC'}

dict = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
print(dict)

## Problem 97: Dictionary value frequency
# **Input:** apple banana apple orange banana apple
# **Output:** {'apple': 3, 'banana': 2, 'orange': 1}

n = input().split()
dict = {}
for i in n:
    dict[i] = dict.get(i,0)+1
print(dict)

## Problem 98: Invert dictionary (keys -> values)
# **Input:** {'a': 1, 'b': 2, 'c': 3}
# **Output:** {1: 'a', 2: 'b', 3: 'c'}

dict = {'a': 1, 'b': 2, 'c': 3}
res = {}
for i, j in dict.items():
    res[j] = i
print(res)

## Problem 99: Sort dictionary by values
# **Input:** {'apple': 3, 'banana': 2, 'orange': 1}
# **Output:** [('orange', 1), ('banana', 2), ('apple', 3)]

dict = {'apple': 3, 'banana': 2, 'orange': 1}
sort = sorted(dict.items(),reverse=True)
print(sort)

## Problem 100: Merge two dictionaries
# **Input:** {'a': 1, 'b': 2}, {'c': 3, 'd': 4}
# **Output:** {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print({**d1,**d2})

## Problem 101: Count word frequency in sentence
# **Input:** the quick brown fox jumps over the lazy dog
# **Output:** {'the': 2, 'quick': 1, 'brown': 1, ...}

str = input().split()
dict = {}
for i in str:
    dict[i] = dict.get(i,0)+1
print(dict)

## Problem 102: Find common elements in sets
# **Input:** {1, 2, 3, 4}, {3, 4, 5, 6}
# **Output:** {3, 4}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.intersection(s2))

## Problem 103: Set operations (Union, Intersection, Difference)
# **Input:** {1, 2, 3}, {2, 3, 4}
# **Output:** Union: {1, 2, 3, 4}, Intersection: {2, 3}, Difference: {1}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f"Union: {s1.union(s2)}, Intersection: {s1.intersection(s2)}, Difference: {s1.difference(s2)}")

## Problem 104: Remove duplicates using set
# **Input:** [1, 2, 2, 3, 4, 1, 5]
# **Output:** [1, 2, 3, 4, 5]

l = [int(i) for i in input().split()]
s = list(set(l))
print(sorted(s))

## Problem 105: Check if key exists in dictionary
# **Input:** {'name': 'Alice', 'age': 25}, 'name'
# **Output:** Key exists

n = {'name': 'Alice', 'age': 25}
key = input() 
if key in n:
    print("Key Exists")
else:
    print("Not exists")

## Problem 106: Get default value from dictionary
# **Input:** {'a': 1, 'b': 2}, 'c'
# **Output:** 'c' not found, using default: 0

dict = {'a': 1, 'b': 2}
key = input()
res = dict.get(key,0)
print(f"Value of '{key}': {res}")

## Problem 107: Dictionary comprehension
# **Input:** [1, 2, 3, 4, 5]
# **Output:** {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

l = [int(i) for i in input().split()]
dict = {i: i ** 2 for i in l}
print(dict)

## Problem 108: Group words by first letter
# **Input:** apple ant bear banana cat cow
# **Output:** {'a': ['apple', 'ant'], 'b': ['bear', 'banana'], 'c': ['cat', 'cow']}

str = input().split()
dict = {}
for j in str:
    dict[j[0]] = [i for i in str if i.startswith(j[0])]
print(dict)

## Problem 109: Symmetric difference of two sets
# **Input:** {1, 2, 3, 4}, {3, 4, 5, 6}
# **Output:** {1, 2, 5, 6}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1^s2)

## Problem 110: Check if set is subset or superset
# **Input:** {1, 2}, {1, 2, 3}
# **Output:** {1, 2} is subset of {1, 2, 3}

s1 = {1, 2}
s2 = {1, 2, 3}
if s1.issubset(s2):
    print(f"{s1} is subset of {s2}")
if s2.issuperset(s1):
    print(f"{s2} is superset of {s1}")