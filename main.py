"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

dt_sample1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(dt_sample1)
# dt_sample2 = datetime.datetime.strptime(sample2, '%H:%M %Y/%B/%d%')
# print(dt_sample2)
dt_sample3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(dt_sample3)
dt_sample4 = datetime.datetime.strptime(sample4, '%m.%d.%Y - %H:%M:%S')
print(dt_sample4)

# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('Yesterday = ', yesterday)
print('Today = ', today)
print('Tomorrow = ', tomorrow)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
some_day1 = datetime.datetime.fromtimestamp(some_day)
print(datetime.datetime.fromtimestamp(some_day))

# Write a function to subtract 2 weeks from timestamp and return new timestamp

days_14 = datetime.timedelta(days = 14)
print(some_day1 - days_14)
# input: timestamp (float)
# output: timestamp (float)