import random


"""Урок 1 (Парадигма ООП, классы, экземпляры классов, атрибуты)
Объявите класс Paint3D для точек с тремя координатами x, y, z. Создайте несколько
    экземпляров этого класса и через них выведите в консоль значения x, y, z.
    Далее сделайте следующие манипуляции:
а) поменяйте любое значения координаты в классе Paint3D и посмотрите как
    это повлияет на отображение величины экземпляров класса.
б) удалите координату z в классе Paint3D и убедитесь, что она будет отсутствовать
    во всех экземплярах.
в) поменяйте координаты в каком либо экземпляре класса и посмотрите на результать.

"""


class Paint3D:
    x = 1
    y = 1
    z = 1


def prac_1():
    p1 = Paint3D()
    p2 = Paint3D()
    print(f"Экзетмряр 1: x-{p1.x}; y-{p1.y}; z-{p1.z}")
    print(f"Экземпляр 2: x-{p2.x}; y-{p2.y}; z-{p2.z}")
    print("------------------------")
    p1.x = 30
    p1.z = 154
    p2.y = 789
    p2.x = 3048
    delattr(p1, "z")
    print(f"Экзетмряр 1: x-{p1.x}; y-{p1.y}; z-{p1.z}")
    print(f"Экземпляр 2: x-{p2.x}; y-{p2.y}; z-{p2.z}")


# ----------------------------------------------------------------------|-------
"""Урок 2 (Методы класса, конструктор и деструктор)
1. Создайте класс Paint3d, который хранит координаты в виде списка. Пропишите 
    у него конструктор для создания экземпляров с локальными координатами. Также 
    добавте методы, позволяющие изменять координаты и получать их (в виде кортежа)
2. Объявить класс Paint с конструктором, который бы позволял создавать экземпляр 
    на основе другого, уже существующего. Если аргументы в конструктор не передаются, 
    то создается объект с локальными атребутами по умолчанию.
3. Напишите программу, в которой пользователь вводит координаты x, y с клавиатуры, 
    создается соответствующий экземпляр и он сохраняется в списке. Колличество 
    введенных объектов N = 5. Затем вывести их атрибуты в консоль.
"""


class Paint3D:
    def __init__(self, koord):
        self.x = koord[0]
        self.y = koord[1]
        self.z = koord[2]

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def setXYZ(self, xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]

    def __str__(self):
        return f"Координаты точки: x-{self.x}; y-{self.y}; z-{self.z}"


class Paint(Paint3D):
    def __init__(self, koord=[0, 0, 0]):
        Paint3D.__init__(self, koord)


def prac_2_1_2():
    p3d = Paint3D([8, 15, 56])
    print(p3d.__dict__)
    print(p3d)
    print("------------------")
    p3d.setX(678)
    p3d.setZ(1257)
    print(p3d)
    p3d.setXYZ((789, 873, 1587))
    print("------------------")
    print(p3d)
    pt = Paint()
    print(pt.__dict__)
    pt.setY(78)
    print(pt)


# ----------------------------------------------------------------------|-------
class Paint:
    def __init__(self, obj, koord):
        self.obj = obj
        self.x = int(koord[0])
        self.y = int(koord[1])


def prac_2_3():
    N = 5
    l = list()
    for i in range(N):
        a = input("Введите координаты точки - X и Y: ").split()
        l.append(Paint(i + 1, a))
    print(a, l, sep="\n")
    for j in l:
        print(f"Координаты {j.obj}ой точки: x = {j.x}, y = {j.y}")


# ----------------------------------------------------------------------|-------
"""Урок 4 (Свойства (property) и дескрипторы классов)
1. Объявите класс Calendar для хранения данных: даты, месяц, год. Определите 
    свойства для записи и считывания этой информации из этого класса. 
    (ДОПОЛНЕНИЕ: используя __slots__ разрешите использовать только строго определенные 
    локальные свойства в экземплярах класса)
2. Объявите класс Rectangle, хранящий координаты верхней левой точки. Создайте дескрипторы 
    для записи и считывания этих значений в классе (атрибуты с данными координат должны быть приватными)
"""


class Calendar:
    __slots__ = ["d", "m", "y"]

    def __init__(self, d=1, m=1, y=2000):
        self.d = d
        self.m = m
        self.y = y

    @staticmethod
    def __vE(x):
        if isinstance(x, int):
            return True
        else:
            return "Упс!!! Введено не число"

    def setDay(self, d):
        if Calendar.__vE(d):
            self.d = d

    def setMonth(self, m):
        if Calendar.__vE(m):
            self.m = m

    def setYear(self, y):
        if Calendar.__vE(y):
            self.y = y

    def getDate(self):
        return self.d, self.m, self.y


def prac_4_1():
    date = Calendar()

    setattr(date, "d", 8)
    setattr(date, "m", 2)
    setattr(date, "y", 1991)
    print(date.getDate())
    date.setDay(17)
    date.setMonth(6)
    date.setYear(1987)
    print(date.getDate())


# ---------------------------------------------------------------
class CoordValue:  # дискриптор
    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Rectangle:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y


def prac_4_2():
    r1 = Rectangle(5, 6)
    r2 = Rectangle(40, 40)
    print(r1.coordX, r1.coordY)
    r1.coordY = 20

    print(r1.__dict__)
    print(r2.__dict__)


# ----------------------------------------------------------------------|-------
"""Урок 5 (Статические методы и свойства класса)
1. Объявите класс Rectangle (прямоугольник), в котором имеется статический метод, 
    вычисляющий площадь прямоугольника. Этот метод принимает два параметра (ширину и длину), 
    вызывается в конструкторе для вычисления площади конкретного прямоугольника и результат 
    присваивается локальному свойству создаваемого экземпляра класса.
2. Создайте класс Dog (собака), в каждом его экземпляре создавайте несколько локальных свойств 
    (например: имя, возраст, порода) и сделайте так, чтобы можно было создать не более пяти экземпляров этого класса.
"""


class Rectangle:
    def __init__(self, w=1, h=1):
        self.__w = w
        self.__h = h
        self.__s = Rectangle.area(self.__w, self.__h)

    @staticmethod
    def area(w, h):
        return w * h

    def getS(self):
        return self.__s


def prac_5_1():
    r1 = Rectangle(5, 4)
    r2 = Rectangle(45, 89)
    r3 = Rectangle(77, 3)
    r4 = Rectangle()
    print(r1.getS())
    print(r2.getS())
    print(r3.getS())
    print(r4.getS())


# --------------------------------------------------------
class Dog:
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            # cls.self.__name = super(Dog, cls).__new__(cls)
            obj = super(Dog, cls).__new__(cls)
            return obj
        else:
            print(f"Экземпляр класса {Dog.__name__} уже создан {Dog.__count} раз")

    # __instance = None
    # def __new__(cls, *args, **kwargs):
    #     if not isinstance(cls.__instance, cls):
    #         cls.__instance = super(Dog, cls).__new__(cls)
    #         cls.__count += 1
    #     else:
    #         print(f"Экземпляр класса {Dog.__name__} уже создан {Dog.__count} раз")

    def __init__(self, name, age, poroda):
        Dog.__count += 1
        self.name = name
        self.age = age
        self.poroda = poroda

    def getDog(self):
        return self.name, self.age, self.poroda


def prac_5_2():  # ?
    d1 = Dog("Жучка", 4, "Мопс")
    d2 = Dog("Белка", 5, "Дворняга")
    d3 = Dog("Стрелка", 3, "Дворняга")
    d4 = Dog("Пух", 1, "Лайка")
    d5 = Dog("Шоц", 9, "Шпиц")
    d6 = Dog("Булдан", 2, "Рабладор")
    # print(d1.getDog(), d2.getDog(), d3.getDog(), d4.getDog(), d5.getDog(), d6.getDog(), sep="\n")
    print(id(d1), id(d2), id(d3), id(d4), id(d5), id(d6), sep="\n")


# ----------------------------------------------------------------------|-------
"""Урок 6 (Простое наследование классов)
1.Создайте суперкласс "Персональные компьютеры" и на его основе подклассы: "Настольный ПК" и "Ноутбуки". 
    В базовом классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных 
    классах уникальные свойства:
- для настольных: монитор, клавиатура, мышь, их габариты. И метод для вызова этой информации в консоль.
- для ноутбука: габариты, диагональ экрана. И метод для вызова этой информации в консоль.
2. Повторите это задание для суперкласса "Человек" и подклассов "Мужчина" и "Женщина". Подумайте 
    какие общие характеристики можно выделить в суперкласс и какие частные свойства указать в подклассах.
"""


class Pc:
    sizeMem = 4096
    hdd = 1000
    model = "Asus"
    CPU = "Intel"


class Nout(Pc):
    __size = 130, 100
    __disp = 15, 6

    def __str__(self):
        return f"Марка - {self.model}\nПроцессор - {self.CPU}\nЖесткий диск - {self.hdd}\nОперативная память - {self.sizeMem}\n" \
               f"Габариты - {self.__size}\nДисплей - {self.__disp}"


class InTable(Pc):
    __mon = "Acer"
    __keyb = "Sven"
    __mouse = "Gaming"

    def __str__(self):
        return f"Марка - {self.model}\nПроцессор - {self.CPU}\nЖесткий диск - {self.hdd}\nОперативная память - {self.sizeMem}\n" \
               f"Монитор - {self.__mon}\nКлавиатура - {self.__keyb}\nМышь - {self.__mouse}"


def prac_6_1():
    nout = Nout()
    pc = InTable()
    nout.model = "HP"
    pc.CPU = "AMD"
    print(nout, pc, sep="\n------------\n")


# -----------------------------------------------------------
class Person:
    def __init__(self, name, age, rost, ves):
        self._name = name
        self._age = age
        self._rost = rost
        self._ves = ves


class Man(Person):
    def __init__(self, name, age, rost, ves, car):
        super().__init__(name, age, rost, ves)
        self.__car = car

    def __str__(self):
        return f"Мужчина\nИмя - {self._name}\nВозраст - {self._age}\nРост - {self._rost}\nВес - {self._ves}\nМашина - {self.__car}"


class Woman(Person):
    def __init__(self, name, age, rost, ves, prich):
        super().__init__(name, age, rost, ves)
        self.__prich = prich

    def __str__(self):
        return f"Женщина\nИмя - {self._name}\nВозраст - {self._age}\nРост - {self._rost}\nВес - {self._ves}\nЦвет волос - {self.__prich}"


def prac_6_2():
    m = Man("Александр", 33, 183, 97, "Skoda")
    w = Woman("Анна", 29, 160, 53, "Рыжий")
    print(m, w, sep="\n------------------\n")


# ----------------------------------------------------------------------|-------
"""Урок 7 (Переопределение и перегрузка методов)
1. Создайте базовый класс "Стол" и дочерний: "Прямоугольные столы" и 
    "Круглые столы". Через конструктор базового класса передайте размер
    поверхности стола: для прямоугольного - ширина и длинна, для 
    круглого радиус. В дочерних классах реализуйте метод вычисления 
    площади поверхности стола.
2. Создайте класс Animal (животные) и разные производные от него 
    подклассы: Fox, Bird, Cat, Dog и т.д. Реализуйте у них общий метод
    say(), который бы возвращал звук, издаваемый этим животным. Создайте
    кортеж из нескольких этих экземпляров классов, переберите их в цикле
    и выведите в консоль их звуки (вызовите метод say()).
"""


class Table:
    __PI = 3.1415

    def __init__(self, *args):
        if len(args) == 2:
            self._width = args[0]
            self._length = args[1]
        elif len(args) == 1:
            self._radius = args[0]
        else:
            print("Неверный ввод!")


class RectTable(Table):
    def area(self):
        return self._width * self._length


class RoundTable(Table):
    def area(self):
        return round(self.__PI * self._radius**2, 2)


def prac_7_1():
    table1 = RectTable(23, 12)
    table2 = RoundTable(34)
    # print(table1.__dict__, table2.__dict__, sep="\n")
    print(table1.area())
    print(table2.area())


# --------------------------------------------------------
# from abc import ABC, abstractmethod
class Animal:
    def __init__(self, sound):
        self._sound = sound

    # @abstractmethod
    def say(self):
        raise NotImplementedError("В дочернем классе не метода sey()")


class Fox(Animal):
    def say(self):
        print(f"{Fox.__name__} издает звук: {self._sound}")


class Bird(Animal):
    def say(self):
        print(f"{Bird.__name__} издает звук: {self._sound}")


class Cat(Animal):
    def say(self):
        print(f"{Cat.__name__} издает звук: {self._sound}")


class Dog(Animal):
    def say(self):
        print(f"{Dog.__name__} издает звук: {self._sound}")


class Mouse(Animal):
    def say(self):
        print(f"{Mouse.__name__} издает звук: {self._sound}")


def prac_7_2():
    lst = list()

    lst.append(Fox("Фыр-фыр"))
    lst.append(Bird("Чирик-чирик"))
    lst.append(Cat("Мяу-мяу"))
    lst.append(Dog("Гав-гав"))
    lst.append(Mouse("Пи-пи-пи"))

    for i in lst:
        i.say()


# ----------------------------------------------------------------------|-------
"""Урок 8 (Множественное наследование)
Создайте дочерний класс Motherboard (материнская плата), которая
    наследуется от классов: CPU (процессор), GPU (графический 
    сопроцессор), Memory (память). В свою очередь CPU наследуется от 
    классов: AMD и Intel, GPU от классов NVidia и GeForce.
Создайте экземпляр класса Matherboard и наполните ее конкретным
    содержимым (локальным свойствам этого объекта присвойте 
    определенные значения). Определите вспомогательные методы в базовых
    классах и выведите итоговую информацию в консоль с помощью метода 
    showInfo() класса Matherboard.
"""


class AMD:
    def __init__(self, amd, *args):
        self._amd = amd
        super().__init__(*args)


class Intel:
    def __init__(self, intel, *args):
        self._intel = intel
        super().__init__(*args)


class Nvidia:
    def __init__(self, nvidia, *args):
        self._nvidia = nvidia
        super().__init__(*args)


class GeForce:
    def __init__(self, geforce, *args):
        self._geforce = geforce
        super().__init__(*args)


class CPU(AMD, Intel):
    pass


class GPU(Nvidia, GeForce):
    pass


class Memory:
    def __init__(self, memory, *args):
        self._memory = memory
        super().__init__(*args)


class Motherboard(CPU, GPU, Memory):
    def showInfo(self):
        print(f"AMD - {self._amd}\nIntel - {self._intel}\nNVidia - {self._nvidia}\n"
              f"GeForce - {self._geforce}\nMemory - {self._memory}")


def prac_8_1():
    pc = Motherboard("AMD", "INTEL", "NVIDIA", "GEFORCE", "16GB")
    pc.showInfo()

    #print(Motherboard.__mro__)


# -------------------------------------------------
class AMD:
    def __init__(self):
        print(f"Обратились к классу {AMD.__name__}")
        super().__init__()


class Intel:
    def __init__(self):
        print(f"Обратились к классу {Intel.__name__}")
        super().__init__()


class Nvidia:
    def __init__(self):
        print(f"Обратились к классу {Nvidia.__name__}")
        super().__init__()


class GeForce:
    def __init__(self):
        print(f"Обратились к классу {GeForce.__name__}")
        super().__init__()


class CPU(AMD, Intel):
    def __init__(self):
        print(f"Обратились к классу {CPU.__name__}")
        super().__init__()


class GPU(Nvidia, GeForce):
    def __init__(self):
        print(f"Обратились к классу {GPU.__name__}")
        super().__init__()


class Memory:
    def __init__(self):
        print(f"Обратились к классу {Memory.__name__}")
        super().__init__()


class Motherboard(CPU, GPU, Memory):
    def __init__(self, amd, intel, nvidia, geforce, memory):
        self._amd = amd
        self._intel = intel
        self._nvidia = nvidia
        self._geforce = geforce
        self._memory = memory
        super().__init__()

    def showInfo(self):
        print(f"AMD - {self._amd}\nIntel - {self._intel}\nNVidia - {self._nvidia}\n"
              f"GeForce - {self._geforce}\nMemory - {self._memory}")


def prac_8_2():
    pc = Motherboard("AMD", "INTEL", "NVIDIA", "GEFORCE", "16GB")
    #print(Motherboard.__mro__)
    pc.showInfo()

# ----------------------------------------------------------------------|-------
"""Урок 9 (Перегрузка операторов)
1. Напишите класс Paint3D для хранения координат в трехмерном 
    пространстве (x, y, z). Реализуйте перегрузку операторов сложения,
    вычитания, умножения и деления для этого класса. Также сделайте
    возможность сравнения координат между собой и запись-считывание
    значений через ключи: "x", "y", "z".
2. Напишите класс Matrix для работы с матрицами. Реализуйте перегрузку
    операторов сложения и вычитания для матриц разных размеров.
    Перегрузите оператор умножения для матриц, которые могут быть 
    перемножены. Также сделайте возможность сравнения матриц между 
    собой (на равенство и неравенство).
3. Напишите класс Complex для работы с комплексными числами. Реализуйте
    операторы сложения, вычитания и умножения. Также сделайте 
    возможность присвоения действительных и мнимых значений через ключи
    <rel> и <img> и через свойства rel, img, реализованных с помощью
    дескрипторов.
"""


class Paint3D:
    def __init__(self, x, y, z):
        if Paint3D.__checkF(x) and Paint3D.__checkF(y) and Paint3D.__checkF(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise TypeError("Введено не число!")

    # Проверка ввода числа
    @staticmethod
    def __checkF(c):
        return isinstance(c, int) or isinstance(c, float)

    # Геттер координат точек
    def getPaint(self):
        return self.__x, self.__y, self.__z

    # Сложение экземпляров класса
    def __add__(self, other):
        if not isinstance(other, Paint3D):
            raise ArithmeticError("Правый операнд должен быть типом Point3D")
        __a = other.getPaint()
        return Paint3D(self.__x + __a[0], self.__y + __a[1], self.__z + __a[2])

    # Вычитание экземпляров класса
    def __sub__(self, other):
        if not isinstance(other, Paint3D):
            raise ArithmeticError("Правый операнд должен быть типом Point3D")
        __a = other.getPaint()
        return Paint3D(self.__x - __a[0], self.__y - __a[1], self.__z - __a[2])

    # Умножение экземпляров класса
    def __mul__(self, other):
        if not isinstance(other, Paint3D):
            raise ArithmeticError("Правый операнд должен быть типом Point3D")
        __a = other.getPaint()
        return Paint3D(self.__x * __a[0], self.__y * __a[1], self.__z * __a[2])

    # Деление экземпляров класса
    def __truediv__(self, other):
        if not isinstance(other, Paint3D):
            raise ArithmeticError("Правый операнд должен быть типом Point3D")
        __a = other.getPaint()
        return Paint3D(round(self.__x / __a[0], 2), round(self.__y / __a[1], 2),
                       round(self.__z / __a[2], 2))

    # Сравнение экземпляров класса
    def __eq__(self, other):
        if not isinstance(other, Paint3D):
            raise ArithmeticError("Правый операнд должен быть типом Point3D")
        __a = other.getPaint()
        return self.__x == __a[0] and self.__y == __a[1] and self.__z == __a[2]

    # Считывание значения через ключ
    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        if item == "x":
            return self.__x
        elif item == "y":
            return self.__y
        elif item == "z":
            return self.__z
        else:
            return "Неверный координата"

    # Запись значения через ключ
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if key == "x":
            self.__x = value
        elif key == "y":
            self.__y = value
        elif key == "z":
            self.__z = value
        else:
            return "Неверный координата"


# Функция сравнения экземпляров класса Paint3D (объектов)
def compr(obj1: Paint3D, obj2: Paint3D):
    if obj1 == obj2:
        print(f"Координаты точек {obj1.getPaint()} и {obj2.getPaint()} одинаковые")
        return True
    else:
        print(f"Увы, координаты точек {obj1.getPaint()} и {obj2.getPaint()} разные")
        return False

def prac_9_1():
    p1 = Paint3D(2, 3, 7)
    p2 = Paint3D(5, 1, 6)
    p7 = Paint3D(5, 1, 6)
    p3 = p1 + p2
    p4 = p1 - p2
    p5 = p1 * p2
    p6 = p1 / p2
    print(p3.getPaint())
    print(p4.getPaint())
    print(p5.getPaint())
    print(p6.getPaint())
    compr(p1, p2)
    compr(p2, p7)
    print(p1["x"], p2["y"], p3["z"])
    p6["z"] = 0
    print(p6.getPaint())


# -------------------------------------------------------
def genMatrix(n: int, m: int):
    return [[random.randrange(1, 10) for i in range(n)] for j in range(m)]


class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix

    @staticmethod
    def checkObj(obj1, obj):
        if len(obj1) != len(obj.getMatrix()):
            print("Матрицы разные")
            exit(0)

    def getMatrix(self):
        return self.__matrix

    def __add__(self, other):
        # return Matrix(numpy.add(self.__matrix, other.getMatrix()))
        self.checkObj(self.__matrix, other)
        self.__t = other.getMatrix()
        self.__r = list()
        for i in range(len(self.__matrix)):
            self.__temp = list()
            for j in range(len(self.__matrix[i])):
                    self.__temp.append(self.__matrix[i][j] + self.__t[i][j])
            self.__r.append(self.__temp)
        return Matrix(self.__r)


def prac_9_2():  # Сложить две матрици разного размера????
    m1 = Matrix(genMatrix(3, 3))
    m2 = Matrix(genMatrix(3, 3))
    m3 = m1 + m2
    print(m1.getMatrix())
    print(m2.getMatrix())
    print(m3.getMatrix())


# --------------------------------------------------
# class Change: ????
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.__name] = value


class Complex:
    # rel = Change()
    # img = Change()

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        self.__comp = complex(self.real, self.imag)

    @property
    def getComp(self):
        return self.__comp

    @getComp.setter
    def rel(self, real):
        self.__comp = complex(real, self.__comp.imag)

    @getComp.setter
    def img(self, imag):
        self.__comp = complex(self.__comp.real, imag)

    def __add__(self, other):
        return Complex(self.__comp.real + other.getComp.real,
                       self.__comp.imag + other.getComp.imag)

    def __sub__(self, other):
        return Complex(self.__comp.real - other.getComp.real,
                       self.__comp.imag - other.getComp.imag)

    def __mul__(self, other):
        return Complex(self.__comp.real * other.getComp.real - self.__comp.imag * other.getComp.imag,
                       self.__comp.imag * other.getComp.real + self.__comp.real * other.getComp.imag)

    def __truediv__(self, other):
        return Complex((self.__comp.real * other.getComp.real + self.__comp.imag * other.getComp.imag) / (other.getComp.real ** 2 + other.getComp.imag ** 2),
                       (self.__comp.imag * other.getComp.real - self.__comp.real * other.getComp.imag) / (other.getComp.real ** 2 + other.getComp.imag ** 2))

    def __setitem__(self, key, value):
        if isinstance(key, str) and isinstance(value, int):
            if key == "rel":
                self.__comp = complex(value, self.__comp.imag)
            elif key == "img":
                self.__comp = complex(self.__comp.real, value)
            else:
                print("Такогоключа нет")
        else:
            print("Ключ не строка")


def prac_9_3():
    c1 = Complex(-5, -1)
    c2 = Complex(-1, 1)
    print(c1.getComp)
    c1["rel"] = 9
    c1["img"] = 8
    print(c1.getComp)
    print(c2.getComp)
    print("------------")
    c3 = c1 + c2
    print("+", c3.getComp)
    c3 = c1 - c2
    print("-", c3.getComp)
    c3 = c1 * c2
    print("*", c3.getComp)
    c3 = c1 / c2
    print("/", c3.getComp)
    print("------------")
    c3.rel = 100
    c3.img = 100
    c2["img"] = 10
    print(c3.getComp)
    print(c2.getComp)


# ----------------------------------------------------------------------|-------
"""Урок 10 (Пример собственных исключений и итераторов)
1. Измените класс Image так, чтобы в нем появился метод resize(width, heigth). Если новая 
    ширина или высота меньше текущего значения, все цвета, оказавшиеся за пределами новых 
    границ изображения, должны удаляться. Если в качестве нового значения ширины или высоты 
    передается None, соответствующее значение ширины или высоты должно оставаться без изменений.
2. Реализуйте класс ListInt для хранения списка целых чисел и сделайте его итерируемым так, 
    чтобы значения возвращались с конца в начало.
3. Создайте класс Persons для хранения списка уникальных посетителей клуба. Сделайте 
    возможность перебора гостей итератором(ми) следующим образом:
- с выводом только их имен
- с выводом только их возраста
- с выводом только их фамилии
"""


class CoordError(Exception):
    pass


class ImageXIterator:
    def __init__(self, img, y: int):
        self.__img = img
        self.__y = y
        self.__limit = img.width
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration
        self.__x += 1
        return self.__img[self.__x - 1, self.__y]


class ImageYIterator:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration
        self.__y += 1
        return ImageXIterator(self.__img, self.__y-1)


class Image:
    def __init__(self, width, height, background="-"):
        self.__width = width
        self.__height = height
        self.__background = background
        self.__pixels = dict()
        self.__colors = {self.__background}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError("Должны быть две координаты точки")
        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError("Координаты за пределами изображения")

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)
        if color == self.__background:
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        return ImageYIterator(self)

    # Задание
    def resize(self, width, height):
        if width is None:
            width = self.__width
        if height is None:
            height = self.__height
        # Удаляет лишнее
        if width < self.__width or height < self.__height:
            self.__width = width
            self.__height = height


# Пример класса итератора
# class MyIter:
#     def __init__(self, limit):
#         self.__limit = limit
#         self.__num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__num >= self.__limit:
#             raise StopIteration
#         self.__num += 1
#         return self.__num


def prac_10_1():
    img = Image(20, 10)
    img[3, 2] = "*"
    img[4, 2] = "*"
    img[5, 2] = "*"
    # for y in range(img.height):
    #     for x in range(img.width):
    #         print(img[x, y], end="")
    #     print()
    for row in img:
        for pixel in row:
            print(pixel, end="")
        print()
    print()
    img.resize(10, None)
    for row in img:
        for pixel in row:
            print(pixel, end="")
        print()


# -----------------------------------------------------
class MyIterator:
    def __init__(self, fig):
        self.__fig = fig.getFig
        self.__num = len(self.__fig)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num <= 0:
            raise StopIteration
        self.__num -= 1
        return self.__fig[self.__num]


class ListInt:
    def __init__(self, *fig):
        self.__fig = list(fig)

    @property
    def getFig(self):
        return self.__fig

    def __iter__(self):
        return MyIterator(self)


def prac_10_2():
    # a = [i for i in range(10)]
    # f = ListInt(a)

    f = ListInt(12, 6, 9, 87, 85, 1, 6, 99, 71)
    print(f.getFig)
    for i in f:
        print(i, end=", ")


# ---------------------------------------------------------
class PersonsIterator:
    def __init__(self, pers):
        self.__pers = pers
        self.__limit = len(self.__pers)
        self.__num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration
        self.__num += 1
        return f"{self.__num} - {self.__pers[self.__num - 1]}"


class Persons:
    def __init__(self, person):
        self.__person = person
        self.__surname = [person[s][0] for s in range(len(person))]
        self.__name = [person[n][1] for n in range(len(person))]
        self.__age = [person[a][2] for a in range(len(person))]

    @property
    def person(self):
        return self.__person

    # Так нельзя, но работает))
    def __iter__(self, f):
        if f == "surname":
            return PersonsIterator(self.__surname)
        elif f == "name":
            return PersonsIterator(self.__name)
        elif f == "age":
            return PersonsIterator(self.__age)
        else:
            raise KeyError("Неверный ключ итератора")


def prac_10_3():
    people = [
        ["Иванов", "Александр", 25],
        ["Чапкин", "Сергей", 38],
        ["Зайцев", "Николай", 19],
        ["Бирсин", "Василий", 21],
        ["Бозак", "Евгений", 46],
    ]

    p = Persons(people)
    for i in p.__iter__("surname"):
        print(i)
    for i in p.__iter__("name"):
        print(i)
    for i in p.__iter__("age"):
        print(i)


# ----------------------------------------------------------------------|-------
"""Урок 11 (Функторы и менеджеры контекстов)
1. Создайте функтор для определения порядка сортировки списка p, состоящий из объектов класса Person:
class Person:
    def __init__(self, surname, forename, old):
        self.forename = forename
        self.surname = surname
        self.old = old
p = [Person("Иванов", "Иван", 20),
     Person("Петров", "Степан", 21),
     Person("Сидоров", "Альберт", 25)]
То есть, вызывая функтор (пусть он называется SortKey) с названием поля SortKey("surname"), 
    сортировка выполнялась бы по этому свойству. Если указать сразу два значения: SortKey("surname", "forname"), 
    то сортировка делалась бы по фамилии, но при их равенстве - по имени.
(Подсказка: используйте метод sort списка p и его именованный параметр key).
2. Создайте менеджер контекста для безопасной обработки элементов словаря. В случае возникновения 
    исключения словарь должен оставаться без изменений. Иначе (при успешной работе) он сохранял бы все изменения.
"""


class Person:
    def __init__(self, surname, forename, old):
        self.forename = forename
        self.surname = surname
        self.old = old


class SortKey:
    def __init__(self, lst):
        self.__lst = lst

    # def algSort(self, args, test): # Попробовать упростить повторяющийся код в __call__ в отдельной функции
    #     self.__tl = list()
    #     #if args == test:
    #
    #
    #     for i in range(len(self.__lst)):
    #         self.__tl.append(self.__lst[i].forename)
    #     self.__tl.sort()
    #     self.__res = []
    #     while len(self.__tl) > 0:
    #         for i in self.__tl:
    #             for j in range(len(self.__tl)):
    #                 if i == self.__lst[j].forename:
    #                     self.__res.append([self.__lst[j].forename, self.__lst[j].surname, self.__lst[j].old])
    #                     self.__tl.remove(i)

    def __call__(self, args, **kwargs):
        self.__tl = list()
        self.__res = []

        if args == "forename":
            for i in range(len(self.__lst)):
                self.__tl.append(self.__lst[i].forename)
            self.__tl.sort()
            for i in self.__tl:
                for j in range(len(self.__tl)):
                    if i == self.__lst[j].forename:
                        self.__res.append((self.__lst[j].surname, self.__lst[j].forename, self.__lst[j].old))

        elif args == "surname":
            for i in range(len(self.__lst)):
                self.__tl.append(self.__lst[i].surname)
            self.__tl.sort()
            for i in self.__tl:
                for j in range(len(self.__tl)):
                    if i == self.__lst[j].surname:
                        self.__res.append((self.__lst[j].surname, self.__lst[j].forename, self.__lst[j].old))

        elif args == "old":
            for i in range(len(self.__lst)):
                self.__tl.append(self.__lst[i].old)
            self.__tl.sort()
            for i in self.__tl:
                for j in range(len(self.__tl)):
                    if i == self.__lst[j].old:
                        self.__res.append((self.__lst[j].surname, self.__lst[j].forename, self.__lst[j].old))

        else:
            return f"{args} - не верный ключ"

        return self.__res


def prac_11_1():
    p = [Person("Иванов", "Иван", 20),
         Person("Петров", "Степан", 21),
         Person("Сидоров", "Альберт", 25)]

    s1 = SortKey(p)

    print(s1("surname"))
    print(s1("forename"))
    print(s1("old"))


# --------------------------------------------------
class SaveDict:
    def __init__(self, dct):
        self.__dct = dct

    def __enter__(self):
        self.__temp = self.__dct.copy()
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if len(self.__temp) == len(self.__dct):
            if exc_tb is None:
                self.__dct.clear()
                self.__dct.update(list(self.__temp.items()))
        else:
            print("Запрещено добаклять или удалять ключи в словаре")
        return False


def prac_11_2():
    d = {"a": "Aa", "b": "Bb", "c": "Cc"}

    with SaveDict(d) as dc:
        dc["a"] = "worked"
        # dc["z"] = "Zz"
        # dc["x"] = "Zz"
        # print(f"Уалено - {dc.popitem()}")

    for i in d:
        print(f"{i} - {d.get(i)}")
    print(d)
# ----------------------------------------------------------------------|-------
