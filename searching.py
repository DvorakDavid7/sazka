import time


data = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
target = 3

class Searching:
    def search(self, target, data):
        if data[0] > target > data[len(data) - 1]:
            return False
        while len(data) > 0:
            midd = int(len(data) / 2)
            if data[midd] == target:
                return True
            if data[midd] < target:
                data = data[midd + 1:]
            else:
                data = data[:midd]
        return False


# x = Searching()
# print(x.search(9, data))
