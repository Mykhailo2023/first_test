def draw_pyramid(height, current_height=1):
    if current_height > height:
        return  # Базовий випадок: вихід, коли досягнуто висоти піраміди
    # Рекурсивний випадок: надрукувати рядок для поточної висоти
    spaces = ' ' * (height - current_height)  # Пробіли для вирівнювання
    stars = '^' * (2 * current_height - 1)  # Зірочки для поточного рядка
    print(spaces + stars)

    # Рекурсивний виклик для наступного рядка
    draw_pyramid(height, current_height + 1)

# Виклик функції
draw_pyramid(6)


# Створення лямбда-функції, яка додає два числа
add = lambda x, y: x + y

# Виклик лямбда-функції
result = add(3, 5)
print(result)  