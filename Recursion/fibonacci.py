def fib(n: int) -> int:
    if n == 0 or n == 1: return n
    return fib(n - 1) + fib(n - 2)
#non optimized
print(fib(4))