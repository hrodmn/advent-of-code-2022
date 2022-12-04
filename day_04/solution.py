TEST_INPUT = [
    ("2-4", "6-8"),
    ("2-3", "4-5"),
    ("5-7", "7-9"),
    ("2-8", "3-7"),
    ("6-6", "4-6"),
    ("2-6", "4-8"),
]

with open("input") as f:
    all_pairs = [pair.split(",") for pair in f]


def get_range(string):
    start, end = (int(i) for i in string.split("-"))
    return range(start, end + 1)


def is_fully_contained(a, b):
    a_range, b_range = (get_range(string) for string in [a, b])

    a_contained = all([i in b_range for i in a_range])
    b_contained = all([i in a_range for i in b_range])

    return a_contained or b_contained


# part 1
test_contained = sum([is_fully_contained(a, b) for a, b in TEST_INPUT])
assert test_contained == 2


n_contained = sum(is_fully_contained(a, b) for a, b in all_pairs)

print(f"there are {n_contained} pairs where on completely contains the other")


# part 2
def check_overlap(a, b):
    a_range, b_range = (get_range(string) for string in [a, b])

    return any(i in b_range for i in a_range)


test_overlap = sum([check_overlap(a, b) for a, b in TEST_INPUT])
assert test_overlap == 4

n_overlapping = sum(check_overlap(a, b) for a, b in all_pairs)
print(f"{n_overlapping} pairs have at least one overlap")
