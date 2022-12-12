from collections import defaultdict
from parse import parse
import json
import math

import numpy as np

ID_FMT = "Monkey {id}:"
STARTING_ITEMS_FMT = "Starting items: {item_string}"
OPERATION_FMT = "Operation: new = {operation}"
TEST_FMT = "Test: divisible by {divisor}"
TEST_LOGIC_FMT = "If {result}: throw to monkey {id}"


def parse_monkeys(input):
    monkeys = defaultdict(dict)
    for line in input:
        if line.strip().startswith("Monkey"):
            id = parse(ID_FMT, line.strip())["id"]
            monkey = monkeys[id]
            monkey["n_inspected"] = 0
        if line.strip().startswith("Starting items"):
            starting_items = parse(STARTING_ITEMS_FMT, line.strip())["item_string"]
            monkey["items"] = [int(i) for i in starting_items.split(", ")]
        if line.strip().startswith("Operation"):
            monkey["operation"] = parse(OPERATION_FMT, line.strip())["operation"]
        if line.strip().startswith("Test"):
            monkey["test_divisor"] = int(parse(TEST_FMT, line.strip())["divisor"])
        if line.strip().startswith("If true"):
            monkey["true_destination"] = parse(TEST_LOGIC_FMT, line.strip())["id"]
        if line.strip().startswith("If false"):
            monkey["false_destination"] = parse(TEST_LOGIC_FMT, line.strip())["id"]

    return monkeys


def play_catch(monkeys, n_rounds, worry_reducer=3):
    lcm = math.lcm(*[monkey["test_divisor"] for monkey in monkeys.values()])
    for _ in range(n_rounds):
        for id, monkey in monkeys.items():
            # adjust worry levels and evaluate where to send item
            for old in monkey["items"][:]:
                monkey["n_inspected"] += 1
                monkey["items"].remove(old)
                # adjust worry during inspection
                adj = int(eval(monkey["operation"]))

                # relax after inspection
                relaxed = int(math.floor(adj / worry_reducer))

                # get remainder from least common multiple
                remainder = relaxed % lcm

                # run test, throw item
                if remainder % monkey["test_divisor"] == 0:
                    dest_monkey = monkeys[monkey["true_destination"]]
                    dest_monkey["items"].append(remainder)
                else:
                    dest_monkey = monkeys[monkey["false_destination"]]
                    dest_monkey["items"].append(remainder)

    return monkeys


with open("test_input") as f:
    test_monkeys = parse_monkeys(f)


test_20 = play_catch(test_monkeys, n_rounds=20, worry_reducer=3)
test_20_inspected = [monkey["n_inspected"] for monkey in test_20.values()]
assert np.prod(sorted(test_20_inspected)[-2:]) == 10605


with open("test_input") as f:
    test_monkeys = parse_monkeys(f)
test_10k = play_catch(test_monkeys, n_rounds=10_000, worry_reducer=1)
test_10k_inspected = [monkey["n_inspected"] for monkey in test_10k.values()]
test_monkeybusiness_10k = np.prod(sorted(test_10k_inspected)[-2:])
assert test_monkeybusiness_10k == 2713310158


with open("input") as f:
    monkeys = parse_monkeys(f)

run_20 = play_catch(monkeys, n_rounds=20, worry_reducer=3)
run_20_inspected = [monkey["n_inspected"] for monkey in run_20.values()]
monkeybusiness_20 = np.prod(sorted(run_20_inspected)[-2:])
print(
    f"with worry reduction factor of 3, monkeybusiness is {monkeybusiness_20} after 20 rounds"
)

with open("input") as f:
    monkeys = parse_monkeys(f)

run_10k = play_catch(monkeys, n_rounds=10_000, worry_reducer=1)
run_10k_inspected = [monkey["n_inspected"] for monkey in run_10k.values()]
monkeybusiness_10k = np.prod(sorted(run_10k_inspected)[-2:])
print(
    f"with worry reduction factor of 1, monkeybusiness is {monkeybusiness_10k} after 10k rounds"
)
