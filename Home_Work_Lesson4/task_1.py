# Task 1. Вычислить число c заданной точностью d

# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141
import math
d = float(input('Задайте математическую точность => '))
count = 0
while d != 1:
    d = d * 10
    count += 1
print(round(math.pi, count))

    


        





# a = [1,2,33] # => <class 'list'> Итерируемый
# print(type(a))
# for i in range(len(a)):
#     print(a[i])

# a = {1,2,4} # => <class 'set'> Множество Неитерируемый
# print(type(a))
# for i in range(len(a)):
#     print(a[i])

# a = 'asdfg' # <class 'str'> Строки Итерируемый
# print(type(a))
# for i in range(len(a)):
#     print(a[i])

# a = 0.123 # <class 'float'>  Неитерируемый нет длины.
# print(type(a))
# for i in range(len(a)):
#     print(a[i])

