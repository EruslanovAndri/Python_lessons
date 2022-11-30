
# def func(arg_list:list):
#     print(arg_list)
# func([123,3445])

# a = 3
# b = a
# a += 4
# print(b)
# Список изменяемый!!!! А сторка не изменяемая!!!
a = [1,2,3] # - СПИСОК 
b = a
a.append(4)
print(b)

a = 'qwertyu' # - СТРОКА
# a[1] = 'h' # TypeError: 'str' object does not support item assignment
print(a[1]) # --> w

# def func(a=[]):
#     a.append(1)
#     print(a)
# func()
# func()
# func()

def func(a=None):
    if a is None:
        a = [3,4]
    a.append(10)
    print(a)
func()