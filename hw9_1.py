# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random
from functools import wraps
from typing import Callable

MIN_LINE = 100
MAX_LINE = 1000
MIN_NUM = 1
MAX_NUM = 100


def import_json(gen_csv):
    @wraps(gen_csv)
    def wrapper(*args):
        data1 = gen_csv(*args)
        with open('import.json', 'w', encoding='UTF-8') as f1:
            json.dump(data1, f1, indent=4, )
    return wrapper



def quadro(gen_csv):
    @wraps(gen_csv)
    def wrapper(*args):
        data = gen_csv(*args)
        res_list = []
        for i in data:
            res_line = [i, quadratic(i)]
            res_list.append(res_line)
        return res_list
    return wrapper


def quadratic(data: list):
    a,b,c = data
    d = b ** 2 - 4 * a * c
    if d > 0:
        return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
    elif d == 0:
        return -b / (2 * a)
    else:
        return


@import_json
@quadro
def gen_csv(csv_name: str):
    num_list = list(
        list(random.randint(MIN_NUM, MAX_NUM) for j in range(3)) for i in range(random.randint(MIN_LINE, MAX_LINE)))
    with open(csv_name, 'w', newline='', encoding='UTF-8') as f:
        csv_file = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_file.writerows(num_list)
    return num_list

gen_csv('hw9_5.csv')