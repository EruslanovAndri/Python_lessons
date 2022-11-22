# Task - 5. Напишите программу, которая принимает на
# вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a = float(input('Enter A = '))
a1 = float(input('Enter A1 = '))
b = float(input('Enter B = '))
b1 = float(input('Enter B1 = '))
result = (b-a)*(b-a)+(b1-a1)*(b1-a1)
print(round(pow(result,0.5),4))
