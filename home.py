a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

#print("1 - додати")
#print("2 - відняти")
#("3 - помножити")
#print("4 - поділити")

c = int(input("Що Ви хочете зробити? 1 - додати, 2 - відняти, 3 - помножити, 4 - поділити, 5 - поділити навпаки "))
if c == 1:
    print(f"Сума чисел {a} i {b} дорівнює {a + b}")
elif c == 2:
    print(f"Різниця чисел {a} i {b} дорівнює {a - b}")
elif c == 3:
    print(f"Добуток чисел {a} i {b} дорівнює {a * b}")
elif c == 5:
    print(f"Ділення чисел {b} на {a} дорівнює {b * a}")
else:
    print(f"Ділення чисел {a} на {b} дорівнює {a / b}")