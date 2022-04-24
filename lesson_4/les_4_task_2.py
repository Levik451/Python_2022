from utils import currency_rates


if __name__ == '__main__':
    val = currency_rates(input('Currency code: '))

    if val:
        print(*val, sep=", ")
    else:
        print(None)
