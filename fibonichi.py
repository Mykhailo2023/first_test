'''n = int(input("Введіть ціле число:"))
def fibonacci(n):


    if n <= 1: # базовий випадок
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок
        print("Повернення результату для n = ", n, ": ", result)
        return result
print(fibonacci(n))

#print(fibonacci(n)) # виведе 55'''

def greeting():
        print('Hello world!')

greeting()