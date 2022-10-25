# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.

import random

numbers = [random.randint(1, 10) for i in range(11)]


def getDoublesCount(numbers):
    counter = 0
    for x in numbers:
        if numbers.count(x) > 1:
            counter += 1
    return counter


print(numbers)
print(f'{getDoublesCount(numbers)} элемента(ов) совпадают')
print(f'Список уникальных элементов {set(numbers)}')
