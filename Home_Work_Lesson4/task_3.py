# Task 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# numbers = [1, 1, 2, 3, 4, 4, 4]
# def get_Unique_num(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for numbers in unique_numbers:
#         list_of_unique_numbers.append(numbers)
#     return list_of_unique_numbers
# print(get_Unique_num(numbers))

# lst = list(map(int,input('Ввдеите элементы в список =>\n').split()))
# print(lst)
# new_lst = []
# [new_lst.append(i) for i in lst if not i in new_lst]
# print(new_lst)
numbers = input('Введите числа через пробел  => ').split()
answ = []
for i in numbers: 
        if numbers.count(i) == 1: answ.append(i)
print(*answ) 
