# Task 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 5, 6]
def checkLenght():   
    if len(my_list) % 2 == 0:
        a = []
        index = 0
        for i in range(len(my_list)//2):
            res = my_list[i] * my_list[index-i-1]
            a.append(res)
        return a
    else:
        a = []
        index = 0
        for j in range(len(my_list)//2+1):
            res = my_list[j] * my_list[index-j-1]
            a.append(res)
        return a
print(checkLenght())



# my_list_1 = [2, 3, 5, 6]
# def product():
#     a = []
#     index = 0
#     for i in range(len(my_list_1)//2):
#         res = my_list_1[i] * my_list_1[index-i-1]
#         a.append(res)
#     print(a)
# product()

