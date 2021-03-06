import random


def victory():
    people = {'А.С.Пушкина': '06.06.1799',
              'Исаака Ньютона': '04.01.1643',
              'Маргарет Тэтчер': '13.10.1925',
              'Альберта Эйнштейна': '14.03.1879',
              'Никола Тесла': '10.06.1856',
              'Стива Джобса': '24.02.1955',
              'Чарльза Дарвина': '12.02.1809',
              'Михаила Ломоносова': '19.11.1711',
              'Екатерины 2': '02.05.1729',
              'Коко Шанель': '19.08.1883'
              }
    days = {'02': 'второе',
            '04': 'четвертое',
            '06': 'шестое',
            '10': 'десятое',
            '12': 'двенадцатое',
            '13': 'тринадцатое',
            '14': 'четырнадцатое',
            '19': 'девятнадцатое',
            '24': 'двадцать четвертое'
            }
    months = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '05': 'мая',
        '06': 'июня',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября'
            }
    print('Приветствую тебя на викторине!',
          '\nВам предстоит отгадать даты рождения нескольких известных людей\n')
    game = True
    while game:
        # key_people = list(people.keys())
        # names = list(people.keys())
        names = [name for name in people.keys()]
        names_questions = random.sample(names, 5)

        print('Введите дату рождения человека в формате dd.mm.yyyy')
        right_answers = 0
        for name in names_questions:
            answer = input(f' {name}: ')
            if answer == people[name]:
                right_answers += 1
            else:
                birthday = list(people[name].split('.'))
                print(f'{days[birthday[0]]} {months[birthday[1]]} '
                      f'{birthday[2]} года')

        print('\nКоличество правильных ответов - ', right_answers)
        print('Количество неправильных ответов - ',
              len(names_questions) - right_answers)

        if input('Если желаете начать игру сначала, '
                 'введите любой символ- ') == '':
            game = False
            print()


if __name__ == '__main__':
    victory()
