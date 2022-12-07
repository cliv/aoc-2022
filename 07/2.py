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

# if i have 7, have used 5, i have 2 left and need 3 then i need to delete 4
# 3 - (7 - 5) = 3 -2 = delete 1

target = 30000000 - (70000000 - stack.get("/", 0))
print("need", target)
target_size = stack.get("/", 0)
target_key = "/"
for key in stack.keys():
    val = stack.get(key, 0)
    if val >= target and val < target_size:
        target_size = val
        target_key = key

print(target_key, target_size)
