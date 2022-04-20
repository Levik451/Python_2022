def num_translate(eng_number: str):
    trans = {
            "one": 'один',
            "two": 'два',
            "thee": 'три',
            "four": 'четыре',
            "five": 'пять',
            "six": 'шесть',
            "seven": 'семь',
            "eight": 'восемь',
            "nine": 'девять',
            "ten": 'десять',
    }

    if eng_number in trans:
        return trans[eng_number]

    return None


if __name__ == '__main__':
    print(num_translate('thee'))
