from files_manager import my_listdir, my_isfile, my_isdir, my_mkdir, my_remove
import os


def test_my_listdir():
    assert len(my_listdir()) == len(os.listdir())
    assert True == ('files_manager.py' in my_listdir())


def test_my_isfile():
    assert True == my_isfile('files_manager.py')
    assert my_isfile('venv') == False


def test_my_isdir():
    assert my_isdir('files_manager.py') == False
    assert my_isdir('venv') == True


# Тесты грязных функций
def test_my_mkdir():
    name = 'dirty_folder'
    assert os.path.exists(name) == False
    my_mkdir(name)
    assert os.path.exists(name) == True


def test_my_remove():
    name = 'dirty_folder'
    assert os.path.exists(name) == True
    my_remove(name)
    assert os.path.exists(name) == False

