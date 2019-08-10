
class Prepare_data:
    def prepare(self,path, save_file):
        data = set(open(path, "r"))
        data = list(data)
        data.sort()
        with open(save_file, "w") as file:
            for item in data:
                file.write(item)
