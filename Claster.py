import random


class Centroid:

    @staticmethod
    def _mean(dane: list) -> float:
        sumka = sum(dane)
        return sumka / len(dane)

    @staticmethod
    def prepare_average_point(data: list) -> list:
        centrum = list()
        wymiary = len(data[0])
        for i in range(0, wymiary):
            centrum.append(Centroid._mean([float(element[i]) for element in data]))
        return centrum

    def __init__(self, start_point: list):
        self.dimensions = len(start_point)
        self.centrum = [anchor + random.uniform(-25, 25) for anchor in start_point]
        self.punkty = list()

    def __str__(self):
        return f"Centroid: {self.centrum}"

    def __len__(self):
        if self.punkty is None:
            return 0
        else:
            return len(self.punkty)

    def get_center(self) -> tuple:
        return tuple(self.centrum)

    def get_points(self) -> tuple:
        return tuple(self.punkty)

    def clear(self):
        self.punkty.clear()

    def add_point(self, point: list):
        self.punkty.append([float(anchor) for anchor in point])

    def count_centroid(self):
        if len(self.punkty) < 1:
            return
        self.centrum = self.prepare_average_point(self.punkty)

    def count_distance(self, otherPoint: list):
        return sum((float(e1) - float(e2)) ** 2 for e1, e2 in zip(self.centrum, otherPoint))
