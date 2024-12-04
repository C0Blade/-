a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
result = [x for x in (a, b, c) if 1 <= x <= 3]
print("Числа из интервала [1, 3]:", result)

number = int(input("Введите двузначное число: "))

if 10 <= number <= 99:  # Проверка на двузначность
    if str(number)[0] == str(number)[1]:
        print("Да")
    else:
        print("Нет")
else:
    print("Ошибка: введите двузначное число.")

    a, b = map(int, input("Введите два числа a и b через пробел: ").split())

    if a < b:
        x = a + b
    elif a > b:
        x = a - b
    else:
        x = 1

    print("Значение x:", x)

    a, b = map(int, input("Введите два числа через пробел: ").split())

    if a > b:
        print("Наибольшее число:", a)
    elif b > a:
        print("Наибольшее число:", b)
    else:
        print("Числа равны.")