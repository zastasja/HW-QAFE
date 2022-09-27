import math
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
def square():
    n = int(input())
    perim = 4 * n
    sq = n**2
    diag = math.sqrt(n**2 * 2)
    return perim, sq, diag

t = square()
print(t)

