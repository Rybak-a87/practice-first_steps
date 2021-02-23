def cesar_shifr_r(strng, n, lang):
    if lang == "ru":
        alf = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    elif lang == "en":
        alf = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in strng:
        if i.lower() in alf:
            new_ind = alf.index(i.lower()) + n
            if new_ind > len(alf):
                new_ind -= len(alf)
            if i.isupper():
                res += alf[new_ind].upper()
            else:
                res += alf[new_ind]
        else:
            res += i
    return res


def cesar_shifr_l(strng, n, lang):
    if lang == "ru":
        alf = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    elif lang == "en":
        alf = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in strng:
        if i.lower() in alf:
            new_ind = alf.index(i.lower()) - n
            if i.isupper():
                res += alf[new_ind].upper()
            else:
                res += alf[new_ind]
        else:
            res += i
    return res


def right_or_left(text, n, derection, lang):
    if derection == "right":
        res = cesar_shifr_r(text, n, lang)
    elif derection == "left":
        res = cesar_shifr_l(text, n, lang)
    return res


text = input("Enter your text: ")
n = int(input("How match? : "))
der = input("Left or right? : ")
lang = input("ru or en? : ")
res = right_or_left(text, n, der, lang)
print(res)
