total = 0
with open("../input.txt") as fp:
    for line in fp:
        line = [set(range(int(j[0]), int(j[1]) + 1)) for j in [
            i.split('-') for i in line.strip().split(',')
        ]
        ]

        if len(line[0].intersection(line[1])):
            total += 1

print(total)
