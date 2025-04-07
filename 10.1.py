# Вариант 14
# 1 Задана квадратная матрица. Переставить строку с максимальным
# элементом на главной диагонали со строкой с заданным номером m.

from random import randint

m = 3
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()

with open ("Зинченко_Кирилл_Русланович_УБ42_vvod1.txt", "w") as vvod:
    a = vvod.write(str(l))
with open ("Зинченко_Кирилл_Русланович_УБ42_vvod1.txt", "r") as vvod:
    print(vvod.read())
    print()

ll = []
for i in range(len(l)):
    ll.append(l[i][i])
maxid = ll.index(max(ll))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')
print()

with open ("Зинченко_Кирилл_Русланович_УБ42_vivod1.txt", "w") as vivod:
    a = vivod.write(str(l))
with open ("Зинченко_Кирилл_Русланович_УБ42_vivod1.txt", "r") as vivod:
    print(vivod.read())
