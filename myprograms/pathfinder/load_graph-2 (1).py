# Author: Takudzwa Clive Mutombo
# Purpose: Lab 4
# Date: 11/15/2022

from vertex import Vertex


def load_graph(file_name):

    vertex_dictionary = {}

    # Opening file to read the lines
    file = open(file_name, "r")

    for line in file:

        list_1 = line.split(";")
        # Cleaning up the whitespaces around the stings in list_1
        for i in range(0, len(list_1)):
            list_1[i] = list_1[i].strip()

        adj_location_list = list_1[1].split(",")
        # Cleaning up the whitespace around the strings in adj_location_list
        for i in range(0, len(adj_location_list)):
            adj_location_list[i] = adj_location_list[i].strip()

        coordinates_list = list_1[2].split(",")
        # Cleaning up the whitespaces
        for i in range(0, len(coordinates_list)):
            coordinates_list[i] = coordinates_list[i].strip()

        vertex_name = list_1[0]
        vertex_obj = Vertex(vertex_name, coordinates_list[0], coordinates_list[1])
        vertex_dictionary[vertex_name] = vertex_obj

    file.close()

    file = open(file_name, "r")  # Must do this to start reading from the beginning

    for line in file:

        list_1 = line.split(";")
        # Clean up the whitespaces around the strings in list_1
        for i in range(0, len(list_1)):
            list_1[i] = list_1[i].strip()

        adj_location_list = list_1[1].split(",")
        # Clean up the whitespace around the strings in adj_location_list
        for i in range(0, len(adj_location_list)):
            adj_location_list[i] = adj_location_list[i].strip()

        vertex_name = list_1[0]
        vertex_obj = vertex_dictionary[vertex_name]
        for adjacent_location in adj_location_list:
            adj_location_obj = vertex_dictionary[adjacent_location]
            vertex_obj.adjacent_list.append(adj_location_obj)

    return vertex_dictionary
