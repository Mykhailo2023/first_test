# Завдання № 1
import datetime

def get_days_from_today(date_str):
    current_date = datetime.datetime.now()
    try:
        input_date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
        days_difference = (current_date - input_date).days
        return days_difference
    except ValueError:
        print('Введіть у правильному форматі дд.мм.рррр')

days_difference = get_days_from_today("15.12.2015")

print(f'Кількість днів з введеної дати: {days_difference}')

# Завдання № 2

import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
# поки довжина списку менша quantity
    while len(numbers) < quantity: 
        number = random.randint(min, max)
        if number not in numbers: 
# перевіряємо чи є номер в списку
            numbers.append(number)
    return numbers

ticket_numbers = get_numbers_ticket(1, 49, 6)
print(ticket_numbers)


# Завдання № 3


import re

def normalize_phone_numbers(numbers):
    pattern = r"[^0-9\+]" ## можна зробити [a-z\s\();\\,\-:!\.] 
    replacement = ""
    #видаляємо все лишнє
    modified_numbers = [re.sub(pattern, replacement, number) for number in numbers]
    # додаємо + або +38
    updated_numbers = [number if number.startswith("+") else "+38" + number[1:] for number in modified_numbers]
    return updated_numbers

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

normal_numbers = normalize_phone_numbers(raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", normal_numbers)

# Завдання № 4



