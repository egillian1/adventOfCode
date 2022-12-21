file1 = open('input.txt', 'r')
lines = file1.readlines()

total = 0

score_map = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6, 
        "Z": 3 + 0
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3, 
        "Z": 3 + 6
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0, 
        "Z": 3 + 3
    },
}

second_score_map = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1, 
        "Z": 6 + 2
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2, 
        "Z": 6 + 3
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3, 
        "Z": 6 + 1
    },
}

for line in lines:
    if line == "\n":
        break

    split = line.split()
    opponent = split[0]
    mine = split[1]
    #total += score_map[opponent][mine]
    total += second_score_map[opponent][mine]

print("total score", total)
