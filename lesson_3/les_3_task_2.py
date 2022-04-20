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


def num_translate_adv(eng_number: str):
    if eng_number.islower():
        return num_translate(eng_number)

    if eng_number.capitalize() != eng_number:
        return None

    return num_translate(eng_number.lower()).capitalize()


if __name__ == '__main__':
    print(num_translate_adv('Five'))
    print(num_translate_adv('seven'))