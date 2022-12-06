# Включение
# a = [(i+1) for i in range(1,11) if i < 7]
# print(a)

# my_list = ['12','42','45']
# print(set(map(int,my_list)))

# my_list = ['12','42','45']
# print(list(filter(lambda x: int(x)< 30, my_list)))

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'


# text = 'Я люблю Джавуабв абви Питон'
# search = 'абв'
# text_split = text.split()
# new_text = ''
# for i in text_split:
#     if search  in i:
#         text_split.remove(i)
#     else:
#         new_text += i+' '
# print(new_text)

# text = 'Я люблю Джавуабв абви Питон'
# search = 'абв'
# text_split = text.split()
# new_text = ''
# for i in text_split:
#     if search not in i:
#          new_text += i+' '    
# print(new_text)

# string = 'Я люблю Джавуабв абви Питон'
# s1 = 'абв'
# print(' '.join([i for i in string.split() if i.count(s1) == 0]))

# my_str = 'Я люблю Джавуабв абви Питон'
# lst = my_str.split(" ")
# my_list = [i for i in lst if "абв" not in i]
# print(*my_list)

my_str = 'Я люблю Джавуабв абви Питон'
filtered_list = list(filter(lambda word: "абв" not in word, my_str.split(' ')))
    

