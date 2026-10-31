import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} выполнилась за {time.perf_counter() - start:.4f} с")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)


def infinite(start):
    n = start
    while True:
        yield n
        n += 1
gen = infinite(1)
print("Ввод:")
for _ in range(10):
    print(next(gen), end=" ")