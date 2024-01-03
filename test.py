
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
#print(US_Info)}##