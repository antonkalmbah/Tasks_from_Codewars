# Выполните функцию квадратной суммы так, чтобы она квадратировала каждое переданное в нее число, 
# а затем суммировала результаты вместе.
# Например, для [1, 2, 2] этого следует вернуться 9, потому 1^2 + 2^2 + 2^2 = 9.

def square_sum(a, b, c):
    print(a ** 2 + b ** 2 + c ** 2)


square_sum(1, 2, 2)

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

# square_sum(1, 2, 2)
# По ответам на данное задание это является правильным решением, хотя мой код также работает
