#нам необходимо найти все делители числа num через функцию

def divisors(num): 
    i = [a for a in range(2,num) if num % a == 0]
    if len(i) == 0:
        return str(num) + " is prime"
    return i

print(divisors(10))