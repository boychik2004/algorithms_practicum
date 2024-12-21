def fib(n):
    fib_sequence = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

    return fib_sequence

if __name__ == "__main__":
    n = 8
    result = fib(n)
    print(result)