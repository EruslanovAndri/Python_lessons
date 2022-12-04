# Task 1. Считать строку из набора чисел из файла.
# Напишите пр-му, которая покажет большее и меньшее число
# В качестве символо разделителя используйте пробел.Результат написать к конец файла(x1, x2)

# 'w' - пересоздает/создает,запись
# 'r' - чтение
# 'a' - дозапись в конец файла
# 'r+' - чтение + дозапись.

# my_file = open('my_list.txt','w')
# my_file.write('1 2 6 8 9 4 32')
# my_file.close()

with open('my_list.txt','w') as data: # Создаем и записываем данные в фаил.
    data.write(f'1 2 6 8 9 4 3\n')

with open('my_list.txt','r') as data: # Читаем фаил.
    lst = data.read()  # Присваиваем данные в переменную lst
new_lst = lst.split(' ') # Делим данные через разделитель.
lst_int = [int(i) for i in new_lst] # Конвертируем в int
max_num = max(new_lst) # Вызываем функцию MAX
min_num = min(new_lst) # Вызываем функцию MIN

with open('my_list.txt','a') as data: # Дозаписываем результат в фаил.
    data.write(f'Max = {max_num}\n')
    data.write(f'Min = {min_num}\n')



# f = open('text.txt','w')
# f.write('Hello world')
# f.close()
# import pathlib
# file_path = r'text.txt'
# with open(file_path,'r') as f_data:
#     print(f_data.read())

# from pathlib import Path
# file_path = Path(r'/Users/eruslanovandrey/Python_lessons/text.txt')
# with open(file_path,'r') as f_data:
#     print(f_data.read())


