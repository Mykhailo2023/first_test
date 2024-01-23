'''
import time
def sum_of_numbers(*args):
    total = sum(args)
    return total

numbers = []
while True:
    try:
        num = input("Введіть число (натисніть Enter для підтвердження, або = для виходу): ")
        if num.lower() == "=":
            break
        numbers.append(float(num))
        current_sum = sum_of_numbers(*numbers)
        print(f"Поточна сума: {round(current_sum, 2)}")
    except ValueError:
        print("Будь ласка, введіть коректне число!")

result = sum_of_numbers(*numbers)
print(f"Загальна сума: {round(result, 2)}")

time.sleep(10)

import tkinter as tk

def update_sum(event=None):
    try:
        num = float(entry.get())
        numbers.append(num)
        current_sum = sum(numbers)
        current_sum_label.config(text=f"Поточна сума: {round(current_sum, 2)}")
        entry.delete(0, tk.END)
    except ValueError:
        current_sum_label.config(text="Будь ласка, введіть коректне число!")

def show_final_sum():
    result = sum(numbers)
    final_sum_label.config(text=f"Загальна сума: {round(result, 2)}")

numbers = []

root = tk.Tk()
root.title("Суматор чисел")

entry = tk.Entry(root, width=10)
entry.pack(pady=30)
entry.bind("<Return>", update_sum)

update_button = tk.Button(root, text="Додати число", command=update_sum)
update_button.pack()

current_sum_label = tk.Label(root, text="Поточна сума: 0")
current_sum_label.pack(pady=10)

final_sum_label = tk.Label(root, text="")
final_sum_label.pack()

final_sum_button = tk.Button(root, text="Показати загальну суму", command=show_final_sum)
final_sum_button.pack(pady=10)


root.mainloop()
'''

import tkinter as tk

def update_sum(event=None):
    try:
        num = float(entry.get())
        numbers.append(num)
        current_sum = sum(numbers)
        current_sum_label.config(text=f"Поточна сума: {round(current_sum, 2)}")
        entry.delete(0, tk.END)
    except ValueError:
        current_sum_label.config(text="Будь ласка, введіть коректне число!")

def show_final_sum():
    result = sum(numbers)
    final_sum_label.config(text=f"Загальна сума: {round(result, 2)}")

def reset():
    numbers.clear()
    current_sum_label.config(text="Поточна сума: 0")
    final_sum_label.config(text="")

numbers = []

root = tk.Tk()
root.title("Суматор чисел")

entry = tk.Entry(root, width=10)
entry.pack(pady=50)
entry.bind("<Return>", update_sum)

update_button = tk.Button(root, text="Додати число", command=update_sum)
update_button.pack()

current_sum_label = tk.Label(root, text="Поточна сума: 0")
current_sum_label.pack(pady=10)

final_sum_label = tk.Label(root, text="")
final_sum_label.pack()

final_sum_button = tk.Button(root, text="Показати загальну суму", command=show_final_sum)
final_sum_button.pack(pady=10)

reset_button = tk.Button(root, text="Скинути результат", command=reset)
reset_button.pack(pady=10)

root.mainloop()