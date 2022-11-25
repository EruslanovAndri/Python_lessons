# Task3. Напишите пр-му, в которой пользователь
# будет задавать две строки,а про-мма будет определять
# количество вхождений одной сторки в другую.

# 1 вариант
# text = 'Я люблю Мариию люлюлю'

# char = input('введите значение поиска: ')
# len_char = len(char)
# i = 0
# count = 0
# while i < len(text)-1:
#     if char.lower() == text[i:len_char+i].lower():
#         count += 1
#     i += 1
# print(count)

# 2 вариант

# text = 'Я люблю Python люблю'
# searchText = input('Введите стороку для подсчета вхождений :')

# # list = text.split(searchText)
# # print(len(list)-1)
# print(text.count(searchText))

# 3 вариант

my_string = 'Я люблю Python люблю'
s2 = input('Введите сторку для проверки вхождений: ')
count = 0
for i in range(len(my_string) - len(s2)+1):
    if my_string[i:i+len(s2)] == s2:
        count += 1
print(count)        
