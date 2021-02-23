from time import time


def timeTest(func):
    start_time = time()
    func()
    finish_time = time()
    print(f"------------------------\nВремя выполнения программы: {finish_time - start_time} сек.")


# ---------Задание 1------------------------
class LittleBell:
    @staticmethod
    def sound():
        print("ding")


# @timeTest
def task_1():
    bell = LittleBell()
    bell.sound()
    bell.sound()
    bell.sound()


# ---------Задание 2------------------------
class Button:
    def __init__(self):
        self.__clk = 0

    def click(self):
        self.__clk += 1

    def click_count(self):
        return self.__clk

    def reset(self):
        self.__clk = 0


# @timeTest
def task_2():
    button = Button()

    # Пример 1
    button.click()
    button.click()
    print(button.click_count())
    button.click()
    print(button.click_count())

    # Пример 2
    button.click()
    button.click()
    print(button.click_count())
    button.reset()
    button.click()
    print(button.click_count())


# ---------Задание 3------------------------
class Balance:
    def __init__(self):
        self.__rt = 0
        self.__lt = 0

    def add_right(self, rt):
        if isinstance(rt, int):
            self.__rt += rt
        else:
            print("R должно быть целое число")
            exit()

    def add_left(self, lt):
        if isinstance(lt, int):
            self.__lt += lt
        else:
            print("L должно быть целое число")
            exit()

    def result(self):
        if self.__rt == self.__lt:
            return "="
        elif self.__rt > self.__lt:
            return "R"
        else:
            return "L"


# @timeTest
def task_3():
    balance = Balance()

    # Пример 1
    # balance.add_right(10)
    # balance.add_left(9)
    # balance.add_left(2)
    # print(balance.result())

    # Пример 2
    balance.add_right(10)
    balance.add_left(5)
    balance.add_left(5)
    print(balance.result())
    balance.add_left(1)
    print(balance.result())


# ---------Задание 4------------------------
class OddEvenSeparator:
    def __init__(self):
        self.__odd = list()
        self.__even = list()

    # getter
    def odd(self):
        return self.__odd

    def even(self):
        return self.__even

    def add_number(self, n):
        if not isinstance(n, int):
            raise TypeError
        else:
            if n % 2 != 0:
                self.__odd.append(n)
            else:
                self.__even.append(n)


# @timeTest
def task_4():
    separator = OddEvenSeparator()

    separator.add_number(1)
    separator.add_number(5)
    separator.add_number(6)
    separator.add_number(8)
    separator.add_number(3)
    print(" ".join(map(str, separator.even())))
    print(" ".join(map(str, separator.odd())))


# ---------Задание 5------------------------
class BigBell:
    __count = 0

    def sound(self):
        self.__count += 1
        if self.__count % 2 != 0:
            print("ding")
        else:
            print("dong")


# @timeTest
def task_5():
    bell = BigBell()
    bell.sound()
    bell.sound()
    bell.sound()


# ---------Задание 6------------------------
class MinMaxWordFinder:
    __fullWord = list()  # список всех слов

    # метод сортировки
    def __sortWord(self, arg):
        self.__needLen = len(self.__fullWord[0])   # размер самого длинного или короткого слова
        self.__res = list()            # список для результом днинных или коротких слов
        if arg == "long":
            for i in self.__fullWord[1:]:     #
                if len(i) > self.__needLen:   # найти способ записать это одной строчкой!!!
                    self.__needLen = len(i)   #
        elif arg == "short":
            for i in self.__fullWord[1:]:
                if len(i) < self.__needLen:
                    self.__needLen = len(i)
        for j in self.__fullWord:
            if len(j) == self.__needLen:
                self.__res.append(j)
        self.__res.sort()
        return self.__res

    # добавление
    def add_sentence(self, st):
        self.__temp = st.lower().strip("!,.?-=+*/-").split()
        for i in self.__temp:
            self.__fullWord.append(i)

    # вывод коротких слов
    def shortest_word(self):
        return self.__sortWord("short")

    # вывод длинных слов
    def longest_word(self):
        return self.__sortWord("long")


# @timeTest
def task_6():
    finder = MinMaxWordFinder()

    # пример 1
    finder.add_sentence("hello abc world")
    finder.add_sentence("def asdf qwert")
    print(" ".join(finder.shortest_word()))
    print(" ".join(finder.longest_word()))

    # пример 2
    # finder.add_sentence("hello")
    # finder.add_sentence("abs")
    # finder.add_sentence("world")
    # finder.add_sentence("def")
    # finder.add_sentence("asdf")
    # finder.add_sentence("qwert")
    # print(" ".join(finder.shortest_word()))
    # print(" ".join(finder.longest_word()))
    #
    # пример 3
    # finder.add_sentence("hello")
    # finder.add_sentence("  abc    def    ")
    # finder.add_sentence("world")
    # finder.add_sentence("          abc        ")
    # finder.add_sentence("asdf")
    # finder.add_sentence("qwert")
    # print(" ".join(finder.shortest_word()))
    # print(" ".join(finder.longest_word()))


# ---------Задание 7------------------------
class BoundingRectangle:
    def __init__(self):
        self.__points = list()

    def add_point(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.__points.append((x, y))
        else:
            print(f"Точка {x, y} не добавлена. X и Y должны быть целыми числами")

    def width(self):
        return abs(self.left_x()) + abs(self.right_x())

    def height(self):
        return abs(self.bottom_y()) + abs(self.top_y())

    def bottom_y(self):
        return min([self.__points[i][1] for i in range(len(self.__points))])

    def top_y(self):
        return max([self.__points[i][1] for i in range(len(self.__points))])

    def left_x(self):
        return min([self.__points[i][0] for i in range(len(self.__points))])

    def right_x(self):
        return max([self.__points[i][0] for i in range(len(self.__points))])


# @timeTest
def task_7():
    rect = BoundingRectangle()

    # пример 1
    # rect.add_point(-1, -2)
    # rect.add_point(3, 4)
    # print(rect.left_x(), rect.right_x())
    # print(rect.bottom_y(), rect.top_y())
    # print(rect.width(), rect.height())

    # пример 2
    # rect.add_point(10, 20)
    # rect.add_point(5, 7)
    # rect.add_point(6, 3)
    # print(rect.left_x(), rect.right_x())
    # print(rect.bottom_y(), rect.top_y())
    # print(rect.width(), rect.height())

    # пример 3
    rect.add_point(-11, -12)
    rect.add_point(13, -14)
    rect.add_point(-15, 10)
    print(rect.left_x(), rect.right_x())
    print(rect.bottom_y(), rect.top_y())
    print(rect.width(), rect.height())
    print()
    rect.add_point(-21, -12)
    rect.add_point(13, -14)
    rect.add_point(-15, 36)
    print(rect.width(), rect.height())
    print(rect.left_x(), rect.right_x())
    print(rect.bottom_y(), rect.top_y())
    print()
    rect.add_point(-21, 78)
    rect.add_point(13, -14)
    rect.add_point(-55, 36)
    print(rect.bottom_y(), rect.top_y())
    print(rect.width(), rect.height())
    print(rect.left_x(), rect.right_x())
