# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import random
import math

for i in range(5):
    x1 = random.randrange(-9, 9)
    x2 = random.randrange(-9, 9)
    y1 = random.randrange(-9, 9)
    y2 = random.randrange(-9, 9)
    print(x1, x2, y1, y2)

    # d = √ (хА – хВ)**2 + (у А – у В)**2

    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(round(d, 2))