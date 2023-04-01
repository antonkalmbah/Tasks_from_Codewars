# сортировка чисел
a = [1, 3, 9, 5, 4]
a.sort(reverse=True) #с помощью reverse мы говорим, чтобы она это делала в обратном порядке
print(a)

#числа по убыванию с помощью функции
num = input()

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


sorting = Descending_Order(num)
print(sorting)

