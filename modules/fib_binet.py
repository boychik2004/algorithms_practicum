import math
def fib(n):
    r = (1 + math.sqrt(5)) / 2
    i = (1 - math.sqrt(5)) / 2
    fibonacci_number = (math.pow(r, n) - math.pow(i, n)) / math.sqrt(5)

    return round(fibonacci_number)
n = int(input("Введите число n: "))

if __name__ == "__main__":
   print(f"Число Фибоначчи F({n}) равно: {fib(n)}")
