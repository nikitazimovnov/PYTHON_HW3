import sys
import time

from Container import Container
from Random import Random
from ReadStrArr import readStrArray

start_time = time.time()
if __name__ == '__main__':
    container = Container()
    if len(sys.argv) != 4 or (sys.argv[1] != "-gen" and sys.argv[1] != "-fill" and sys.argv[1] != "-rnd"):
        print("Incorrect command line!")
        print(sys.argv[1])
        exit()

    elif sys.argv[1] == "-fill":
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]

        input_file = open(inputFileName)
        str = input_file.read()
        input_file.close()

        strArray = str.replace("\n", " ").split(" ")
        phrases = readStrArray(container, strArray)

    else:
        count = int(sys.argv[2])
        for number in range(count):
            container.store.append(Random.getRandomPhrase())

    #  Создание тестового файла на рандомных данных.
    if sys.argv[1] == "-gen":
        out_file = open(sys.argv[3], 'w')
        container.writeToTestFile(out_file)

        print('==> Test file generated sucsessfully!\n==> Program stopped')
        exit()

    print('==> Container filled sucsessfully! Start working...')
    out_file = open(sys.argv[3], 'w')
    container.write(out_file)

    container.shakerSort(out_file)
    out_file.close()

    print('==> Finish')
    end_time = time.time()

    print("Working time =", end_time - start_time, "seconds")