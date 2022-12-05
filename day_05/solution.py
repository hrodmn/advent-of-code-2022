from parse import parse

import collections

TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

MOVE_FMT = "move {n:d} from {from_stack:d} to {to_stack:d}"

# real input
with open("input") as f:
    input = "".join(line for line in f)


def parse_input(input):
    raw_crates = input.split("\n\n")
    rows = raw_crates[0].split("\n")
    moves = raw_crates[1].split("\n")
    stacks = collections.defaultdict(list)
    for _, row in enumerate(rows[:-1]):
        stack = 1
        for ii, c in enumerate(row):
            if (ii - 1) % 4 == 0:
                if c != " ":
                    stacks[stack].append(c)
                stack += 1

    stacks = dict(sorted(stacks.items()))

    return stacks, moves


def move_crates_9000(input):
    stacks, moves = parse_input(input)
    after_stacks = stacks.copy()
    for move in moves:
        parsed = parse(MOVE_FMT, move)
        if parsed:
            to_stack = after_stacks[parsed["to_stack"]]
            from_stack = after_stacks[parsed["from_stack"]]
            for i in range(parsed["n"]):
                to_stack.insert(
                    0,
                    from_stack.pop(0),
                )

    top_crates = [crates[0] for crates in after_stacks.values()]
    return "".join(top_crates)


assert move_crates_9000(TEST_INPUT) == "CMZ"

print(move_crates_9000(input))


def move_crates_9001(input):
    stacks, moves = parse_input(input)
    after_stacks = stacks.copy()
    for move in moves:
        parsed = parse(MOVE_FMT, move)
        if parsed:
            to_stack = after_stacks[parsed["to_stack"]]
            from_stack = after_stacks[parsed["from_stack"]]
            for i in reversed(range(parsed["n"])):
                to_stack.insert(
                    0,
                    from_stack.pop(i),
                )

    top_crates = [crates[0] for crates in after_stacks.values()]
    return "".join(top_crates)


assert move_crates_9001(TEST_INPUT) == "MCD"
print(move_crates_9001(input))
