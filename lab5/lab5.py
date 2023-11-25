from enum import Enum
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Polynom:
    def __init__(self, points, color):
        self.points = points
        self.color = color

    def __repr__(self):
        return f"Polynom({self.points}, {self.color})"

    def perimeter(self):
        if len(self.points) < 2:
            return 0

        perimeter = 0
        for i in range(len(self.points) - 1):
            perimeter += math.dist((self.points[i].x, self.points[i].y),
                                    (self.points[i + 1].x, self.points[i + 1].y))

        perimeter += math.dist((self.points[-1].x, self.points[-1].y),
                                (self.points[0].x, self.points[0].y))
        return perimeter

    def longest_diagonal(self):
        if len(self.points) < 2:
            return 0

        max_diagonal = 0
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                diagonal = math.dist((self.points[i].x, self.points[i].y), (self.points[j].x, self.points[j].y))
                max_diagonal = max(max_diagonal, diagonal)

        return max_diagonal

    def sort_by_x(self):
        self.points.sort(key=lambda point: point.x)

    def sort_by_y(self):
        self.points.sort(key=lambda point: point.y)

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 0)
    point3 = Point(1, 1)
    point4 = Point(0, 1)

points_list = [point1, point2, point3, point4]

poly = Polynom(points_list, Color.RED)

print(f"Perimeter: {poly.perimeter()}")
print(f"Longest Diagonal: {poly.longest_diagonal()}")

print("Before sorting by x:")
for p in points_list:
    print(p)

poly.sort_by_x()
print("\nAfter sorting by x:")
for p in points_list:
    print(p)

print("\nBefore sorting by y:")
for p in points_list:
    print(p)

poly.sort_by_y()
print("\nAfter sorting by y:")
for p in points_list:
    print(p)

print("\nPolynom representation:")
print(poly)
