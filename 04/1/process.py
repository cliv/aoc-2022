total = 0
with open("../input.txt") as fp:
    for line in fp:
        line = [set(range(int(j[0]), int(j[1]) + 1)) for j in [
            i.split('-') for i in line.strip().split(',')
        ]
        ]

        if len(line[0].difference(line[1])) == 0:
            total += 1
        elif len(line[1].difference(line[0])) == 0:
            total += 1

print(total)
