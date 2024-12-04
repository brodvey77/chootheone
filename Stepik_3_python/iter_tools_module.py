# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)
#
# import itertools as it
# import time
#
# dicso = ['🟥', '🟥', '🟧', '🟧', '🟨', '🟨', '🟧', '🟧',
#          '🟥', '🟥', '🟧', '🟧', '🟨', '🟨', '🟧', '🟧',
#          '🟩', '🟩', '🟦', '🟦', '🟪', '🟪', '🟦', '🟦',
#          '🟩', '🟩', '🟦', '🟦', '🟪', '🟪', '🟦', '🟦',]
#
# dance = ['__(ツ)__', '\_(ツ)__', '¯\(ツ)__', '¯¯(ツ)__', '/¯(ツ)\_',
#          '_/(ツ)¯\\', '__(ツ)¯¯', '__(ツ)/¯', '__(ツ)_/', '__(ツ)__',
#          '__(ツ)__', '__(ツ)_/', '__(ツ)/¯', '__(ツ)¯¯', '_/(ツ)¯\\',
#          '/¯(ツ)\_', '¯¯(ツ)__', '¯\(ツ)__', '\_(ツ)__', '__(ツ)__',]
#
# for light, move in zip(it.cycle(dicso), it.cycle(dance)):
#     print(f'{light} {move} {light}', end='\r')
#     time.sleep(0.075)
#
# #
# from itertools import cycle
#
# cycler = cycle('17')
#
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# from itertools import repeat
#
# repeater = repeat(['bee', 'ff'])
#
# for _ in range(100):
#     next(repeater)
#
# print(next(repeater))
# print(next(repeater))

# from itertools import repeat
#
# repeater = repeat('geek', 4)
#
# print(list(repeater))

#
# from itertools import repeat
#
# beegeek = ['bee', 'geek']
# repeater = repeat(beegeek)
#
# print(next(repeater))
#
# beegeek = beegeek + ['imposter']
#
# print(next(repeater))


# import itertools as it
# def tabulate(func):
#     return (func(i) for i in it.count(1))
#
#
# from itertools import count
#
# def tabulate(func):
#     return map(func, count(1))
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# func = lambda x: x
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
#
# # TEST_2:
# func = lambda x: x + 10
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
# print(next(values))
#
# # TEST_3:
# func = lambda x: x ** 2
# values = tabulate(func)
#
# for _ in range(100):
#     print(next(values))
#
# # TEST_4:
# def func(n):
#     return 'beegeek' * n
#
# values = tabulate(func)
#
# for _ in range(10):
#     print(next(values))


# from itertools import accumulate, count
# from operator import mul
#
# def fuck(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * factorials(x - 1)
#
#
# def factorials(n):
#     return accumulate(range(1, n + 1), mul)
#
# from itertools import accumulate
#
# def factorials(n):
#     yield from accumulate(range(1, n + 1), lambda x, y: x * y)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# numbers = factorials(6)
#
# print(*numbers)
#
# # TEST_2:
# numbers = factorials(2)
#
# print(next(numbers))
# print(next(numbers))
#
# # TEST_3:
# numbers = factorials(100)
#
# print(*numbers)
#
# # TEST_4:
# numbers = factorials(1001)
#
# for _ in range(1000):
#     next(numbers)
#
# print(next(numbers))
# from itertools import cycle
# import string
#
# def alnum_sequence():
#     digits = (num for num in range(1, 27))
#     letters = map(lambda x: x, string.ascii_uppercase)
#     return cycle(j for i in zip(digits, letters) for j in i)
#
# from itertools import cycle
# from string import ascii_uppercase
#
#
# def alnum_sequence():
#     for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
#         yield from item
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(55)))
#
# # TEST_2:
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(100)))
#
# # TEST_3:
# alnum = alnum_sequence()
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
#
# # TEST_4:
# alnum = alnum_sequence()
#
# for _ in range(10_000):
#     next(alnum)
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
#
# # TEST_5:
# alnum = alnum_sequence()
#
# for _ in range(100_000):
#     next(alnum)
#
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))
# print(next(alnum))

# import itertools
#
# def roundrobin(*args):
#     a = itertools.zip_longest(*args, fillvalue='')
#     return (j for i in a for j in i if j != '')
#
# def roundrobin(*args):
#     iters = tuple(iter(a) for a in args)
#     while True:
#         err_counter = 0
#         for i in iters:
#             try: res = next(i)
#             except: err_counter += 1
#             else: yield res
#         if err_counter == len(iters):
#             break


# # INPUT DATA:
#
# # TEST_1:
# print(*roundrobin('abc', 'd', 'ef'))
#
# # TEST_2:
# numbers = [1, 2, 3]
# letters = iter('beegeek')
#
# print(*roundrobin(numbers, letters))
#
# # TEST_3:
# print(list(roundrobin()))
#
# # TEST_4:
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = range(5)
# letters = iter('beegeek')
#
# print(*roundrobin(numbers1, numbers2, letters))
#
# # TEST_5:
# letters = iter('stepik')
#
# print(*roundrobin(letters))
#
# # TEST_6:
# numbers = roundrobin(map(abs, range(-10, 10)))
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
#
# # TEST_7:
# numbers1 = map(abs, range(-10, 10))
# numbers2 = filter(None, range(-10, 10))
# numbers3 = map(abs, range(-5, 5))
# numbers4 = filter(None, range(-5, 5))
# numbers5 = map(abs, range(-1, 1))
# numbers6 = filter(None, range(-1, 1))
#
# print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))
#
# # TEST_8:
# print(list(roundrobin([], [], [], [])))
#
# # TEST_9:
# numbers = iter([1, 2, 3])
# nones = iter([None, None, None, None])
#
# print(*roundrobin(numbers, nones))


# from itertools import islice
#
# print(*islice('hello world!', None))


# from itertools import count
# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# for i in count():
#     print(factorial(i))


# from itertools import dropwhile
#
#
# def drop_while_negative(iterable):
#     return dropwhile(lambda x: x >= 0, iterable)