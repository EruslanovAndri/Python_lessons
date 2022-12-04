# Task 2. Найдите корни квадратного уравнения Ax2 + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python (получить картеж)
import random


def get_squre(a, b, c) -> tuple[float]:
    print(f'коэффициент А ={a}\n'
          f'коэффициент B ={b}\n'
          f'коэффициент C ={c}\n')
    d = b ** 2 - 4*a * c
    print(f'дискиминант = {d}\n')
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f'Корень x1 = {x1}')
        print(f'Корень x2 = {x2}')
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        print(f'Корень x = {x}')
        return x,
    return 'Кореней нет'


print(get_squre(a=random.randint(1, 15),
                b=random.randint(1, 15),
                c=random.randint(1, 15)))

a = {1,1,2,2,4,5} # Множество = set
print(a)

# Словари 
my_dict = {
    'key_1':100,
    'key_2':
    {
        'key_3': 123
    }
}
for item in my_dict:
    print(item)

