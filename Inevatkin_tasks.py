from random import randint
from random import uniform
from scipy.stats import norm
import math
from functions import *


def task_1():
    patients_from_onefive = randint(1, 2)
    patients_from_six = patients_from_onefive * 3
    vsego=patients_from_six+patients_from_onefive*5
    answer = "1. \n"
    text = f"1. В больнице у кабинета врача ожидают приема по {int(patients_from_onefive)} больному из палат № 1-5 и {int(patients_from_six)} больных из палаты № 6 " \
           "Врач наугад приглашает по одному больному. Какова вероятность того, что:\n"#problem
    text += "a) первым будет приглашен больной из палаты № 6, а второй — не из палаты № 6\n"
    ot1 = patients_from_six/(vsego)*(patients_from_onefive*5)/(vsego-1)
    answer += f"а) P = ({patients_from_six}/{vsego})*({patients_from_onefive*5}/{vsego-1}) = {round(ot1,4)}\n"
    text += f"б) трое первых больных, принятых врачом, окажутся соответственно из палат № 1, 2 и 3?\n"#problem
    ot2 = patients_from_onefive/vsego*patients_from_onefive/(vsego-1)*patients_from_onefive/(vsego-2)
    answer += f"б) P = {patients_from_onefive}/{vsego} * {patients_from_onefive}/{vsego-1} * {patients_from_onefive}/{vsego-2} ={round(ot2,4)}\n"
    return text, answer


def task_2():
    juice_sm = randint(5, 8)
    juice_vish = randint(3, 7)
    vin = juice_sm-1
    vsego = vin+juice_vish+juice_sm
    vibor = randint(5,8)
    vibora = int(vin/2)
    answer = "2. \n"
    text = (f"2. На прилавках супермаркета 'Тройка' выставлены одинаковые банки: {juice_sm} - с соком смородины, "
            f"{juice_vish} - с соком вишни и {vin} - с вином. Неразборчивый покупатель не глядя берет "
            f"{vibor} банок. Найти вероятность того, что:\n")
    text += f"а) {vibora} из них будут с вином;\n"
    p_three_vin = combination(vin,vibora)[1]/combination(vsego,vibor)[1]
    answer += f"а) P = {combination(vin,vibora)[2]}/{combination(vsego,vibor)[2]} = {round(p_three_vin,5)}\n"

    p2 = (combination(juice_vish,2)[1]*combination(juice_vish,2)[1]*combination(vin,vibor-4)[1])/combination(vsego,vibor)[1]
    text += "б) две банки будут со смородиновым и две — с вишневым соком.\n"
    answer += f"б) P = ({combination(juice_vish,2)[2]}*{combination(juice_vish,2)[2]}*{combination(vin,vibor-4)[2]})/{combination(vsego,vibor)[2]} = {round(p2,5)}\n"

    return text, answer


def task_3():
    text = (
        "3. Машинно-котельная установка состоит из двух котлов и одной машины. Рассмотрим события: A - исправна машина; "
        "Bk - исправен k-й котел (k = 1,2); C - установка исправна. Установка считается исправной, если работает машина и "
        "хотя бы один котел. Выразить события C и ¬C через A и Bk.\n")
    answer = "3. \n" \
             "C = A ∩ (B1 ∪ B2)\n" \
             "¬C = ¬A ∪ (¬B1 ∩ ¬B2)\n"
    return text, answer


def task_4():
    s1 = randint(6, 9) / 10
    s2 = randint(4, 7) / 10
    answer = "4. \n"
    text = f"4.В университете ожидают иностранную делегацию,в которую входят два иллюзиониста. Первый из них дает интервью " \
           f"с вероятностью {s1}, второй — {s2}. Какова вероятность того, что корреспонденту газеты «Транспортник»:\n"
    text += "а) дадут интервью оба иллюзиониста;\n"
    answer += f"a) {round(s1 * s2, 2)}\n"

    text += "б) даст интервью хотя бы один из них;\n"
    answer += f"б) {round(1 - ((1-s1)*(1-s2)), 2)}\n"

    text += "в) даст интервью только первый иллюзионист?\n"
    o2 = (s1 * (1 - s2))
    answer += f"в) {round(o2, 2)}\n"
    return text, answer

def task_5():
    kr1 = randint(2, 8) / 10
    kr2 = round(1-kr1,2)
    text = (
        f"5. Вероятность того, что в течение месяца на кафедру высшей математики по электронной почте придет контрольная "
        f"работа студента-заочника из г. Бердяуш, равна {kr1}, а из г. Топки — {kr2}. В течение месяца были получены 4 "
        f"контрольные работы. Какова вероятность, что работ из Бердяуша было больше, чем из Топков?\n")
    p = (kr1**3*kr2)+(kr1**4)
    answer = f"5.\n P = {kr1}^3*{kr2}+{kr1}^4 = {round(p, 6)}\n"
    return text, answer

def task_18():
    sigma = randint(20, 30)  # сигма случайных ошибок взвешивания
    error_limit = randint(5, 15)  # предельная ошибка взвешивания

    text = f"18. Производится взвешивание некоторого вещества без систематических ошибок. " \
           f"Случайные ошибки взвешивания подчинены нормальному закону сигма = {sigma} г. " \
           f"Найти вероятность того, что очередное взвешивание будет произведено с ошибкой, " \
           f"не превосходящей по абсолютной величине {error_limit} г.\n"

    # Используем функцию интеграла Лапласа для вычисления вероятности
    probability = round(0.5 - float(integr_lapl(round(error_limit / sigma, 2))), 5)

    answer = f"18.\nP = {probability}"

    return text, answer

def task_19():
    lambd = randint(1,4)/10
    x1=randint(1,5)
    x2=randint(x1+5,14)
    text = "19. Число отказавших за время T элементов аппаратуры — случайная величина X, распределенная "\
            f"экспоненциально (λ = {lambd}). Указать плотность и функцию распределения, построить их "\
            "графики, найти среднее число элементов, которые могут выйти из строя за время T. Какова "\
            f"вероятность того, что число отказавших элементов заключено между {x1} и {x2}?\n"
    answer = "19.\n"
    answer+=f"f(x)={lambd}*e^(-{lambd}*t), t>0\n"
    answer+=f"F(x)=1-e^(-{lambd}*t), t>0\n"
    answer+=f"σ(x) = 1/{lambd} = {round(1/lambd,4)}\n"
    answer+=f"P = e^(-{x1}*{lambd})-e^(-{x2}*{lambd}) = {round(1-math.exp(-x2*lambd)-1+math.exp(-x1*lambd),5)}\n"

    return text,answer


def task_20():
    d1 = randint(6,10)/100
    d2 = randint(int((d1+0.02)*100),12)/100
    text="20. Браковка шариков для подшипников происходит так: если шарик не проходит через отверстие "\
         f"диаметром {d1}, но проходит через отверстие диаметром {d2} > {d1}, то размер шарика считается "\
         f"приемлемым. Иначе шарик бракуется. Пусть диаметр шарика D принадлежит N(m,σ), где m = ({d1} + {d2})/2; "\
         f"σ = ({d2} – {d1})/3. Какова вероятность того, что он будет забракован?\n"
    answer="20.\n"
    m = (d1 + d2) / 2  # математическое ожидание
    sigma = (d2 - d1) / 3  # стандартное отклонение
    answer+=f"P = {round(1-2*integr_lapl(round((d2-m)/sigma,2)),5)}"

    return text,answer


def task_21():
    num_dumpcars = randint(4, 6)*5
    num_tankers = randint(5, 10)*5
    num_boxcars = randint(4,7)*5
    m1 = 58
    s1 = 3
    m2 = 60
    s2 = 2
    m3 = 60
    s3 = 3
    matozh=num_dumpcars*m1+num_tankers*m2+num_boxcars*m3
    maxi=randint(matozh+15,matozh+30)
    text = f"21. Состав содержит {num_dumpcars} думпкаров, {num_tankers} цистерн и {num_boxcars} полувагонов. Массы думпкаров распределены в диапазоне ({m1} +- {s1*3}) т, " \
           f"массы цистерн — в диапазоне ({m2} +- {s2*3}) т, массы) полувагонов — в диапазоне ({m3} +- {s3*3}) т. Один локомотив может везти " \
           f"состав массой не более {maxi} т, иначе прицепляется второй. Найти вероятность того, что кратная тяга не потребуется.\n"
    disp1 = s1**2
    disp2 = s2**2
    disp3 = s3**2
    disp = disp1*num_dumpcars+disp2*num_tankers+disp3*num_boxcars
    sigm = round(math.sqrt(disp),3)
    answer="21.\n"
    answer+=f"P = {round(norm.cdf((maxi-matozh)/sigm),4)}, M(X) = {matozh}; D(X) = {disp}; σ={sigm}\n"

    return text,answer
