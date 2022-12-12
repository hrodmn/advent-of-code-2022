import string

import numpy as np


def get_elevation(x):
    if x == "S":
        x = "a"
    if x == "E":
        x = "z"

    return string.ascii_lowercase.index(x)


def find_shortest_path(input):
    rows = [list(line.strip()) for line in input]
    index_array = np.array(rows)
    current_coords = np.where(index_array == "S")
    dest_coords = np.where(index_array == "E")

    elev_array = np.vectorize(get_elevation)(index_array)
    current_elev = elev_array[current_coords]
    dest_elev = elev_array[dest_coords]

    dist = 0

    print(f"start coords: {current_coords}")
    print(f"elevation at start: {current_elev}")
    print(f"end coords: {dest_coords}")
    print(f"elevation at end: {dest_elev}")

    while current_coords != dest_coords:
        gradient = elev_array - current_elev

        print(gradient)
        options = gradient <= 1
        print(options)
        break
        # reset current elev and current coords
        dist += 1


with open("test_input") as input:
    find_shortest_path(input)
