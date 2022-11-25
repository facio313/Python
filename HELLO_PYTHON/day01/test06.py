# 가위 / 바위 / 보를 넣으세요 가위
# 나 : 가위
# 컴 : 가위
# 결과 : 비김
from random import random

a = input("가위 / 바위 / 보를 넣으세요 ")
print("나 : " + a)
b = int(random()*3)
c = ""

if b == 0 :
    c = "가위"
elif b == 1 :
    c = "바위"
else :
    c = "보"
print("컴 : " + c)
    
if a == c :
    print("결과 : 비김")
elif (a == "가위" and c == "바위") or (a == "바위" and c == "보") or (a == "보" and c == "가위") :
    print("결과 : 짐")
else :
    print("결과 : 이김")

""" 선생님 : 모르는 사람에게 보여주어야 한다면 직관적인 것이 낫다
if com == "가위" and mine == "가위" :   result = "비김"
if com == "가위" and mine == "바위" :   result = "짐"
if com == "가위" and mine == "보" :   result = "이김"
if com == "바위" and mine == "가위" :   result = "이김"
if com == "바위" and mine == "바위" :   result = "비김"
if com == "바위" and mine == "보" :   result = "짐"
if com == "보" and mine == "가위" :   result = "이김"
if com == "보" and mine == "바위" :   result = "짐"
if com == "보" and mine == "보" :   result = "비김"
"""