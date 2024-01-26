# from datetime import datetime, timedelta

# users = [
#     {"name": "John Doe", "birthday": "2023.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.03.20"},
#     {"name": "Janet Smith", "birthday": "2003.01.24"}
# ]

# def sort_birthday(users):
#     for user in users:
#         user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#     #users.sort(key=lambda x: x["birthday"])
#     return users



# def check_weekend(date, week, next_week, last_birthday):
#     week = []
#     next1_week = []
#     last_birthday = []

#     today = datetime.now().date()
#     if date <= today + timedelta(days=7):  # Порівнюємо з сьогоднішньою датою та датою, яка є не далі як за 7 днів
#         week.append(date)
#         return 'Ця дата випадає на цьому тижні'
#     else:
#         days_passed = (today - date).days
#         last_birthday.append((date, days_passed))
#         return f'Ця дата вже пройшла. Пройшло {days_passed} днів з дня народження'
# list = check_weekend(users)    
#     print(week)
#     print(next1_week)
#     print(last_birthday)
    
# # print(list)
# def birthday_greetings(users):
#     greetings = []
#     today = datetime.now().date()
    
    
#     for user in users:
#         if user["birthday"] == today:
#             greetings.append(f'Вітаємо {user["name"]} з днем народження!')
#         elif user["birthday"] > today:
#             days_until_birthday = (user["birthday"] - today).days
#             greetings.append(f'{user["name"]} народиться через {days_until_birthday} дні(в)')
#         else:
#             next_birthday = user["birthday"].replace(year=today.year + 1)
#             days_until_birthday = (next_birthday - today).days
#             greetings.append(f'{user["name"]} народився {days_until_birthday} дні(в) тому. День народження вже відбувся.')
    
#     return greetings

# sorted_users = sort_birthday(users)
# # print(sorted_users)

# greetings = birthday_greetings(users)
# print("Привітання:")
# print(greetings)

# from datetime import datetime, timedelta

# from datetime import datetime, timedelta

# users = [
#     {"name": "John Doe", "birthday": "2023.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.03.20"},
#     {"name": "Janet Smith", "birthday": "2003.01.24"}
# ]

# def sort_birthday(users):
#     for user in users:
#         user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#     #users.sort(key=lambda x: x["birthday"])
#     return users

# def check_dates(dates, this_week, weekend, this_year):
#     today = datetime.now().date()
#     for date in dates:
#         if date <= today + timedelta(days=7) and date.weekday() < 5:
#             this_week.append(date)
#         elif date <= today + timedelta(days=7) and date.weekday() >= 5:
#             weekend.append(date)
#         elif date.year == today.year:
#             this_year.append(date)


# this_week = []
# weekend = []
# this_year = []

# check_dates(dates, this_week, weekend, this_year)

# # Вивід результатів
# print("Дати цього тижня, які не є вихідними:", this_week)
# print("Дати цього тижня, які є вихідними:", weekend)
# print("Дати цього року:", this_year)

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "2002.01.12"},
    {"name": "Jane Smith", "birthday": "1990.03.20"},
    {"name": "Janet Smith", "birthday": "2003.01.28"}
]

def sort_birthday(users):
    for user in users:
        user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    # users.sort(key=lambda x: x["birthday"])
    return users

def check_dates(dates, this_week, weekend, this_year):
    today = datetime.now().date()
    for date in dates:
        date_obj = datetime.strptime(date, "%Y.%m.%d").date()
        if date_obj <= today + timedelta(days=7) and date_obj.weekday() < 5:
            this_week.append(date_obj)
        elif date_obj <= today + timedelta(days=7) and date_obj.weekday() >= 5:
            weekend.append(date_obj)
        if date_obj.year == today.year:  # Перевірка, чи день народження вже пройшов у цьому році
            if (date_obj.month, date_obj.day) >= (today.month, today.day):
                this_year.append((date_obj, date_obj.strftime("%A")))

# Створення списку `dates` з днями народження користувачів

dates = [user["birthday"] for user in users]

this_week = []
weekend = []
this_year = []

# Виклик функції `check_dates` з визначеними змінними `dates`, `this_week`, `weekend` та `this_year`
check_dates(dates, this_week, weekend, this_year)

# Вивід результатів
print("Дати цього тижня, які не є вихідними:", this_week)
print("Дати цього тижня, які є вихідними:", weekend)
print("Дати цього року:", this_year)