class fileDuplicator:
    def __init__(self):
        self.history = []
        file_obj = open("user_name.txt", 'r')
        while True:
            line = file_obj.readline()
            if not line:
                break
            self.history.append(line)
        file_obj.close()

    def getHistory(self):
        return self.history
