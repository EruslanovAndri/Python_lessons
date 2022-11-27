# Task 5. Реализуйте алгоритм перемешивания списка.
import random

# 1 Вариант
list = [1, 2, 6, 34, 12, 7]
for i in range(len(list)):
    print(list[i], end=' ')
random.shuffle(list)
print()
print(list)

# 2 Вариант
list = [1,23,45,23,5,2,1,5,6]
def mixed(list):
    list_copy = list[:]
    list_length = len(list)
    for i in range(list_length):
        index_rnd =random.randint(0,list_length-1)
        temp = list[i]
        list[i] = list_copy[index_rnd]
        list_copy[index_rnd] = temp
    return list_copy
mixed_list = mixed(list)
print('Исходный массив')
print(list)
print('Перемешанный массив')
print(mixed_list)





# for i in range(5):
#     i = random.randint(0,100)
#     print(i,end=' ')

# print('Firts\nSecond')
# text = 'This is some text...'
# print(text.strip(' . '))
# import random
# num = random.random()
# num = num * 10
# print(num)

# num = random.randint(0,9)
# print(num)

# num1 = random.randint(0,1000)
# num2 = random.randint(0,1000)
# new_random = num1 / num2
# print(new_random)

# num = random.randrange(0,100,5)
# print(num)

# import turtle
# turtle.shape('turtle')
# for i in range(0,5):
#     turtle.forward(100)
#     turtle.right(72)
# turtle.exitonclick()
#
# for i in range(0,10):
#     turtle.right(36)
#     for i in range(0,5):
#         turtle.forward(100)
#         turtle.right(72)
# turtle.exitonclick()
