previous_number = 1
n = 64  # Кількість разів
for _ in range(n):
    next_number = previous_number * 2
    print(next_number, end = ' ')
    previous_number = next_number
