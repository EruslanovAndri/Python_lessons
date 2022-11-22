# Task_1 Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом второго.
#
one = int(input('Enter number one:'))
two = int(input('Enter number two:'))
if (one**2 == two) or (two**2 == one):
    print('Yes')
else: 
    print('No')

num_1 = 2
num_2 = 2
a = 2 if (num_1 == num_2) else 4 # Тернарный оператор