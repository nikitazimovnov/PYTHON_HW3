from Aphorism import Aphorism
from Puzzle import Puzzle
from Poverb import Poverb


def readStrArray(container, str_array):
    array_length = len(str_array)
    i = 0  # Индекс, задающий текущую строку в массиве
    phrase_number = 0
    while i < array_length:
        str = str_array[i]
        key = int(str[0])
        if key == 1:  # признак афоризма
            i += 1
            phrase = Aphorism()
            i = phrase.readStrArray(str_array, i)  # чтение афоризма с возвратом позиции за ним
        elif key == 2:  # признак загадки
            i += 1
            phrase = Puzzle()
            i = phrase.readStrArray(str_array, i)  # чтение загадки с возвратом позиции за ней
        elif key == 3:  # признак пословицы
            i += 1
            phrase = Poverb()
            i = phrase.readStrArray(str_array, i)  # чтение пословицы с возвратом позиции за ней
        else:
            return phrase_number
        if i == 0:
            return phrase_number
        phrase_number += 1
        container.store.append(phrase)
    return phrase_number
