import os
import random
def clear(): return os.system("cls")
clear()
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input()
# def summa(x):
#     if float(x) < 0:
#         x = float(x) * (-1)
#     number = 0
#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number
# print(f'{summa(num)}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from math import factorial
# def func():
#     n = int(input("Введите число N: "))
#     for i in range(1, n+1):
#         print(f'{factorial(i)}', end = " ")
# func()


# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06

# n = int(input())
# dict_num = {}
# for i in range(1,n+1):
#     dict_num[i] = round((1+1/i)**i,2)
# print(dict_num)
# print(sum(dict_num.values()))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(random.randint(-n,n))
#     return list
# n = int(input())
# nums = list(n)
# print(nums)
# file = r'C:\Users\Data\Desktop\Попытка поумнеть\pyhton\Seminar_2\File.txt'
# x = open(file,"r")
# result = nums[int(x.readline())]*nums[int(x.readline(2))]
# print(result)

# Реализуйте алгоритм перемешивания списка.

# lst = [random.randint(0,10) for i in range(random.randint(5,10))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")
