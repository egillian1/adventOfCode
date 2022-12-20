file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]

#        [H]         [S]         [D]
#    [S] [C]         [C]     [Q] [L]
#    [C] [R] [Z]     [R]     [H] [Z]
#    [G] [N] [H] [S] [B]     [R] [F]
#[D] [T] [Q] [F] [Q] [Z]     [Z] [N]
#[Z] [W] [F] [N] [F] [W] [J] [V] [G]
#[T] [R] [B] [C] [L] [P] [F] [L] [H]
#[H] [Q] [P] [L] [G] [V] [Z] [D] [B]
# 1   2   3   4   5   6   7   8   9 

stacks = []
stacks.append([])
stacks.append(["H", "T", "Z", "D"])
stacks.append(["Q", "R", "W", "T", "G", "C", "S"])
stacks.append(["P", "B", "F", "Q", "N", "R", "C", "H"])
stacks.append(["L", "C", "N", "F", "H", "Z"])
stacks.append(["G", "L", "F", "Q", "S"])
stacks.append(["V", "P", "W", "Z", "B", "R", "C", "S"])
stacks.append(["Z", "F", "J"])
stacks.append(["D", "L", "V", "Z", "R", "H", "Q"])
stacks.append(["B", "H", "G", "N", "F", "Z", "L", "D"])


#stacks = [[], ["Z", "N"], ["M", "C", "D"], ["P"]]

def parse_line(line):
    split = line.split()

    return int(split[1]), int(split[3]), int(split[5])

def move_stacks(stacks, quantity, from_idx, to_idx):
    for i in range(quantity):
        moved_crate = stacks[from_idx].pop()
        stacks[to_idx].append(moved_crate)

def print_tops(stacks):
    tops = ""
    for stack in stacks:
        if len(stack) != 0:
            tops += stack[len(stack) - 1]

    print(tops)

for line in stripped:
    if len(line) == 0:
        break

    quantity, from_stack, to_stack = parse_line(line)
    move_stacks(stacks, quantity, from_stack, to_stack)

print(stacks)
print_tops(stacks)
