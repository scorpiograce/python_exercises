# 每一位是前两位的和 0 1 1 2 3 5 8


def fib(n):
    a, b = 0, 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a+b


def fib2(n):
    a, b = 0, 1
    r = []
    r.append(a)
    while b < n:
        r.append(b)
        a, b = b, a + b

    return r