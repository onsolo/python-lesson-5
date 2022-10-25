table = [['', '', ''], ['', '', ''], ['', '', '']]


def PrintTable():
    for row in table:
        print(row, end='\n')


def SetValue(sign):
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбика: '))
    if row < 4 and column < 4:
        if table[row - 1][column - 1] == '':
            table[row - 1][column - 1] = sign
        else:
            print('Позиция уже занята')
            SetValue(sign)
    else:
        print('Введено недопустимое значение')
        SetValue(sign)


def CheckWin():
    # Проверка строк
    for row in table:
        if len(set(row)) == 1 and all(x != '' for x in row):
            return 1

    # Проверка столбиков
    for row in zip(table[0], table[1], table[2]):
        if len(set(row)) == 1 and all(x != '' for x in row):
            return 1

    # Проверка диагоналей
    diagonal1 = [table[0][0], table[1][1], table[2][2]]
    diagonal2 = [table[0][2], table[1][1], table[2][0]]
    if len(set(diagonal1)) == 1 and all(x != '' for x in diagonal1):
        return 1
    if len(set(diagonal2)) == 1 and all(x != '' for x in diagonal1):
        return 1


win = 0
step = 1
player = 'крестики'

while not win and step != 9:
    print(f'{step} ход ')
    if step % 2:
        player = 'крестики'
        print('Ходят крестики')
        SetValue('x')
    else:
        player = 'нолики'
        print('Ходят нолики')
        SetValue('o')
    PrintTable()
    win = CheckWin()
    step += 1
    print()

if step == 9:
    print('Ничья')
else:
    print(f'Победили {player}')
