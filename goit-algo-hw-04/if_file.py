# from pathlib import Path

# # Створення об'єкту Path для директорії
# directory = Path("./test")

# # Виведення переліку всіх файлів та піддиректорій
# for path in directory.iterdir():
#     print(path)
from pathlib import Path

path = Path("./test")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")