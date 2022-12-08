# Task 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Я люблю своюабв семьюабв иабв Марию'
search = 'абв'
split_text = my_text.split()
normal_text = ''
for i in split_text:
    if search not in i:
        normal_text += i + ' '
print(normal_text)

text = 'Я люблю своюабв семьюабв иабв Марию'
normal_text = ' '
print(list(filter(lambda normal_text: 'абв' not in normal_text,text.split())))
