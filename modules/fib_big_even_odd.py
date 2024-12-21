def fib_eo(n):
    pisano_period = 60
    n = n % pisano_period
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10

    return "even" if b % 2 == 0 else "odd"

if __name__ == "__main__":
    n = int(input("Введите число n: "))
    print(fib_eo(n))
