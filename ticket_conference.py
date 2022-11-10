ticket_needs = int(input('Введите необходимое количество билетов ='))
numerator = 1
money = 0
for i in range(ticket_needs):
    age = int(input('Возраст='))
    if age < 18:
        money += 0
        print('билет бесплатно')
    elif 18 <= age < 25:
        money += 990
        print('билеты цена', money)
    else:
        money +=1390
        print('билеты цена', money)

if ticket_needs > 3:
    print(f'Скидка 10% потому что {ticket_needs} посетителей')
    money = money - ((money / 100) * 10)

print( f"ВСЕГО: {money} руб." )















