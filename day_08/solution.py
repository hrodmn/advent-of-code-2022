import numpy as np


def read_trees(input):
    rows = []
    for line in input:
        rows.append([int(i) for i in line.strip()])

    return np.array(rows)


def find_visible_trees(trees, r_range, c_range):
    vis = np.zeros_like(trees)
    for r in r_range:
        prev = -1
        for c in c_range:
            if trees[r, c] > prev:
                vis[r, c] = 1
            prev = max([trees[r, c], prev])

    for c in c_range:
        prev = -1
        for r in r_range:
            if (trees[r, c] > prev) or not (r * c):
                vis[r, c] = 1
            prev = max([trees[r, c], prev])

    return vis


def count_visible_trees(trees):
    vis_forward = find_visible_trees(
        trees,
        list(range(trees.shape[0])),
        list(range(trees.shape[1])),
    )

    vis_backward = find_visible_trees(
        trees,
        list(reversed(range(trees.shape[0]))),
        list(reversed(range(trees.shape[1]))),
    )

    return np.sum(np.maximum(vis_forward, vis_backward))


def check_scenic_score(trees):
    scenic = np.zeros_like(trees)

    rows = list(range(trees.shape[0]))
    cols = list(range(trees.shape[1]))

    for r in rows:
        for c in cols:
            tree = trees[r, c]

            # look east
            east_score = 0
            if c < max(cols):
                for east in range(c + 1, max(cols) + 1):
                    if tree > trees[r, east]:
                        east_score += 1
                    if tree <= trees[r, east]:
                        east_score += 1
                        break

            # look west
            west_score = 0
            if c > min(cols):
                for west in reversed(range(min(cols), c)):
                    if tree > trees[r, west]:
                        west_score += 1
                    if tree <= trees[r, west]:
                        west_score += 1
                        break

            # look south
            south_score = 0
            if r < max(rows):
                for south in range(r + 1, max(rows) + 1):
                    if tree > trees[south, c]:
                        south_score += 1
                    if tree <= trees[south, c]:
                        south_score += 1
                        break

            # look north
            north_score = 0
            if r > min(rows):
                for north in reversed(range(min(rows), r)):
                    if tree > trees[north, c]:
                        north_score += 1
                    if tree <= trees[north, c]:
                        north_score += 1
                        break

            # total score
            scenic[r, c] = east_score * south_score * west_score * north_score

    return scenic


with open("test_input") as f:
    test_trees = read_trees(f)


assert count_visible_trees(test_trees) == 21

assert np.max(check_scenic_score(test_trees)) == 8

with open("input") as f:
    trees = read_trees(f)

visible_trees = count_visible_trees(trees)
print(f"there are {visible_trees} visible trees")


max_scenic_score = np.max(check_scenic_score(trees))
print(f"the maximum scenic score is {max_scenic_score}")
