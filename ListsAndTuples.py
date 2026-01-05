## Problem 71: Read N numbers into list
# **Input:** 5\n1 2 3 4 5
# **Output:** List: [1, 2, 3, 4, 5]

# n = int(input())
# l = [int(input()) for i in range(n)]
# print(l)

## Problem 72: Max and min without built-in
# **Input:** 6\n4 2 9 7 5 1
# **Output:** Maximum: 9\nMinimum: 1

# n = int(input())
# l = [int(input()) for i in range(n)]
# min = l[0]
# max = l[-1]
# for i in range(len(l)):
#     if l[i] > max:
#         max = l[i]
#     elif l[i] < min:
#         min = l[i]
# print(f"Maximum: {max}\nMinimum: {min}")


## Problem 73: Sum and average
# **Input:** 4\n10 20 30 40
# **Output:** Sum: 100\nAverage: 25.0

# n = int(input())
# l = [int(input()) for i in range(n)]
# sum = 0
# avg = 0
# for i in range(len(l)):
#     sum = sum + l[i]
# avg = sum/len(l)
# print(f"Sum: {sum}\nAverage: {avg}")

## Problem 74: Count element occurrences
# **Input:** 6\n1 2 3 2 4 2\n2
# **Output:** Occurrences of 2: 3

# n = int(input())
# l = [int(i) for i in input().split()]
# k = int(input())
# print(f"Occurence of {k}: {l.count(k)}")

## Problem 75: Remove all occurrences of element
# **Input:** 7\n1 2 3 2 4 2 5\n2
# **Output:** List after removal: [1, 3, 4, 5]

# n = int(input())
# l = [int(i) for i in input().split()]
# k = int(input())
# res = [i for i in l if i != k]
# print(res)

## Problem 76: Remove duplicates (preserve order)
# **Input:** 8\n1 2 2 3 4 1 5 3
# **Output:** Unique list: [1, 2, 3, 4, 5]

# n = int(input())
# l = [int(i) for i in input().split()]
# l.sort()
# unique = []
# for i in l:
#     if i not in unique:
#         unique.append(i)
# print(unique)

## Problem 77: Second largest element
# **Input:** 6\n4 2 9 7 5 1
# **Output:** Second largest: 7

# n = int(input())
# l = [int(i) for i in input().split()]
# first = second = float('-inf')
# for i in l:
#     if i > first:
#         second = first
#         first = i
#     elif i > second and i != first:
#         second = i
# print(second)

## Problem 78: Separate even and odd
# **Input:** 7\n1 2 3 4 5 6 7
# **Output:** Even: [2, 4, 6]\nOdd: [1, 3, 5, 7]

# n = int(input())
# l = [int(i) for i in input().split()]
# even = [i for i in l if i%2 == 0]
# odd = [i for i in l if i%2 != 0]
# print(f"Even: {even}\nOdd: {odd}")

## Problem 79: Merge two sorted lists
# **Input:** 3\n1 3 5\n4\n2 4 6 8
# **Output:** Merged sorted list: [1, 2, 3, 4, 5, 6, 8]


## Problem 80: Reverse list in-place
# **Input:** 5\n1 2 3 4 5
# **Output:** Reversed list: [5, 4, 3, 2, 1]

# n = int(input())
# l = [int(i) for i in input().split()]

# left = 0
# right = len(l) - 1

# while left < right:
#     l[left], l[right] = l[right], l[left]
#     left += 1
#     right -= 1

# print(l)


## Problem 81: Rotate list by K
# **Input:** 7\n1 2 3 4 5 6 7\n3
# **Output:** Rotated list: [5, 6, 7, 1, 2, 3, 4]

# n = int(input())
# l = [int(i) for i in input().split()]
# k = int(input())
# rotate = k % len(l)
# print(f"Rotated list: {l[rotate:]+l[:rotate]}")


## Problem 82: Common elements in two lists
# **Input:** 5\n1 2 3 4 5\n5\n3 4 5 6 7
# **Output:** Common elements: [3, 4, 5]

# n1 = int(input())
# l = [int(i) for i in input().split()]
# n2 = int(input())
# m = [int(i) for i in input().split()]
# res = [i for i in l if i in m]
# print(res)


## Problem 83: List1 - List2 (difference)
# **Input:** 5\n1 2 3 4 5\n5\n3 4 5 6 7
# **Output:** List1 - List2: [1, 2]

# n1 = int(input())
# l = [int(i) for i in input().split()]
# n2 = int(input())
# m = [int(i) for i in input().split()]
# res = [i for i in l if i not in m]
# print(res)

## Problem 84: Flatten nested list
# **Input:** [[1,2], [3,4], [5]]
# **Output:** Flattened: [1, 2, 3, 4, 5]


## Problem 85: Split list into chunks of size K
# **Input:** 10\n1 2 3 4 5 6 7 8 9 10\n3
# **Output:** Chunks: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


## Problem 86: Two-sum (pair with target)
# **Input:** 4\n2 7 11 15\n9
# **Output:** Indices: 0 1

# def two_sum(l,k):
#     target = k
#     m = []
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i] + l[j] == target:
#                 pair = (i,j)
#                 m.append(pair)
#     return m

# n = int(input())
# l = [int(i) for i in input().split()]
# k = int(input())
# res = two_sum(l,k)
# for i in res:
#     print(f"Indices: {i[0]} {i[1]}")

## Problem 87: All triplets summing to zero
# **Input:** 6\n-1 0 1 2 -1 -4
# **Output:** Triplets: [[-1, -1, 2], [-1, 0, 1]]



## Problem 88: Sort tuple list by second element
# **Input:** [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# **Output:** Sorted by score: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]



## Problem 89: K-th largest element
# **Input:** 6\n3 2 1 5 6 4\n2
# **Output:** 2nd largest: 5



## Problem 90: Maximum subarray sum (Kadane's)
# **Input:** 9\n-2 1 -3 4 -1 2 1 -5 4
# **Output:** Maximum subarray sum: 6

# def max_sub_arr_sum(l):
#     m = []
#     for i in range(len(l)):
#         for j in range(i+1, len(l)+1):
#             m.append(l[i:j])

#     sum_m = []
#     for i in m:
#         sum_m.append(sum(i))
#     max_sum = max(sum_m)
#     print(max_sum)
#     max_sum_index = sum_m.index(max_sum)
#     print(m[max_sum_index])

# n = int(input())
# l = [int(i) for i in input().split()]
# max_sub_arr_sum(l)

## Problem 91: Check if list is sorted
# **Input:** 5\n1 2 3 4 5
# **Output:** List is sorted



## Problem 92: Binary search on sorted list
# **Input:** 7\n1 3 5 7 9 11 13\n7
# **Output:** Found at index: 3

# n = int(input())
# l = [int(i) for i in input().split()]
# k = int(input())
# l.sort()

# left = 0
# right = len(l) - 1
# while left < right:
#     mid = (left+right)//2
#     if l[mid] < k:
#         left = mid + 1
#     elif l[mid] > k:
#         right = mid - 1
#     elif l[mid] == k:
#         print(mid)
#         break


## Problem 93: Permutations of list
# **Input:** [1, 2, 3]
# **Output:** [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


## Problem 94: Longest increasing subsequence
# **Input:** 8\n10 9 2 5 3 7 101 18
# **Output:** LIS length: 4


## Problem 95: Generate all unique pairs
# **Input:** [1, 2, 3, 4]
# **Output:** [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# l = [1, 2, 3, 4]
# res = []
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         pair = (l[i],l[j])
#         res.append(pair)
# print(res)