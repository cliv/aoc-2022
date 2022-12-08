import os
from pprint import pprint

stack = []
with open("./input.txt") as fp:
    for line in fp:
        line = line.strip()
        stack.append([int(i) for i in list(line)])

pprint(stack)
max_y = len(stack)
max_x = len(stack[0])

visible_count = 0
blocked_count = 0
for y in range(max_y):
    for x in range(max_x):
        val = stack[y][x]
        visible = False
        # edges are always visible so don't bother checking for blocks
        if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
            visible = True
        else:

            if max(stack[y][0:x]) < val:
                visible = True
            if max(stack[y][x + 1 : max_x]) < val:
                visible = True
            if max([i[x] for i in stack[0:y]]) < val:
                visible = True
            if max([i[x] for i in stack[y + 1 : max_y]]) < val:
                visible = True

        if visible:
            visible_count += 1
        else:
            blocked_count += 1


print("Final Count is", visible_count, blocked_count, visible_count + blocked_count)
