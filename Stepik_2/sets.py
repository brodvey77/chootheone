import math
#
# x = 36
# y = 4
#
# a = math.sqrt(x / y)
# b = math.sqrt(x * y)
# c = math.sqrt(x - y)
# d = math.sqrt(x + y)
#
# print(a)
# print(b)
# print(c)
# print(d)

# c = int(input())
# b = int(input())
#
# a = math.sqrt(c**2 - b**2)
#
# print(a)


# n, m, k, x, y, z = 25, 20, 7, 8, 3, 10
#
# clear_n = n - x
# clear_m = m - x - y
# clear_k = k - y
# al = clear_n + x + clear_m + y + clear_k + z
#
# print(al)

# n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
#
# n_m = n + m - x
# m_k = m + k - y
# k_n = k + n - z
# only_n = n - (n_m - t) - (k_n - t) - t
# only_m = m - (n_m - t) - (m_k - t) - t
# only_k = k - (k_n - t) - (m_k - t) - t
# only_one = only_k + only_n + only_m
# only_two = (n_m - t) + (m_k - t) + (k_n - t)
# not_read = a - (only_one + (n_m -t) + (m_k - t) + (k_n - t) + t)
# print(only_one, only_two, not_read, sep='\n')

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# fruits_sorted = sorted(fruits, reverse=True)
# print(*fruits_sorted, sep='\n')

# print(len(set(input())))

# numbers = input()
# if len(numbers) == len(set(numbers)):
#     print('YES')
# else:
#     print('NO')

# s1 = input()
# s2 = input()
# s3 = s1 + s2
# if len(set(s3)) != 10:
#     print('NO')
# else:
#     print('YES')

# numbers = set(input() + input())
# print('YES' if len(numbers) == 10 else 'NO')


# a = input()
# b = input()
#
# if set(a) == set(b):
#     print('YES')
# else:
#     print("NO")

# print('YES' if set(input()) == set(input()) else 'NO')

# text = input().split()
# if set(text[0]) == set(text[1]) == set(text[2]):
#     print('YES')
# else:
#     print("NO")

# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(myset)
# print(len(myset))

# n = int(input())
# my_list = []
#
# for i in range(n):
#     my_list.append(input().lower())
#
# for i in my_list:
#     print(len(set(i)))

# for _ in range(int(input())):
#     print(len(set(input().lower())))


