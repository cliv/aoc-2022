import string
from math import floor

total = 0
pos = -1
items = {}

with open("../input.txt") as fp:
    for line in fp:
        line = line.strip()
        pos += 1

        if items.get(floor(pos / 3)):
            items[floor(pos / 3)].append(line)
        else:
            items[floor(pos / 3)] = [line]

for key in items:
    item = items[key]
    common_letter = set(item[0]).intersection(
        set(item[1])).intersection(set(item[2]))
    total += (string.ascii_letters.index(list(common_letter)[0]) + 1)

print(total)
