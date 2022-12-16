from pathlib import Path

def write_data(num1, num2, operator):
    d = Path('our_data.txt')
    with open(d, 'w',encoding="UTF-8") as data:
        a = f"{num1} {num2} {operator}"
        data.write(a)

def read_data():
    d = Path('our_data.txt')
    with open(d, 'r',encoding="UTF-8") as data:
        return data.read().split()

def write_data_res(res):
    d = Path('our_res.txt',encoding="UTF-8")
    with open(d, 'w') as data:
        return data.write(str(res))
