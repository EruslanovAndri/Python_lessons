# Task 2.Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# 52 = [2,2,13]

def factor(n):
    a = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        a.append(n)
    return a


print(factor(123))
