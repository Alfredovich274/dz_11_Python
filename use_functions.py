"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько
пополнить счет
после того как пользователь вводит сумму, она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и
переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например
(еда) снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход.
Выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os


def to_deposit(check):
    return check + int(input('Для пополнения счета введите сумму - '))


def buy(check, price, name):
    """
    Покупка.
    :param check: Сумма денежных средств на счете;
    :param price: Цена покупаемого товара;
    :param name: Название товара;
    :return: остаток денежных средств на счету после покупки.
    """
    if price <= check:
        with open('my_history.txt', 'a') as file:
            file.write(f'{name} - {price}\n')
        return check - price
    else:
        print('Не хватает денег')
        return check


def history_buy():
    with open('my_history.txt', 'r') as file:
        history = file.read()
    return history


def account_action(check):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню - ')
        if choice == '1':
            check = to_deposit(check)
        elif choice == '2':
            product = input('Введите название продукта: ')
            price = int(input('Введите стоимость продукта: '))
            check = buy(check, price, product)
        elif choice == '3':
            print(history_buy())
            print(f'Остаток средств: {check}\n')
        elif choice == '4':
            with open('my_wallet.txt', 'w') as file:
                file.write(str(check))
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    if os.path.exists('my_wallet.txt'):
        with open('my_wallet.txt', 'r') as f_wall:
            money = int(f_wall.read())
    else:
        with open('my_wallet.txt', 'w') as f_wall:
            f_wall.write('0')
    if not os.path.exists('my_history.txt'):
        story = 'Название, Сумма\n'
        with open('my_history.txt', 'w') as f:
            f.write(story)
    account_action(money)
