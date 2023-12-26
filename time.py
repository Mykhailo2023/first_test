n = int(input("Введіть кількість секунд:"))


hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60
print("З", n, "секунд буде:")
print(hours, "годин")
print(minutes, "хвилин")
print(seconds, "Секунд")
print("👌")