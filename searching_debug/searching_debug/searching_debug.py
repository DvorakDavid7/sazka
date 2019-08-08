import time


class Jirka:
    def init(self):
        self.data = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19]
        self.targets = [5,8,13,15,16,18]
        self.results = []

    def jirka_search(self):
        pom = self.data
        super = self.data
        i = 0
        for target in self.targets:

            key = True

            if self.data[0] > target > self.data[len(self.data) - 1]:
                continue
            print("target: {} - pom: {}".format(target, pom))
            while len(pom) > 0:
                midd = int(len(pom) / 2)
                if pom[midd] == target:
                    pom = super[target - 2:]
                    print("True")
                    key = False
                    i += 1 
                    break
                if pom[midd] < target:
                    pom = pom[midd + 1:]
                else:
                    pom = pom[:midd]

            if key:
                pom = super[self.targets[i-1]:]
                print("False")





x = Jirka()
x.init()
x.jirka_search()
