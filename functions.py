import math


def my_filter(iterable, function):
    return list(filter(function, iterable))


def my_map(x):
    return x.upper()


def my_sorted(x):
    return x[-1]


def my_pi():
    return math.pi


def my_sqrt(x):
    return math.sqrt(x)


def my_pow(x, y):
    return math.pow(x, y)


def my_hypot(x, y):
    return math.hypot(x, y)
