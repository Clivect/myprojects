# Author: Takudzwa Clive Mutombo
# Purpose: Lab 4
# Date: 11/15/2022

from collections import deque
from vertex import Vertex
from load_graph import *


def bfs(start, goal):
    frontier = deque()
    backpointer_dic = {}
    frontier.append(start)
    backpointer_dic[start] = None

    while len(frontier) != 0:
        curr_v = frontier.popleft()

        for adj_v in curr_v.adjacent_list:
            if adj_v not in backpointer_dic:
                frontier.append(adj_v)
                backpointer_dic[adj_v] = curr_v

        if goal in backpointer_dic:
            break

    path = []
    v = goal
    while v != None:
        path.append(v)
        backpointer = backpointer_dic[v]
        v = backpointer
    return path
