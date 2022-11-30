# n = 9
# while k:=len(input('-->').split()) != n:
#     print('Try again')

# def func(a_1,a_2,a_3,*args,**kwargs):
#     return a_1,a_2,args,kwargs # (1, 2, (), {}) --> () = картеж, {} = словарь.
# print(func(1,2,3,'ad',1234,'dfse',key_1=312,key_2='jfjj'))

# Task 1. Реализуйте алгоритм задания случайных чисел без 
# использования встроенного генератора псевдослучайных чисел.

import time
def my_random(ranMin:int,ranMax:int):
    a = (time.time())*100000
    temp = (round(a)%ranMax)+ranMin
    return temp
mini = int(input('Введите от: '))   
maxi = int(input('Введите до: '))
print(my_random(mini,maxi))



