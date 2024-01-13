'''
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
                  'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
                  'India': (3166391, 1380004385)}

# Defining a function
def country_information(d, name):
  print('Country:', name)
  print('Area:', d[name][0], 'sq km')
  print('Population:', round(d[name][1]/1000000, 2), 'MM')

# Testing the function
country_information(countries_dict, 'Brazil')
country_information(countries_dict, 'Germany')



'''

# Define a function
def is_odd(n):
  if n % 2 == 0:
    return "even"
  else:
    return "odd"

# Testing function
print('5 is', is_odd(5))
print('3 is', is_odd(3))
'''
def organize_books_on_shelf(**kwargs):
    # Порожній словник для представлення книжкової полиці
    bookshelf = {}
    # Перегляньте кожну пару "назва - жанр" у наданому словнику kwargs
    for title, genre in kwargs.items():
        # Перевірте, чи жанр уже існує на книжковій полиці
        if genre not in bookshelf:
            # If the genre doesn't exist, add it as a key with an empty list
            bookshelf[genre] = []
        # Додайте назву книги до списку відповідного жанру на книжковій полиці
        bookshelf[genre].append(title)
    # Створіть повідомлення про розташування книг на книжковій полиці
    message = "Books placed on the bookshelf:\n"
    for genre, books_in_genre in bookshelf.items():
        message += f"{genre}: {', '.join(books_in_genre)}\n"
    # Повернути повідомлення як результат функції
    return message
# Приклад використання функції
result = organize_books_on_shelf(
    Book1="Science Fiction",
    Book2="Mystery",
    Book3="Science Fiction",
    Book4="Adventure",
    Book5="Mystery"
)

print(result)


def calculate_taxi_cost(driver_name, has_discount=False, **kwargs):
# Видобути значення з kwargs
  client_name = kwargs['client_name']
  trip_time = kwargs['trip_time']
  petrol_cost = kwargs['petrol_cost']

# Розрахувати базовий тариф
  base_fare = trip_time * 10

# Застосувати знижку, якщо це можливо
  if has_discount:
    base_fare *= 0.9

# Розрахувати загальну вартість
  total_cost = base_fare + petrol_cost
  print(f'Total cost for {driver_name} is {total_cost}')

# Приклади виклику функції
calculate_taxi_cost('John', has_discount=True, client_name='Alice', trip_time=30, petrol_cost=20)
calculate_taxi_cost('Alex', client_name='Max', trip_time=10, petrol_cost=30)

'''