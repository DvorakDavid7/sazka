import time


data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
target = 3

print(data)
while len(data) > 0:
    midd = int(len(data) / 2)
    print(data[midd])
    if data[midd] == target:
        print(True)
        break
    if data[midd] < target:
        data = data[midd + 1:]
        print(data)
    else:
        data = data[:midd]
        print(data)
