"""
2. В модуле написать тесты для встроенных функций filter, map, sorted, а также
для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на
каждую функцию - тем лучше
"""
from functions import my_filter, my_map, my_sorted, my_pi, my_sqrt,\
    my_pow, my_hypot


letters = ['ae', 'bf', 'cg', 'dh']


def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]
    assert my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2]
    assert my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5]
    assert my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b']


def test_my_map():
    assert list(map(my_map, letters)) == ['AE', 'BF', 'CG', 'DH']


def test_my_sorted():
    assert sorted(letters, key=my_sorted,
                  reverse=True) == ['dh', 'cg', 'bf', 'ae']


def test_my_pi():
    assert my_pi() == 3.141592653589793


def test_my_sqrt():
    assert my_sqrt(1) == 1
    assert my_sqrt(2) == 2**(1/2)
    assert my_sqrt(5) == 5 ** (1 / 2)


def test_my_pow():
    assert my_pow(1, 1) == 1 ** 1
    assert my_pow(2, 2) == 2 ** 2
    assert my_pow(3, 5) == 3 ** 5


def test_my_hypot():
    assert my_hypot(1, 1) == (1**2 + 1**2) ** (1/2)
    assert my_hypot(3, 4) == (3**2 + 4**2) ** (1/2)
    assert my_hypot(4, 7) == (4**2 + 7**2) ** (1/2)
