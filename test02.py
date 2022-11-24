# 첫 번째 수를 넣으세요 1
# 두 번재 수를 넣으세요 10
# 1에서 10까지 합은 55입니다.
a = int(input("첫 번째 수를 넣으세요 "))
b = int(input("두 번째 수를 넣으세요 "))
arr = range(a,b+1)
sum = 0
for i in arr :
    sum += i
# print(str(a) + "에서 " + str(b) + "까지 합은 " + str(sum) + "입니다")
print("{}에서 {}까지 합은 {}입니다.".format(a, b, sum))
