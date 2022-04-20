from random import sample, choice


def get_jokes(amount: int, no_repeats: bool = False) -> [str]:
    """
    Get custom jokes from the dictionaries: nouns, adverbs, adjectives
    :param amount: count of jokes
    :param no_repeats: forbidden to use any words more than once
    :return: list of the jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    max_len = len(min(nouns, adverbs, adjectives))

    if amount > max_len and no_repeats:
        return 'Input is not valid'

    if not no_repeats:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for _ in range(amount)]

    noun_ids = sample(range(len(nouns)), amount)
    adverbs_ids = sample(range(len(adverbs)), amount)
    adjectives_ids = sample(range(len(adjectives)), amount)

    return [f'{nouns[noun_ids[i]]} {adverbs[adverbs_ids[i]]} {adjectives[adjectives_ids[i]]}' for i in range(amount)]


if __name__ == '__main__':
    print(get_jokes(2))
    print(get_jokes(5))
    print(get_jokes(10))

    print(get_jokes(2, True))
    print(get_jokes(5, True))
    print(get_jokes(5, True))
