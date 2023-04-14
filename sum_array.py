a = [1, 5.2, 4, 0, -1]
sum = 0


def sum_array(a, sum = 0):
    for i in a:
        sum += i
    return sum


sum_array(a)