# Task - 1.
# Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Enter a number from 1 to 7 = '))
if n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
    print('No')
elif n == 6 or n == 7:
    print('Yes')
else:
    print('Wrong number! The number should be less than seven')    
