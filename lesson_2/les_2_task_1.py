separated_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def readable_string_from_list(words: list):
    result = ''
    quote_start = True

    for i in range(len(words)):
        item = words[i]

        if item == '"':
            if quote_start:
                result += item
            else:
                result = f'{result[0:-1]}{item} '
            quote_start = not quote_start
        else:
            result += f'{item} '

    return result


def get_indexes_with_numbers(words: list, callback=None):
    indexes = []

    for i in range(len(words)):
        prefix = ''
        word = words[i]

        if word.startswith('-') or word.startswith('+'):
            prefix = word[:1]
            word = word[1:]

        if word.isdigit():
            indexes.append(i)

            if callback:
                callback(words, i, int(word), prefix)

    return indexes


def update_number_in_list(words: list, i: int, num: int, prefix: str):
    if int(num) < 10:
        words[i] = f'{prefix}0{num}'


def cover_list_elements_via_quotes(words: list, indexes: list):
    indexes.sort(reverse=True)

    for i in indexes:
        words.insert(i + 1, '"')
        words.insert(i, '"')


indexes_with_nums = get_indexes_with_numbers(separated_words, update_number_in_list)
cover_list_elements_via_quotes(separated_words, indexes_with_nums)
print(separated_words)

readable_string = readable_string_from_list(separated_words)
print(readable_string)
