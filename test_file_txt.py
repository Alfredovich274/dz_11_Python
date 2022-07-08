from files_manager import file_or_dir
from use_functions import history_buy, buy


def test_file_or_dir():
    assert type(file_or_dir(print_file=True)) == tuple
    assert type(file_or_dir(print_file=True)[0]) == str


def test_history_buy():
    assert type(history_buy()) == str


def test_buy():
    assert buy(5, 6, 100) == 5
    assert buy(10, 5, 100) == 5
    with open('my_history.txt', 'r') as file:
        test_text = file.read()
    assert test_text.find('100 - 5') > 0
