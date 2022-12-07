with open("./input.txt") as fp:
    content = list(fp.read().strip())
    buffer = []
    for i in range(len(content)):
        buffer.append(content[i])
        if len(buffer) < 14:
            continue
        if len(set(buffer)) == 14:
            print(f"Hit on {i + 1}", buffer)
            break
        buffer.pop(0)
