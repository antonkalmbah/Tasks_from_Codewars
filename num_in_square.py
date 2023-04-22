num = 246


def square_digits(num):
    result = []
    for i in str(num):
        result.append(int(i)**2)

    print(int(''.join(str(i) for i in result)))


square_digits(num)
