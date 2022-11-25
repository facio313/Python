# 홀/짝을 넣으세요 홀
# 나 : 홀
# 컴 : 짝
# 결과 : 젔음
import random

a = input("홀/짝을 넣으세요 ")
print("나 : " + a)
b = random.random()
c = ""

if b > 0.5 :
    c = "짝"
else :
    c = "홀"
print("컴 : " + c)

if a == c :
    print("결과 : 이김")
else :
    print("결과 : 졌음")