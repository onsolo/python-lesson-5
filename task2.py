# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random

numbers = [random.randint(1, 20) for i in range(10)]

sequence = [numbers[random.randint(0, len(numbers) - 1)]]
index = 0

for i in range(len(numbers) - 1):
    rand = numbers[random.randint(0, len(numbers) - 1)]
    if rand > sequence[index]:
        index += 1
        sequence.append(rand)

print(numbers)
print(sequence)
