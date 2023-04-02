def high_and_low(numbers):
    a = [int(i) for i in sorted(numbers.split())]
    b = sorted(a)
    print(f'{b[-1]}' + ' ' + f'{b[0]}')


high_and_low('1 5 8 44 66 -18')