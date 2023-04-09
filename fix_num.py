num = '12312312312!'
num_1 = 'efRFS:)0207ERGQREG88349F82!'


def is_it_a_num(num):
    join_num = ''.join(num)
    true_num = []

    for i in join_num:
        if i.isdigit():
            true_num.append(i)
        else:
            i.replace(i, '')

    int_true_num = ''.join(true_num)

    if int_true_num[0] == '0' and len(int_true_num) == 11:
        print(int_true_num)
    else:
        print('Not a phone number')

    # number = ''.join(i for i in num if i.isdigit())
    # print(number if number[0] == '0' and len(number) == 11 else 'Not a phone number')


is_it_a_num(num_1)
