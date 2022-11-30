# Task 2. Задайте список. Напишите программу,
# которая определялит,присутствует ли в списке строк некое число.
# ['sdf13''fds66','34'] --> 3 --> 'sdf13' '34'

list = ['sdf13', 'fds66', '3s4']
def in_list(list_, find_):
    result = False
    for i in list_:
        if find_ in i:
            print(i)
    
print(in_list(list,'s'))

# def in_list_(list_,find_):
#     for i in range(len(list_)):
#         if list_[i].find(find_) > -1:
#             print(list_[i])

# in_list_(list,'s')