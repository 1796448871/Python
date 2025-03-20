# -*- coding: utf-8 -*-
import math

class Circle:
    def __init__(self, center, radius):
        """
        初始化圆的中心和半径
        :param center: 圆心坐标，格式为 (x, y)
        :param radius: 圆的半径
        """
        self.center = center
        self.radius = radius

    def circumference(self):
        """
        计算圆的周长
        :return: 圆的周长
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        计算圆的面积
        :return: 圆的面积
        """
        return math.pi * self.radius ** 2

    def is_point_inside(self, point):
        """
        判断某点是否在圆内
        :param point: 点的坐标，格式为 (x, y)
        :return: 如果点在圆内，返回 True；否则返回 False
        """
        x, y = point
        center_x, center_y = self.center
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        return distance <= self.radius

circle = Circle(center=(0, 0), radius=5)
print("圆的半径：",circle.radius)
print("圆的周长：", circle.circumference())
print("圆的面积：", circle.area())
print("点 (3, 3) 是否在圆内：", circle.is_point_inside((3, 3)))
print("点 (6, 6) 是否在圆内：", circle.is_point_inside((6, 6)))