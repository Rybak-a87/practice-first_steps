import course.section2_basics_of_programming.section2 as BOP_s2
import course.section3_standard_functions.section3 as SF_s3
import course.section4_object_oriented_programming.section4 as oop_s4
import course.section5_creating_programs_with_a_GUI.section5 as gui_s5
import course.section6_creation_of_client_server_applications.section6 as csa_s6



# -----------------
# Основы программирования на Python
# -----------------


# ============================================================
#       *********        *********        **********         =
#       ***   ***        ***   ***        ***    ***         =
#       *******          ***   ***        ***    ***         =
#       ***   ***        ***   ***        **********         =
#       ***   ***        ***   ***        ***                =
#       *********        *********        ***                =
# ============================================================


""" Раздел 2 (1 Hello, world!)
1) Выведите с помощью двух функций print два предложения: «Я прохожу курс по Python»
    и «Я учу Python по курсу: ‘Программирование на Python с Нуля до Гуру’».
2) Выведите с помощью только одного вызова функции print два предложения из предыдущего
    пункта, причём после первого предложения должен быть переход на новую строку.
"""


# BOP_s2.lesson_1()


""" Раздел 2 (2 Переменные и их типы)
1) Создайте переменную со значением 10.
2) Выведите данную переменную с помощью функции print().
3) Измените значение переменной на 15.
4) Выведите значение переменной в таком виде: «Значение переменной ИМЯ_ПЕРЕМЕННОЙ равно ЗНАЧЕНИЕ_ПЕРЕМЕННОЙ».
    То есть должно получиться примерно так: «Значение переменной abc равно 15».
5) Создайте 2 строковые переменные со значениями: «Значение переменной» и «равно».
6) Выведите аналогичную строку из пункта 4, но с использованием переменных из пункта 5.
7) Создайте 2 булевских переменных со значениями: True и False.
8) Выведите их так, как написано в 6 пункте (то есть с использованием строковых переменных).
"""


# BOP_s2.lesson_2()


""" Раздел 2 (4 Арифметические операции)
1) Создайте 2 числовые переменные со значениями на Ваш выбор.
2) Выведите через print() результат: суммы, разности, произведения, остатка от деления, получение
    целой части при делении, возведении в степень этих чисел.
3) С помощью print() посчитайте, чему равно значение следующего выражения: ((15 * 10 – 20) / 2) + 14 * 10 + (-45)
4) Создайте переменную, в которую запишите значение одного из чисел в двоичной системе счисления.
5) Выведите эту переменную.
"""


# BOP_s2.lesson_4()


""" Раздел 2 (5 Догические операции)
1) Самостоятельно подумайте, чему будет равно следующее логическое выражение:
    True and (True or (False and True or False) and True or True != False)
2) Проверьте себя, выведя результат этого выражения с помощью функции print().
3) Самостоятельно подумайте, чему будет равно следующее логическое выражение:
    15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18)
4) Проверьте себя, выведя результат данного выражения с помощью функции print().
"""


# BOP_s2.lesson_5()


""" Раздел 2 (6 Строковые операции)
1) Попросите пользователя ввести 3 числа.
2) Выведите пользователю среднее арифметическое этих чисел.
    Примечание: среднее арифметическое чисел
                равно сумме этих чисел поделённое на их количество.
"""


# BOP_s2.lesson_6()


""" Раздел 2 (7 Условные операции)
1) Попросите пользователя ввести 2 числа.
2) Сохраните в переменную результат деления первого числа на второе 
    при условии, что делитель не равен 0. Если делитель равен 0, то сохранить 
    в переменную строку: «бесконечность».
3) Вывести пользователю ответ в таком виде: «ЧИСЛО_1 / ЧИСЛО_2 = ОТВЕТ».
    Примечание: разумеется, вместо «ЧИСЛО_1», «ЧИСЛО_2» и «ОТВЕТ» должны быть 
    подставлены соответствующие переменные.
"""


# BOP_s2.lesson_7()


""" Раздел 2 (8 Цикл while)
1) Напишите программу, которая будет принимать числа от пользователя и суммировать
    их, пока он не напишет слово «sum».
2) Когда пользователь напишет слово «sum», должна быть выведена сумма всех чисел и
    начат процесс заново.
3) Если пользователь напишет «exit» или «quit», программа должна быть завершена.
"""


# BOP_s2.lesson_8()


""" Раздел 2 (9 Массивы (списки))
1) Создайте список, состоящий из строк.
2) Выведите все элементы списка в таком виде: «ИНДЕКС_ЭЛЕМЕНТА – ЭЛЕМЕНТ;»
3) Попросите пользователя ввести индекс того элемента, значение которого он 
    хочет посмотреть.
4) Выведите значение элемента по индексу, полученному от пользователя.
    Примечание: если пользователь ввёл индекс, которого нет, то написать 
    ему об этом так: «Элемента с таким индексом не существует».
"""


# BOP_s2.lesson_9()


""" Раздел 2 (10 Цикл for и генераторы списков)
1) Создайте список из 5 чисел.
2) Определите сумму чисел в списке и выведите её.
3) Определите среднее арифметическое чисел в списке и выведите его.
    Примечание: при выполнении заданий используйте цикл for.
"""


# BOP_s2.lesson_10()


""" Раздел 2 (11 Множества)
1) Попросите пользователя ввести количество элементов для списка.
2) Создайте список, состоящий из целых случайных чисел от 0 до 100, 
    заданного пользователем количества.
3) Выведите этот список с помощью цикла while.
4) С помощью множеств удалите из списка все повторяющиеся значения.
5) Выведите получившийся список с помощью цикла for.
"""

# BOP_s2.lesson_11()


""" Раздел 2 (12 Кортежи)
1) Попросите пользователя ввести произвольную строку.
2) Создайте кортеж, состоящий из символов, введённой пользователем строки.
3) Выведите кортеж, используя цикл for.
"""


# BOP_s2.lesson_12()


""" Раздел 2 (13 Словари)
1) Создайте словарь с двумя ключами «Name» и «Age» и значениями «Без имени» и «-1».
2) Попросите пользователя ввести своё имя.
3) Попросите пользователя ввести свой возраст.
4) Примите эти данные и измените соответствующие элементы словаря.
5) Выведите этот словарь (ключи и значения), используя цикл for.
"""


# BOP_s2.lesson_13()


""" Раздел 2 (14 функции)
1) Создайте функцию, которая проверяет чётное число передано в параметре 
    или нет. Она должна возвращать True или False.
2) Создайте функцию, которая принимает список и возвращает максимальное 
    значение из списка.
3) Создайте функцию с переменным числом аргументов, внутри которой должно 
    выводиться среднее арифметическое переданных чисел.
    Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое 
    на их количество.
"""

# BOP_s2.lesson_14_1(22)
# l = [32, 4, 56, 32, 7, 87]
# s2.lesson_14_2(l)
# s2.lesson_14_3(46, 78, 98, 4, 3, 6, 7)


""" Раздел 2 (15 Глобальные переменные)
1) Создайте переменную со значением числа пи: «3.141592».
2) Напишите функцию, которая будет возвращать площадь окружности по переданному 
    в параметре радиусу.
3) Проверьте работу функции.
    Примечание: площадь окружности = пи * радиус * радиус. Значение числа пи надо 
    взять из глобальной переменной, созданной в первом пункте.
"""


# s = BOP_s2.lesson_15(3)
# print(f"Площадь окружности равна: {s}")


""" Раздел 2 (16 Модули)
1) Создайте свой модуль и подключите его в основном файле.
2) Напишите в модули 3 функции, каждая из которых принимает список. Первая 
    функция – получение максимального значения, вторая – получение минимального 
    значения, третья – получение суммы всех элементов.
3) Проверьте работу этих функций в основном файле.
"""

# a = [1, 2, 4, 5, 6, 23, -1]
# BOP_s2.lesson_16_1(a)
# BOP_s2.lesson_16_2(a)
# BOP_s2.lesson_16_3(a)


""" Раздел 2 (17 Исключения)
1) Узнайте, какое исключение появляется при делении числа на 0.
2) Попросите пользователя ввести 2 числа.
3) Выведите результат деления.
4) Перехватите исключение при делении на 0 и выведите пользователю в 
    качестве результата слово «бесконечность».
"""


# BOP_s2.lesson_17()


""" Раздел 2 (18 Выполнение команд)
1) Откройте командную строку в своей системе.
2) Узнайте, с помощью какой команды можно получить текущую дату, используя 
    команду help, либо документацию к своей ОС.
3) Напишите программу, которая выполняет эту команду и выводит результат с 
    помощью функции print().
"""


# BOP_s2.lesson_18()


""" Раздел 2 (19 Отладка)
1) Создайте список из 5 чисел.
2) Напишите функцию, которая находит все отрицательные числа и выводит их.
3) С помощью отладки пройдите все шаги выполнения программы, анализируя 
    значения всех переменных.
"""


# l = [3, 5, 7, -1, 6, -23, 65, 64, -12]
# BOP_s2.lesson_19(l)


# ============================================
#       *********         **********         =
#       ***               ***                =
#       *********         *******            =
#             ***         *******            =
#             ***         ***                =
#       *********         ***                =
# ============================================


""" Раздел 3 (1 Математические функции)
1) Выведите число, округлив его до 2 знаков после запятой.
2) Выведите с шагом в 1 градус все значения синуса угла
    от 0 до 180 градусов в таком виде: «sin(УГОЛ_В_ГРАДУСАХ) = РЕЗУЛЬТАТ».
Примечание: разумеется, стоит использовать цикл.
"""


# SF_s3.lesson_1()


""" Раздел 3 (2 Строковые функции)
1) Попросите пользователя ввести произвольную строку.
2) Выведите коды всех символов строки, введённой пользователем.
3) Попросите пользователя ввести строку, состоящую только из цифр.
4) Используя соответствующую функцию, проверьте введённую пользователем
    строку, и если он ввёл правильно, то написать «Спасибо!», иначе
    выбросить исключение, в обработке которого вывести строку
    «Некорректный ввод!».
"""


# SF_s3.lesson_2()


""" Раздел 3 (3 Функции для работы со списками и кортежами)
1) Попросите пользователя указать, какое количество элементов надо
    создать в списке.
2) Сделайте цикл на соответствующее число итераций, в каждой из
    которых просите пользователя ввести число в таком формате:
    «Введите число N:», где N – текущий номер числа.
3) Добавляйте каждое это число в список.
4) По завершению цикла выведите получившийся список.
"""


# SF_s3.lesson_3()


""" Раздел 3 (4 Функции для работы с множествами)
1) Создайте 2 множества, состоящие из 10 случайных целых чисел
    от 1 до 10 (включая 1 и 10).
2) Выведите 3 множества: объединением этих двух множеств,
    их разницей и их пересечением.
"""


# SF_s3.lesson_4()


""" Раздел 3 (5 Функции для работы со словарями)
1) Создайте словарь из 3-х ключей «Hello», «Bуe» и «Lesson» и
    значениями соответственно «Здравствуй», «Пока» и «Урок».
2) В бесконечном цикле выводите случайное значение из словаря
    и просите пользователя написать перевод на английском.
3) Проверяйте на соответствие введённой пользователем строки
    и ключа словаря. Если пользователь ввёл всё правильно,
    то выводить ему следующее слово. Если неправильно,
    то сообщать ему об этом, и заново ждать от него уже
    другого ответа. И так до тех пор, пока он не введёт правильный ответ.
4) Если пользователь вводит команду «show», то вывести словарь.
5) Если пользователь вводит «quit», то завершать программу.
Примечание: не забывайте, что если пользователь будет писать,
    например: «hello», «Hello» или «HELlo» - то это всё считать
    правильными ответами.
"""


# SF_s3.lesson_5()


""" Раздел 3 (6 Функции для работы с файлами)
1) Попросите пользователя ввести команду «read» или «copy».
2) Попросите у пользователь ввести путь к файлу, содержимое которого
    он хочет посмотреть, либо скопировать. Причём, если пользователь
    ввёл до этого «read», то надо написать: «Напишите путь к файлу,
    содержимое которого Вы хотите посмотреть:». А если была команда «write»,
    то: «Напишите путь к файлу, который Вы хотите скопировать:»
3) Если была команда «read», то вывести пользователю содержимое файла.
4) Если была команда «write», то сделайте копию файла. Копия файла должна
    называться так же, как и исходный файл, и находиться она должна в
    директории files, находящейся в той же директории, что и файл скрипта.
Примечание: будьте аккуратны и не очистите какие-нибудь важные файлы в
    процессе экспериментов. Создайте лучше какой-нибудь новый файл для этой задачи.
"""

# SF_s3.lesson_6()


""" Раздел 3 (7 Функции для работы с датой и временем)
1) Попросите пользователя ввести 3 числа: год, месяц и число рождения.
2) Напишите ему, сколько секунд он уже живёт.
"""


# SF_s3.lesson_7()


# ============================================================
#       *********        *********        **********         =
#       ***   ***        ***   ***        ***    ***         =
#       ***   ***        ***   ***        ***    ***         =
#       ***   ***        ***   ***        **********         =
#       ***   ***        ***   ***        ***                =
#       *********        *********        ***                =
# ============================================================


""" Раздел 4 (2 Создание класса)
1) Создайте класс прямоугольника со следующими свойства:
    координаты левого верхнего угла, ширина и высота.
2) Создайте экземпляр этого класса.
3) Измените значения его свойств и выведите их.
"""


# oop_s4.lesson_2()


""" Раздел 4 (3 Конструктор класс)
1) Возьмите за основу класс прямоугольника из предыдущего
    упражнения.
2) Создайте у него конструктор, принимающий в качестве
    параметров все его свойства.
3) Внутри конструктора инициализируйте свойства переданными
    в него параметрами.
4) Используя конструктор, создайте экземпляр класса.
5) Выведите его свойства.
"""


# oop_s4.lesson_3()


""" Раздел 4 (4 Методы класса)
1) Дополните класс из предыдущего упражнения методом __str__(),
    где верните строку в таком формате: «Прямоугольник с
    координатами (X; Y) шириной W и высотой H». Вместо X, Y, W, H
    должны быть соответствующие значения свойств.
2) Создайте метод, который будет возвращать площадь прямоугольника.
3) Создайте метод, который будет возвращать периметр прямоугольника.
4) Проверьте работу всех созданных методов.
Примечание: площадь прямоугольника = ширина * высота, а периметр =
    (ширина + высота) * 2.
"""


# oop_s4.lesson_4()


""" Раздел 4 (5 Модификаторы доступа)
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
"""


# oop_s4.lesson_5()


""" Раздел 4 (6 Наследование классов)
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
"""


# oop_s4.lesson_6()


""" Раздел 4 (7 Абстрактные классы)
1) Сделайте класс автомобиля из предыдущего упражнения абстрактным.
2) Сделайте метод движения у этого класса так же абстрактным.
3) Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь
    конкретной модели и реализуйте абстрактный метод движения.
"""


# oop_s4.lesson_7()


# ============================================================
#       *********        ***   ***        *********          =
#       ***              ***   ***           ***             =
#       ***              ***   ***           ***             =
#       ***   ***        ***   ***           ***             =
#       ***   ***        ***   ***           ***             =
#       *********        *********        *********          =
# ============================================================


"""Раздел 5 (1 Создание окна)
1) Создайте окно размером 1000 на 500 пикселей.
2) Расположите его в верхнем левом углу.
3) Расположите его в правом верхнем углу.
Примечание: в 3-ем задании не пишите конкретные значения координат
    расположения. Используйте встроенные функции, позволяющие получить
    разрешение экрана у пользователя, и на их основе рассчитайте координаты
    местоположения, чтобы правый верхний угол Вашего окна располагался
    в правом верхнем углу экрана.
"""


# gui_s5.lesson_1()


""" Раздел 5 (2 Метки)
1) Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
Примечание: то есть при каждом запуске программы там должно появляться случайное число.
"""


# gui_s5.lesson_2()


""" Раздел 5 (3 Кнопки)
1) Посмотрите в справочнике, какие есть параметры у Button.
2) Добавьте несколько кнопок с различными значениями атрибутов в окно.
"""


# gui_s5.lesson_3()


""" Раздел 5 (4 Текстовое поле)
1) Создайте текстовое поле.
2) Попросите пользователя ввести в консоли произвольную строку.
3) Выведите эту строку в текстовом поле окна.
Примечание: запрос строки и её вывод в текстовом поле должны происходить до mainloop().
"""


# gui_s5.lesson_4()


""" Раздел 5 (5 Текстовая область)
1) Создайте текстовый файл с произвольным текстом.
2) Выведите текстовую область в окно, где должен быть выведен весь текст из файла,
    созданном в предыдущем пункте.
Примечание: разумеется, надо воспользоваться функциями для работы с файлами.
"""


# gui_s5.lesson_5()


""" Раздел 5 (6 Чекбокс)
1) Выведите чекбокс, который при каждом запуске программы случайным образом
    должен быть либо включенным, либо выключенным.
"""


# gui_s5.lesson_6()


""" Раздел 5 (7 Радио-кнопка)
1) Создайте список из 5-ти значений с названиями городов.
2) Выведите радиокнопки с этими названиями городов, используя цикл по списку.
Примечание: для параметра variable создайте отдельную переменную и её значением
    должен быть индекс списка. То есть, если в списке город «Москва» имеется индекс 3,
    то и value при создании радио-кнопки должен быть равен 3.
"""


# gui_s5.lesson_7()


""" Раздел 5 (8 Scrollbar)
1) Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
Примечание: при необходимости в текстовый файл надо добавить ещё текста,
    чтобы scrollbar стал активным.
"""


# gui_s5.lesson_8()


""" Раздел 5 (9 Список)
1) В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
2) Когда пользователь введёт 0, то нужно выйти из цикла.
3) Используя созданный список, выведите его с помощью Listbox в окно программы.
"""


# gui_s5.lesson_9()


""" Раздел 5 (10 Создание фреймов)
1) Создайте 3 элемента Frame.
2) В первый Frame добавьте label с текстом «Важная форма».
3) Во второй Frame добавьте 2 текстовых поля.
4) В третий Frame добавьте кнопку «Отправить форму».
5) Разместите все 3 элемента Frame в окне.
"""


# gui_s5.lesson_10()


""" Раздел 5 (11 Компоновщик pack)
1) Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
2) Выведите первый Label вверху по центру, второй и третий слева и справа соответственно
    под первым элементом, а четвёртый по центру снизу.
"""


# gui_s5.lesson_11()


""" Раздел 5 (12 Компоновщик place)
1) Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация»,
    под ней 2 текстовых поля и метки слева от них («Логин:», «Пароль:»), а уже под этими
    элементами выведите кнопку («Войти»).
Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.
"""


# gui_s5.lesson_12()


""" Раздел 5 (13 Компоновщик grib)
1) Сделайте предыдущее упражнение, но уже используя grid.
"""


# gui_s5.lesson_13()


""" Раздел 5 (14 Работа с изображениями)
1) Попросите пользователя ввести путь к картинке.
2) Следующим шагом попросите его указать, с каким масштабом выводить изображение.
3) Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит,
    он хочет его сжать, и для этого потребуется функция subsample, а также перевод,
    например, 0.2 в число 5 (1 / 0.2).
"""


# gui_s5.lesson_14()


""" Раздел 5 (15 Обработка событий. Часть 1)
1) Сделайте кнопку с текстом «Сгенерировать случайное число».
2) При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
Примечание: для вывода сгенерированного числа используйте Label.
"""


# gui_s5.lesson_15()


""" Раздел 5 (16 Обработка событий. Часть 2)
1) Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
2) При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен
    меняться на случайный элемент из списка, созданного в предыдущем пункте.
3) При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.
"""


# gui_s5.lesson_16()


""" Раздел 5 (17 Обработка событий. Часть 3)
1) Выведите, используя метку, в окне такую строку: «ax^2 + bx + c = 0».
2) Добавьте 3 текстовых поля с метками «a:», «b:» и «c:».
3) Добавьте кнопку «Вычислить корни уравнения».
4) После вычисления их нужно вывести под кнопкой в формате: «x1 = …; x2 = …;».
5) Если число под корнем отрицательное, то вывести в метке для результата строку: «Нет корней».
"""


# gui_s5.lesson_17()


# ============================================================
#       *********        *********          ******           =
#       ***   ***        ***               **    **          =
#       ***              *********        ***    ***         =
#       ***              *********        **********         =
#       ***   ***              ***        ***    ***         =
#       *********        *********        ***    ***         =
# ============================================================


"""Раздел 6 (1 Чтение данных с сайта)
1) Создайте словарь, где ключами будут названия телефонов из урока, а значениями будут их цены.
2) Выведите его в консоль, чтобы убедиться, что всё правильно.
Примечание: разумеется, цены этих телефонов надо вытащить с сайта, используя показанные в
    уроке инструменты для парсинга.
"""

# csa_s6.lesson_1()


""" Раздел 6 (2 Создание серверной части)
1) Создайте сервер, который получает число, умножает его на 10 и отправляет обратно клиенту.
2) При получении команды «stop», сервер должен быть остановлен (в примере из урока это можно
    сделать, завершив бесконечный цикл с помощью break).
"""


# csa_s6.lesson_2()


""" Раздел 6 (3 Создание коиентской части)
1) Создайте клиента, который отправляет серверу из предыдущего упражнения число 5, затем ещё
    число 10 и затем команду «exit».
2) Убедитесь, что всё работает правильно, то есть сервер после первой команды должен прислать
    «50», после второй – «100», а после команды «exit» должен быть остановлен (то есть
    программа из предыдущего упражнения должна остановиться).
"""


# csa_s6.lesson_3()


""" Раздел 6 (4 Создание Web - страницы)
1) Запустите сервер с помощью Python, чтобы можно было открывать Web-страницы в браузере через localhost.
2) Создайте страницу, на которой выведите HTML-код какой-нибудь реально существующей Web-страницы.
Примечание: тут Вам поможет вывод многострочной строки с помощью ‘’’строка’’’ или “””строка”””.
    Саму страницу выберите любую, которую найдёте в Интернете, откройте исходник (с помощью Ctrl+U) и
    скопируйте оттуда весь код. Обратите внимание, что велика вероятность того, что внешний вид страницы
    будет странным (например, нарушится вёрстка или исчезнут некоторые изображения), это является
    нормальным. Главное, чтобы хоть что-то открылось.
"""


# csa_s6.lesson_4()
