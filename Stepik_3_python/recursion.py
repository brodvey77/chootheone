# def message():
#     print('Это рекурсивная функция')
#     message()
#
# message()

# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#
# bee(3)

# def bee(n):
#     if n > 0:
#         bee(n - 1)
#         print(n)
#
# bee(3)

# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#         print(n)
#
# bee(2)


# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#     print(n)
#
# bee(2)


# def bee(n):
#     print(n)
#     if n > 0:
#         print(n)
#         bee(n - 1)
#
# bee(2)

# def beegeek(n):
#     if n > 0:
#         print('bee')
#         beegeek(n - 1)
#     else:
#         print('geek')
#
# beegeek(3)


# def bee(n):
#     if n >= 777:
#         print('bee')
#     else:
#         bee(n + 1)
#
# bee(666)


# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         print(n)
#         bee(n + 1)
#
#
# bee(4)

# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         bee(n + 1)
#         print(n)
#
#
# bee(4)

# def draw_rect(width, height, step):
#     if step < height:
#         print('*' * width)
#         draw_rect(width, height, step + 1)
#
# draw_rect(4, 3, 0)
# print()
# draw_rect(6, 6, 0)
# print()
# draw_rect(10, 2, 0)

# def draw_rect(width, height, step=0):
#     if step < height:
#         print('*' * width)
#         draw_rect(width, height, step + 1)

# def draw_rect(width, height):
#     def rec(step):
#         if step < height:
#             print('*' * width)
#             rec(step + 1)
#     rec(0)

# def bee(n):
#     if n < 5:
#         bee(n + 1)
#     else:
#         print(n)
#
# bee(0)


# def traffic(n):
#     while n > 0:
#         print('Не парковаться')
#         n -= 1


# def traffic(n):
#     if n > 0:
#         print('Не парковаться')
#         traffic(n - 1)


def number_arr():
    def num(number):
        if number < 101:
            print(number)
            num(number + 1)

    num(1)


number_arr()