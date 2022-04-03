staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(staff)):
    staff[i] = staff[i].split()[-1].capitalize()

for item in staff:
    print(f'Привет {item}')