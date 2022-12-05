RULES = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8,
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9,
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7,
    }
}

total = 0
with open("../input.txt") as fp:
    for line in fp:
        line = line.strip().split(' ')
        total += RULES[line[0]][line[1]]
print(total)
