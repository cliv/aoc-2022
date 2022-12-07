with open("./input.txt") as fp:
    content = list(fp.read().strip())
    buffer = []
    for i in range(len(content)):
        buffer.append(content[i])
        if len(buffer) < 4:
            continue
        if len(set(buffer)) == 4:
            print(f"Hit on {i + 1}", buffer)
            break
        buffer.pop(0)
