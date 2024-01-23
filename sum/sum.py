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
    final_sum_label.config(text=f"Загальна сума: {result}")

def reset():
    numbers.clear()
    current_sum_label.config(text="Поточна сума: 0")
    final_sum_label.config(text="")

def save_to_memory():
    global memory
    memory = sum(numbers)
    memory_label.config(text=f"Збережено в пам'яті: {memory}")

def retrieve_from_memory():
    if 'memory' in globals():
        numbers.append(memory)
        current_sum = sum(numbers)
        current_sum_label.config(text=f"Поточна сума: {round(current_sum, 2)}")
    else:
        memory_label.config(text="Пам'ять порожня")

numbers = []

root = tk.Tk()
root.title("Суматор чисел")
root.geometry("400x350")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
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

save_button = tk.Button(root, text="Запам'ятати", command=save_to_memory)
save_button.pack(pady=10)

retrieve_button = tk.Button(root, text="Витягнути з пам'яті", command=retrieve_from_memory)
retrieve_button.pack(pady=10)

memory_label = tk.Label(root, text="")
memory_label.pack()

root.mainloop()