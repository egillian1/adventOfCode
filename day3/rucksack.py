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

for line in stripped:
    if len(line) == 0:
        break

    halfway = int(len(line) / 2)
    
    first_compartment = line[:halfway]
    second_compartment = line[halfway:]

    for char in first_compartment:
        if char in second_compartment:
            total += getPriority(char)
            break

print(total)
