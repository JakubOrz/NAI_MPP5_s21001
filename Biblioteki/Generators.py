import random
import math


def color_generator():
    while True:
        yield [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


def point_generator():
    while True:
        yield random.uniform(-10, 1000)


def generate_points_circle(start_point: list, n: int = 1, r: float = 5.0):
    delta = math.pi * 2 / n
    alpha = 0
    result = list()
    if len(start_point) < 2:
        for i in range(n):
            result.append(start_point[0] + alpha)
            alpha += delta
    else:
        for i in range(n):
            result.append(
                [start_point[0] + r * math.sin(alpha),
                 start_point[1] + r * math.cos(alpha)])
            alpha += delta
    return result
