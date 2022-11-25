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
            
# for c in range(0, len(arr)) :
#     if c == 0 :
#         pass
#     else :
#         d = arr[c - 1] # arr[0]
#         e = arr[c] # arr[1]
#         if arr[c - 1] > arr[c] :
#             arr[c - 1] = e
#             arr[c] = d
#         else :
#             pass
# print(arr)

""" 선생님 """
# arr45 = range(0, 46)
# for k in range(1000) :
#     rnd = int(random()*45)
#     a = arr45[0]
#     b = arr45[rnd]
#     arr45[0] = b
#     arr45[rnd] = a
# print(arr45[0], arr45[0], arr45[2], arr45[3], arr45[4], arr[5])

 
        