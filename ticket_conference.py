ticket_needs = int(input('Введите необходимое количество билетов ='))
no_money = 0
money = 0
money_pay = 0
for i in range(ticket_needs):
    age = int(input('Возраст='))
    if age < 18:
        money += 0
        no_money += 1
        print('билет бесплатно')
    elif 18 <= age < 25:
        money += 990
        money_pay += 1
        print('билет цена=990 руб.')
    else:
        money +=1390
        money_pay += 1
        print('билет цена=1390 руб.')

if ticket_needs > 3 and money > 3960 :
    print('цена билетов всего =', money)
    print(f'Скидка 10% потому что оплата за {money_pay} посетителей')
    money = money - ((money / 100) * 10)


print( f"ВСЕГО: {money} руб." )
print(f'Бесплатно- {no_money} посетителей')















