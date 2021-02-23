from dataclasses import dataclass, field


# --------------------------------------------------------------------------------
# Дата класс
@dataclass(order=True)    # имеет встроеный метод __init__ и __repr__ (order=True - позволяет сортивоваль датаклассы по инстансам, предоставляет датаклассам возможность сравнения по инстансам) 
class MyClassDataClass:
    x: int
    y: int = field(compare=False)    # compare=False - переменная не учавствует в сравнениях
    z: int = field(repr=False)    # repr=False - не выводить переменную в __repr__ (при принте) с помощью функции field()
    a: int = field(repr=False, default=10)    # default= - установка значения по умолчанию

    def __post_init__(self):    # позволяет производить любые действия в датаклассах
        self.generated_attr = self.x + self.y + self.z + self.a


# Обычный класс
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):    # или метод __str__
        return f"(x={self.x}, y={self.y})"


# --------------------------------------------------------------------------------
# Дата класс Frozen только для чтения
@dataclass(frozen=True)    # frozen=True - делает класс только для чтения (не возможно переопределить переменные и т.д.)
class MyClassDataClassFrozen:
    x: int
    y: int


# обычный класс по анологии Frozen
class MyClassFrozen:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


# --------------------------------------------------------------------------------
# Тест
test_1 = MyClass(2, 3)
print(test_1)

test_2 = MyClassDataClass(1, 4, 3)
print(test_2)
print(test_2.generated_attr)

test_3 = MyClassDataClass(1, 7, 3)

print(sorted([test_2, test_3]))
