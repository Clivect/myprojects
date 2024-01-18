# Author: Takudzwa Clive Mutombo
# Date: 10/22/2022
# Purpose: Lab 2_Solar system

from body import Body
from math import *

G = 6.67384 * pow(10, -11)  # the gravity constant


class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def update(self, timestep):
        i = 0
        while i < len(self.body_list):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay, timestep)
            self.body_list[i].update_position(timestep)
            i = i + 1

    def compute_acceleration(self, n):
        global G

        ax = 0
        ay = 0

        for j in range(0, len(self.body_list)):

            if j != n:
                dx = self.body_list[j].x - self.body_list[n].x  # x distance between two planets
                dy = self.body_list[j].y - self.body_list[n].y  # y distance between two planets

                r = sqrt(pow(dx, 2) + pow(dy, 2))  # total distance be two planets (x and y components)
                a = G * self.body_list[j].mass / (r * r)  # total acceleration

                ax = ax + a * dx / r
                ay = ay + a * dy / r

        return ax, ay

    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)
