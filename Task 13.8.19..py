Ntick= int(input('Введите количество билетов дл¤ покупки: '))
Stick = 0
for i in range(Ntick):
    age = int(input('Введите возраст покупателя: '))
    i = i+1
    if 0 < age < 18:
        Stick = 0
        print('Билет бесплатно')
    elif 18<= age <25:
        Stick = 990 + Stick
        print('Билет за 990р.')
    elif 25 <= age < 100:
        Stick = 1390 + Stick
        print('Билет за 1390р.')

if Ntick > 3:
    Stick = Stick - 0.1*Stick
    print('Цена за билеты со скидкой 10% дл¤ группы более 3 чел.: ', Stick)
else:
    print('Цена за билеты: ', Stick)
