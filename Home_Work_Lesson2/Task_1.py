# Task 1. Напишите программу, которая
# принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 0,56 -> 11
n = float(input('Введите вещественное число: '))
x = str(n) # Преобразовал дробное число в string
x = x.split('.') # Разделил введенное число на целую и дробную часть
a = (x[0]) # целая часть 
b = (x[1]) # дробная часть
c = int(b) # преобразовал string в int
res = 0
while c != 0:
    res = res + (c % 10) 
    c = c // 10    
print(res)
