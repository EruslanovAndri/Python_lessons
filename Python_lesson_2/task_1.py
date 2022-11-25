# i = 0
# while i < 11:
#     print(i,end = ' ') # End выводит числа в одну строку.
#     i += 1
# else:
#     print('END')
# result = 0 1 2 3 4 5 6 7 8 9 10 END

# Task 1.Напишите прог-му, которая принимает число N и выдает 
# последовательность из N челенов.
# Пример: Для N = 5: Результат = 1,-3,9,-27,81 
# N = 5 значит кол-во элементов

n = -3
for i in range(5):
    res = n ** i
    print(res, end=' ')

# while x:=int(input('--> ')) < 0: Моржовый оператор!!!!
#     print('Enter a number above 0 -->')