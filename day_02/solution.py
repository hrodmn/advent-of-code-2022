THEIRS = {
    "A": 1,
    "B": 2,
    "C": 3,
}
MINE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
RESULTS = {
    1: {1: 3, 2: 0, 3: 6},
    2: {1: 6, 2: 3, 3: 0},
    3: {1: 0, 2: 6, 3: 3},
}

score = 0
with open("input") as f:
    for line in f:
        theirs, mine = line.strip().split(" ")
        score += MINE[mine] + RESULTS[MINE[mine]][THEIRS[theirs]]

assert score == 12772
print(f"my total score would be {score}")

RESULT_SCORES = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
COUNTERS = {
    1: {0: 3, 3: 1, 6: 2},
    2: {0: 1, 3: 2, 6: 3},
    3: {0: 2, 3: 3, 6: 1},
}

score = 0
with open("input") as f:
    for line in f:
        theirs, result = line.strip().split(" ")
        result_score = RESULT_SCORES[result]
        score += result_score + COUNTERS[THEIRS[theirs]][result_score]

print(f"my revised total score would be {score}")
