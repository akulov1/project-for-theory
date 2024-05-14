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
    answer += f"б) {round(otvet2,5)}\n"
    return text, answer


def task_2():
    vsego = randint(5, 13) * 5
    rus = int(vsego / 5 + 6)
    tatar = int(vsego / 5+2)
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
    text = f"8. В {bairon} (из {vsego} оставшихся) экзаменационных билетах по эстетике вопрос связан с поэзией Джорджа Ноэля Гордона Байрона, в {balmont} — со стихами русского " \
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
    text = f"9. В магазин вошло {vsego} покупателей. Найдите вероятность события, состоящего в том, что {buyer} из них будут что-нибудь покупать. " \
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
    answer += f"\t| {round(p0 + p1,2)}, 1<x<=2\n"
    answer += f"\t| {round(p0 + p1 + p2,2)}, 2<x<=3\n"
    answer += f"\t| 1, 3<x\n"

    return text, answer


def task_13():
    p = randint(1, 5) / 100
    q = round(1 - p, 2)
    n = randint(6, 9)
    answer = "13. \n"
    text = f"13. Вероятность отказа локомотива на линии за время полного оборота составляет {p}. " \
           f"На линии работает {n} локомотивов. Составить ряд распределения числа отказов. " \
           "Найти M(X) и D(X) этой случайной величины.\n"
    answer += "X|\t"
    for i in range(0, 4):
        answer += f"{i}\t\t\t|\t\t\t\t"
    answer += f"... |\t\t{n}\nP|\t"
    answer += f"{q}^{n}\t"
    for i in range(1, 4):
        answer += f"\t|{combination(n, i)[2]}*{p}^{i}*{q}^{n - i}"
    answer += f" |\t\t\t\t... |\t{p}^{n}\t\n\n"
    answer += f"M(X) = {round(n * p, 3)}\nD(X) = {round(n * p * q, 5)}\n"

    return text, answer


def task_14():
    p = randint(1, 5) / 100
    q = round(1 - p, 2)
    n = randint(10, 20) * 10
    answer = "14. \n"
    text = f"14. Вероятность выхода из строя монитора компьютера после оговоренного срока работы равна {p}. " \
           f"Проведены наблюдения за работой {n} мониторов. Составить ряд распределения числа мониторов, вышедших из " \
           "строя после оговоренного срока работы. Найти M(X) этой случайной величины.\n"
    answer += "X|\t"
    for i in range(0, 4):
        answer += f"{i}\t\t\t|\t\t\t\t\t"
    answer += f"... |\t\t{n}\nP|\t"
    answer += f"{q}^{n}\t"
    for i in range(1, 4):
        answer += f"|{combination(n, i)[2]}*{p}^{i}*{q}^{n - i} "
    answer += f" |\t\t\t\t\t... |\t\t{p}^{n}\t\n\n"
    answer += f"M(X)={round(n * p, 5)}\n"

    return text, answer


def task_15():
    x1 = -3
    x2 = 1
    x3 = 5
    p1 = randint(2,4)/10
    p2 = randint(15,35)/100
    p3 = round(1-p1-p2,3)
    dictx = {x1: p1, x2: p2, x3: p3}
    y1 = 2
    y2 = 4
    q1 = randint(2,6)/10
    q2 = round(1-q1,3)
    dicty = {y1: q1, y2: q2}
    text = f"X\t|\t{x1} |\t{x2}\t|\t{x3}\t|\n"
    text += f"P\t|\t{p1}|\t{p2}|\t{p3}|\n\n"
    text += f"Y\t|\t{y1}\t|\t{y2}\t|\n"
    text += f"Q\t|\t{q1} |\t{q2}\t|\n\n"

    answer = "15.\n"
    text += "15. Независимые случайные величины X и Y заданы таблицами распределений. Найти: \n"
    text += "1) M(X), M(Y), D(X), D(Y);"
    answer += f"1) M(X)={round(x1 * p1 + x2 * p2 + x3 * p3, 4)} \nD(X)={round(discr_dispersion(dictx), 4)}\n"
    answer += f"M(Y)={round(discr_math_expectation(dicty), 4)}\nD(Y)={round(discr_dispersion(dicty), 4)}\n"

    text += "2) таблицы распределения случайных величин Z1 = 2X+Y, Z2 = X*Y;\n"
    answer += "2)\nZ1=2X+Y\n"
    answer+=f"Z1\t|\t{2*x1+y1}\t|\t{2*x1+y2}\t|\t{2*x2+y1}\t|\t{2*x2+y2}\t|\t{2*x3+y1}\t|\t{2*x3+y2}\t|\n"
    answer+=f"P1\t|  {round(p1*q1,3)} |  {round(p1*q2,3)} |  {round(p2*q1,3)} |  {round(p2*q2,3)} |  {round(p3*q1,3)} |  {round(p3*q2,3)} |\n\n"
    dictz1 = {2*x1+y1:round(p1*q1,3), 2*x1+y2:round(p1*q2,3),2*x2+y1:round(p2*q1,3),2*x2+y2:round(p2*q2,3),2*x3+y1:round(p3*q1,3),2*x3+y2:round(p3*q2,3)}

    answer+="Z2 = X*Y\n"
    answer += f"Z1\t|\t{x1*y1}\t|\t{x1*y2}\t|\t{x2*y1}\t|\t{x2*y2}\t|\t{x3*y1}\t|\t{x3*y2}\t|\n"
    answer += f"P1\t|  {round(p1 * q1, 3)} |  {round(p1 * q2, 3)} |  {round(p2 * q1, 3)} |  {round(p2 * q2, 3)} |  {round(p3 * q1, 3)} |  {round(p3 * q2, 3)} |\n\n"
    dictz2 = {x1*y1: round(p1 * q1, 3), x1*y2: round(p1 * q2, 3), x2*y1: round(p2 * q1, 3),
              x2*y2: round(p2 * q2, 3), x3*y1: round(p3 * q1, 3), x3*y2: round(p3 * q2, 3)}

    text+="3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам распределений и на основании свойств математического ожидания и дисперсии."
    answer+=f"3) M(Z1)={round(discr_math_expectation(dictz1),4)} \nM(Z2)={round(discr_math_expectation(dictz2),4)}\n"
    answer+=f"D(Z1)={round(discr_dispersion(dictz1),4)} \nD(Z2)={round(discr_dispersion(dictz2),4)}\n"
    return text, answer


def task_16():
    text = '16. Дана функция распределения F(x) непрерывной случайной величины X.\n' \
           'Требуется:\n1) найти плотность вероятности f(x);\n2) построить графики F(x) и f(x);\n' \
           '3) найти M(X), D(X), (Х);\n4) найти Р(α < X < β) для данных α, β\n'
    text += '\t|\t0, x <= -π/2;\nF(x)= |\tcosx, -π/2 < x <= 0;\n\t|\t1, x > 0;\n'

    alfa = '-π/2'
    beta = '-π/6'
    alfa_type = randint(1, 2)
    if alfa_type == 2:
        alfa = '-π/4'
        beta = '-π/3'
    text += f'α = {alfa}, β = {beta}\n'

    answer="16. \n"
    answer += '\t|\t0, x <= -π/2;\nf(x)= |\t-sinx, -π/2 < x <= 0;\n\t|\t0, x > 0;\n'
    answer += 'M(X) = 1, M(X^2) = π+1, \nD(X) = π, ' \
              'Отклонение = √π\n'
    if alfa_type == 1:
        answer += f'P(α < x < β) = P({alfa} < x < {beta}) = √3/2'
    else:
        answer += f'P(α < x < β) = P({alfa} < x < {beta}) = (1 - √2)/2'

    return text, answer

def task_17():
    answer = '17.\n '
    alfa = randint(1, 2)
    beta = randint(3, 5)
    text = '17. 1) проверить свойство  ∫( f(x)dx ) = 1;\n' \
           '2) построить график f(x);\n3) найти функцию распределения F(x);\n' \
           '4) найти Р(α < X < β) для данных α, β;\n5) найти М(Х), D(X), σ(X).\n'
    text += '\t |\t0, x <= -1;\n\t |\t1/4, -1 < x <= 2;\nf(x)=|\t1/36 * (x-5)^2, 2 < x <= 5;\n\t |\t0, x>5;\n'
    text += f'α = {alfa}, β = {beta}\n'

    answer += '\t |\t1, x <= -1;\n\t |\t1/4*x, -1 < x <= 2;\nF(x)=|' \
              '\t1/108 * (x-5)^3, 2 < x <= 5;\n\t |\t1, x>5;\n'

    num = round(((beta-5)**3)/108, 3)
    num -= round(alfa/4, 3)
    answer += f'Р(α < X < β) = P({alfa} < X < {beta}) = {num}\n'

    MX = round(3/8+11/16, 3)
    MX2 = round(3/4+79/40, 3)
    DX = round(MX2 - MX ** 2, 3)
    std = round(math.sqrt((DX)), 3)
    answer += f'M(X) = {MX}, D(X) = {DX}, Отклонение = {std}\n'

    return text, answer

def task_18():
    dlina = randint(12,20)*10
    delta = randint(8,14)
    more = dlina+delta-2
    text = f"18. Автомат штампует детали. Проектная длина детали равна {dlina} мм. Фактическая длина детали X распределена нормально (m = {dlina} мм). "\
            f"При контроле работы автомата выяснилось, что длина изготовленных деталей {dlina-delta} X {dlina+delta} (мм). "\
            f"Какова вероятность того, что длина наугад взятой детали более {more} мм?\n"
    answer = "18. \n"
    answer+=f"P = {local_lapl((more-dlina)/delta)}"

    return text, answer

def task_19():
    time = randint(120,140)*10
    text=f"19. Время T работы рессорного подвешивания до выхода из строя имеет экспоненциальное распределение с математическим ожиданием {time} ч. "\
          f"Какова вероятность того, что данный комплект рессор проработает до выхода из строя: а) не менее {time} ч; б) от {time} до {time*2} ч; в) менее 500 ч?\n"
    answer="19.\n"
    answer+=f"a) {round(1-math.exp(-(time/time)),5)}\n"
    answer+=f"б) {round(math.exp(-(time/time))-math.exp(-((time*2)/time)),5)}\n"
    answer+=f"в) {round(1-math.exp(-500/time),5)}"

    return text,answer

def task_20():
    mat = randint(4,6)*10
    disp = randint(2,4)
    sigma = round(math.sqrt(disp),3)
    x1=mat-disp
    x2=mat+disp
    text=(f"20. Длина изделий, выпускаемых цехом, имеет нормальное распределение с параметрами: математическое ожидание m = {mat} см, дисперсия D = {disp} см2. "
          f"Записать формулу f(x) для длины изделий. Какова вероятность того, что длина наугад взятого изделия находится в интервале от {x1} до {x2} см?\n")
    answer="20.\n"
    answer+=f"f(x)=1/(√(2*π*{disp}))*e^(-(x-{mat})^2/(2*{disp}))\n"
    z1=round((x1-mat)/sigma,2)
    z2 = round((x2 - mat) / sigma, 2)
    answer+=f"P = {round(2*integr_lapl(z2),3)}"

    return text,answer

def task_21():
    vsego = randint(55,65)
    m = randint(60,64)
    delta = randint(1,2)
    maxi = randint(vsego*m+6,vsego*m+30)
    text=(f"21. В составе имеется {vsego} цистерны с нефтью, причем масса каждой цистерны Xi имеет одно и то же нормальное распределение (m = {m} т;σ = {delta} т). "
          f"Один тепловоз может везти состав массой не более {maxi} т, иначе необходимо прицеплять второй. Какова вероятность того, что потребуется кратная тяга?\n")
    mat=vsego*m
    disper = delta**2*64
    sigma=math.sqrt(disper)
    num = (maxi-mat)/sigma
    answer="21. \n"
    answer+=f"P = {local_lapl((maxi-mat)/sigma)}\n(M(X)={mat};D(X)={disper};σ={sigma})"

    return text,answer

