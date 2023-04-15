lines = ["a", "b", "c", "", "o"]


def number(lines):
    lines_2 = []
    for z, i in enumerate(lines):
        lines_2.append(f'{z+1}: {i}')

    print(lines_2)


number(lines)