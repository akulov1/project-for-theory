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
    answer += f"a) ({combination(rus, chrus)[2]}*{combination(tatar, chtatar)[2]}*{combination(ost, chost)[2]})/{combination(vsego, vibor)[2]}\n"

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
    text = "В коробке находятся 7 новых и 3 израсходованные батарейки для фотоаппарата. Какова вероятность того, что две вынутые наугад" \
           "батарейки окажутся новыми?"
