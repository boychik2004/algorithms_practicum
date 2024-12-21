import time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr

def measure_execution_time():
    test_values = [5, 10, 15, 20, 32]
    for n in test_values:
        start_time = time.time()
        result = fib(n)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"fib({n}) = {result}, time: {elapsed_time:.2f} ms")

if __name__ == "__main__":
    measure_execution_time()
