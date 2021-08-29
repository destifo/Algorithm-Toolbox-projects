# python3


def fibonacci_number_naive(n):
    print("compute F sub", n)
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n < 2:
        return n
    a_0 = 0
    a_1 = 1
    curr_fib = 0
    for i in range(2, n + 1):
        curr_fib = a_0 + a_1
        a_0 = a_1
        a_1 = curr_fib
    return curr_fib




#if __name__ == '__main__':
n = int(input())
print(fibonacci_number(n))
