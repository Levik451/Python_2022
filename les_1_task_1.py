"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек
"""

duration = int(input('Введите время в секундах: '))
seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // (3600 * 24)

if duration <= 59:
    print(f'{duration} сек')
elif duration <= 3599:
    print(f'{minutes} мин {seconds} сек')
elif duration <= 86399:
    print(f'{hours} ч {minutes} мин {seconds} сек')
else:
    print(f'{days} дн {hours} ч {minutes} мин {seconds} сек')
