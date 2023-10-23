import time


def fibonacci(n):
    if n < 0:
        raise ValueError("Error")

    fib = {0: 0, 1: 1}

    if n in fib:
        return fib[n]

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = 412
start_time = time.time()
result = fibonacci(n)
end_time = time.time()
elapsed_time = end_time - start_time

print(f'fibonacci({n}) = {result}')
print(f'Time: {elapsed_time} seconds')
