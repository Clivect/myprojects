# Author: Takudzwa Clive Mutombo
# Purpose: Lab 4
# Date: 11/15/2022

from cs1lib import *
from lab4_checkpoint import *
from vertex import *
from bfs import *

m_pressed = False
m_x = 0
m_y = 0
start_vertex = None
end_vertex = None

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
FRAMERATE = 12
path = []

img = load_image("dartmouth_map.png")


def main_draw():
    global start_vertex, end_vertex, m_pressed, path
    draw_image(img, 0, 0)

    for vtx_key in vertex_dict:  # for key in dictionary, draw vertex and edges
        vertex_dict[vtx_key].draw_vertex(0, 0, 1)
        vertex_dict[vtx_key].draw_all_edges(0, 0, 1)

    if m_pressed:
        for vtx in vertex_dict:  # for key in dictionary, if clicked assign coordinates to start vertex
            if vertex_dict[vtx].within_vertex(m_x, m_y):
                start_vertex = vertex_dict[vtx]

    for item in vertex_dict:  # identify end vertex
        if vertex_dict[item].within_vertex(m_x, m_y) and start_vertex != None:
            end_vertex = vertex_dict[item]

    if start_vertex != None and end_vertex != None:
        start_vertex.draw_vertex(1, 0, 0)
        end_vertex.draw_vertex(1, 0, 0)

    if start_vertex != None and end_vertex != None:  # find path
        path = bfs(start_vertex, end_vertex)

    for i in range(0, len(path) - 1):
        path[i].draw_vertex(1, 0, 0)
        path[i].draw_edge(path[i + 1], 1, 0, 0)


def mouse_pressed(mx, my):
    global m_pressed, m_y, m_x
    m_pressed = True
    m_x = mx
    m_y = my


def mouse_released(mx, my):
    global m_pressed
    m_pressed = False


def mouse_moved(mx, my):
    global m_y, m_x

    m_x = mx
    m_y = my


start_graphics(main_draw, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, framerate=FRAMERATE, mouse_press=mouse_pressed,
               mouse_release=mouse_released, mouse_move=mouse_moved)
