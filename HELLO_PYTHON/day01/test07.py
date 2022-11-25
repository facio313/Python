# 출력할 단수를 넣으세요 4
# 4 * 1 = 4
# 4 * 2 = 8

a = int(input("출력할 단수를 넣으세요 "))

for i in range(1, 10) :
    print("{} * {} = {}".format(a, i, a*i))