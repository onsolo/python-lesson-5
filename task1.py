# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

numbers = [random.randint(1, 30) for i in range(15)]
filtered_numbers = list(filter(lambda item: item > 5, numbers))
print(filtered_numbers)
