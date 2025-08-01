from functools import lru_cache

@lru_cache(maxsize=None)  # Cache all computed values
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(20):
    print(f"fibonacci({i}) = {fibonacci(i)}")
