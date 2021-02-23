import time


# проверка любой функции
def test_time(func):
    start_time = time.time()
    a = func()
    finish_time = time.time()
    res_time = finish_time - start_time
    print(f"\nВремя работы данной программы составляет: {res_time}сек.")
    return a


# проверка функции с аргументом и выводом(return)
def testTime(func):
    def wrapper(*args):
        start_time = time.time()
        a = func(*args)
        finish_time = time.time()
        res_time = finish_time - start_time
        print(f"\nВремя работы данной программы составляет: {res_time}сек.")
        return a
    return wrapper
