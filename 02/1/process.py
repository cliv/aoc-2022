CHOICE_VALUES = {
    "X": {
        "value": 1,
        "results": {
            "A": 3,
            "B": 0,
            "C": 6,
        },
    },
    "Y": {
        "value": 2,
        "results": {
            "A": 6,
            "B": 3,
            "C": 0,
        },
    },
    "Z": {
        "value": 3,
        "results": {
            "A": 0,
            "B": 6,
            "C": 3,
        },
    },
}

sum = 0
with open("../input.txt") as fp:
    for line in fp:
        line = line.strip().split(' ')
        sum += CHOICE_VALUES[line[1]]["value"]
        sum += CHOICE_VALUES[line[1]]["results"][line[0]]
print(sum)
