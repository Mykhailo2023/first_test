'''
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(123456))


x = (1, 2, 3, 4, 5, 6)
for i in x:
    print(i % 10, end=" ")
   # print(i // 10)

a, _ , c, *_ = (1, 2, 3, 4, 5)
print(a)
#print(b)
print(c)

a = 1, 2
b = 3, 4, 5
packet = a, b
print(packet)

def create_user_profile(**kwargs):
    if not kwargs:
        return "No profile data provided."

    profile_parts = []
    for key, values in kwargs.items():
        profile_parts.append(f"{key.capitalize()}: {values}")
    
    return "\n".join(profile_parts)

profile = create_user_profile(name="Alice", age=30, occupation="Engineer")
print(profile)


temp_celsius = [0, 25, 30, 40, 100]

# Step 2: Create a custom function for conversion
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Step 3: Use map() with the custom function
temp_fahrenheit = map(celsius_to_fahrenheit, temp_celsius)

# Step 4: Convert the map object to a list and print
temp_fahrenheit_list = list(temp_fahrenheit)
print(temp_fahrenheit_list)

temp_celsius = [2, 22, 31, 45, 100]

# Step 2: Create a custom function for conversion
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Step 3: Use map() with the custom function
temp_fahrenheit = map(celsius_to_fahrenheit, temp_celsius)

# Step 4: Convert the map object to a list and print
temp_fahrenheit_list = list(temp_fahrenheit)
print(temp_fahrenheit_list)


def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result

input_data =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(input_data))
'''
a = int(input("Inpunt a: "))
match a:
    case a%2==0:
            print("Division on 2")
   