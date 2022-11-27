# Tas.k 4. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на
# указанных индексах. Индексы вводятся одной строкой, через пробел
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите количество элементов в списке = '))
list = []
b = True
result = 0
for i in range(-n, n+1):
    list.append(i)  # Добавляем элементы в список
print()
print(list)


index = input('Укажите индексы через пробел: ')
div_index = index.split(' ')
print(div_index)

for j in div_index[1:]:
    if b == True:
        result = int(list[int(div_index[0])])
        b = False
    j= int(j)
    result = result * list[j]

print(result, end=' ')

# Сам не смог решить, одногрупник помогал. Очень сложно для меня на данном этапе.
