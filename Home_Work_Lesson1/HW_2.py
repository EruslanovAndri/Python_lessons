# Task-2.
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not (x and y and z)):
                print(x, y, z)
                
