a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть друге число: "))
d1 = int(b ** 2 - (4 * a * c))
d = int(d1 ** 0.5)
b1 = b * (-1)
x1 = (b1 - d)/(2 * a)
x2 = (b1 + d)/(2 * a)
print(f"Дискримінант =", d)
print(b1)
print(x1)
print(x2)
if x1 < 0:
    print("Розвязків немає")
else:
    print(f"x1 = {x1 ** 0.5}")
if x2 < 0:
    print("Розвязків немає")
else:
    print(f"x2 =  -{x2 ** 0.5} i {x2 ** 0.5}")

