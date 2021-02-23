# Создание программ с GUI
import tkinter
import random
from math import sqrt


from course.section5_creating_programs_with_a_GUI.setwindow import SetWindow


# def setWindow(root, w=400, h=300):
#     root.title("Мое первое окно :-)")   # !заголовок
#     root.resizable(False, False)   # !разрешение на изменения размера окна
#
#     # w = 400   # !ширина окна
#     # h = 300   # !высота окна
#
#     wx = root.winfo_screenwidth()   # !ширина экрана монитора
#     wy = root.winfo_screenheight()   # !высота экрана монитора
#     x = int(wx/2 - w/2)   # !координата левой верхней точки окна
#     y = int(wy/2 - h/2)   # !координата левой верхней точки окна
#
#     root.geometry(f"{w}x{h}+{x}+{y}")   # !размер и расположение окна
#     # root.mainloop()   # !запуск отображения окна (запуск бесконечного цикла)


# --------------------------------------------------------
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


def lesson_1():
    # !создание окна (родительский контейнер)
    root = tkinter.Tk()
    # !заголовок
    root.title("Мое первое окно :)")
    # !разрешение или запрет на изменения размера окна
    root.resizable(False, False)
    # !размер окна и его расположения по левому верхнему углу
    # задание 1-2
    width = 1000
    height = 500
    # x = -7
    y = 30
    # задание 3
    pc_w = root.winfo_screenwidth()
    # pc_h = window.winfo_screenheight()   # не нужно в этом задании
    x = pc_w - width
    root.geometry(f"{width}x{height}+{x}+{y}")
    # !запуск бесконечного цикла для отображения окна
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (2 Метки)
1) Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
Примечание: то есть при каждом запуске программы там должно появляться случайное число.
"""


def lesson_2():
    a = random.randrange(1, 1000)
    root = tkinter.Tk()   # !родительский контейнер
    # !функция создания окна
    setWindow(root)
    # !создание метки
    label = tkinter.Label(root, text=f"{a}", font="Tahoma 50", bg="Red", fg="#000")
    # !вызов метки
    label.pack()
    # !вывод окна
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (3 Кнопки)
1) Посмотрите в справочнике, какие есть параметры у Button.
2) Добавьте несколько кнопок с различными значениями атрибутов в окно.
"""


def lesson_3():
    root = tkinter.Tk()
    setWindow(root)

    button1 = tkinter.Button(root, text="ДА", bg="Blue", fg="White", font="Arial 20", width=10, height=1)
    button2 = tkinter.Button(root, text="НЕТ", bg="Red", fg="White", font="Arial 20", width=10, height=1)
    button3 = tkinter.Button(root, text="НЕ ЗНАЮ", bg="Green", fg="White", font="Arial 20", width=10, height=1)

    # !вызов кнопки с указанием стороны
    # button1.pack(side="left")   # !слева
    # button2.pack()   # !в случайном месте
    button3.pack(side="right")   # !справа

    # !вызов кнопки с указанием координат левой верхней точки
    button1.place(x="100", y="300")
    button2.place(x="200", y="100")

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (4 Текстовое поле)
1) Создайте текстовое поле.
2) Попросите пользователя ввести в консоли произвольную строку.
3) Выведите эту строку в текстовом поле окна.
Примечание: запрос строки и её вывод в текстовом поле должны происходить до mainloop().
"""


def lesson_4():
    root = tkinter.Tk()
    setWindow(root)
    # !создаем поле
    # entry = tkinter.Entry(root, font="Arial 18", bd=4, bg="Green", fg="Red")
    # мой эксперимент
    entry = tkinter.Entry(root)
    entry["font"] = "Arial 18"   # шрифт и размер шрифта
    entry["bd"] = 2   # ширина линии поля
    entry["bg"] = "Green"   # цвет фона
    entry["fg"] = "Red"   # цвет текста
    # !вставка текста в поле
    input_text = input("Введите текст, для поля: ")
    entry.insert(tkinter.END, input_text)
    # !визов поля
    entry.pack()

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (5 Текстовая область)
1) Создайте текстовый файл с произвольным текстом.
2) Выведите текстовую область в окно, где должен быть выведен весь текст из файла,
    созданном в предыдущем пункте.
Примечание: разумеется, надо воспользоваться функциями для работы с файлами.
"""


def lesson_5():
    def readFile(filename):
        with open(f"course/section5_creating_programs_with_a_GUI/files/{filename}", encoding="utf-8") as f:
            return f.read()

    fname = "file.txt"

    root = tkinter.Tk()
    setWindow(root)
    # !создаем текстовую область (пока для меня так более читабельней)
    text = tkinter.Text(root)
    text["font"] = "Arial 18"   # шрифт и размер шрифта
    text["bd"] = 20   # ширина линии расми
    text["fg"] = "Yellow"   # цвет шрифта
    text["bg"] = "Black"   # цвет фона
    text["width"] = "33"   # ширина текстовой области (по символам)
    text["height"] = "4"   # высота текстовой области (по строкам)
    text["padx"] = "10"   # отступы слева-справа (поля)
    text["pady"] = "10"   # отступы сверху-снизу (поля)
    # !добакляем текст с файла в текстовую область
    text.insert(tkinter.END, readFile(fname))
    # !визываем текстовую область
    text.pack()
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (6 Чекбокс)
1) Выведите чекбокс, который при каждом запуске программы случайным образом
    должен быть либо включенным, либо выключенным.
"""


def lesson_6():
    root = tkinter.Tk()
    setWindow(root)
    # !переменная для определения значения чек бокса
    choice = tkinter.IntVar()
    # !изменение значения переменной
    choice.set(random.randrange(1, 100) % 2)   # так больше шансов на вкл и выкл чем просто с 1 и 0
    # !создание чек бокса
    check = tkinter.Checkbutton(root, bd=30, text="Я веселый чек бокс :))", variable=choice, onvalue=1, offvalue=0)

    check.pack()
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (7 Радио-кнопка)
1) Создайте список из 5-ти значений с названиями городов.
2) Выведите радиокнопки с этими названиями городов, используя цикл по списку.
Примечание: для параметра variable создайте отдельную переменную и её значением
    должен быть индекс списка. То есть, если в списке город «Москва» имеется индекс 3,
    то и value при создании радио-кнопки должен быть равен 3.
"""


def lesson_7():
    cities = ["Бердянск", "Одесса", "Киев", "Запорожье", "Днепр"]

    root = tkinter.Tk()
    setWindow(root)
    # !вызываем метку
    label = tkinter.Label(root, text="Список городов\n\nВыбери город мечты\n", font="Arial 20", fg="Blue")
    label.pack()
    # !переменная для радио кнопки
    choice = tkinter.IntVar()
    choice.set(-1)   # делает радиокнопки не отмечеными
    # !создаем радиокнопку
    for i in range(len(cities)):
        rb = tkinter.Radiobutton(root, text=f"{cities[i]}", font="Arial 18",
                                 variable=choice, value=f"{cities.index(cities[i])}")
        rb.pack()

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (8 Scrollbar)
1) Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
Примечание: при необходимости в текстовый файл надо добавить ещё текста,
    чтобы scrollbar стал активным.
"""


def lesson_8():
    def readFile(filename):
        with open(f"course/section5_creating_programs_with_a_GUI/files/{filename}", encoding="utf-8") as f:
            return f.read()

    fname = "file.txt"

    root = tkinter.Tk()
    setWindow(root)
    # !создаем текстовую область (пока для меня так более читабельней)
    text = tkinter.Text(root)
    text["font"] = "Arial 18"   # шрифт и размер шрифта
    text.config(bd=20)   # ширина линии расми
    text.config(fg="Yellow")   # цвет шрифта
    text.config(bg="Black")   # цвет фона
    text.config(width=33)   # ширина текстовой области (по символам)
    text.config(height=4)   # высота текстовой области (по строкам)
    text.config(padx=10)   # отступы слева-справа (поля)
    text.config(pady=10)   # отступы сверху-снизу (поля)
    # !добавляем текст с файла в текстовую область
    text.insert(tkinter.END, readFile(fname))
    # !добавляем скролбар
    scrollbar = tkinter.Scrollbar(root, command=text.yview(), orient=tkinter.VERTICAL)
    text["yscrollcommand"] = scrollbar.set
    # !визываем текстовую область
    text.pack(side="left")
    # !вызов скролбара
    scrollbar.pack(side="left", fill=tkinter.Y)
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (9 Список)
1) В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
2) Когда пользователь введёт 0, то нужно выйти из цикла.
3) Используя созданный список, выведите его с помощью Listbox в окно программы.
"""


def lesson_9():
    cities = list()
    while True:
        a = input("Введите город:")
        if a == "0":
            break
        print("Для завершения ввода, введите 0")
        cities.append(a)
    root = tkinter.Tk()
    setWindow(root)
    # !создание списка
    listbox = tkinter.Listbox(root, font="Arial 18", width=10, height=5, selectmode=tkinter.MULTIPLE)
    # !добавление элементов в список листбокс
    for i in cities:
        listbox.insert(tkinter.END, i)
    # !вызов списка
    listbox.pack()
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (10 Создание фреймов)
1) Создайте 3 элемента Frame.
2) В первый Frame добавьте label с текстом «Важная форма».
3) Во второй Frame добавьте 2 текстовых поля.
4) В третий Frame добавьте кнопку «Отправить форму».
5) Разместите все 3 элемента Frame в окне.
"""


def lesson_10():
    root = tkinter.Tk()
    setWindow(root)
    # !создание фреймов
    frame1 = tkinter.Frame(root, bg="Black", bd=1)
    frame2 = tkinter.Frame(root)
    frame3 = tkinter.Frame(root)
    # !добавление во фреймы метки, два текстовых поля и кнопки
    label = tkinter.Label(frame1, font="Arial 20", text="Важная форма")
    entry1 = tkinter.Entry(frame2, font="Tahoma 20")
    entry2 = tkinter.Entry(frame2, font="Tahoma 20")
    button = tkinter.Button(frame3, font="Arial 25", text="Отправить форму", bd=5)
    # !вызов фреймов
    frame1.pack()
    frame2.pack()
    frame3.pack()
    # !вызов содержимого фреймов
    label.pack()
    entry1.pack()
    entry2.pack()
    button.pack()
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (11 Компоновщик pack)
1) Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
2) Выведите первый Label вверху по центру, второй и третий слева и справа соответственно
    под первым элементом, а четвёртый по центру снизу.
"""


def lesson_11():
    root = tkinter.Tk()
    setWindow(root)
    label1 = tkinter.Label(root, text="Метка 1", bg="Red", width=10, height=2)
    label2 = tkinter.Label(root, text="Метка 2", bg="Green", width=10, height=2)
    label3 = tkinter.Label(root, text="Метка 3", bg="Yellow", width=10, height=2)
    label4 = tkinter.Label(root, text="Метка 4", bg="Blue", width=10, height=2)

    label1.pack(side="top")
    label2.pack(side="left", expand=True, anchor="e")
    label3.pack(side="right", expand=True, anchor="w")
    label4.pack(side="bottom")

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (12 Компоновщик place)
1) Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация»,
    под ней 2 текстовых поля и метки слева от них («Логин:», «Пароль:»), а уже под этими
    элементами выведите кнопку («Войти»).
Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.
"""


def lesson_12():
    root = tkinter.Tk()
    setWindow(root)
    # !метки
    label_aut = tkinter.Label(root, text="Авторизация", font="Arial 20")
    label_log = tkinter.Label(root, text="Логин:", font="Tahoma 16")
    label_pass = tkinter.Label(root, text="Пароль:", font="Tahoma 16")
    # !текстовые поля
    entry_log = tkinter.Entry(root, font="Arial 16", bd=3, width=10)
    entry_pass = tkinter.Entry(root, font="Arial 16", bd=3, width=10)
    # !кнопка
    button_in = tkinter.Button(root, text="Войти", font="Arial 18", bd=3)
    # !рисуем интерфейс методом - place
    label_aut.place(relx=0.5, rely=0.1, anchor="n")
    label_log.place(relx=0.43, rely=0.3, anchor="e")
    entry_log.place(relx=0.43, rely=0.3, anchor="w")
    label_pass.place(relx=0.43, rely=0.4, anchor="ne")
    entry_pass.place(relx=0.43, rely=0.4, anchor="nw")
    button_in.place(relx=0.5, rely=0.55, anchor="n")

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (13 Компоновщик grib)
1) Сделайте предыдущее упражнение, но уже используя grid.
"""


def lesson_13():
    root = tkinter.Tk()
    setWindow(root)
    # !фрэцм
    frame = tkinter.Frame(root)
    # !метки
    label_aut = tkinter.Label(frame, text="Авторизация", font="Arial 20")
    label_log = tkinter.Label(frame, text="Логин:", font="Tahoma 16")
    label_pass = tkinter.Label(frame, text="Пароль:", font="Tahoma 16")
    # !текстовые поля
    entry_log = tkinter.Entry(frame, font="Arial 16", bd=3, width=10)
    entry_pass = tkinter.Entry(frame, font="Arial 16", bd=3, width=10)
    # !кнопка
    button_in = tkinter.Button(frame, text="Войти", font="Arial 18", bd=3)
    # !рисуем интерфейс методом - grid
    frame.place(relx=0.5, rely=0.3, anchor="center")
    label_aut.grid(row=0, column=0, columnspan=2, pady=5)
    label_log.grid(row=1, column=0, sticky="e")
    entry_log.grid(row=1, column=1, sticky="w")
    label_pass.grid(row=2, column=0, sticky="e")
    entry_pass.grid(row=2, column=1, sticky="w")
    button_in.grid(row=3, column=0, pady=5, columnspan=2)

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (14 Работа с изображениями)
1) Попросите пользователя ввести путь к картинке.
2) Следующим шагом попросите его указать, с каким масштабом выводить изображение.
3) Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит,
    он хочет его сжать, и для этого потребуется функция subsample, а также перевод,
    например, 0.2 в число 5 (1 / 0.2).
"""


def lesson_14():
    root = tkinter.Tk()
    setWindow(root, 800, 600)

    img = input("Введите путь к изображению: ")
    zm = input("Какой масштаб изображения вы хотите увидеть: ")
    photo = tkinter.PhotoImage(file=img)
    if not zm.isdigit():
        zm = int(1 / float(zm))
    else:
        zm = int(zm)
    if zm > 1:
        p = photo.zoom(zm, zm)
    elif zm < 1:
        p = photo.subsample(abs(zm), abs(zm))
    else:
        p = photo

    image = tkinter.Label(root, image=p)

    image.pack()
    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (15 Обработка событий. Часть 1)
1) Сделайте кнопку с текстом «Сгенерировать случайное число».
2) При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
Примечание: для вывода сгенерированного числа используйте Label.
"""


def lesson_15():
    def click(event):
        # !функция вывода в окно случайного числа
        label.config(text=f"{random.randint(1, 100)}")

    root = tkinter.Tk()
    setWindow(root)
    # !кнопка
    button = tkinter.Button(root, text="Сгенерировать случайное число", font="Arial 18")
    button.place(relx=0.5, rely=0.3, anchor="center")
    # !присваивание кнопке функцию при нажатии на нее лев. кнопкой мыши
    button.bind("<Button-1>", click)
    label = tkinter.Label(root, font="Arial 18")
    label.place(relx=0.5, rely=0.5, anchor="n")

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (16 Обработка событий. Часть 2)
1) Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
2) При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен
    меняться на случайный элемент из списка, созданного в предыдущем пункте.
3) При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.
"""


def lesson_16():
    colors = ["Red", "Yellow", "Blue", "Green", "Gray", "Black", "Brown", "Pink"]

    # !функция меняющая цвет фона окна
    def color_in(event):
        event.widget.config(bg=random.choice(colors))

    # !функция возвращающая белый цвет фона окна
    def color_out(event):
        event.widget.config(bg="SystemButtonFace")

    root = tkinter.Tk()
    setWindow(root)
    # !определение навеление и отведения курсона на окно
    root.bind("<Enter>", color_in)
    root.bind("<Leave>", color_out)

    root.mainloop()


# --------------------------------------------------------
""" Раздел 5 (17 Обработка событий. Часть 3)
1) Выведите, используя метку, в окне такую строку: «ax^2 + bx + c = 0».
2) Добавьте 3 текстовых поля с метками «a:», «b:» и «c:».
3) Добавьте кнопку «Вычислить корни уравнения».
4) После вычисления их нужно вывести под кнопкой в формате: «x1 = …; x2 = …;».
5) Если число под корнем отрицательное, то вывести в метке для результата строку: «Нет корней».
"""


def lesson_17():
    # ! функция обработки нажатия кнопки
    def processing(event=False):
        try:
            D = float(en_b.get())**2 - 4*float(en_a.get())*float(en_c.get())
            if D < 0:
                result.config(text="Нет корней")
            elif D > 0:
                x1 = (-float(en_b.get())+sqrt(D)) / (2*float(en_a.get()))
                x2 = (-float(en_b.get())-sqrt(D)) / (2*float(en_a.get()))
                result.config(text=f"x1 = {x1};\nx2 = {x2}")
            else:
                x = (-float(en_b.get())+sqrt(D)) / (2*float(en_a.get()))
                result.config(text=f"Корень один:\nx = {x}")
        except ValueError:
            if not en_a.get() or not en_b.get() or not en_c.get():
                result.config(text="Вы ничего не ввели...")
            else:
                result.config(text="Введены не числа")
    # ! создание окна
    root = tkinter.Tk()
    # setWindow(root)
    wind = SetWindow(root, 800, 600, "My Window")
    # ! заголовок
    header = tkinter.Label(root, text="ax^2 + bx + c = 0", font="Arial 20")
    # ! метки для a b c
    label_a = tkinter.Label(root, text="a: ", font="Tahoma 16")
    label_b = tkinter.Label(root, text="b: ", font="Tahoma 16")
    label_c = tkinter.Label(root, text="c: ", font="Tahoma 16")
    # ! текстовые поля для a b c
    en_a = tkinter.Entry(root, font="Tahoma 16", width=5)
    en_b = tkinter.Entry(root, font="Tahoma 16", width=5)
    en_c = tkinter.Entry(root, font="Tahoma 16", width=5)
    # ! кнопка
    button = tkinter.Button(root, text="Вычислить корни уравнения", font="Arial 18", command=processing)
    # ! метка с результатом
    result = tkinter.Label(root, font="Arial 18")
    # ! обработка при нажатии на Enter
    en_a.bind("<Return>", processing)
    en_b.bind("<Return>", processing)
    en_c.bind("<Return>", processing)
    # ! рисуем интерфейс
    header.place(relx=0.5, rely=0.01, anchor="n")
    label_a.place(relx=0.5, rely=0.2, anchor="ne")
    label_b.place(relx=0.5, rely=0.3, anchor="ne")
    label_c.place(relx=0.5, rely=0.4, anchor="ne")
    en_a.place(relx=0.5, rely=0.2, anchor="nw")
    en_b.place(relx=0.5, rely=0.3, anchor="nw")
    en_c.place(relx=0.5, rely=0.4, anchor="nw")
    button.place(relx=0.5, rely=0.6, anchor="center")
    result.place(relx=0.5, rely=0.7, anchor="n")

    wind.run()
    # root.mainloop()
