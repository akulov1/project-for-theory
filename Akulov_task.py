from random import randint
from random import uniform
import math
from functions import *


def task_1():
    zadachi = randint(2, 5) * 4
    bernulli = zadachi / 4
    classic = zadachi / 2
    geom = zadachi / 4
    answer = "1. \n"
    text = f"1. На экзамене по теории вероятностей предлагаются {int(classic)} задач на классическую схему и по {int(bernulli)} — на схему " \
           "Бернулли и геометрическую схему. Студент последовательно пытается решить 3 задачи. Какова вероятность того, что:\n"
    text += "a) первая задача окажется на классическую схему, вторая — на схему Бернулли и третья — на геометрическую схему\n"
    otvet1 = (classic / zadachi) * (bernulli / (zadachi - 1)) * (geom / (zadachi - 2))
    answer += f"а) {otvet1}, {int(classic * bernulli * geom)}/{(zadachi * (zadachi - 1) * (zadachi - 2))}\n"
    text += f"б) первая задача была не на классическую схему?\n"
    otvet2 = 1 - ((bernulli + geom) / zadachi)
    answer += f"б) {otvet2}\n"
    return text, answer


def task_2():
    vsego = randint(5, 13) * 5
    rus = int(vsego / 5 + 10)
    tatar = int(vsego / 5)
    ost = vsego - rus - tatar
    vibor = randint(4, 7)

    answer = "2. \n"
    text = f"2. В сборнике «Сказки» из {vsego} сказок — {rus} русских и {tatar} татарских. Учитель наугад по оглавлению выбирает {vibor} сказки." \
           "Найти вероятность того, что среди выбранных сказок:\n"
    text += "а) ни одной русской и ни одной татарской сказки;\n"
    answer += f"a) {combination(vsego - (rus + tatar), vibor)[2]}/{combination(vsego, vibor)[2]}\n"

    chrus = int(vibor / 2)
    chtatar = chrus - 1
    chost = vibor - chtatar - chrus
    text += f"б) {chrus} русских и {chtatar} татарская сказка.\n"
    answer += f"б) ({combination(rus, chrus)[2]}*{combination(tatar, chtatar)[2]}*{combination(ost, chost)[2]})/{combination(vsego, vibor)[2]}\n"

    return text, answer


def task_3():
    text = "3. Опыт состоит в бросании двух монет. Рассматриваются следующие события: А — появление герба на первой" \
           "монете; С — появление герба на второй монете; В — появление хотя бы одного герба. Определить, каким событиям" \
           "этого списка равносильны следующие события:\n" \
           "a) A ∪ C;\n" \
           "б) A ∩ C.\n"
    answer = "3. \n" \
             "а) A ∪ C равносильно B.\n" \
             "б) A ∩ C равносильно B.\n"
    return text, answer


def task_4():
    s1 = randint(6, 9) / 10
    s2 = randint(4, 7) / 10
    answer = "4. \n"
    text = f"4.Две студентки посещают концерты Омского камерного оркестра, первая — с вероятностью {s1}, вторая — с вероятностью {s2}." \
           " Какова вероятность того, что в очередной «музыкальный» четверг в университетский актовый зал придут на концерт:\n"

    text += "а) обе студентки;\n"
    answer += f"a) {round(s1 * s2, 2)}\n"

    text += "б) только одна из них;\n"
    o2 = ((s1 * (1 - s2)) + ((1 - s1) * s2))
    answer += f"б) {round(o2, 2)}\n"

    text += "в) хотя бы одна из них?\n"
    answer += f"в) {round(1 - ((1 - s1) * (1 - s2)), 2)}\n"
    return text, answer


def task_5():
    None


def task_6():
    vsego = randint(6, 12)
    new = vsego - int((vsego / 3))
    old = vsego - new
    need = randint(2, new)
    answer = "6.\n"
    text = f"6. В коробке находятся {new} новых и {old} израсходованные батарейки для фотоаппарата. Какова вероятность того, что {need} вынутые наугад" \
           "батарейки окажутся новыми?\n"
    o = combination(new, need)[1] / combination(vsego, need)[1]
    answer += f"{round(o, 5)}, {combination(new, need)[2]}/{combination(vsego, need)[2]}\n"
    return text, answer


def task_7():
    f1 = randint(6, 9) / 10
    f2 = randint(6, 9) / 10
    f3 = randint(6, 9) / 10
    answer = "7. \n"
    text = f"7. На склад поступают диваны с трех мебельных фабрик. Первая и третья фабрики изготавливают одинаковое количество продукции, а вторая — вдвое больше. Вероят" \
           f"ность для первой, второй и третьей фабрики сделать бракованный диван равна {f1}, {f2} и {f3} соответственно. " \
           "Какова вероятность того, что счастливый обладатель дивана, купленного наудачу, будет спать спокойно?\n"
    otv = 0.25 * f1 + 0.5 * f2 + 0.25 * f3
    answer += f" {round(otv, 4)}\n"

    return text, answer


def task_8():
    vsego = randint(8, 14)
    bairon = int(vsego / 3)
    balmont = int(vsego / 2)
    mits = vsego - bairon - balmont
    f1 = randint(6, 9) / 10
    f2 = randint(5, 9) / 10
    f3 = randint(3, 9) / 10
    answer = "8. \n"
    text = f"В {bairon} (из {vsego} оставшихся) экзаменационных билетах по эстетике вопрос связан с поэзией Джорджа Ноэля Гордона Байрона, в {balmont} — со стихами русского " \
           f"поэта Константина Дмитриевича Бальмонта и в {mits} — с творчеством польского поэта Адама Мицкевича. Вероятность того, что экзаменатор попросит (в развитие темы билета) " \
           f"студента прочесть наизусть стихи Байрона, равна {f1}, стихи Бальмонта — {f2}, стихи Мицкевича — {f3}. Счастливый студент, сдавший экзамен, сообщил, что стихов " \
           "на экзамене не читал. Какова вероятность того, что ему достался билет по творчеству Байрона?\n"
    answer += f"{round((bairon / vsego) * (1 - f1), 4)}\n"

    return text, answer


def task_9():
    p = randint(2, 8) / 10
    q = round(1 - p, 2)
    vsego = randint(6, 12)
    buyer = randint(1, vsego - 2)
    answer = "9. \n"
    text = f"В магазин вошло {vsego} покупателей. Найдите вероятность события, состоящего в том, что {buyer} из них будут что-нибудь покупать. " \
           f"Вероятность того, что любой из вошедших в магазин не уйдет без покупки, равна {p}.\n"
    otv = combination(vsego, buyer)[1] * pow(p, buyer) * pow(q, vsego - buyer)
    answer = f"{combination(vsego, buyer)[2]}*({p})^{buyer}*{q}^{vsego - buyer} = {round(otv, 4)}"

    return text, answer


def task_10():
    vsego = randint(10, 16) * 1000
    p = round(1 / 6, 4)
    q = round(1 - p, 4)

    answer = "10. \n"
    text = f"10. Игральная кость бросается {vsego} раз. Какова вероятность того, что шестерка появится:\n"

    st = randint(15, 24) * 100
    sig = st + randint(2, 4) * 100
    text += f"а) не менее {st} и не более {sig} раз;\n"
    x1 = round((st - vsego * p) / (p * q * vsego), 2)
    x2 = round((sig - vsego * p) / (p * q * vsego), 2)
    answer += f"a) {round(integr_lapl(x2) - integr_lapl(x1), 4)}\n"

    x = vsego / 2
    text += f"б) {int(x)} раз?\n"
    answer += f"б) {local_lapl((x - vsego * p) / (p * q * vsego))}\n"

    return text, answer


def task_11():
    vsego = randint(3, 6) * 1000
    p = round(randint(10, 40) / 1000, 5)
    k = int(vsego / 100)
    answer = "11. \n"
    text = f"11. Завод отправил на базу {vsego} лампочек. Вероятность повреждения лампочки при перевозке равна {p}. Найдите вероятность того, что поврежденными окажутся {k} лампочек.\n"

    answer += f"{combination(vsego, k)[2]}*({p}^{k})*({round(1 - p, 5)}^{vsego - k})\n"

    return text, answer


def task_12():
    s1 = randint(5, 9) / 10
    s2 = randint(4, 9) / 10
    s3 = randint(3, 9) / 10
    answer = "12. \n"
    text = f"12. Три стрелка делают по одному выстрелу в мишень. Вероятность попадания в нее для первого стрелка равна {s1}; для второго — {s2}; для третьего — {s3}." \
           " Составить ряд распределения числа попаданий в мишень. " \
           "Найти М(Х), D(X), σ(X), F(X) этой случайной величины.\n"

    x0 = 0;
    x1 = 1;
    x2 = 2;
    x3 = 3
    p0 = round((1 - s1) * (1 - s2) * (1 - s3), 2)
    p1 = round(s1 * (1 - s2) * (1 - s3) + (1 - s1) * s2 * (1 - s3) + (1 - s1) * (1 - s2) * s3, 2)
    p2 = round(s1 * s2 * (1 - s3) + s1 * (1 - s2) * s3 + (1 - s1) * s2 * s3, 2)
    p3 = round(s1 * s2 * s3, 2)
    dictionary = {x0: p0, x1: p1, x2: p2, x3: p3}

    answer += "X\t"
    for i in range(0, 4):
        answer += f"{i}\t\t"
    answer += "\n"
    answer += f"P\t{p0}\t{p1}\t{p2}\t{p3}"
    answer += '\n\n'

    M = discr_math_expectation(dictionary)
    D = discr_dispersion(dictionary)
    S = discr_standart_deviation(dictionary)
    answer += f'M(X) = {M}\nD(X) = {D}\nσ = {S}\n'

    answer += "F(x):\n"
    answer += "\t| 0, x<=0\n"
    answer += f"\t| {p0}, 0<x<=1\n"
    answer += f"\t| {p0+p1}, 1<x<=2\n"
    answer += f"\t| {p0+p1+p2}, 2<x<=3\n"
    answer += f"\t| 1, 3<x\n"

    return text, answer

def task_13():
    p = randint(1,5)/100
    q = round(1-p,2)
    n = randint(6,9)
    answer = "13. \n"
    text=f"Вероятность отказа локомотива на линии за время полного оборота составляет {p}. "\
        f"На линии работает {n} локомотивов. Составить ряд распределения числа отказов. "\
         "Найти M(X) и D(X) этой случайной величины.\n"
    answer+="X|\t"
    for i in range(0,4):
        answer+=f"{i}\t\t\t|\t\t\t\t"
    answer+=f"... |\t\t{n}\nP|\t"
    answer+=f"{q}^{n}\t"
    for i in range(1,4):
        answer+=f"\t|{combination(n,i)[2]}*{p}^{i}*{q}^{n-i}"
    answer+=f" |\t\t\t\t... |\t{p}^{n}\t\n\n"
    answer+=f"M(X) = {round(n*p,3)}\nD(X) = {round(n*p*q,5)}\n"

    return text,answer

def task_14():
    p = randint(1, 5) / 100
    q = round(1 - p, 2)
    n = randint(10,20)*10
    answer="14. \n"
    text=f"Вероятность выхода из строя монитора компьютера после оговоренного срока работы равна {p}. "\
        f"Проведены наблюдения за работой {n} мониторов. Составить ряд распределения числа мониторов, вышедших из "\
        "строя после оговоренного срока работы. Найти M(X) этой случайной величины.\n"
    answer += "X|\t"
    for i in range(0, 4):
        answer += f"{i}\t\t\t|\t\t\t\t\t"
    answer += f"... |\t\t{n}\nP|\t"
    answer += f"{q}^{n}\t"
    for i in range(1, 4):
        answer += f"|{combination(n, i)[2]}*{p}^{i}*{q}^{n - i} "
    answer += f" |\t\t\t\t\t... |\t\t{p}^{n}\t\n\n"
    answer+=f"M(X)={round(n*p,5)}\n"

    return text,answer

