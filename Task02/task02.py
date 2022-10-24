# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];

from collections import OrderedDict
def simple_mult(num):
    mult_list = []
    mult = 2
    while mult*mult <= num:
        if num % mult == 0:
            mult_list.append(mult)
            num //= mult
        else:
            mult += 1
    if num > 1:
        mult_list.append(num)
    return list(OrderedDict.fromkeys(mult_list))

print(simple_mult(374220))