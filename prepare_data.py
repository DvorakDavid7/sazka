
class Prepare_data:
    def prepare(self,path):
        data = set(open(path, "r"))
        data = list(data)
        data.sort()
        with open("sorted_data.txt", "w") as file:
            for item in data:
                file.write(item)
