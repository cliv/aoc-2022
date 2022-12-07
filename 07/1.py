import os
from pprint import pprint

stack = {}
pos = []
with open("./input.txt") as fp:
    for line in fp:
        line = line.strip()

        # Handle directory traversal
        if line.startswith("$ cd"):
            if line == "$ cd ..":
                pos.pop()
            else:
                pos.append(line[4:].strip())

        # skip dirs, we don't care
        elif line.startswith("dir"):
            pass

        # skip ls commands, we don't care
        elif line.startswith("$ ls"):
            pass

        # if it's not a command, and not a file
        else:
            file = line.split(" ")
            path = ""
            for item in pos:
                path = os.path.join(path, item)
                stack[path] = stack.get(path, 0) + int(file[0])

final_sum = 0
for key in stack.keys():
    total = stack.get(key, 0)
    if total <= 100000:
        final_sum += total

print(final_sum)
