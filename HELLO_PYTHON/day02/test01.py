# 구구단 2단부터 9단까지 전부 춝겨
# 9, 8, 7, 2

arr = [9, 8, 7, 2]
def gugudan():
    for i in arr :
        for j in range(1, 10):
            print("{} * {} = {}".format(i, j, i*j))
            
gugudan()