def factorial(n: int) -> int:
    if n == 1: return 1
    return n * factorial(n - 1)

# Calculate Fact(4)
# Fact(1) = 1
# Fact(2) = 2 * Fact(1)
# Fact(3) = 3 * Fact(2)
# Fact(4) = 4 * Fact(3) 