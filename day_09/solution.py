import math


def track_knot_position(input, n_knots=2, initial_coords=(0, 0)):
    knot_coords = [[initial_coords] for i in range(n_knots)]
    xy = [list(initial_coords) for i in range(n_knots)]
    for move, line in enumerate(input):
        vect = line.strip().split(" ")
        vect[1] = int(vect[1])
        if vect[0] in ["L", "D"]:
            head_delta = -1
        else:
            head_delta = 1
        if vect[0] in ["L", "R"]:
            axis = 0
            other = 1
        else:
            axis = 1
            other = 0

        for i in range(vect[1]):
            for knot in range(n_knots):
                if knot == 0:
                    xy[knot][axis] += head_delta
                else:
                    dists = [0, 0]
                    for ii in [axis, other]:
                        dists[ii] = xy[knot - 1][ii] - xy[knot][ii]

                    hypot = math.sqrt(sum([dist**2 for dist in dists]))
                    if hypot == 2:
                        if abs(dists[axis]) == 2:
                            if dists[axis] > 0:
                                xy[knot][axis] += 1
                            else:
                                xy[knot][axis] += -1
                        else:
                            if dists[other] > 0:
                                xy[knot][other] += 1
                            else:
                                xy[knot][other] += -1
                    elif hypot > 2:
                        if dists[axis] > 0:
                            xy[knot][axis] += 1
                        else:
                            xy[knot][axis] += -1
                        if dists[other] > 0:
                            xy[knot][other] += 1
                        else:
                            xy[knot][other] += -1

                    knot_coords[knot].append(tuple(xy[knot]))

        print(f"positions after move {move}")
        for knot in range(n_knots):
            print(f"knot {knot}: {xy[knot]}")

    return knot_coords


with open("test_input") as f:
    test_knot_coords = track_knot_position(f, n_knots=2, initial_coords=(0, 0))

assert len(set(test_knot_coords[-1])) == 13


with open("input") as f:
    knot_coords = track_knot_position(f, n_knots=2, initial_coords=(0, 0))

print(f"the tail occupies {len(set(knot_coords[-1]))} unique positions")


with open("test_input") as f:
    test_knot_coords2 = track_knot_position(f, n_knots=10, initial_coords=(0, 0))

assert len(set(test_knot_coords2[-1])) == 1


print(f"running test 2")
with open("test_input2") as f:
    test_knot_coords2 = track_knot_position(f, n_knots=10, initial_coords=(0, 0))


assert len(set(test_knot_coords2[-1])) == 36


with open("input") as f:
    knot_coords = track_knot_position(f, n_knots=10, initial_coords=(0, 0))

print(f"the tail occupies {len(set(knot_coords[-1]))} unique positions")
