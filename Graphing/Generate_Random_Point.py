import random


def generate(n):
    point = []
    for i in range(n):
        x = random.uniform(-5, 5)
        point.append(x)
    return tuple(point)
