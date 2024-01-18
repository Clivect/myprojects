# Author: Takudzwa Clive Mutombo
# Purpose: Lab 4
# Date: 11/15/2022

from cs1lib import *

radius = 5
width = 2


class Vertex:
    def __init__(self, vtx_name, x_coordinate, y_coordinate):
        self.vtx_name = vtx_name
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.adjacent_list = []

    def __str__(self):
        adj_string = ""
        for i in range(0, len(self.adjacent_list)):  # printing everything in adjacent_list as a string
            if i == len(self.adjacent_list) - 1:
                adj_string = adj_string + self.adjacent_list[i].vtx_name
            else:
                adj_string = adj_string + self.adjacent_list[i].vtx_name + ","

        return self.vtx_name + ";" + "Location:" + str(self.x_coordinate) + "," + str(
            self.y_coordinate) + ";" + "Adjacent vertices:" + adj_string

    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x_coordinate, self.y_coordinate, radius)

    def draw_edge(self, vertex_name, r, g, b):
        set_stroke_color(r, g, b)
        draw_line(self.x_coordinate, self.y_coordinate, vertex_name.x_coordinate, vertex_name.y_coordinate)

    def draw_all_edges(self, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(width)
        for vtx in self.adjacent_list:
            self.draw_edge(vtx, r, g, b)

    def within_vertex(self, x, y):
        return self.x_coordinate - radius < x < self.x_coordinate + radius and self.y_coordinate - radius < y < self.y_coordinate + radius
