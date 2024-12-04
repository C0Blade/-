# Рекурсивная функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Рекурсивная функция для вычисления x^n
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# Ввод данных
x = int(input("Введите натуральное число X: "))
n = int(input("Введите натуральное число N: "))

# Вычисление результата
result = power(x, n) / factorial(n)

# Вывод результата
print(f"Результат: {result}")

# Рекурсивная функция для нахождения максимального числа
def find_max():
    number = int(input())
    if number == 0:
        return 0
    return max(number, find_max())

# Ввод последовательности и вычисление результата
print("Введите последовательность чисел (завершается числом 0):")
maximum = find_max()

# Вывод результата
print(f"Наибольшее значение в последовательности: {maximum}")