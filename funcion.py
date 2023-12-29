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





# Define a function
def is_odd(n):
  if n % 2 == 0:
    return "even"
  else:
    return "odd"

# Testing function
print('2 is', is_odd(2))
print('3 is', is_odd(3))