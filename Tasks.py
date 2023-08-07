import random
# # Задача 30
#
# def getting_a_list_with_an_arithmetic_progression(a1: int, d: int, n: int) -> list:
#     list_1 = []
#     for i in range(n):
#         an = a1 + i * d
#         list_1.append(an)
#     return list_1
#
#
# num1 = int(input('Введите "а" '))
# num2 = int(input('Введите "d" '))
# num3 = int(input('Введите "n" '))
# progression = getting_a_list_with_an_arithmetic_progression(num1, num2, num3)
# for i in progression:
#     print(i)
#
# # Задача 32
#
#
# def get_list(val_min: int, val_max: int, len_list: int) -> list:
#     list_1 = [random.randint(val_min, val_max) for _ in range(len_list)]
#     return list_1
#
#
# def find_index_in_desired_range(value_min: int, value_max: int, list1: list) -> list:
#     list_2 = []
#     for i in range(len(list1)):
#         if value_min <= list1[i] <= value_max:
#             list_2.append(i)
#     return list_2
#
#
# min_val = int(input('Введите минимальное значение в списке '))
# max_val = int(input('Введите максимальное значение в списке '))
# len_list1 = int(input('Введите количество элементов '))
# list_1_get = get_list(min_val, max_val, len_list1)
# print(list_1_get)
# min_value = int(input('Введите минимальное значение в диапазоне '))
# max_value = int(input('Введите максимальное значение в диапазоне '))
# print(find_index_in_desired_range(min_value, max_value, list_1_get))

