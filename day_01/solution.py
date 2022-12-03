vals = []
cals = []
with open("input") as f:
    for line in f:
        if cal := line.strip():
            cals.append(int(cal))
        else:
            vals.append(cals)
            cals = []
    # add the last one
    vals.append(cals)

assert len(vals[-1]) == 10

# total calories per elf
elf_cals = [sum(l) for l in vals]

# get top 3 calorie totals
elf_cals.sort(reverse=True)
top_cals = elf_cals[0:3]

print(f"top three elf calorie counts: {top_cals}")
print(f"sum of top three: {sum(top_cals)}")
print(f"maximum calorie count: {max(elf_cals)}")
