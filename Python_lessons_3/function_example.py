
# def = defenition = определение
def sayHallo(): # называем функцию
    print('Hello') #тело функции 
    print('World')
    print('and everybody')
sayHallo() # вызываем функцию

def square(x):
    print('Квадрат числа',x,'=', x**2)
square(8)
square(10)
for i in range(1,11):
    square(i)

def multiply(a,b):
    print(a*b)
multiply(3,5)
