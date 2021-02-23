# Объектно-ориентированное программирование на Python


#--------------------------------------------------------
'''Раздел 4 (2 Создание класса)
1) Создайте класс прямоугольника со следующими свойства:
    координаты левого верхнего угла, ширина и высота.
2) Создайте экземпляр этого класса.
3) Измените значения его свойств и выведите их.
'''


def lesson_2():
    class Rectangle:
        left_top_corner_x = 0
        left_top_corner_y = 0
        width = 0
        heigth = 0


    rec1 = Rectangle()
    x1 = rec1.left_top_corner_x = 10
    y1 = rec1.left_top_corner_y = 15
    w1 = rec1.width = 20
    h1 = rec1.heigth = 30    
    print(f"Вегхний левый угол: х = {x1}; y = {y1}\nШирина = {w1}; Высота = {h1}")


#--------------------------------------------------------
'''Раздел 4 (3 Конструктор класс)
1) Возьмите за основу класс прямоугольника из предыдущего
    упражнения.
2) Создайте у него конструктор, принимающий в качестве
    параметров все его свойства.
3) Внутри конструктора инициализируйте свойства переданными
    в него параметрами.
4) Используя конструктор, создайте экземпляр класса.
5) Выведите его свойства.
'''


def lesson_3():
    class Rectangle:
        left_top_corner_x = 0
        left_top_corner_y = 0
        width = 0
        heigth = 0

        def __init__(self, left_top_corner_x, left_top_corner_y, width, heigth):
            self.left_top_corner_x = left_top_corner_x
            self.left_top_corner_y = left_top_corner_y
            self.width = width
            self.heigth = heigth


    r1 = Rectangle(15, 20, 40, 50)
    print(f"Вегхний левый угол: х = {r1.left_top_corner_x}; y = {r1.left_top_corner_y}\nШирина = {r1.width}; Высота = {r1.heigth}")


#--------------------------------------------------------
'''Раздел 4 (4 Методы класса)
1) Дополните класс из предыдущего упражнения методом __str__(),
    где верните строку в таком формате: «Прямоугольник с
    координатами (X; Y) шириной W и высотой H». Вместо X, Y, W, H
    должны быть соответствующие значения свойств.
2) Создайте метод, который будет возвращать площадь прямоугольника.
3) Создайте метод, который будет возвращать периметр прямоугольника.
4) Проверьте работу всех созданных методов.
Примечание: площадь прямоугольника = ширина * высота, а периметр =
    (ширина + высота) * 2.
'''


def lesson_4():
    class Rectangle:
        x = 0 #координаты верхнего правого угла
        y = 0 #координаты верхнего правого угла
        w = 0 #ширина
        h = 0 #высота

        def __init__(self, x , y , w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

        def __str__(self):
            return f"Прямоугольник с координатами (x: {self.x}; y: {self.y}), шириной: {self.w} и высотой: {self.h}"

        def area(self): #1 метод класса
            return f"Площадь: {self.w * self.h}"

        def perimetr(self): #1 метод класса
            return f"Периметр: {(self.w+self.h) * 2}"

        def area1(self, rec): #2 метод класса с другими данными
             return f"Площадь 1: {rec.w * rec.h}"

        def perimetr1(self, rec): #2 метод класса с другими данными
            return f"Периметр 1: {(rec.w+rec.h) * 2}"


    r1 = Rectangle(212, 32, 20, 6)
    print(r1)
    print(r1.area()) #1 использовать метод класса
    print(r1.perimetr())
    print(r1.area1(Rectangle(2, 2, 3, 4))) #2 использовать метод класса с другими данными
    print(r1.perimetr1(Rectangle(2, 2, 3, 4)))


#--------------------------------------------------------
'''Раздел 4 (5 Модификаторы доступа)
1) Сделайте у класса из предыдущего упражнения закрытыми все его поля.
2) Добавьте методы get и set для всех полей. Поскольку полей всего 4,
    то должно быть 4 метода get и 4 метода set.
3) Убедитесь, что доступа к полям уже нет за пределами класса.
4) Проверьте работу методов get и set.
5) Сделайте закрытый метод printlog(), в котором с помощью функции
    print() выводите значение переданного параметра.
6) В методах get и set вызывайте метод printlog с параметром:
    «Запрошено свойство NAME» (для методов get) или «Изменено свойство NAME»
    (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.
'''


def lesson_5():
    class Rectangle:
        __x = 0 #координаты верхнего правого угла
        __y = 0 #координаты верхнего правого угла
        __w = 0 #ширина
        __h = 0 #высота
        def __init__(self, x , y , w, h):
            self.__x = x
            self.__y = y
            self.__w = w
            self.__h = h

        def __str__(self):
            return f"Прямоугольник с координатами (x: {self.__x}; y: {self.__y}), шириной: {self.__w} и высотой: {self.__h}"

        def __printlog(self, met):
            if met == self.getX or met == self.getY or met == self.getW or met == self.getH:
                print(f"Запрошено свойство GET")
            elif met == self.setX or met == self.setY or met == self.setW or met == self.setH:
                print(f"Изменено свойство SET")

        def getX(self):
            self.__printlog(self.getX)
            return self.__x

        def getY(self):
            self.__printlog(self.getY)
            return self.__y

        def getW(self):
            self.__printlog(self.getW)
            return self.__w

        def getH(self):
            self.__printlog(self.getH)
            return self.__h

        def setX(self, x):
            self.__x = x
            self.__printlog(self.setX)

        def setY(self, y):
            self.__y = y
            self.__printlog(self.setY)

        def setW(self, w):
            self.__w = w
            self.__printlog(self.setW)

        def setH(self, h):
            self.__h = h
            self.__printlog(self.setH)


    r1 = Rectangle(1, 2, 3, 4)
    print(r1)
    # r1.setX(33)
    # r1.setY(22)
    # r1.setW(50)
    # r1.setH(20)
    #-----------
    x, y, w, h = 9, 8, 7, 6
    r1.setX(x)
    r1.setY(y)
    r1.setW(w)
    r1.setH(h)
    #-----------
    print(r1.getX())
    print(r1.getY())
    print(r1.getW())
    print(r1.getH())
    print(r1)


#--------------------------------------------------------
'''Раздел 4 (6 Наследование классов)
1) Создайте класс для автомобилей, указав у этого класса необходимые
    свойства (подумайте, какие именно свойства можно указать для всех автомобилей,
    но обязательно должны быть координаты x и y, в которых находится автомобиль).
2) Создайте метод движения, где через print выведите: «Движение автомобиля
    в точку x, y», где x и y – это координаты, переданные в методе. Не забудьте
    обновить x и y в этом методе на новые.
3) Создайте дочерний класс для какой-нибудь конкретной модели автомобиля.
    Придумайте какое-нибудь свойство, которое характерно именно для этой модели,
    и добавьте его.
4) Переопределите метод движения. В новом методе должны так же меняться координаты,
    но при этом в print должно выводиться не «автомобиль», а название конкретного
    автомобиля, для которого был создан этот класс.
5) Создайте экземпляры обоих классов и проверьте работу их свойств и методов.
'''


def lesson_6():
    class Auto:
        x = 0 #координата местоположения
        y = 0 #координата местоположения
        c = "класный" #color - цвет
        w = 1000 #weight - масса
        f = "бензин" #fuel - топливо

        def __init__(self, x, y, w, f):
            self.x = x
            self.y = y
            self.w = w
            self.f = f

        def painting(self, c):
            self.c = c
            print(f"Перекрашен в {self.c} цвет")

        def move(self, x, y):
            self.x = x
            self.y = y
            print(f"Движене автомобиля в точку: x-{self.x}; y-{self.y}")

        def gps(self):
            print(f"Автомобиль сейчас находится в координатах: x-{self.x}; y-{self.y}")

        def __str__(self):
            return f"Цвет авто: {self.c}\nВес: {self.w}кг.\nТопливо: {self.f}\nНаходится по координатам: x-{self.x}; y-{self.y}"


    class Audi(Auto):
        brend = "Audi"
        model = None
        kpp = None

        def __init__(self, x, y, w, f, model, kpp):
            Auto.__init__(self, x, y, w, f)
            self.model = model
            self.kpp = kpp

        def move(self, x, y):
            self.x = x
            self.y = y
            print(f"{self.brend} движется в точку: x-{self.x}; y-{self.y}")

        def __str__(self):
            return f"Марка {self.brend} (модель {self.model})\nЦвет авто: {self.c}\nВес: {self.w}кг.\nТопливо: {self.f}\nНаходится по координатам: x-{self.x}; y-{self.y}"



    auto1 = Auto(10, 10, 2000, "Бензин")
    print(auto1)
    print("------Действия---------------------")
    auto1.painting("Желтый")
    auto1.move(135, 114)
    print("-----------------------------------")
    print(auto1)
    print("-----------------------------------")
    auto2 = Audi(40, 40, 1000, "ДТ", "Q7", "Автомат")
    print(auto2)
    print("------Действия---------------------")
    auto2.move(1003, 3425)
    auto2.painting("Белый")
    auto2.gps()
    print("-----------------------------------")
    print(auto2)


#--------------------------------------------------------
'''Раздел 4 (7 Абстрактные классы)
1) Сделайте класс автомобиля из предыдущего упражнения абстрактным.
2) Сделайте метод движения у этого класса так же абстрактным.
3) Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь
    конкретной модели и реализуйте абстрактный метод движения.
'''


def lesson_7():
    from abc import ABC, abstractmethod


    class Auto(ABC): #Абстрактный класс
        brend = None
        model = None
        x = 0 #координата местоположения
        y = 0 #координата местоположения
        c = "Черный" #color - цвет
        w = 1000 #weight - масса
        f = "Бензин" #fuel - топливо

        def __init__(self, brend, model, x, y, w, f):
            self.brend = brend
            self.model = model
            self.x = x
            self.y = y
            self.w = w
            self.f = f

        def painting(self, c):
            self.c = c
            print(f"{self.brend} {self.model} перекрашена в {self.c} цвет")

        @abstractmethod
        def move(self, x, y):
            pass

        def gps(self):
            print(f"{self.brend} {self.model} сейчас находится в координатах: x-{self.x}; y-{self.y}")

        @abstractmethod #Абстрактный метод
        def __str__(self):
            pass


    class Audi(Auto):
        kpp = None #коробка передач
        def __init__(self, brend, model, x, y, w, f, kpp):
            Auto.__init__(self, brend, model, x, y, w, f)
            self.kpp = kpp

        def move(self, x, y):
            self.x = x
            self.y = y
            print(f"{self.brend} {self.model} движется в точку: x-{self.x}; y-{self.y}")

        def __str__(self):
            return f"Марка {self.brend} (модель {self.model})\nЦвет авто: {self.c}\nВес: {self.w}кг.\nТопливо: {self.f}\nКоробка передач: {self.kpp}\nНаходится по координатам: x-{self.x}; y-{self.y}"


    class Skoda(Auto):
        od = None #объем двигателя

        def __init__(self, brend, model, x, y, w, f, od):
            Auto.__init__(self, brend, model, x, y, w, f)
            self.od = od

        def move(self, x ,y):
            self.x = x
            self.y = y
            print(f"{self.brend} {self.model} движется в точку: x-{self.x}; y-{self.y}")

        def __str__(self):
            return f"Марка {self.brend} (модель {self.model})\nЦвет авто: {self.c}\nВес: {self.w}кг.\nТопливо: {self.f}\nОбъем двигатебя: {self.od}\nНаходится по координатам: x-{self.x}; y-{self.y}"

            
    auto1 = Audi("Audi", "Q7", 15, 20, 1800, "Газ-бензин", "Автомат")
    auto2 = Skoda("Skoda", "Fabia 2", 10, 20, 900, "ДТ", 1.6)
    print("-------------------------------------------")
    print(auto1)
    print("---------Действия--------------------------")
    auto1.move(1947, 5478)
    auto1.painting("Белый")
    auto1.gps()
    print("-------------------------------------------")
    print(auto1)
    print("-------------------------------------------")
    print("-------------------------------------------")
    print(auto2)
    print("---------Действия--------------------------")
    auto2.move(8963, 454)
    auto2.painting("Синий")
    auto2.gps()
    print("-------------------------------------------")
    print(auto2)




#--------------------------------------------------------
