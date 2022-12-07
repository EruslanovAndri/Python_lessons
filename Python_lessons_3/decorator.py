# Decorator

def header(func):

    def inner(*args,**kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')
    return inner

def table(func):

    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    return inner
@header
@table
def say(name,surname,age):
    print('Hello',name,surname,age)

# def buy():
#     print('Buy world')

# say = table(header(say))
say('Andrey','Eruslanov','38')
# buy = decorator(buy)
# buy()

