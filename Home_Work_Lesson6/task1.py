# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Lambda

# Лямбда-функции могут иметь любое количество аргументов,
# но у каждой может быть только одно выражение.
# Выражение вычисляется и возвращается.
# Эти функции могут быть использованы везде, где требуется объект-функция.
from pathlib import Path
def a(x, y): return x*y+2

print(a(3, 2))

# Найти все четные числа в диапазоне
list = [i for i in range(1, 21) if i % 2 == 0]
print(list)

# Найти все нечетные числа в диапазоне
list = [i for i in range(1, 21) if i % 2 != 0]
print(list)

def f(x):
    return x**2
lst = [(i,f(i)) for i in range(1,21) if i%2==0]
print(lst)


db = []
def write_data():
    with open(r'data.txt','w',encoding='UTF-8') as data:
        data.write(input('Enter a number => '))
write_data()

def read_data():
    with open(r'data.txt','r',encoding='UTF-8') as data:
        for i in data:
            db.append(i)

read_data()

print(db)
x = str(db).split()
print(x)


