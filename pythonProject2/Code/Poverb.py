from Phrase import *

class Poverb (Phrase):
    def __init__(self):
        self.country_name_length = 0
        self.signs_count = 0
        self.text_length = 0

    def readStrArray(self, str_array, i):
        if i >= len(str_array) - 2:
            return 0
        self.country_name_length = int(str_array[i])
        self. signs_count = int(str_array[i + 1])
        self.text_length = int(str_array[i + 2])
        i += 3
        return i

    #  запись параметров пословицы в файл (получение ответа).
    def write(self, stream):
        stream.write("Aphorism:\nCountry's name length = {}\nText length = {}\nSigns' count = {}"
                     "\nMainFunc = {}\n".format
                     (self.country_name_length, self.text_length, self.signs_count, self.mainFunc()))
        pass

    #  запись параметров пословицы в файл (генерация входного файла).
    def writeToTestFile(self, stream):
        stream.write("3 {} {} {}".format(self.country_name_length, self.text_length, self.signs_count))
        pass

    #  вычисление mainFunc от пословицы.
    def mainFunc(self):
        return float(self.signs_count) / self.text_length
        pass