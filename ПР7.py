# Выбор фигуры
print("Выберите фигуру для вычисления площади:")
print("1 - Квадрат")
print("2 - Прямоугольник")
print("3 - Круг")
print("4 - Треугольник")

choice = int(input("Введите номер фигуры: "))

if choice == 1:
    # Площадь квадрата
    side = float(input("Введите длину стороны квадрата: "))
    area = side ** 2
    print(f"Площадь квадрата: {area}")
elif choice == 2:
    # Площадь прямоугольника
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print(f"Площадь прямоугольника: {area}")
elif choice == 3:
    # Площадь круга
    radius = float(input("Введите радиус круга: "))
    area = 3.14159 * radius ** 2
    print(f"Площадь круга: {area}")
elif choice == 4:
    # Площадь треугольника (по основанию и высоте)
    base = float(input("Введите длину основания треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print(f"Площадь треугольника: {area}")
else:
    print("Ошибка: неверный номер фигуры.")

# Ввод трёх массивов
arrays = []
for i in range(1, 4):
    print(f"Введите элементы массива {i} (не более 15 чисел, через пробел):")
    arr = list(map(int, input().split()))
    if len(arr) > 15:
        print("Ошибка: массив содержит больше 15 элементов.")
        exit()
    arrays.append(arr)

# Обработка каждого массива
for i, array in enumerate(arrays, 1):
    total = sum(array)
    average = total / len(array) if len(array) > 0 else 0
    print(f"Массив {i}: {array}")
    print(f"Сумма элементов массива {i}: {total}")
    print(f"Среднее арифметическое массива {i}: {average}")
