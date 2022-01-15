class Container:
    def __init__(self):
        self.store = []

    #  запись элементов контейнера в файл (получение выходного файла)
    def write(self, stream):
        stream.write("Container contains {} phrases:\n\n".format(len(self.store)))
        for phrase in self.store:
            phrase.write(stream)
            stream.write("\n")
        pass

    #  запись элементов контейнера в файл (генерация входного файла).
    def writeToTestFile(self, stream):
        for number in range(len(self.store) - 1):
            self.store[number].writeToTestFile(stream)
            stream.write("\n")
        self.store[len(self.store) - 1].writeToTestFile(stream)
        pass

    # def shellSort(self, stream):
    #     n = len(self.store)
    #     gap = n / 2
    #     while int(gap) > 0:
    #         for i in range(int(gap), n):
    #             temp = self.store[i]
    #             j = i
    #             while j >= gap and self.store[int(int(j) - int(gap))].mainFunc() > temp.mainFunc():
    #                 self.store[int(j)] = self.store[int(j - int(gap))]
    #                 j -= gap
    #             self.store[int(j)] = temp
    #         gap /= 2
    #     stream.write("-----------------------\nShell-Sorted container:\n\n")
    #     for phrase in self.store:
    #         phrase.write(stream)
    #         stream.write("\n")
    # pass

    def shakerSort(self, stream):
        length = len(self.store)
        swapped = True
        start_index = 0
        end_index = length - 1
        while swapped:
            swapped = False
            for i in range(start_index, end_index):
                if self.store[i].mainFunc() > self.store[i + 1].mainFunc():
                    self.store[i], self.store[i + 1] = self.store[i + 1], self.store[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end_index = end_index - 1
            for i in range(end_index - 1, start_index - 1, -1):
                if self.store[i].mainFunc() > self.store[i + 1].mainFunc():
                    self.store[i], self.store[i + 1] = self.store[i + 1], self.store[i]
                    swapped = True
            start_index = start_index + 1
        stream.write("-----------------------\nShake-Sorted container:\n\n")
        for language in self.store:
            language.write(stream)
            stream.write("\n")
    pass

