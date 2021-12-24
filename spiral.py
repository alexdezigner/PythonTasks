''' Выведите таблицу размером n x n, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла
  и закрученной по часовой стрелке во внутрь '''

matrix = []
x = 0
y = 0
storona = 'right'
n = int(input('Введите число:'))
step0 = n - 1
step = step0
povtor = 2
for j in range(n):
    matrix.append([])
    for i in range(n):
        matrix[j].append(0)
for i in range(1, (n**2)+1):
    matrix[y][x] = i
    # проверка направления и шагов
    if step == 0:
        if storona == 'right':
            storona = 'down'
        elif storona == 'down':
            storona = 'left'
        elif storona == 'left':
            storona = 'up'
        else:
            storona = 'right'
        if povtor == 0:
            povtor = 1
            step0 = step0 - 1
        else:
            povtor = povtor - 1
        # нужно восстановить step (строка_32), при этом отслеживать уменьшения step на 1 после 2ух ходов (строка_28)
        step = step0
    if storona == 'right':
        x = x + 1
    elif storona == 'left':
        x = x - 1
    elif storona == 'up':
        y = y - 1
    else:
        y = y + 1
    step = step - 1
# печатаем список (построчно, поэлементно)
for elem in matrix:
    print(*elem, end='\n')
