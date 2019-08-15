import time
import json


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


    def finder_jirka(self,arrExcel, arrDatabase):
        matches = []
        k = 0
        for i in range(len(arrExcel)):
            for j in range(k, len(arrDatabase)):
                if arrExcel[i] < arrDatabase[j]:
                    k = j + 1
                    break

                elif arrExcel[i] == arrDatabase[j]:
                    matches.append(arrExcel[i])
                    break
        return matches

    def json_finding(self, json_database_path):
        with open(json_database_path, "r") as json_file:
            self.json_data = json.load(json_file)
