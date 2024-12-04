# Ввод размера матрицы
n = int(input("Введите размер матрицы N: "))

# Ввод матрицы
print("Введите элементы матрицы построчно через пробел:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("Ошибка: длина строки не равна N.")
        exit()
    matrix.append(row)

# Вычисление суммы и количества положительных элементов над главной диагональю
positive_sum = 0
positive_count = 0

for i in range(n):
    for j in range(i + 1, n):  # Только элементы над главной диагональю
        if matrix[i][j] > 0:
            positive_sum += matrix[i][j]
            positive_count += 1

# Вывод результата
print("Сумма положительных элементов над главной диагональю:", positive_sum)
print("Количество положительных элементов над главной диагональю:", positive_count)

# Ввод размеров матрицы
n, m = map(int, input("Введите размеры матрицы N и M через пробел: ").split())

# Ввод матрицы
print("Введите элементы матрицы построчно через пробел:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != m:
        print("Ошибка: длина строки не равна M.")
        exit()
    matrix.append(row)

# Обработка строк матрицы
for i in range(n):
    # Поиск максимального и минимального элементов
    max_index = row.index(max(matrix[i]))
    min_index = row.index(min(matrix[i]))

    # Замена максимального элемента с первым
    matrix[i][0], matrix[i][max_index] = matrix[i][max_index], matrix[i][0]

    # Замена минимального элемента с последним
    matrix[i][-1], matrix[i][min_index] = matrix[i][min_index], matrix[i][-1]

# Вывод обработанной матрицы
print("Матрица после замены:")
for row in matrix:
    print(*row)
