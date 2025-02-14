def karatsuba(x, y, cache=None):
    # Initialize cache (for memoization)
    if cache is None:
        cache = {}

    # Base case: single-digit multiplication
    if x < 10 or y < 10:
        return x * y

    # Check if the result is already cached
    if (x, y) in cache:
        return cache[(x, y)]

    # Find the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers into high and low parts
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    # Recursively calculate P1, P2, and P3
    p1 = karatsuba(a, c, cache)          # High parts product
    p2 = karatsuba(b, d, cache)          # Low parts product
    p3 = karatsuba(a + b, c + d, cache)  # Cross terms product

    # Use Karatsuba's formula
    result = (10**(2*m)) * p1 + (10**m) * (p3 - p1 - p2) + p2

    # Cache the result
    cache[(x, y)] = result

    return result

# Example usage
x = 12345678
y = 87654321
result = karatsuba(x, y)
print(f"{x} * {y} = {result}")
