# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
# .        '79*x4   + '13*x3   + '86*x2   +'5*x +'10'

import random

k = int(input('Укажите степень => '))
final_lst = ''
while k >= 0:
    lst = [random.randint(0, k)]
    gen_num = random.randint(0, 100)
    if k > 1:
        lst.append(f'{gen_num}*x{k} + ')
    elif k == 1:
        lst.append(f'{gen_num}*x + ')
    elif k == 0:
        lst.append(f'{gen_num} = {k}')
    lst1 = str(lst)
    with open('my_file.txt', 'a') as data:
        data.write(lst1)
    g = str(gen_num)
    k1 = str(k)
    final_lst += lst1
    lst1.replace(g,k1)
    print(lst)
    k = k - 1

f = final_lst.split(' ')
print(final_lst)
f1 = []
for i in range(len(f)):
        f1.append(f[i])
print(f1)

filtered_list = list(filter(lambda simbol: " " not in simbol,f1))
print(filtered_list)

# Получается очень странный вывод с лишними цифрами и знаками. Нужно доработать!!!