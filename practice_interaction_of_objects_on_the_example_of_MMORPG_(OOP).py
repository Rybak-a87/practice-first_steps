# Взаимодействие объектов на примере ММОРПГ (ООП) операции с сумкой персонажа


import inspect
import sys


class Sword:    # Меч
    def __init__(self, name):
        self.name = name

    def __repr__(self):    # (пердставление) при принте объекта возвращает результат этой функции
        return self.name


class Shield(Sword):    # Шит (та же логика что и у меча)
    pass


class Backpack:    # сумка
    MAX_SIZE = 16
    MIN_SIZE = 6

    def __new__(cls, *args, **kwargs):
        slots = args[0]
        if cls.MAX_SIZE >= slots > cls.MIN_SIZE:
            return super().__new__(cls)
        error_kwargs = {
            "slots": slots,
            "min_size": cls.MIN_SIZE,
            "max_size": cls.MAX_SIZE
        }
        error_msg = "Inapropriate size of backpack. Input size {slots}. Max size: {max_size}, min size: {min_size}"
        raise Exception(error_msg.format(**error_kwargs))

    def __init__(self, slots):
        self.slots = slots
        self.backpack = []

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self.backpack]) + "]"

    def put(self, item, qty=None):    # добавить в сумку
        if len(self.backpack) <= self.slots:
            if inspect.isclass(item):    # проверка - не является ли переданный item просто классом
                raise Exception("Item must be instance, not -class")
            if not qty:
                self.backpack.append({item: 1})
            else:
                self.backpack.append({item: qty})
            return
        raise Exception("Backpack is full")

    def remove(self, item_to_remove, qty=None):    # удаление с сумки
        class_item = item_to_remove.__class__
        lst = list(filter(lambda x: item_to_remove.name == str(list(x.keys()).pop()), self.backpack))
        if len(lst) >= 2 and not qty:
            raise Exception("There are 2 or more items of the item name. Pleace set 'qty' attr.")
        elif len(lst) >= 2 and qty:
            item_to_remove = {item_to_remove: qty}
            for item in self.backpack:
                if str(item_to_remove) == str(item):
                    self.backpack.remove(item)
                    sys.stdout.write(f"Item {item_to_remove} with qty - {qty} successfully remove from backpack\n")
        else:
            item_to_remove = {item_to_remove: 1}
            for item in self.backpack:
                if str(item_to_remove) == str(item):
                    self.backpack.remove(item)
                    sys.stdout.write(f"Item {item_to_remove} successfully remove from backpack\n")

    def split_item(self, item, qty, qty_to_split):    # разбивает предметы при определенных условиях
        if qty <= 1:
            raise Exception("You can split items, those have qty more than 1")
        if qty_to_split >= qty:
            raise Exception("qty_to_split is more or equil to qty")
        item_backpack = {item: qty}
        if item_backpack in self.backpack:
            item_original = list(filter(lambda x: x == item_backpack, self.backpack)).pop()
            self.backpack.remove(item_backpack)
            item_original[item] = qty - qty_to_split
            self.backpack.append(item_original)
            self.backpack.append({item: qty_to_split})


# Тест
backpack = Backpack(16)
sword = Sword("Supersword")
sword1 = Sword("Supersword1")
shield = Shield("Shield")
shield1 = Shield("Shield1")

backpack.put(sword)
backpack.put(sword1)
backpack.put(shield)
backpack.put(shield1, 6)
print(backpack)
backpack.remove(sword)
print(backpack)
backpack.split_item(shield1, 6, 3)
print(backpack)
backpack.remove(shield1, 3)
print(backpack)