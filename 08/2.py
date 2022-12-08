import os


def calc_distance(stack: list[int], height: int, rev: bool) -> int:
    distance = 0
    if rev:
        stack.reverse()
    for i in stack:
        distance += 1
        if i >= height:
            break
    return distance


stack = []
with open("./input.txt") as fp:
    for line in fp:
        line = line.strip()
        stack.append([int(i) for i in list(line)])

max_y = len(stack)
max_x = len(stack[0])

highest_score = 0
for y in range(max_y):
    for x in range(max_x):
        height = stack[y][x]

        # calculate left
        score = (
            calc_distance(stack[y][0:x], height, True)  # Left
            * calc_distance(stack[y][x + 1 : max_x], height, False)  # Right
            * calc_distance([i[x] for i in stack[0:y]], height, True)  # Up
            * calc_distance([i[x] for i in stack[y + 1 : max_y]], height, False)  # Down
        )

        highest_score = max([highest_score, score])
print(highest_score)
