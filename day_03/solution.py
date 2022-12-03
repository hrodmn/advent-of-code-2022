import string

INDEX = list(string.ascii_lowercase) + list(string.ascii_uppercase)

TEST_INPUT_1 = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

TEST_INPUT_2 = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

with open("input") as f:
    all_rucksacks = [rucksack for rucksack in f]


def find_error_priority(rucksack):
    half = len(rucksack) // 2
    c1 = rucksack[:half]
    c2 = rucksack[half:]
    for item in c1:
        if item in c2:
            return INDEX.index(item) + 1


test_priority_sum = 0
for rucksack in TEST_INPUT_1:
    test_priority_sum += find_error_priority(rucksack)

assert test_priority_sum == 157

priority_sum = 0
for rucksack in all_rucksacks:
    priority_sum += find_error_priority(rucksack)

print(f"sum of priorities for erroneous items: {priority_sum}")


def find_badge_item_priority(rucksacks):
    for item1 in rucksacks[0]:
        for item2 in rucksacks[1]:
            for item3 in rucksacks[2]:
                if item1 == item2 == item3:
                    return INDEX.index(item1) + 1


group_size = 3
test_priority_sum_2 = 0
test_rucksack_groups = zip(*(iter(TEST_INPUT_2),) * group_size)
for rucksacks in test_rucksack_groups:
    test_priority_sum_2 += find_badge_item_priority(rucksacks)

assert test_priority_sum_2 == 70

priority_sum_2 = 0
rucksack_groups = zip(*(iter(all_rucksacks),) * group_size)
for rucksacks in rucksack_groups:
    priority_sum_2 += find_badge_item_priority(rucksacks)

print(f"sum of priorities for badge items: {priority_sum_2}")
