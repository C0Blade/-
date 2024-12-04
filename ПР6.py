# Ввод массива
n = int(input("Введите количество элементов массива N: "))
array = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()))

if len(array) != n:
    print("Ошибка: количество введенных элементов не совпадает с N.")
else:
    # Нахождение максимального элемента
    max_element = max(array)
    print("Максимальный элемент массива:", max_element)

    # Вывод массива в обратном порядке
    print("Массив в обратном порядке:", array[::-1])

    # Ввод массива
    array = list(map(float, input("Введите массив действительных чисел через пробел: ").split()))

    if len(array) == 0:
        print("Ошибка: массив пуст.")
    else:
        # Нахождение среднего арифметического
        average = sum(array) / len(array)

        # Замена нулевых элементов
        updated_array = [average if x == 0 else x for x in array]

        # Вывод результата
        print("Массив после замены нулевых элементов:", updated_array)