arr = [3, 2, 1]
arr.append(4)
# arr.append(5)
# arr.remove(4)
# arr.clear()
#   arr.insert(5, 7) # 인덱스를 벗어나도 그냥 끝에 넣어줌
arr.insert(len(arr), 7) # == arr.append(7)

print(arr)