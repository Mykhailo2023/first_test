cars = ['mazda', 'lexus', 'bmw', 'tesla', 'kia']
new_list = []
# Creating for loop
for car in cars:
    # Creating if part to check if car == 'bmw'
    if car == 'bmw':
        # Adding element to the list
        new_list.append(car.upper())
    # Creating elif part to check elif car == 'kia'
    elif car == 'kia':
        # Adding element to the list
        new_list.append(car.upper())
   # Creating else part
    else:
        # Adding elements to the list
        new_list.append(car.title())
print(new_list)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# створення циклу for
for i in list_of_numbers:
    # написання умови if
    if i == 1:
        print(f'number{i} - {i}st')
    # написання першої умови elif
    elif i == 1:
        print(f'number{i} - {i}nd')
    # написання другої умови elif
    elif i == 3:
        print(f'number{i} - {i}rd')
    # написакння умови else
else:
        print(f'number{i} - {i}th')