'''
def check_triangle(side_1, side_2, side_3):
# Використали індентацію, для створення тіла функції
# Перевірили чи можуть аргументи бути сторонами трикутника
    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        print('The sides of the triangle must be positive values.')
        return 0

    if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
        perimeter = side_1 + side_2 + side_3
        return perimeter
    else:
        print('The given sides cannot form a triangle.')
        return 0


print(check_triangle(-1, 1, 1))
print(check_triangle(2, 2, 7))
print(check_triangle(3, 4, 5))


def calculate_interest(principal, rate, years):
    # Перевірте типи вхідних даних: перевірте, чи тип вхідних даних належить значенням у кортежі
    if type(principal) not in (int, float):
        print('Principal amount must be a number.')
        return 0
    
    if type(rate) not in (int, float):
        print('Interest rate must be a number.')
        return 0
    
    if type(years) is not int:
        print('Number of years must be an integer.')
        return 0
    
    # Розрахуйте складні відсотки за допомогою вбудованих функцій
    amount = principal * (1 + rate/100) ** years
    interest = amount - principal
    
    # Округліть відсотки до двох знаків після коми за допомогою вбудованої функції round().
    interest = round(interest, 2)
    
    # Повернути нараховані відсотки
    return interest


  
print(calculate_interest(2000, '5', 3))
print(calculate_interest(2000, 5, 1))


def calculate_total_cost(price, quantity, discount=0, tax_rate=0):

    discounted_price = price - (price * discount)
    subtotal = discounted_price * quantity
    total_cost = subtotal + (subtotal * tax_rate)
    return total_cost
  
# Розрахувати загальну вартість без урахування знижки та з урахуванням ставки податку 0,15
cost1 = calculate_total_cost(10, 5, tax_rate=0.15)
print(f'The first cost is {cost1}')

# Розрахуйте загальну вартість із знижкою 20% і ставкою податку за замовчуванням
cost2 = calculate_total_cost(10, 5, discount=0.2)
print(f'The second cost is {cost2}') 

def calculate_average(*args):
  len_args = len(args)
  if len_args == 0:
     return 0
  total = sum(args)
  print(total)
  average = total / len_args
  return average

# Приклад використання
print(calculate_average(10, 20, 30, 40, 50))
print(calculate_average(5))
print(calculate_average())

def process_data(name, *args, verbose=False):
  print(f'Processing data for {name}')
    
# Виконайте деякі обчислення над довільними аргументами
  total = sum(args)
  if len(args) == 0:
    average=0

  else:
    average = total / len(args)
    
  if verbose:
    print(f'Data: {args}')
    print(f'Total: {total}')
    print(f'Average: {average}')
  print(f'Data for {name} was processed with result {average}\n')

process_data('Jane', 5, 7, 9, True)


def merge_string_lists(*args):
    merged_string = ''

# Ітерувати всі рядки в args
    for string_list in args:
        merged_string += ' '.join(string_list) + ' '

# Повернути результуючий рядок
    return merged_string

# Приклад використання
list1 = ['Hello,', 'world!']
list2 = ['I', 'am', 'Python!']
list3 = ['Nice', 'to', 'meet', 'you!']
result = merge_string_lists(list1, list2, list3)
print(result)



def calculate_statistics(numbers):
    if len(numbers) == 0:
        return 0, 0, 0, 0
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum

# Приклад використання
data = [12, 7, 15, 9, 22, 13, 18]
total, average, minimum, maximum = calculate_statistics(data)

print(f'Total Sum: {total}')
print(f'Average: {round(average, 2)}')
print(f'Minimum Value: {minimum}')
print(f'Maximum Value: {maximum}')


def greet(name):
    print(f'Hello, {name}!')

result = greet('Alice')
print(result)

'''

