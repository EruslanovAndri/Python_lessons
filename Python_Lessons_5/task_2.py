# 2. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9
import pathlib

a = '1 2 3 4 6 7 8'

with open('numberx.txt','w') as data:
    data.write(a)

with open('numberx.txt','r') as data:
    lst = a.split()
    for i in range(1,len(lst)):
        if  (int(lst[i])- 1) != (int(lst[i-1])):
            print(int(lst[i])-1)

with open('numberx.txt','') as data:
    lst = a.split()
    for i in range(1,len(lst)):
        if  (int(lst[i])- 1) != (int(lst[i-1])):
            print(int(lst[i])-1)



        

        
            
