from Phrase import *

class Aphorism (Phrase):
    def __init__(self):
        self.authors_name_length = 0
        self.signs_count = 0
        self.text_length = 0

    def readStrArray(self, str_array, i):
        if i >= len(str_array) - 2:
            return 0
        self.authors_name_length = int(str_array[i])
        self. signs_count = int(str_array[i + 1])
        self.text_length = int(str_array[i+2])
        i += 3
        return i

    #  запись параметров афоризма в файл (получение ответа).
    def write(self, stream):
        stream.write("Aphorism:\nAuthor's name length = {}\nText length = {}\nSigns' count = {}"
                     "\nMainFunc = {}\n".format
                     (self.authors_name_length,self.text_length, self.signs_count, self.mainFunc()))
        pass

    #  запись параметров афоризма в файл (генерация входного файла).
    def writeToTestFile(self, stream):
        stream.write("3 {} {} {}".format(self.authors_name_length,self.text_length,self.signs_count))
        pass

    #  вычисление mainFunc.
    def mainFunc(self):
        return float(self.signs_count) / self.text_length
        pass
