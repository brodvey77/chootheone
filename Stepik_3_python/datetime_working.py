# from datetime import date
#
# dates = [date(2000, 12, 31), date(1999, 3, 8), date(1999, 2, 22)]
#
# max_date = max(dates)
# min_date = min(dates)
#
# print(max_date.year + min_date.day)

# from datetime import date
#
# dates = [date(2023, 1, 1), date(2020, 7, 20), date(2021, 9, 17), date(2022, 6, 10)]
#
# print(*sorted(dates, key=lambda d: d.day), sep=', ')


# # импортируем тип date из модуля datetime
# from datetime import date
#
# # выводим текущую дату
# print(date.today())


# # импортируем тип date из модуля datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1992,8,24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())


# from datetime import date
# florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
#
# # счетчик для нужного количества ураганов
# early_hurricanes = 0
#
# # цикл по датам в которые был ураган
# for hurricane in florida_hurricane_dates:
#     # если месяц урагана меньше чем июнь (порядковый номер 6)
#     if hurricane.month < 6:
#         early_hurricanes += 1
#
# print(early_hurricanes)


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
#          date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
#          date(1666, 6, 6), date(1968, 5, 26)]
#
# for i in dates:
#     print(f'{i.year}-Q{(i.month+2)//3}')


# from datetime import date
#
# def get_min_max(d):
#     if len(d) > 0:
#         return min(d), max(d)
#     else:
#         return ()
#
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))
# print(get_min_max([]))



# from datetime import date
# def get_date_range(start, end):
#     c = date.toordinal(end) - date.toordinal(start)
#     l = []
#     for i in range(c + 1):
#         a = date.toordinal(start)
#         a += i
#         l.append(date.fromordinal(a))
#     return l
#
#
#
#
#
# date1 = date(2019, 6, 7)
# date2 = date(2019, 6, 5)
#
# print(get_date_range(date1, date2))
#
#
#
# def get_date_range(start, end):
#     return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

# from datetime import date
#
# def saturdays_between_two_dates(a, b):
#     if a > b:
#         a, b = b, a
#     l = [date.weekday(date.fromordinal(i)) for i in range(a.toordinal(), b.toordinal() + 1)]
#     return l.count(5)
#
#
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))

# from datetime import date
#
# my_date = date(2019, 2, 4)
#
# print(my_date)

# from datetime import time
#
# my_time = time(8, 20, 15)
#
# print(my_time)

# from datetime import date
#
# my_date = date(2021, 12, 31)
#
# print(my_date.strftime('%d %B %Y'))


# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))


# from datetime import date
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))


# from datetime import date
# # присваиваем самую раннюю дату урагана в переменную first_date
# first_date = date(2022, 12, 5)
#
# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
#
# print(iso)
# print(ru)
# print(us)


# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B(%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# n = 'python'
#
# try:
#     n = int(n)
#     print(n * 2)
# except ValueError:
#     print('Произошла ошибка')

# try:
#     names = ['Tim', 'Tom', 'Jerry', 'Alvin', 'Wall-e']
#     print(names[-5])
#     print(names[5])
# except:
#     print('IndexError')

# from datetime import date
#
# a, b = date.fromisoformat(input()), date.fromisoformat(input())
# print(min(a, b).strftime('%d-%m (%Y)'))

from datetime import date



# from datetime import date
# l = list(map(lambda x: x.strftime('%d/%m/%Y'),sorted([date.fromisoformat(input()) for i in range(int(input()))])))
# print(*l)


from datetime import date

# определяем функцию, печатающую красивую дату
# def print_good_dates(dates):
#     l = []
#     for i in dates:
#         if i.strftime('%Y') == '1992' and int(i.strftime('%d')) + int(i.strftime('%m')) == 29:
#             l.append(i)
#     s = sorted(l)
#     for i in s:
#         print(i.strftime('%B %d, %Y'))
#
#
# dates = []
# print_good_dates(dates)
#
#
# def print_good_dates(dates):
#     for d in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
#         print(d.strftime('%B %d, %Y'))

# from datetime import date
#
# def is_correct(d, m, y):
#     try:
#         if date(day=d, month=m, year=y):
#             return True
#     except:
#         return False
#
#
#
# def is_correct(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except:
#         return False


# print(is_correct(31, 13, 2021))


# from datetime import date
#
# def is_correct(year, month, day):
#     try:
#         date(int(year), int(month), int(day))
#         return True
#     except:
#         return False
#
#
# text = input()
# counter = 0
# while text != 'end':
#     day, month, year = text.split('.')
#     if is_correct(year, month, day):
#         print('Корректная')
#         counter += 1
#     else:
#         print('Некорректная')
#     text = input()
# print(counter)


# from datetime import datetime
#
# birthday = datetime(1992, 10, 6, 9, 48, 17)
#
# birthday.replace(year=9999, month=11)
#
# print(birthday)


# from datetime import datetime
#
# datetimes = [datetime(2022, 6, 11, 13, 26),
#              datetime(2000, 12, 31, 23, 59),
#              datetime(2077, 1, 1, 12),
#              datetime(2042, 7, 29)]
#
# print(min(datetimes, key=lambda dt: dt.hour))
# print(max(datetimes, key=lambda dt: dt.year))


# from datetime import date, time, datetime
#
# dt = datetime.combine(date(2022, 6, 10), time(13, 50, 59))
#
# print(dt.day + dt.second)


# from datetime import datetime
#
# text = 'Experiment Date 01/28/2005; Time 23::50::13'
#
# dt = datetime.strptime(text, 'Experiment Date %m/%d/%Y, Time %H:%M:%S')
#
# print(dt)

# from datetime import datetime
#
# text = 'Дорогой дневник, 11.02.2021 произошло нечто невероятное. На часах было 18:09..'
# pattern = 'Дорогой дневник, %d.%m.%Y произошло нечто невероятное. На часах было %H:%M..'
#
# dt = datetime.strptime(text, pattern)
#
# print(dt)

# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)



# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

# pm = 0
# am = 0
# for i in times_of_purchases:
#     a = i.time().strftime(('%H'))
#     if int(a) >= 12:
#         pm += 1
#     else:
#         am += 1
# if am > pm:
#     print('До полудня')
# else:
#     print('После полудня')


# for i in times_of_purchases:
#     print(i.strftime('%p'))

# dts = [d.strftime('%p') for d in times_of_purchases]
# print(['До полудня', 'После полудня'][dts.count('PM')>dts.count('AM')])

# from datetime import date, time, datetime
#
# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
#
# l = list(zip(dates, times))
#
# s = list(map(lambda x: datetime.combine(x[0], x[1]), l))
# a = sorted(s, key=lambda x: x.second)
# for i in a:
#     print(i)

# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# a = sorted(list(map(lambda x: datetime.combine(x[0], x[1]), list(zip(dates, times)))), key=lambda x: x.second)
# for i in a:
#     print(i)
#
#
# datetimes = [datetime.combine(d, t) for d, t in zip(dates, times)]
#
# print(*sorted(datetimes, key=lambda dt: dt.second), sep='\n')