from random import randint
from random import uniform
import math
from functions import *


def task_1():
    quantity_stud = randint(10, 20)
    answer = "1. \n"
    text = f"1. Студенты трех групп (по {int(quantity_stud)} человек в каждой) выбирают трех человек для участия в профсоюзной конференции: руководителя делегации, докладчика и содокладчика." \
           "Какова вероятность того, что:\n"
    text += "a) для этого будут выбраны старосты первой, второй и третьей групп соответственно\n"
    otvet1 = (1 / (quantity_stud ** 3))
    answer += f"a) {round(otvet1,5)}\n"
    text += f"б) докладчиком и содокладчиком будут выбраны старосты?\n"
    otvet2 = (1 / (quantity_stud ** 2))
    answer += f"б) {round(otvet2,5)}\n"
    return text, answer


def task_2():  #хз что с этим делать
    whole = randint(5, 13) * 5
    rus = int(whole / 5 + 5)
    france = int(whole / 6)
    sur = whole - rus - france
    choice0 = (randint(6, rus - 2))
    choice1 = choice0 - randint(1, choice0 - 4)
    choice2 = int((choice0-2) / 2)
    answer = "2. \n"
    text = f"2. В Зеленом зале художественного салона развешаны картины: {rus} натюрмортов русских художников, {int(france)} полотен французских импрессионистов и {int(sur)} картины представителей сюрреализма." \
           f"Воры в темноте наугад снимают {choice0} картин. Какова вероятность того, что среди этих картин:\n"
    text += f"а) {choice1}  натюрморта\n"
    maincomb = combination(whole,choice0)[1]
    acomb = combination(rus,choice1)[1]*combination(whole-rus,choice0-choice1)[1]
    answer += f"а) P = ({combination(rus,choice1)[2]}*{combination(whole-rus,choice0-choice1)[2]})/{combination(whole,choice0)[2]} =  {round(acomb/maincomb, 5)}\n"
    text += f"б) по {choice2} картины импрессионистов и сюрреалистов\n"
    bcomb = combination(france,choice2)[1]*combination(sur,choice2)[1]*combination(rus,choice0-2*choice2)[1]
    answer += f"б) P = ({combination(france,choice2)[2]}*{combination(sur,choice2)[2]}*{combination(rus,choice0-2*choice2)[2]})/{combination(whole,choice0)[2]} = {round(bcomb/maincomb, 5)}\n"
    return text, answer

def task_3():
    text = "3.Пусть X - число очков, выпавших на верхней грани игральной кости при однократном подбрасывании." \
           "События: А - Х кратно трем; В - Х нечетно; D - Х кратно двум; Е - Х дробно; Н - Х больше шести. " \
           "Постройте множество элементарных исходов и выявите состав подмно- жеств, соответствующих событиям: \n" \
           "А) B;\n " \
           "Б) E ∪ D\n" \
           "B) A ∩ B \n" \
           "Г) E ∩ H\n"
    answer = "3. \n" \
             "А) B={1,3,5} \n" \
             "Б) E ∪ D = {2,4,6}\n" \
             "В) A ∩ B = {3}\n" \
             "Г) E ∩ H = Ø\n"
    return text, answer


def task_4():
    melon = randint(6, 9) / 10
    cream = randint(4, 7) / 10
    answer = "4. \n"
    text = f"4. Кошка Фуша выбирает из предложенных ей продук- тов сметану с вероятностью 0,7, дыню - с вероятностью 0,95." \
           "Какова вероятность того, что сегодня: \n"
    text += " a) кошка Фуша выберет только дыню;\n"
    a1 = (melon * (1 - cream))
    answer += f"a) {round(a1, 4)}\n"
    text += "б) не выберет ни дыню, ни сметану;\n"
    a2 = ((1 - melon) * (1 - cream))
    answer += f"б) {round(a2, 4)}\n"
    text += "c) выберет либо дыню, либо сметану?\n"
    a3 = (melon + cream) - (melon * cream)
    answer += f"c) {round(a3, 4)}\n"
    return text, answer


def task_5():
    water1 = randint(6, 9) / 10
    water2 = randint(5, 8) / 10
    answer = "5. \n"
    text = f"5. Иван Иванович покупает бутылку минеральной воды «Карачинская» с вероятностью {water1}, а «Омская-1» - с вероятностью {water2}." \
           "Сегодня он купил 3 бутылки минеральной воды. Какова вероятность, что «Омской-1» он купил больше, чем «Карачинской»?\n"
    a1 = (pow(water2, 3))
    a2 = (combination(3, 2)[1] * water1 * (1 - water1) * (water2 ** 2) * (1 - water2))
    answer += f"{round(a1 + a2, 6)}\n"
    return text, answer


def task_6():
    words = ['ТЮЛЬПАН', 'АКУЛА', 'ЮРА', 'СУДЬБА', 'ЁЖИК']
    choice = randint(0, 4)
    text = f"6. На семи карточках написаны буквы "
    for j in range(0, len(words[choice])):
        text += f"{words[choice][j]}"
        if j != len(words[choice]) and j != len(words[choice]) - 1:
            text += ", "
    text += f". Карточки тщательно перемешивают, затем берут по одной и кладут последовательно рядом. Какова вероятность того, что получится слово «{words[choice]}»?\n"
    a = (1 / (choice ** choice))
    answer = "6. \n" \
             f"{round(1 / math.factorial(len(words[choice])), 5)}\n"
    return text, answer


def task_7():
    rab = randint(2, 4) / 10
    bez = rab / 4
    kom = 1 - rab - bez
    rabv = randint(4, 7) / 10
    bezv = round(randint(3, 5) / 10, 2)
    komv = round(randint(1, 4) / 10, 2)
    answer = "7. \n"
    text = f"7. В один из кризисных годов {rab * 100}% выпускников одной из групп университета путей сообщения устроились работать по специальности, " \
           f" {bez * 100}% не нашли работу и {kom * 100}% занялись коммерцией. Вероятность того, что выпускник, работающий по специальности, " \
           f"ближайшее лето проведет на курорте Боровое, равна {rabv}, для неработающего выпускника эта вероятность составляет {bezv}, " \
           f"для коммерсанта - {komv}. Первый позвонивший вам выпускник этой группы с горечью сообщил, что лето вынужден провести на Канарских островах." \
           "Какова вероятность, что он работает по специальности?\n"
    a1 = ((rabv * rab) + (bezv * bez) + (komv * kom))
    a2 = ((rabv * rab) / a1)
    answer += f"{round(a2, 4)}\n"
    return text, answer


def task_8():
    # Вероятности сидеть рядом с каждым из студентов
    p_Furman = randint(3, 6) / 10
    p_Mokin = round(p_Furman / 1.5,3)
    p_Sitnikov = round(1 - p_Mokin - p_Furman,3)
    answer = "8. \n"
    # Вероятности быть выгнанным доцентом Заблоцкой в зависимости от того, с кем сидел Щукин
    p_expulsion_Furman = randint(4, 7) / 10
    p_expulsion_Mokin = p_expulsion_Furman / 5
    p_expulsion_Sitnikov = 1 - p_expulsion_Mokin - p_expulsion_Furman
    text = f"8. На лекции по математике студент Щукин с вероятностью {p_Furman} садится рядом с Фурманом," \
           f"с вероятностью {p_Mokin} - с Мокиным, с вероятностью {p_Sitnikov} - с Ситниковым." \
           f"В первом случае вероятность того, что доцент Заблоцкая выгонит Щукина с лекции, равна {p_expulsion_Furman}," \
           f"во втором случае - {p_expulsion_Mokin}, в третьем - {p_expulsion_Sitnikov}. Сегодня студент Щукин дослушал лекцию до конца. С кем рядом вероятнее всего он сидел?\n"
    # Рассчитаем общие вероятности быть выгнанным для каждого из студентов
    p_expulsion = p_Furman * p_expulsion_Furman + p_Mokin * p_expulsion_Mokin + p_Sitnikov * p_expulsion_Sitnikov

    # Вероятность, что Щукин досидит лекцию до конца
    p_stay = 1 - p_expulsion

    # Найдем вероятность сидеть рядом с каждым студентом, учитывая, что Щукин досидел лекцию
    p_stay_Furman = p_Furman * p_expulsion_Furman / p_stay
    p_stay_Mokin = p_Mokin * p_expulsion_Mokin / p_stay
    p_stay_Sitnikov = p_Sitnikov * p_expulsion_Sitnikov / p_stay

    # Определим с кем вероятнее всего Щукин сидел
    max_probability = max(p_stay_Furman, p_stay_Mokin, p_stay_Sitnikov)
    if max_probability == p_stay_Furman:
        answer += f"{round(max_probability, 4)} Furman\n"
    elif max_probability == p_stay_Mokin:
        answer += f"{round(max_probability, 4)} Mokin\n"
    else:
        answer += f"{round(max_probability, 4)} Sitnikov\n"
    return text, answer


def task_9():
    n = randint(5, 10)
    falshivka = randint(2, 12)
    proknulo = randint(2, 4)
    text = f"9. Пара одинаковых игральных костей бросается {n} раз." \
           f"Какова вероятность того, что сумма очков, выпавших на обеих костях, равная {int(falshivka)}, повторится {int(proknulo)}?\n"
    a = (combination(n, proknulo)[1] * ((1 / 36) ** proknulo) * ((35 / 36) ** (n - proknulo)))
    answer = "9. \n"
    answer += f"{round(a, 4)}\n"
    return text, answer


def task_10():
    answer = "10. \n"
    n = randint(100, 150)
    p = randint(5, 9) / 10
    k = randint(50, 70)
    skail = randint(10, 20)
    text = f"10. Имеется {int(n)} станков, работающих независимо друг от друга." \
           f"Каждый из них включен в течение {p} рабочего времени. Какова вероятность того, что в произвольный момент окажутся включенными:" \
           f"a) {k} станков; б) от {k} до {k + skail} станков?\n"
    x = (k - n * p) / (n * p * (1 - p))
    y = (k + skail - n * p) / (n * p * (1 - p))
    otvet = local_lapl(x)
    answer += f'a) {otvet}\n'
    answer += f'б) {round(integr_lapl(round(y, 2)) - integr_lapl(round(x, 2)), 5)}\n'
    return text, answer


def task_11():
    answer = "11. \n"
    n = randint(1000, 2000)
    p = randint(1, 9) / 1000
    k = randint(1, 10)
    text = f"11. Радиоаппаратура состоит из {n} электроэлементов. Вероятность отказа одного элемента в течение одного года " \
           f"работы равна {p} и не зависит от состояния других элементов. Какова вероятность отказа не менее {k} электроэлементов за год?\n"
    lam = n * p
    a = (lam ** k) / (math.factorial(k)) * math.exp(-lam)
    answer += f"{round(a, 4)}\n"
    return text, answer


def task_12():
    answer = "12. \n"
    p1 = randint(70, 95) / 100
    p2 = randint(70, 95) / 100
    text = f"12. Каждые сутки со станции отправляются по два скорых поезда. Вероятность своевременного прибытия их " \
           f"на конечный пункт составляет соответственно {p1} и {p2}. Составить ряд распределения числа поездов, " \
           "которые прибудут в пункт назначения без опоздания. Найти M(X), D(X), G(X), F(X) этой случайной величины." \
           "Построить график F(X).\n"
    x0 = (1 - p1) * (1 - p2)
    x1 = ((1 - p2) * p1) + ((1 - p1) * p2)
    x2 = p1 * p2
    arr = {0: x0, 1: x1, 2: x2}
    m = discr_math_expectation(arr)
    d = discr_dispersion(arr)
    sig = math.sqrt(d)
    answer += "xi   |0|     |1|     |2|\n"
    answer += f"pi   |{round(x0, 3)}| |{round(x1, 3)}| |{round(x2, 3)}|\n"
    answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}, σ(X)={round(sig, 3)}\n"
    answer += f"F(x)= 0 при X<0\n"
    answer += f"F(x)= {round(x0, 3)} при 0<=X<1\n"
    answer += f"F(x)= {round(x1, 3)} при 1<=X<2\n"
    answer += f"F(x)= {round(x2, 3)} при 2<=X\n"
    return text, answer


def task_13():
    answer = "13. \n"
    n = randint(1, 3)
    p = randint(1, 6) / 10
    text = f"13. Случайная величина Х - число попаданий мячом в корзину при {n} броске. " \
           f"Вероятность попадания равна {p}. Составить ряд распределения случайной величины Х. Найти M(X) и D(X).\n"
    if n == 1:
        x0 = 1 - p
        x1 = p
        arr = {0: x0, 1: x1}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    elif n == 2:
        x0 = (1 - p) ** n
        x1 = 2 * ((1 - p) * p)
        x2 = p ** 2
        arr = {0: x0, 1: x1, 2: x2}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    elif n == 3:
        x0 = round((1 - p) ** 3, 3)
        x1 = round(3 * (((1 - p) ** 2) * p), 3)
        x2 = round(3 * ((pow(p, 2)) * (1 - p)), 3)
        x3 = round(p ** 3, 3)
        arr = {0: x0, 1: x1, 2: x2, 3: x3}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    return text, answer


def task_14():
    answer = '14. \n'
    n = randint(100, 200)
    k = randint(1, 9) / 100
    text = f"14. Вероятность выпуска бракованного изделия равна {k}. " \
           f"Выпущено {n} изделий. Составить ряд распределения числа бракованных изделий. " \
           "Найти М(X) этой случайной величины.\n"
    answer += "Ряд распределения:\n"
    m = n * k
    arr = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 7):
        p = combination(n, i)[1] * k ** i * (1 - k) ** (n - i)
        arr[i] = p
    answer += "|0|     |1|     |2|     |3|     |4|     |5|     |6|      ...\n"
    for i in range(0, 7):
        answer += f"|{round(arr[i], 3)}| "
    answer += "    ...\n"
    answer += f"M(x)={round(m, 5)}\n"
    return text, answer


def task_15():
    x1 = -1
    x2 = 1
    x3 = 2
    p1 = randint(1, 2) / 10
    p2 = randint(15, 35) / 100
    p3 = round(1 - p1 - p2, 3)
    dictx = {x1: p1, x2: p2, x3: p3}
    y1 = 3
    y2 = 4
    q1 = randint(2, 6) / 10
    q2 = round(1 - q1, 3)
    dicty = {y1: q1, y2: q2}
    text = f"X\t|\t{x1} |\t{x2}\t|\t{x3}\t|\n"
    text += f"P\t|\t{p1}|\t{p2}|\t{p3}|\n\n"
    text += f"Y\t|\t{y1}\t|\t{y2}\t|\n"
    text += f"Q\t|\t{q1} |\t{q2}\t|\n\n"

    answer = "15.\n"
    text += "15. Независимые случайные величины X и Y заданы таблицами распределений. Найти: \n"
    text += "1) M(X), M(Y), D(X), D(Y);\n"
    answer += f"1) M(X)={round(x1 * p1 + x2 * p2 + x3 * p3, 4)} \nD(X)={round(discr_dispersion(dictx), 4)}\n"
    answer += f"M(Y)={round(discr_math_expectation(dicty), 4)}\nD(Y)={round(discr_dispersion(dicty), 4)}\n"

    text += "2) таблицы распределения случайных величин Z1 = 2X+Y, Z2 = X*Y;\n"
    answer += "2)\nZ1=2X+Y\n"
    answer += f"Z1\t|\t{2 * x1 + y1}\t|\t{2 * x1 + y2}\t|\t{2 * x2 + y1}\t|\t{2 * x2 + y2}\t|\t{2 * x3 + y1}\t|\t{2 * x3 + y2}\t|\n"
    answer += f"P1\t|  {round(p1 * q1, 3)} |  {round(p1 * q2, 3)} |  {round(p2 * q1, 3)} |  {round(p2 * q2, 3)} |  {round(p3 * q1, 3)} |  {round(p3 * q2, 3)} |\n\n"
    dictz1 = {2 * x1 + y1: round(p1 * q1, 3), 2 * x1 + y2: round(p1 * q2, 3), 2 * x2 + y1: round(p2 * q1, 3),
              2 * x2 + y2: round(p2 * q2, 3), 2 * x3 + y1: round(p3 * q1, 3), 2 * x3 + y2: round(p3 * q2, 3)}

    answer += "Z2 = X*Y\n"
    answer += f"Z1\t|\t{x1 * y1}\t|\t{x1 * y2}\t|\t{x2 * y1}\t|\t{x2 * y2}\t|\t{x3 * y1}\t|\t{x3 * y2}\t|\n"
    answer += f"P1\t|  {round(p1 * q1, 3)} |  {round(p1 * q2, 3)} |  {round(p2 * q1, 3)} |  {round(p2 * q2, 3)} |  {round(p3 * q1, 3)} |  {round(p3 * q2, 3)} |\n\n"
    dictz2 = {x1 * y1: round(p1 * q1, 3), x1 * y2: round(p1 * q2, 3), x2 * y1: round(p2 * q1, 3),
              x2 * y2: round(p2 * q2, 3), x3 * y1: round(p3 * q1, 3), x3 * y2: round(p3 * q2, 3)}

    text += "3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам распределений и на основании свойств математического ожидания и дисперсии."
    answer += f"3) M(Z1)={round(discr_math_expectation(dictz1), 4)} \nM(Z2)={round(discr_math_expectation(dictz2), 4)}\n"
    answer += f"D(Z1)={round(discr_dispersion(dictz1), 4)} \nD(Z2)={round(discr_dispersion(dictz2), 4)}\n"
    return text, answer


def task_16():
    text = '16. Дана функция распределения F(x) непрерывной случайной величины X.\n' \
           'Требуется:\n1) найти плотность вероятности f(x);\n2) построить графики F(x) и f(x);\n' \
           '3) найти M(X), D(X), (Х);\n4) найти Р(α < X < β) для данных α, β\n'
    text += '\t|\t0, x <= 3π/4;\nF(x)= |\tcos2x, 3π/4 < x <= π;\n\t|\t1, x > π;\n'
    alfa = '3π/4'
    beta = '3π/2'
    alfa_type = randint(1, 2)
    if alfa_type == 2:
        alfa = 'π/6'
        beta = 'π'
    text += f'α = {alfa}, β = {beta}\n'
    answer = "16. \n"
    answer += '\t|\t0, x <= 3π/4;\nf(x)= |\tsin2x/2, 3π/4 < x <= π;\n\t|\t0, x > π;\n'
    answer += 'M(X) = 1,4281, M(X^2) = 4,0966, \nD(X) = 2,6685, ' \
              'σ = 1,6335\n'
    if alfa_type == 1:
        answer += f'P(α < x < β) = P({alfa} < x < {beta}) = 1/2'
    else:
        answer += f'P(α < x < β) = P({alfa} < x < {beta}) = -√3/4'

    return text, answer


def task_17():
    answer = '17.\n '
    alfa = randint(2, 3)
    beta = randint(4, 6)
    text = '17. 1) проверить свойство  ∫( f(x)dx ) = 1;\n' \
           '2) построить график f(x);\n3) найти функцию распределения F(x);\n' \
           '4) найти Р(α < X < β) для данных α, β;\n5) найти М(Х), D(X), σ(X).\n'
    text += '\t |\t0, x <= 2;\n\t |\t3/10(x-2)^2, 2 < x <= 3;\nf(x)=|\t3/10, 3 < x <= 6;\n\t |\t0, x>6;\n'
    text += f'α = {alfa}, β = {beta}\n'

    answer += '\t |\t1, x <= 2;\n\t |\t3/10*(x^3/3 - 2x^2 +4x), -1 < x <= 2;\nF(x)=|' \
              '\t3/10x, 3 < x <= 6;\n\t |\t1, x>6;\n'

    num = round(3 / 10 * alfa, 3)
    num -= round((3 / 10) * ((beta ** 3) / 3 - ((2 * beta) ** 2) + (4 * beta)), 3)
    answer += f'Р(α < X < β) = P({alfa} < X < {beta}) = {num}\n'

    MX = round(11 / 40 + 81 / 20, 3)
    MX2 = round(19 / 25 + 189 / 10, 3)
    DX = round(MX2 - MX ** 2, 3)
    std = round(math.sqrt((DX)), 3)
    answer += f'M(X) = {MX}, D(X) = {DX}, σ(X) = {std}\n'
    return text, answer


def task_18():
    answer = "18. \n"
    σ = randint(1, 3)
    m = randint(4, 7)
    p1 = randint(10, 15)
    p2 = randint(8, 11)
    text = f"18. Динамическая нагрузка X на автосцепку вагона распределена по нормальному закону (m = {m} т; σ = {σ} т). " \
           f"Какова вероятность того, что нагрузка не превысит {p1} т? " \
           f"Какова вероятность нагрузок не более {p2} т?\n"
    a1 = integr_lapl(round((p1 - m) / σ, 2))
    a2 = integr_lapl(round((p2 - m) / σ, 2))
    answer += f"1)P={a1}\n"
    answer += f"2)P={a2}\n"
    return text, answer


def task_19():
    answer = "19. \n"
    t = randint(1, 5) * 5
    text = "19. Минутная стрелка электрических часов на вокзале перемещается скачкообразно в конце каждой минуты. " \
           "Найти вероятность того, что в данное мгновение часы по-казывают время, " \
           f"которое отличается от истинного более чем на {t} с.\n"
    a = round(1 - (t / 30), 3)
    answer += f"P={a}\n"
    return text, answer


def task_20():
    m = randint(5, 9)
    σ = randint(2, 5)
    inter = randint(10, 15)
    answer = "20. \n"
    text = f"20. Случайная величина X имеет нормальное распределение с плотностью: " \
           f"f(x) =1/{σ}√2π e^-(x-{m})^2/2*{σ}^2 " \
           "Определить вероятность события {X > " \
           f"{inter}" \
           "}, построить кривую распределения" \
           "и указать интервал наиболее вероятных значений [m - 3σ; m + 3σ].\n"
    a1 = 0.5 - integr_lapl(round(((inter - m) / σ), 2))
    a2 = (m - (3 * σ))
    a3 = (m + (3 * σ))
    answer += f"P(X>{inter})={round(a1, 4)}\n"
    answer += f"[{a2},{a3}]\n"
    return text, answer


def task_21():
    n = randint(50, 100)
    r1 = randint(20, 25)
    r2 = randint(30, 40)
    t1 = randint(25, 35)
    t2 = randint(70, 100)
    answer = "21. \n"
    text = f"21. Состав содержит {n} вагонов, причем тормозное усилие в колодках каждого вагона Аi " \
           f"- случайная величина, имеющая равномерное распределение от {r1} до {r2} т. Для достаточной" \
           f"обеспеченности поезда тормозными средствами должно выполняться неравенство: А ≥ {t1}n - {t2}," \
           "где А - суммарное тормозное усилие в колодках; n - число вагонов в поезде." \
           "С какой вероятностью поезд достаточно обеспечен тормозными средствами?\n"
    m = (r1 + r2) / 2
    sig = (r2 - r1) / (math.sqrt(12))
    ma = m * n
    siga = round(sig * math.sqrt(n), 2)
    p = 0.5 - integr_lapl(round((((t1 * n) - t2) - ma) / siga, 2))
    answer += f"P = {round(p, 4)}\n"
    return text, answer
