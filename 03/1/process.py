import string

total = 0
with open("../input.txt") as fp:
    for line in fp:
        line = line.strip()
        line_break = int(len(line) / 2)
        items_a = []
        for i in range(0, line_break):
            items_a.append(line[i])

        dup_item = ""
        for i in range(line_break, line_break * 2):
            val = items_a.count(line[i])
            if val:
                dup_item = line[i]
                break

        total += (string.ascii_letters.index(dup_item) + 1)
print(total)
