def thesaurus(*args: str):
    names = {}

    for name in args:
        if name[0] in names:
            names[name[0]].append(name)
        else:
            names[name[0]] = [name]

    return names


def thesaurus_adv(*args: str):
    dictionary = {}

    for full_name in args:
        last_name = full_name.split()[1]

        if last_name[0] in dictionary:
            dictionary[last_name[0]].append(full_name)
        else:
            dictionary[last_name[0]] = [full_name]

    for key, value in dictionary.items():
        dictionary[key] = thesaurus(*value)

    return dictionary


def get_sorted_dict(data: dict):
    keys = sorted(data)
    result = {}

    for key in keys:
        result[key] = data[key]

    return result


if __name__ == '__main__':
    name_list = thesaurus("Иван", "Мария", "Петр", "Илья", 'Максим')
    print(name_list)
    print(get_sorted_dict(name_list))

    name_list_2 = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Максим Савельев")
    print(name_list_2)