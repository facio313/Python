# 로또를 생성하시(1~45 숫자 중에서 중복 없이 6개 가져오기)
from random import random

arr = []
for i in range(0, 6) :
    arr.append(int(random()*45 + 1))
    for j in range(0, i) :
        if arr[i] == arr[j] :
            arr[i].append(int(random()*45 + 1))
        else :
            pass
print(arr)
            
for k in range(0, 5) :
    for l in range(k + 1, 6) :
        a = arr[k]
        b = arr[l]
        if a > b :
            arr[k] = b
            arr[l] = a
print(arr)


""" 선생님 """
# arr45 = range(0, 46)
# for k in range(1000) :
#     rnd = int(random()*45)
#     a = arr45[0]
#     b = arr45[rnd]
#     arr45[0] = b
#     arr45[rnd] = a
# print(arr45[0], arr45[0], arr45[2], arr45[3], arr45[4], arr[5])

 
        