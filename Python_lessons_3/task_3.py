# Task 3. Напишите пр-му,которая определяет
# позицию второго вхождения строки в список либо сообщит,что её нет.
# Например:
# - список ['qwe','asd','zxc','qwe','ertqwe'], ищем: 'qwe', ответ: 3
# - список ['йцу','фыв','ячс','цук','йцукен','йцу'], ищем: 'йцу', ответ: 5
# - список ['йцу','фыв','ячс','цук','йцукен'], ищем: 'йцу', ответ: -1
# - список ['123','234',123,'567'], ищем: '123', ответ: -1
# - список [ ], ищем: '123', ответ: -1

# def func():
#     list_a = ['qwe','asd','zxc','qwe','ertqwe']
#     find_char = 'qwe'
#     new_list = []
#     for i in range(len(list_a)):
#         if find_char == list_a[i]:
#             new_list.append(i)
#     if len(new_list) <= 1:
#         return - 1
#     return new_list[1]
# print(func())

def func():
    list_a = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
    a = input('Введите искомую строку: ')
    count = 0
    for i in range(len(list_a)):
        if list_a[i] == a:
            count += 1
            if count == 2:
                return i
    return -1
func()
