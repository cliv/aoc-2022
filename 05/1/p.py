#                     [Q]     [P] [P]
#                 [G] [V] [S] [Z] [F]
#             [W] [V] [F] [Z] [W] [Q]
#         [V] [T] [N] [J] [W] [B] [W]
#     [Z] [L] [V] [B] [C] [R] [N] [M]
# [C] [W] [R] [H] [H] [P] [T] [M] [B]
# [Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
# [B] [R] [B] [C] [D] [H] [D] [C] [N]
#  1   2   3   4   5   6   7   8   9

stack = [
    [*"BQC"],
    [*"RQWZ"],
    [*"BMRLV"],
    [*"CZHVTW"],
    [*"DZHBNVG"],
    [*"HNPCJFVQ"],
    [*"DGTRWZS"],
    [*"CGMNBWZP"],
    [*"NJBMWPFP"],
]
with open("../input.txt") as fp:
    for line in fp:
        line = line.strip().split(" ")

        new_stack = []
        for i in range(int(line[1])):
            new_stack.append(stack[int(line[3]) - 1].pop())

        new_stack.reverse()
        stack[int(line[5]) - 1].extend(new_stack)

for item in stack:
    print(item[-1], end='')
print()
