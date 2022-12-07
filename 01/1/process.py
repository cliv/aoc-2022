max = 0
sum = 0
with open("01-1/input.txt") as fp:
    for line in fp:
        line = line.strip()
        if line:
            sum += int(line)
        else:
            print(f"Sum is {sum}")
            if sum > max:
                max = sum
                print("New Max!")
            sum = 0
print(f"Done, max is {max}")
