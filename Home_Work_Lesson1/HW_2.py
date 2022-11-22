# Task-2.
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

x = int(input('Enter X = '))
y = int(input('Enter Y = '))
z = int(input('Enter Z = '))

if (x != x or y != y or z != z) == x != x and y != y and z != z:
    print(True)
   

