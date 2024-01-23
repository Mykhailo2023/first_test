# import random

# def get_numbers_ticket(min, max, quantity):
#     list = []
#     while len(list) < quantity:
#         i = random.randint(min, max)
#     print(list)
# get_numbers_ticket(1, 49, 6)


# import random

# def get_numbers_ticket(min, max, quantity):
#     numbers = []
#     while len(numbers) < quantity:
#         number = random.randint(min, max)
#         if number not in numbers:
#             numbers.append(number)
#     return numbers

# ticket_numbers = get_numbers_ticket(1, 49, 6)
# print(ticket_numbers)

# import datetime

# #def get_days_from_today(time_old, ):
# i = datetime.datetime.now()
# try:
#     time_old = str(input('Введіть дату у форматі дд.мм.рррр: '))
# except ValueError:
#     time_old = str(input('Введіть у правильному форматі дд.мм.рррр: '))  


# datatime_time_old = datetime.datetime.strptime(time_old, '%d.%m.%Y')
# day = i - datatime_time_old

# #day_print = day.strftime(%d)
# #year = i.strftime("%Y")
# # data = i.strftime("%d")
# print(day)#_print)
# print(datatime_time_old)
# print(i)
# #print("year = ", year)
# # print("day = ", data)

# import datetime

# def get_days_from_today(date_str):
#     current_date = datetime.datetime.now()
#     try:
#         input_date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
#         days_difference = (current_date - input_date).days
#         return days_difference
#     except ValueError:
#         print('Введіть у правильному форматі дд.мм.рррр')

# days_difference = get_days_from_today("5.12.2025")

#print(f'Кількість днів з введеної дати: {days_difference}')

import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
pattern = r"[^0-9\+]" # можна зробити [a-z\s\();\\,\-:!\.] 
replacement = ""
modified_numbers = [re.sub(pattern, replacement, number) for number in raw_numbers]
#print(type(modified_numbers))
print("Очищені номери: ", modified_numbers)
#updated_numbers = ["+38" + number[1:] if len(number) == 10 else "+" + number for number in modified_numbers]
updated_numbers = [number if number.startswith("+") else "+38" + number[1:] for number in modified_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", updated_numbers)
# for number in modified_numbers:
#     if len(number) < 11:
#         print(f'+38{number}')
#     elif len(number) < 13:
#         print(f'+{number}')
#     else:
#         print(number)
#updated_numbers = ["+38" + number[1:] if len(number) == 10 else number for number in numbers]

print(updated_numbers)