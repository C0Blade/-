# Ввод двух чисел
a, b = map(int, input("Введите два числа A и B (A ≤ B), через пробел: ").split())

# Проверяем условие A ≤ B
if a <= b:
    # Вывод всех чисел от A до B включительно
    for number in range(a, b + 1):
        print(number, end=' ')
else:
    print("Ошибка: условие A ≤ B не выполнено.")