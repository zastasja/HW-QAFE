#Первая цифра после точки
# a = float(input())
# b = int(a)
# c = a-b
# d = c*10
# print(int(d))
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# a, b, c = int(input()), int(input()), int(input())
# maxi = max(a,b,c)
# mini = min(a,b,c)
# midi = (a+b+c)-(mini+maxi)
# print(maxi, midi, mini, sep="\n")
# #Интересное число
# #Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет.
# # Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
# num = int(input())
# first = num//100
# third = num%10
# second = (num%100 - third)//10
# mini = min(third, second, first)
# maxi = max(third, second, first)
# midi = (first+second+third)-(maxi+mini)
# diff = maxi - mini
#
# if diff == midi:
#     print("Число интересное")
# else:
#     print("Число неинтересное")
import math

# # Арифметические строки
# # Вводятся 3 строки в случайном порядке.
# # Напишите программу, которая выясняет можно ли из длин этих строк
# # построить возрастающую арифметическую прогрессию.
#
# a, b, c = input(), input(), input()
# mini = min(len(a), len(b), len(c))
# maxi = max(len(a), len(b), len(c))
#
# if (mini+maxi)/2 == (len(a)+len(b)+len(c))/3:
#     print('YES')
# else:
#     print('NO')
#

# #Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates.
# x1, y1, x2, y2 = float(input()), float(input()),float(input()),float(input())
# print(math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)))

#Площадь и длина круга
# # Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.
# r = float(input())
# square = math.pi * (r ** 2)
# c = 2 * math.pi * r
# print(square, c, sep="\n")
