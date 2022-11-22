# Task - 3. Напишите программу, которая принимает 
# на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter X = '))
y = int(input('Enter Y = '))

if x > 0 and y > 0:
    print('Coordinates are in the first quadrant.')
elif x < 0 and y > 0:
    print('Coordinates are in the second quadrant.')
elif x < 0 and y < 0:
    print('Coordinates are in the third quadrant.')  
elif x > 0 and y < 0:
    print('Coordinates are in the fourth quadrant.') 
else:
    print('Your enter the wrong coordinates')         
