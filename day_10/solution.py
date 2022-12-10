def run_program(input):
    X = []
    add = 0
    for i, line in enumerate(input):
        if i == 0:
            start = 1
        else:
            start = X[-1]
        x = start + add
        cmd = line.strip().split(" ")
        if cmd[0] == "noop":
            X.append(x)
            add = 0
        elif cmd[0] == "addx":
            for ii in range(2):
                X.append(x)
            add = int(cmd[1])

    X.append(X[-1] + add)

    return X


def signal_strength_by_index(X, indices):
    subset = []
    for i, x in enumerate(X, start=1):
        if i in indices:
            subset.append(x * i)

    return subset


def print_screen(X):
    output = ""
    for i, x in enumerate(X, start=0):
        rel_i = i % 40
        if (x - 1) <= rel_i <= (x + 1):
            output += "#"
        else:
            output += " "
        if rel_i == 39:
            output += "\n"

    print(output)


with open("mini_test_input") as input:
    X_mini = run_program(input)
    assert X_mini == [1, 1, 1, 4, 4, -1]


with open("test_input") as input:
    X_test = run_program(input)
    # for i, x in enumerate(X_test, start=1):
    #     print(f"{i}: {x}")
    test_signal_strength = signal_strength_by_index(
        X_test, [20, 60, 100, 140, 180, 220]
    )
    assert sum(test_signal_strength) == 13140
    print_screen(X_test)


with open("input") as input:
    X = run_program(input)
    signal_strength = signal_strength_by_index(X, [20, 60, 100, 140, 180, 220])
    print(f"total signal strength is {sum(signal_strength)}")
    print_screen(X)
