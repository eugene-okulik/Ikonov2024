# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

print('Найти гипотенузу и площадь прямоугольного треугольника')

    a = float(input("Введите значение катета a: "))
    b = float(input("Введите значение катета b: "))

print('Катеты прямоугольного треугольника:', a, ', ', b)

        c1= a**2 + b**2
        c=c1 ** 0.5

print('Гипотенуза треугольника = ', c)

   p = (a + b + c) / 2
   print('Полупериметр ', p)
   sq = (((p * (p-a)) * (p-b) * (p-c))) ** 0.5

print("Площадь треугольника по формуле Герона =", sq)



