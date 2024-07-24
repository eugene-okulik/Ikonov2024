# Даны числа x и y. Получить x − y / 1 + xy

print('Даны числа x и y. Получить x − y / 1 + xy')

    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))

print('Даны числа: ', x, ',', y)

        ura1 = x * y
        ura2 = y / 1
        ura3 = ura1 + ura2
        ura4 = x - ura3

print('Вычислить: x − y / 1 + xy')

print('Порядок действий:')

print('1. x * y = ', ura1)

print('2. y / 1 = ', ura2)

print('3. y / 1 + xy = ', ura3)

print('4. x − y / 1 + xy = ', ura4)

print('Ответ:', x - ((y / 1) + (x * y)))
