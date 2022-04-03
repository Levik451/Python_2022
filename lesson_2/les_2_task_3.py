import random


def get_readable_price(price: float):
    rubles, coins = str(price).split('.')
    coins = f'0{coins}' if len(coins) == 1 and int(coins) < 10 else coins

    return f'{rubles} руб. {coins} коп.'


prices = [round(random.uniform(50, 200), 2) for item in range(20)]

# PriceList
print(', '.join([get_readable_price(item) for item in prices]))

# Sorted PriceList
prices.sort(reverse=True)
print(', '.join([get_readable_price(item) for item in prices]))

# New PriceList with opposite sorting type
prices_2 = prices.copy()
prices_2.reverse()

# Print top 5
print(' || '.join([get_readable_price(price) for price in prices[:5]]))