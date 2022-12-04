# Task 3. Задайте два числа. Напишите пр-му, которая
# найдет НОК (наименьшее общее кратное) этих двух чисел.



x = 45
y = 60
count = x * y
while x != y:
    if x > y:
        x = x - y
        res = count / x
    else:
        y = y - x
        res = count / x
print(res)


# Нахождения общего делителя.

# x = 45
# y = 60
# while x != y:
#     if x > y:
#         x = x - y
#     else:
#         y = y - x
# print(x)
# print(y)
