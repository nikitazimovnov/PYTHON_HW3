from random import randint

from Puzzle import Puzzle
from Poverb import Poverb
from Aphorism import Aphorism


class Random:

    @staticmethod
    def getRandomPhrase():
        val = randint(1, 3)
        if val == 1:
            return Random.getRandomAforism()
        elif val == 2:
            return Random.getRandomPuzzle()
        elif val == 3:
            return Random.getRandomPoverb()

    @staticmethod
    def getRandomAforism():
        aphorism = Aphorism()
        text = Random.getRandomText()
        authors_name = Random.getRandomSpecial()
        aphorism.authors_name_length = len(authors_name)
        aphorism.text_length = len(text)
        aphorism.signs_count = Random.getSignsNumber(text)
        return aphorism

    @staticmethod
    def getRandomPuzzle():
        puzzle = Puzzle()
        text = Random.getRandomText()
        authors_name = Random.getRandomSpecial()
        puzzle.authors_name_length = len(authors_name)
        puzzle.text_length = len(text)
        puzzle.signs_count = Random.getSignsNumber(text)
        return puzzle

    @staticmethod
    def getRandomPoverb():
        poverb = Poverb()
        text = Random.getRandomText()
        authors_name = Random.getRandomSpecial()
        poverb.authors_name_length = len(authors_name)
        poverb.text_length = len(text)
        poverb.signs_count = Random.getSignsNumber(text)
        return poverb

    @staticmethod
    def getRandomText():
        text_length = randint(10, 60)
        text = ""
        for i in range(text_length):
            text += chr(randint(ord('a'), ord('z') + 1))
            flag = randint(0, 15)
            if flag == 0:
                text += '.'
            elif flag == 1:
                text += ','
            elif flag == 2:
                text += '-'
        return text + "."

    @staticmethod
    def getRandomSpecial():
        special_length = randint(4, 14)
        special = ""
        for i in range(special_length):
            special += chr(randint(ord('a'), ord('z') + 1))

        return special

    @staticmethod
    def getSignsNumber(text):
        count = 0
        for sym in text:
            if sym == '-' or sym == '.' or sym == ',':
                count += 1

        return count
