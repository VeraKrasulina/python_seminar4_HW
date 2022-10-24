# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

some_list = [random.randint(0, i) for i in range(20)]
print(f" Исходный список: {some_list}")

def remove_dubs (lst: list) -> list:
    result_list = []
    for i in some_list:
        if i not in result_list:
            result_list.append(i)
    return result_list

print(f"Список без дубликатов: {remove_dubs(some_list)}")
