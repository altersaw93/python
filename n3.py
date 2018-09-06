import math

a = int(input("Введите значение A:"))

b = int(input("Введите значение B:"))

c = int(input("Введите значение C:"))

D = b ** 2 - 4 * a * c
#print("Дискриминант равен:",D)

if D  < 0:
    print("Корней нет")
elif D > 0:
    x1 = int((-b + math.sqrt(D)) / (2 * a))
    x2 = int((-b - math.sqrt(D)) / (2 * a))
    print("Квадратный корень 1 равен:",x1)
    print("Квадратный корень 2 равен:",x2)
else:
    x = int((-b - math.sqrt(D)) / (2 * a))
    print(x)