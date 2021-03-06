# Консольный файловый менеджер
import sys
import os
import shutil
from use_functions import account_action
from victorina import victory


def my_mkdir(x):
    return os.mkdir(x)


def my_listdir():
    return os.listdir()


def my_isfile(x):
    return os.path.isfile(x)


def my_isdir(x):
    return os.path.isdir(x)


def my_remove(x):
    return shutil.rmtree(x, ignore_errors=True)


def file_or_dir(print_file=False, print_dir=False):
    name_dir = []
    name_file = []
    for name_list in my_listdir():
        if my_isdir(name_list) and print_dir:
            name_dir.append(name_list)
        if my_isfile(name_list) and print_file:
            name_file.append(name_list)
    return ', '.join(name_dir), ', '.join(name_file)


def decorator_menu(func):
    def inner_func(*args, **kwargs):
        print('Выберите пункт меню:', end=' ')
        return func()
    return inner_func


@ decorator_menu
def input_data(my_int=True):
    in_data = ''
    if my_int:
        try:
            in_data = int(input())
        except ValueError:
            print('Это не число, введите число!')
    else:
        in_data = input()
    return in_data


def print_menu():
    print('1 - создать папку;\n'
          '2 - удалить (файл/папку);\n'
          '3 - копировать (файл/папку);\n'
          '4 - просмотр содержимого рабочей директории;\n'
          '5 - посмотреть только папки;\n'
          '6 - посмотреть только файлы;\n'
          '7 - просмотр информации об операционной системе;\n'
          '8 - создатель программы;\n'
          '9 - играть в викторину;\n'
          '10 - мой банковский счет;\n'
          '11 - смена рабочей директории;\n'
          '12 - сохранить содержимое рабочей директории в файл;\n'
          '0 - выход.')


if __name__ == '__main__':
    menu = 99
    print_menu()

    while menu:
        if menu == 1:
            # После выбора пользователь вводит название папки,
            # создаем её в рабочей директории
            name = input('Введите имя папки: ')
            if name in my_listdir():
                print('Папка существует')
            else:
                my_mkdir(name)
        elif menu == 2:
            # После выбора пользователь вводит название папки или файла, удаляем
            # из рабочей директории если такой есть;
            name = input('Введите название папки/файла: ')
            # проверяем наличие папки/файла
            if name in my_listdir():
                os.remove(name) if my_isfile(name) else my_remove(name)
                # if my_isfile(name):
                #     os.remove(name)
                # else:
                #     my_remove(name)
            else:
                print('Папка/файл не существует')
        elif menu == 3:
            # После выбора пользователь вводит название папки/файла и новое
            # название папки/файла. Копируем;
            name = input('Введите название папки/файла и '
                         'новое название через пробел: ')
            name = name.split()
            # проверяем наличие папки/файла !!!!!
            shutil.copy(name[0], name[1]) \
                if my_isfile(name[0]) \
                else shutil.copytree(name[0], name[1])
            # if my_isfile(name[0]):
            #     shutil.copy(name[0], name[1])
            # else:
            #     shutil.copytree(name[0], name[1])
        elif menu == 4:
            # вывод всех объектов в рабочей папке;
            print(*my_listdir(), sep='  ')
        elif menu == 5:
            # вывод только папок которые находятся в рабочей папке;
            names, _ = file_or_dir(print_dir=True)
            print(f'dirs: {names}')
            print(type(names))
        elif menu == 6:
            # вывод только файлов которые находятся в рабочей папке;
            _, names = file_or_dir(print_file=True)
            print(f'files: {names}')
        elif menu == 7:
            # вывести информацию об операционной системе
            # (можно использовать пример из 1 -го урока);
            print('Операционная система - ', sys.platform)
        elif menu == 8:
            # вывод информации о создателе программы;
            print('*** Создатель программы - Павел ***')
        elif menu == 9:
            # запуск игры викторина из предыдущего дз;
            victory()
        elif menu == 10:
            # запуск программы для работы с банковским счетом из предыдущего дз
            # (задание учебное, после выхода из программы управлением счетом в
            # главной программе сумму и историю покупок можно не запоминать);
            account_action()
        elif menu == 11:
            # Усложненное задание пользователь вводит полный /home/user/...
            # или относительный user/my/... путь. Меняем рабочую директорию на
            # ту что ввели и работаем уже в ней;
            old_path = os.getcwd()
            print('Текущий каталог ', old_path)
            new_path = input('Введите полный или относительный путь: ')
            if os.path.exists(new_path):
                os.chdir(new_path)
            else:
                old_path = old_path.split('/')
                new_path = new_path.split('/')
                if new_path[0] in old_path:
                    for name in old_path:
                        if name == new_path[0]:
                            key = old_path.index(name)
                            path = os.path.join('/', *old_path[1:key],
                                                *new_path)
                            if os.path.exists(path):
                                os.chdir(path)
                elif new_path[0] in my_listdir():
                    path = os.path.join('/', *old_path[1:], *new_path)
                    if os.path.exists(path):
                        os.chdir(path)
                else:
                    print('Путь не существует')
            print('Текущий каталог ', os.getcwd())
        elif menu == 12:
            dirs, files = file_or_dir(print_file=True, print_dir=True)
            with open('listdir.txt', 'w') as file:
                file.write(f'files: {files}\n')
                file.write(f'dirs: {dirs}')
        elif menu == 99:
            pass
        else:
            print('В меню нет такого пункта')
        menu = input_data()

    print('Выход')
