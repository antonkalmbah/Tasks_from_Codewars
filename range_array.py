lines = ["a", "b", "c", "", "o"]


def number(lines):
    lines_2 = []
    for z, i in enumerate(lines, 1):
        lines_2.append(f'{z}: {i}')

    print(lines_2)


number(lines)