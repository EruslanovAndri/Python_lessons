# Task 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.
# Индексы: 0, 1, 2, 3, 4
# Пример: [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

my_list = [2,3,5,9,3,100]
def odd_Sum():
    sum = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            sum += my_list[i]
    print(sum)
odd_Sum()