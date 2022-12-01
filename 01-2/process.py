sum = 0
sums = []
with open("01-1/input.txt") as fp:
    for line in fp:
        line = line.strip()
        if line:
            sum += int(line)
        else:
            print(f"Sum is {sum}")
            sums.append(sum)
            sum = 0

sums.sort(reverse=True)
print(
    f"top 3 are {sums[0]},{sums[1]},{sums[2]} total is {sums[0] + sums[1] + sums[2]}")
