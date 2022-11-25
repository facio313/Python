def addminmuldiv(a, b):
    return a + b, a - b, a * b, a / b

# sum, min, mul, div = addminmuldiv(5, 4)
sum = addminmuldiv(5, 4)

print("sum", sum)
print("sum[0]", sum[0])
# print("min", min)
# print("mul", mul)
# print("div", div)

# 리턴 개수 맞춰줘야 함
# 안 맞으면 구동 시 에러
# 리턴 여러 개, 하나의 변수 => 배열 같이 나옴 = 튜플
# 튜플은 자바에는 없고, 배열 같이 쓸 수 있음