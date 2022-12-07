from collections import defaultdict
import json


def get_file_tree(input):
    dirtree = []
    contents = defaultdict(dict)
    for line in input:
        line = line.strip()
        line_split = line.split(" ")
        if line_split[0] == "$":
            if line_split[1] == "cd":
                dirname = line_split[2]
                if dirname == "..":
                    dirtree = dirtree[:-1]
                else:
                    dirtree.append(dirname)
                pwd = contents
                for dir in dirtree:
                    pwd = pwd[dir]
            elif line_split[1] == "ls":
                pass
            else:
                assert False, f"something went wrong: {line}"

        elif line_split[0] == "dir":
            dirname = line_split[1]
            if not pwd.get(dirname):
                pwd[dirname] = {}

        else:
            # otherwise we have a file with a size
            pwd[line_split[1]] = int(line_split[0])

    return contents


def get_dir_sizes(contents):
    size = 0
    dirs = {}
    for name, _contents in contents.items():
        if isinstance(_contents, int):
            size += _contents
        else:
            dirs[name] = get_dir_sizes(_contents)

    for _, _contents in dirs.items():
        size += _contents["files"]

    return {"files": size, "dirs": dirs}


def find_small_dirs(dirname, data, max_size=100000):
    hits = []
    n_checked = 1
    if data["files"] <= max_size:
        hits.append((dirname, data["files"]))
    for _dirname, _data in data["dirs"].items():
        # print(f"checking {_dirname}")
        _hits, _n_checked = find_small_dirs(_dirname, _data, max_size=max_size)
        hits.extend(_hits)
        n_checked += _n_checked
    return hits, n_checked


with open("test_input") as f:
    test_file_tree = get_file_tree(f)

test_dir_sizes = get_dir_sizes(test_file_tree)
assert test_dir_sizes["dirs"]["/"]["files"] == 48381165
assert test_dir_sizes["dirs"]["/"]["dirs"]["a"]["files"] == 94853

test_small_dirs, n_checked = find_small_dirs("/", test_dir_sizes["dirs"]["/"])
test_small_dirs_sum = sum(x[1] for x in test_small_dirs)

assert test_small_dirs_sum == 95437

with open("input") as f:
    file_tree = get_file_tree(f)

with open("/tmp/file_tree.json", "w") as f:
    f.write(json.dumps(file_tree, indent=2))


dir_sizes = get_dir_sizes(file_tree)

with open("/tmp/dir_sizes.json", "w") as f:
    f.write(json.dumps(dir_sizes, indent=2))

small_dirs, n_checked = find_small_dirs(
    dirname="/", data=dir_sizes["dirs"]["/"], max_size=100000
)

print(n_checked)
with open("/tmp/small_dirs.json", "w") as f:
    f.write(json.dumps(small_dirs, indent=2))


small_dirs_sum = sum(x[1] for x in small_dirs)

print(small_dirs_sum)


all_dirs, n_checked = find_small_dirs(
    dirname="/", data=dir_sizes["dirs"]["/"], max_size=float("inf")
)

total_disk_capacity = 70000000
need_disk = 30000000

current_disk_usage = dir_sizes["files"]
current_disk_capacity = total_disk_capacity - current_disk_usage
print(f"you have {current_disk_capacity} available")

disk_to_clear = need_disk - current_disk_capacity

options = [(dir, size) for dir, size in all_dirs if size >= disk_to_clear]
print(f"you need to clear {disk_to_clear}")
print(options)
best_option = [
    (dir, size) for dir, size in options if size == min(size for _, size in options)
]

print(best_option)
