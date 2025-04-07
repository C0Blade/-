# 2 Составить программу, которая заполняет квадратную матрицу порядка
# п натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по спирали».
# Например, для п = 5 получаем следующую матрицу:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 14 12 11 10 9

def spiral_fill(n):
    # Создаем пустую матрицу n x n
    matrix = [[0] * n for _ in range(n)]

    # Определяем границы
    left, right = 0, n - 1
    top, bottom = 0, n - 1

    num = 1  # Начальное число для заполнения

    while left <= right and top <= bottom:
        # Заполняем верхнюю строку
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Заполняем правый столбец
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Заполняем нижнюю строку, если еще есть строки для заполнения
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Заполняем левый столбец, если еще есть столбцы для заполнения
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


# Пример использования
n = int(input("Введите число строк и столбцов в матрице: "))
spiral_matrix = spiral_fill(n)
print_matrix(spiral_matrix)

with open ("Зинченко_Кирилл_Русланович_УБ42_vvod2.txt", "w") as vvod:
    a = vvod.write(str(n))
with open ("Зинченко_Кирилл_Русланович_УБ42_vvod2.txt", "r") as rewrite1:
    print(rewrite1.read())

with open ("Зинченко_Кирилл_Русланович_УБ42_vivod2.txt", "w") as vivod:
    b = vivod.write(str(spiral_matrix))
with open ("Зинченко_Кирилл_Русланович_УБ42_vivod2.txt", "r") as rewrite2:
    print(rewrite2.read())