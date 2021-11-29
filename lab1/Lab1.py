import sys
import math


def get_coef(index, prompt):

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def main():

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # дискриминант
    D = b ** 2 - 4 * a * c

    if a != 0:
        if D < 0:
            print("Корней нет")
        elif D == 0:
            x = -b / (2 * a)
            if x == 0:
                print("x = 0.0")
            elif x > 0:
                print("x =", math.sqrt(x), "and x =", -math.sqrt(x))
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            if x1 == 0:
                print("x = 0.0")
            elif x1 > 0:
                print("x =", math.sqrt(x1), "and x =", -math.sqrt(x1))
            x2 = (-b - math.sqrt(D)) / (2 * a)
            if x2 == 0:
                print("x = 0.0")
            elif x2 > 0:
                print("x =", math.sqrt(x2), "and x =", -math.sqrt(x2))
    elif b == 0:
        if c == 0:
            print("Бесконечное множество корней")
        else:
            print("Корней нет")
    else:
        x = -c / b
        if x == 0:
            print("x = 0.0")
        elif x > 0:
            print("x =", math.sqrt(x), "and x =", -math.sqrt(x))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4