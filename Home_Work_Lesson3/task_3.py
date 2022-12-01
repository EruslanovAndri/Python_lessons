# Task 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 10.01]
a = []
for i in range(len(my_list)):
    res = my_list[i] * 10 % 10
    a.append(res)
print(a)
max = a[0]
min = a[0]
res = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    else:
        if a[i] < min:
            min = a[i]
res = (max - min)/10 
print('Max is = ',max)
print('Min is = ',min)
print('Difference is = ',round(res,4))


