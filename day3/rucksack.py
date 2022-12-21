file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]


def getPriority(char):
    lowercase_ascii_offset = 96
    uppercase_ascii_offset = 64
    alphabet_offset = 26    

    if char.islower():
        return ord(char) - lowercase_ascii_offset
    else:
        return ord(char) - uppercase_ascii_offset + alphabet_offset
    
total = 0
groups = []
group_total = 0

for idx, line in enumerate(stripped):
    if len(line) == 0:
        break

    if idx % 3 == 0:
        groups.append([])

    groups[len(groups) - 1].append(line)

    halfway = int(len(line) / 2)
    
    first_compartment = line[:halfway]
    second_compartment = line[halfway:]

    for char in first_compartment:
        if char in second_compartment:
            total += getPriority(char)
            break

for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            group_total += getPriority(char)
            break

print(total)
print(group_total)
