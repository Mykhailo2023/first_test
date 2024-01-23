month = int(input("Vvedit chuslo: "))
# Creating the first if statement
if 3<= month <6:
    print('It is spring.')
# Creating the second if statement
if 6<= month <9:
    print('It is summer.')
# Creating the third if statement
if 9 <= month < 12:
    print('It is autumn.')
#Creating the fourth if statement
if  month == 1 or month == 2 or month == 12:
    print('It is winter.')


# Приклад речення
sentence = "List comprehension in Python is fun and powerful! power shell"

# Голосні, на які слід звернути увагу
vowels = 'aeiou'

# Використовуємо генератор списків з умовою 
capitalized_vowels = [char.upper() for char in sentence if char.lower() in vowels]

# Виведи список з голосними
print(capitalized_vowels)




# Initial data
countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154],
            ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417],
            ["India", 3166391, 1380004385]]

# Iterating over external list
for i in range(len(countries)):
    if type(countries[i]) is list:
        # Computing population density for a country
        pop_dens = round(countries[i][2]/countries[i][1], 2)
        print(countries[i][0], pop_dens, 'people per km²')



countries = [['USA', 9629091, 331002651], ['Canada', 9984670, 37742154], 
['Germany', 357114, 83783942], ['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]


# Iterate over list
for country in countries: 
  # Iterate over nested list
  for j in country:
    print(j, end = ' ')
  print('\n') # Print new line after nested loop finish




# Initial list
values = [1, [2, 3], 4, "code"]

# Initialize a for loop over indexes
for i in range(len(values)):
  print("Index:", i)
  print("Value:", values[i])
  print("----") # Delimiter




# Range with three arguments
for i in range(10, 30, 5):
  print(i, end = ' ')



values = [1, [2, 3], 4, "code"]

# Initialize a for loop
for el in values:
  print(el, end = ' ')



# Assign starting number (counter)
i = 1

# While loop will print all the numbers to 10
while i < 10: # Condition
  print(i, end = ' ') # Action
  i = i + 1 # Increasing variable


# Initial dictionary
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
            'Germany': (357114, 83783942)}

# Update dictionary with two countries
countries_dict["Brazil"] = (8515767, 212559417)
countries_dict["India"] = (3166391, 1380004385)
print(countries_dict)


countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
            'Germany': (357114, 83783942)}

# Information about Canada
print(countries_dict["Canada"])


def id_generator():
    count = 1
    while True:
        yield f"ID_{count}"
        count += 1

# Використання генератора для отримання унікальних ID
id_gen = id_generator()

# Отримання перших п'яти ідентифікаторів
for i in range(5):
    unique_id = next(id_gen)
    print(unique_id)

    def cat_name_generator():
    cat_names = ["Whiskers", "Fluffy", "Mittens", "Shadow", "Oliver"]
    for name in cat_names:
        yield name

# Крок 2: Створення екземпляра генератора
cat_name_gen = cat_name_generator()

# Крок 3: виклик next() для отримання імені
first_cat_name = next(cat_name_gen)
print(first_cat_name)

## Крок 4: виклик next() для отримання другого імені
second_cat_name = next(cat_name_gen)
print(second_cat_name)


def traffic_light_generator():
    while True:
        yield "Red"
        yield "Yellow"
        yield "Green"

# Використання генератора для імітації роботи світлофора
traffic_light = traffic_light_generator()

# Друк станів світлофора за кілька циклів
for _ in range(9):
    print(next(traffic_light))



def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
      
print(sum_of_digits(123456))

# Create tuple
#people = (('Alex', 23, 178), ('Noah', 34, 189), ('Peter', 29, 175),
#('John', 41, 185), ('Michelle', 35, 165))

# Information about Peter
#print(people[2])
# Height of John
#print(people[3][2])
# Age of Alex
#print(people[0][1])


#two_d_countries = (('USA', 9629091, 331002651), ('Canada', 9984670, 37742154), 
#                   ('Germany', 357114, 83783942), ('Brazil', 8515767, 212559417), 
#                   ('India', 3166391, 1380004385))
#
# Get information about India
#print(two_d_countries[4])
# Get the area of India
#print(two_d_countries[4][1])


# Initial tuple
#US_Info = ("USA", 9629091, 331002651)
# New data
#US_Info_new = ("Washington D.C.", 50)
# Concatenate two tuples and save the result
#US_Info_upd = US_Info + US_Info_new
#print(US_Info_upd)

# Create a list 
#list_variable = [1, 2, 3]
# Convert it into a tuple
#tuple_variable = tuple(list_variable)
# Print the type of the converted variable
#print(type(tuple_variable))

# Two-dimensional list
#countries_2d = [['USA', 9629091], ['Canada', 9984670], ['Germany', 357114]]

# Pull elements
#print(countries_2d[0])
#print(countries_2d[2][0])


#{revenue = 2000

#Check if revenue is less than 2000
#if revenue < 2000:
#  print("We're operating at a loss!")
#else:
#  print("Everything is good!")
#
# if len(test) > 20:
#    print("String: '", test, "' is large")
#elif len(test) > 10:
#    print("String: '", test, "' is medium")
#else:
#    print("String: '", test, "' is small")


#US_Info = ["USA", 9629091, 331002651]
#US_Info_new = ["Washington D.C.", 50]

# Add new data using concatenation
#print(US_Info + US_Info_new)

# Add new data using list method
#US_Info.extend(US_Info_new)
#print(US_Info)}##'''